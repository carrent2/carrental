from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone
from .forms import LoginForm, UserRegistrationForm, RentalForm
from .models import Car, Rental


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnianie zakończyło się sukcesem.')
            else:
                return HttpResponse('Konto jest zablokowane.')
        else:
            return HttpResponse('Nieprawidłowe dane uwierzytelniające.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})



@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


def register(request):
            if request.method == 'POST':
                user_form = UserRegistrationForm(request.POST)
                if user_form.is_valid():
                     #Created new object for user
                    new_user = user_form.save(commit=False)
                    #setting password
                    new_user.set_password(user_form.cleaned_data['password'])
                    #Zuuser object save
                    new_user.save()
                    return render(request, 'account/register_done.html',{'new_user':new_user})
            else:
                 user_form = UserRegistrationForm()
            return render(request, 'account/register.html', {'user_form': user_form})


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars_list.html', {'cars': cars})


def calculate_price(car, start_date, end_date):
    days = (end_date - start_date).days + 1  # Add 1 to include last day
    return car.price * days

def rent_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            
            if start_date < timezone.now().date() or end_date < start_date:
                error_message = "Wybrana data jest nieprawidłowa."
                return render(request, 'validation_error_past.html', {'error_message': error_message})
            
            # Check if car is available 
            conflicting_rentals = Rental.objects.filter(
                car=car,
                start_date__lte=end_date,
                end_date__gte=start_date
            )
            
            if conflicting_rentals.exists():
                error_message = "Auto jest niedostępne w tym terminie, proszę wybrać inny termin."
                return render(request, 'validation_error.html', {'error_message': error_message})
            
            price = calculate_price(car, start_date, end_date)
            rental = Rental(car=car, user=request.user, start_date=start_date, end_date=end_date)
            
            try:
                rental.full_clean()
                rental.price = price
                rental.save()
                return redirect('user_rentals')
            except ValidationError as e:
                error_message = str(e)
                return render(request, 'validation_error.html', {'error_message': error_message})
    else:
        form = RentalForm()
    
    return render(request, 'rent_car.html', {'car': car, 'form': form})

def user_rentals(request):
    rentals = Rental.objects.filter(user=request.user)
    return render(request, 'user_rentals.html', {'rentals': rentals})

def contact_view(request):
    return render(request, 'contact.html')
