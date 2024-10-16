
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsView, NewCarView
from accounts.views import register_views, login_views, logout_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_views, name='register'),
    path('login/', login_views, name='login'),
    path('logout/', logout_views, name='logout'),
    path('cars/', CarsView.as_view(), name='cars_list'),
    path('new_car/', NewCarView.as_view(), name='new_car_views'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
