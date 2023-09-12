from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('KnowledgeBase.urls')),
    path('auth/', include('django.contrib.auth.urls')),
] 