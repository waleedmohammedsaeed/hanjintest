from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('catering', views.catering, name='catering'),
    path('constructions', views.constructions, name='constructions'),
    path('energy', views.energy, name='energy'),
    path('entertainment', views.entertainment, name='entertainment'),
    path('marketing', views.marketing, name='marketing'),
    # path('category/', views.category, name='category'),
    # path('delete_category/<int:id>/', views.delete_category, name='delete_category'),

]
