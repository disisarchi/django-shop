from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.single_course, name='single_course'),
    path('basket/', views.view_basket, name='view_basket'),
    path('add/<int:course_id>/', views.add_to_basket, name='add_to_basket'),
    path('remove/<int:item_id>/', views.remove_from_basket, name='remove_from_basket'),
]