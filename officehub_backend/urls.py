from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userApp.urls')),
    path('event/', include('eventApp.urls')),
    path('blog/', include('blogApp.urls')),
    path('notification/', include('notificationApp.urls')),
    path('api/', include('survey.urls')),  # Assign a unique path for survey
    path('api/', include('applicationApp.urls')),  # Assign a unique path for applicationApp
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
