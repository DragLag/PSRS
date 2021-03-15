from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


API_TITLE = 'PSRS'
API_DESCRIPTION = 'Python scripts rest scheduler'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('scripts/', include('fileman.urls')),
    path('cron/', include('cronman.urls')),
    path('run/', include('runman.urls')),
    path('', include('viewman.urls')),

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)