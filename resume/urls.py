
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('cv.urls')),
    path('', include('django.contrib.auth.urls')),
    # path('candidats/', include('candidats.urls')),
    # path('candidats/', include('django.contrib.auth.urls')),


    # re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    # re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

admin.site.index_title = "CV en OR"
admin.site.site_header = "CV administration"
admin.site.site_title = "CV en OR"


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

