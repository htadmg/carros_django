
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_views, new_car_views
from accounts.views import register_views, login_views, logout_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_views, name='register'),
    path('login/', login_views, name='login'),
    path('logout/', logout_views, name='logout'),
    path('cars/', cars_views, name='cars_list'),
    path('new_car/', new_car_views, name='new_car_views'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
