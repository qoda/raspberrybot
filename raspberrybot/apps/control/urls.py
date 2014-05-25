from django.conf.urls import patterns, url


# control specific url patterns
urlpatterns = patterns('raspberrybot.apps.control.views',
    url(r'^(?P<direction>\S+)/$', 'command', name='command'),
)
