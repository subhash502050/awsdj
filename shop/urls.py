from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from shop import views

urlpatterns = [
    path('', views.shop_home, name='index'),
    path('cart/', views.shop_cart, name = 'cart'),
    path('upload/', views.upload, name = 'upload'),
    path('uploads/',views.upload_data, name='uploads'),
]
# Serve media files during development (only works if DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)