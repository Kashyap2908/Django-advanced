from django.urls import path
from student import views

urlpatterns = [
    path('', views.data,name='home'),
    path('edit<int:id>/', views.edit,name='edit'),
    path('delete<int:id>/', views.delete,name='delete'),
    
]
