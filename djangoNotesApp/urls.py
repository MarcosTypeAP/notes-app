from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # django
    path('admin/', admin.site.urls, name='admin'),

    # users
    path('users/', include(('users.urls', 'users'), namespace='users')),

    # notes
    path('', include(('notes.urls', 'notes'), namespace='notes')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
