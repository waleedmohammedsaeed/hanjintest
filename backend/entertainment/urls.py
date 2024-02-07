from django.urls import path
from . import views 

urlpatterns = [
    path('', views.entertainment, name='entertainment'),
    # path('', views.entertainment, name='entertainment'),

]