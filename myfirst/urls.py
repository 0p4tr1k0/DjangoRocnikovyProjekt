from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('tanks/', views.TankListView.as_view(), name='tanks'),

]