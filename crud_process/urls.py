from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('addCar/',views.add_car,name='add_car'),
    path('carList/',views.car_list,name='car_list'),
    path('updateCar/<int:pk>/',views.update_car,name='updateCar'),
    path('deleteCar/<int:pk>/',views.delete_car,name='deleteCar'),
]
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)