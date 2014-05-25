from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views import generic


admin.autodiscover()

# static url patterns
urlpatterns = patterns('raspberrybot.views',
    url(r'^$', generic.TemplateView.as_view(template_name="index.html"), name='index'),
)

# control url patterns
urlpatterns += patterns('',
    url(r'^control/', include('raspberrybot.apps.control.urls', namespace='control'))
)

# admin url patterns
urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
