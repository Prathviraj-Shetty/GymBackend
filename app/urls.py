from django.contrib import admin
from django.urls import path
from app import views 
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (TokenRefreshView)
urlpatterns = [

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',views.register,name='register'),
    path('verifyusername/', views.verifyusername),
    path('usertype/<str:uname>/', views.usertype),
    path('isregistered/<str:uid>/', views.isregistered),
    path('isgymregistered/<str:uid>/', views.isgymregistered),

    path('admin/', admin.site.urls),
    path('searchgym/', views.searchgym),
    path('searchgymdynamic/<str:str>/', views.searchgymdynamic),
    path('getgymdetails/<str:id>/', views.getgymdetails),
    path('gettrainers/<str:uid>/', views.gettrainers),
    path('gettrainersdynamic/<str:uid>/<str:str>/', views.gettrainersdynamic),
    path('getgymtrainers/<str:gym>/', views.getgymtrainers),
    path('userprofile/<str:str>/', views.userprofile),
    path('getuserprofile/<str:uid>/', views.getuserprofile),
    path('trainerprofile/', views.trainerprofile),
    path('gymprofile/<str:str>/', views.gymprofile),
    path('addschedule/', views.addschedule),
    path('getgymprofile/<str:uid>/', views.getgymprofile),
    path('getschedule/<str:uid>/', views.getschedule),
    path('getgymschedule/<str:gym>/', views.getgymschedule),
    path('bookslot/', views.bookslot),
    path('slotbookings/<str:id>/', views.slotbookings),
    path('getbookingdetail/<str:id>/', views.getbookingdetail),
]
