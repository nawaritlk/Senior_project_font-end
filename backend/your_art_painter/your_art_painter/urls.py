from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('create/', include('create_your_art.urls')),
    path('submission/', include('create_your_art.urls')),
    path('profile/', include('authentication.urls')),
    path('community/', include('authentication.urls')),
    # path('register/', include('authentication.urls')),
    path('auth/', include('authentication.urls')),
    path('temp/', include('temp.urls')),
    path('upload/', include('create_your_art.urls'))
    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += path('__debug__', include('debug_toolbar.urls'))
