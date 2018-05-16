from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'simplemooc.forum.views.index', name='index'),
]