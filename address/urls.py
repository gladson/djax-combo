# coding=utf-8
from django.conf.urls import patterns, url
from address.models import Estado, Cidade, Bairro
from core.api.json_response import JSONDetailView, JSONListView

urlpatterns = patterns('address.views',
    url(r'^confirmar-endereco/$', 'confirmar_endereco', name='confirmar-endereco'),
    url(r'^endereco-automatico/$', 'endereco_automatico', name='endereco-automatico'),
    url(r'^remover-endereco/$', 'remover_endereco', name='remover-endereco'),
)

urlpatterns += patterns('',
    # JSON Detail
    url(r'^estado/(?P<pk>\d)$', JSONDetailView.as_view(model=Estado), name="estado"),
    url(r'^cidade/(?P<pk>\d)$', JSONDetailView.as_view(model=Cidade), name="cidade"),
    url(r'^bairro/(?P<pk>\d)$', JSONDetailView.as_view(model=Bairro), name="bairro"),

    # JSON List
    url(r'^estados/$', JSONListView.as_view(model=Estado), name="estados"),
)
