from django.contrib import admin
from django.urls import path, include
from website import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('sponsors', views.sponsersf, name='sponsers'),
    path('registration', views.registerf, name='registration'),
    path('team', views.teamf, name='team'),
    path('gallery', views.galleryf, name='gallery'),
    path('events', views.eventsf, name='event'),
    path('users/', include('accounts.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
