from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import handle404, handle500 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('saler/', include('saler.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include('pages.api_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

<<<<<<< HEAD
handler404 = 'project.views.handel404'
handler404 = 'project.views.handel500'
=======
handler404 = handle404  
handler500 = handle500
>>>>>>> 3738c40297a90c60ed23658c5cea61cbeabb80d1
