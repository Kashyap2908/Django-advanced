from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add_player,name='add'),
    path("edit/<int:id>/",views.edit_player, name="edit"),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('details/<int:id>/',views.player_details,name='details')
]
