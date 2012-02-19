from django.conf.urls.defaults import *
import apiviews

urlpatterns = patterns('',
    (r'^route/(?P<slug>.*)$', apiviews.route), #FIXME: better regexp for route alias?
    (r'^stop/(?P<slug>.*)$', apiviews.stop),
)
