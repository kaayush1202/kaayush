from django.urls import path

from .import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/',views.register ,name="register"),
    path('login/',views.my_login ,name="login"),
    path('email_verify/',views.email_verify,name="email_verify"),
    path('users/',views.user_list,name="user_list"),
    path('users/<int:id>/',views.user_details,name="user_id"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('add_adress/',views.add_address,name="add_address"),
    path('show_address/',views.show_address,name="show_address")

]