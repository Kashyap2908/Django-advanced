from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


router=routers.DefaultRouter()

router.register('emp',views.EmpViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view())
]
