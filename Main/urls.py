from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('edit/<int:id>', views.Update),
    path('about/<int:id>', views.About),
    path('addData/', views.AddData),
    path('addVideo/<int:id>', views.AddVideo),
    path('editVideo/<int:id>', views.editVideo),
    path('deleteVideo/<int:id>', views.deleteVideo),
    path('login/', views.Log_in),
    path('signUp/', views.sign_up),
    path('logout/', views.Log_out),
    path('category/', views.category),
    path('search/', views.search),
    path('playAddFreeVideo/', views.playAddFreeVideo),
]
