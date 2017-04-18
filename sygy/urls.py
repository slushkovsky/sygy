from django.conf.urls import url

import website.views as website


urlpatterns = [
    url(r'^/?$', website.home)
]
