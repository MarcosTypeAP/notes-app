from django.urls import path

from users import views


urlpatterns = [
    
    path(
        route='signup/', 
        view=views.SignupView.as_view(), 
        name="signup",
    ),
    path(
        route='logout/', 
        view=views.LogoutView.as_view(), 
        name='logout',
    ),
    path(
        route='login/', 
        view=views.LoginView.as_view(), 
        name='login',
    ),
    path(
        route='me/profile', 
        view=views.ProfileView.as_view(), 
        name='update_profile',
    ), 

]