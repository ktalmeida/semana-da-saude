from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='list'),
    url(r'^new$', views.create, name='new'),
    url(r'^(?P<patient_id>[0-9]+)$', views.edit, name='edit'),
    # url(r'^(?P<patient_id>[0-9]+)$', views.results, name='delete')
]
