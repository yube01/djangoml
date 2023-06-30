
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
   
    path('api/',include('irisApp.urls')), # endpoint api for predictor
    path('admin/', admin.site.urls),

]
