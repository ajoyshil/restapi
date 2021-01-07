from django.urls import path
# from .views import RegisterView, LoginView, ProfileView, profileViewUpdate
from .views import RegisterView, LoginView, ProfileView, ProfileDetailView, EmployeeView, EmployeeDetailView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<int:id>', ProfileDetailView.as_view()),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('employee/<int:id>', EmployeeDetailView.as_view()),
    path('employee/', EmployeeView.as_view(), name='profile'),

]
