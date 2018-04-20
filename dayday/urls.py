from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
import xadmin
from daydays.urls import router as daydays_router
from article.urls import router as article_router
from others.urls import router as others_router
xadmin.autodiscover()
urlpatterns = [
                  # url(r'^admin/', include(admin.site.urls)),
                  url(r'^xadmin/', include(xadmin.site.urls)),
                  url(r'^user/', include('daydays.urls', namespace='daydays')),
                  url(r'', include('article.urls', namespace='article')),
                  url(r'^others/', include('others.urls', namespace='others')),
                  url(r'^uploader', include('ckeditor_uploader.urls')),
                  url(r'api/', include(daydays_router.urls)),
                  url(r'art/', include(article_router.urls)),
                  url(r'other/', include(others_router.urls)),
                  url(r'search/', include('haystack.urls')),
                  url(r'', include('comment.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
