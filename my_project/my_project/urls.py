from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import robots_txt
# from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt/', robots_txt, name='robots_txt'),
    # path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type='text/plain'), name='robots_txt'),
    path('app/', include('my_app.urls')),
    path('', include('my_app.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)