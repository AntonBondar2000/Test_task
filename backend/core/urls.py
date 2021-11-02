from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.survey.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token),
    path('docs/', get_swagger_view(title='Test task', url='')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
