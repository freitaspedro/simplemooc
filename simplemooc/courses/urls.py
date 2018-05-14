from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'simplemooc.courses.views.index', name='index'),
    # url(r'^(?P<pk>\d+)/$', 'simplemooc.courses.views.details', name='details'),
    url(r'^(?P<slug>[\w_-]+)/$', 'simplemooc.courses.views.details', name='details'),
    url(r'^(?P<slug>[\w_-]+)/inscricao/$', 'simplemooc.courses.views.enrollment', name='enrollment'),
    url(r'^(?P<slug>[\w_-]+)/cancelar-inscricao/$', 'simplemooc.courses.views.undo_enrollment', name='undo_enrollment'),
    url(r'^(?P<slug>[\w_-]+)/anuncios/$', 'simplemooc.courses.views.announcements', name='announcements'),
    url(r'^(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)/$', 'simplemooc.courses.views.current_announcement', name='current_announcement'),
    url(r'^(?P<slug>[\w_-]+)/aulas/$', 'simplemooc.courses.views.lessons', name='lessons'),
    url(r'^(?P<slug>[\w_-]+)/aulas/(?P<pk>\d+)/$', 'simplemooc.courses.views.current_lesson', name='current_lesson'),
    url(r'^(?P<slug>[\w_-]+)/materiais/(?P<pk>\d+)/$', 'simplemooc.courses.views.material', name='material')
]
