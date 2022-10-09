from django.urls import path
from . import views
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('signup/', views.signup, name='signup'),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),
  path('add_post/', views.add_post, name='addpost'),
  path('update_post/<int:id>/', views.update_post, name='updatepost'),
  path('delete_post/<int:id>/', views.delete_post, name='deletepost'),
]