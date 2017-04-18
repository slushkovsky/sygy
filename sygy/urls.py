from django.conf.urls import url

import website.views as website


urlpatterns = [
    url(r'^$', website.home),
    url(r'^eyeGuest/?$', website.eye_guest),
    url(r'^eyeWish/?$', website.eye_wish),
    url(r'^eyeService/?$', website.eye_service),
    url(r'^eyeMerketer/?$', website.eye_merketer),
    url(r'^about/?$', website.about_us),
    url(r'^support/?$', website.support)
]
