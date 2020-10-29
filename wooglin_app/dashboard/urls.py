from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.dashboard_view, name="dashboard"),
    path('dashboard', views.dashboard_view, name="dashboard"),
    # path('create', views.SoberBroSignupCreateView.as_view(), name="editsbs")
]
