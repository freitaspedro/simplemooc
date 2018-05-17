from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'simplemooc.forum.views.index', name='index'),
    url(r'^tag/(?P<tag>[\w_-]+)/$', 'simplemooc.forum.views.index', name='indextagged'),
    url(r'^(?P<slug>[\w_-]+)/$', 'simplemooc.forum.views.thread', name='thread'),
    url(r'^respostas/(?P<pk>\d+)/correta$', 'simplemooc.forum.views.replycorrect', name='replycorrect'),
    url(r'^respostas/(?P<pk>\d+)/incorreta$', 'simplemooc.forum.views.replyincorrect', name='replyincorrect'),
]