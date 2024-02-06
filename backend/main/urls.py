from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('delete_category/<int:id>/', views.delete_category, name='delete_category'),

]
