
from django.contrib import admin
from django.urls import path, include
from users.views import UsersViewSet
from ativos.views import ArcondicionadoViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='Users')
router.register('arcondiconados', ArcondicionadoViewSet, basename='Arcondiconados')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)