from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('login/', auth_views.LoginView.as_view(), name='login'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('', views.dashboard, name='dashboard'),
     path('password_change/',
         auth_views.PasswordChangeView.as_view(),
         name="password_change"),
     path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
     path('password_reset/',
          auth_views.PasswordResetView.as_view(), name='password_reset'),
     path('password_reset/done/',
          auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
     path('reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
     path('', include('django.contrib.auth.urls')),
     path('register/', views.register, name='register'),
     path('cars/', views.car_list, name='car_list'),
     path('cars/<int:car_id>/rent/', views.rent_car, name='rent_car'),
     path('rentals/', views.user_rentals, name='user_rentals'),
     path('validation-error/', views.rent_car, name='validation_error'),
     path('kontakt/', views.contact_view, name='contact'),
     path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
     path('cancel_rental/<int:rental_id>/', views.cancel_rental, name='cancel_rental'),
     path('rental/<int:rental_id>/', views.rental_detail, name='rental_detail'),
     path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
     path('contact/', views.contact_view, name='email_sent'),

]


