from django.urls import path

from users import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('me/', views.UserDetailView.as_view(), name='user-detail'),
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
]
