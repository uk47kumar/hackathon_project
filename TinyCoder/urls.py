from django.urls import path, include
from TinyCoder import views

# admin.site.site_header = "MADPHARM "
# admin.site.site_title = "MADPHARM PORTAL"
# admin.site.index_title = "MADPHARM WELCOMES U"

urlpatterns = [
    path("Article_Login", views.Article_Login, name='Article_Login'),
    path("", views.index, name='home'),
    path("Login", views.Login, name='Login'),
    path("Signup", views.Signup, name='Signup'),
    path("Article_main", views.Article_main, name='Article_main'),
    path("appointment", views.appointment, name='appointment'),

    path("saveEnquiry", views.saveEnquiry, name='saveEnquiry'),
    path("contactEnquiry", views.contactEnquiry, name="contactEnquiry"),
    # path("Log",views.Log,name="Log"),
    # path("Sign", views.Sign, name='Sign'),
    # path("doctors",views.doctor,name='doctor')
    path("Appointment", views.Appointment, name="Appointment"),
    # path('abcd', views.abcd, name='abcd')
    path('enterotp/', views.otpvalidation, name = "otp"),
]
