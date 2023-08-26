from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Car, Rental
from datetime import datetime


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
                     #Utworzenie nowego obiektu użytkownika, jednak nie zapisujemy go jeszcze w bazie danych
                    new_user = user_form.save(commit=False)
                    #Ustawienie wybranego hasła
                    new_user.set_password(user_form.cleaned_data['password'])
                    #Zapisane obiektu User.
                    new_user.save()
                    return render(request, 'account/register_done.html',{'new_user':new_user})
            else:
                 user_form = UserRegistrationForm()
            return render(request, 'account/register.html', {'user_form': user_form})


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars_list.html', {'cars': cars})


def rent_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    
    if request.method == 'POST':
        start_date = datetime.strptime(request.POST['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(request.POST['end_date'], '%Y-%m-%d').date()
        price = car.price * (end_date - start_date).days
        
        rental = Rental(car=car, user=request.user, start_date=start_date, end_date=end_date, price=price)
        rental.save()
        return redirect('user_rentals')
    
    return render(request, 'rent_car.html', {'car': car})


def user_rentals(request):
    rentals = Rental.objects.filter(user=request.user)
    return render(request, 'user_rentals.html', {'rentals': rentals})