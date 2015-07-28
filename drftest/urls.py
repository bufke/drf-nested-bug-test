from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from demo.views import BookSnippetViewSet


router = routers.DefaultRouter()
router.register(r'snippets', BookSnippetViewSet)


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
