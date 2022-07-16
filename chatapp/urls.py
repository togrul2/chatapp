from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('', include('chat.urls')),
    path('blog/', include('blog.urls'))
] + static(settings.STATIC_URL, document=settings.STATIC_ROOT)
