from django.urls import path
from . import views

app_name = "user_profile"

urlpatterns = [
    path("", views.user_profile, name="user_profile"),
    path("purchases/", views.purchase_history, name="purchases"),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

]