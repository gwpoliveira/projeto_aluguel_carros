# urls.py
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from aluguel_carros.views import HomeView, CustomLogoutView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('aluguel/', include('aluguel_carros.urls')),  # Adicione '/' no final para consistência
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
