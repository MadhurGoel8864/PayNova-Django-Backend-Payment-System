from django.urls import path
from account import views

app_name = "account"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("", views.account, name="account"),
    path("kyc-reg/", views.kyc_registration, name="kyc-reg"),
    path("edit-kyc/", views.edit_kyc, name="edit-kyc"),
]
