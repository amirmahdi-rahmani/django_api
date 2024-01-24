from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views




urlpatterns = [
    path('',views.category),
    path('famous/',views.famous),
    path('foods/',views.foods),
    path('places/',views.places),
    # Authentication endpoint
    path('register/',views.register),
    path('login/',views.log_in),
    path('logout/',views.log_out),
    path('me/',views.me)


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
