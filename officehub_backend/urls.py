from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userApp.urls')),
    path('event/', include('eventApp.urls')),
    path('blog/', include('blogApp.urls')),
    path('notification/', include('notificationApp.urls')),
    path('api/', include('survey.urls')),
]
