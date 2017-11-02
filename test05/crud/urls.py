# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'Author', views.AuthorViewSet,base_name='Author')
router.register(r'Book', views.BookViewSet, base_name='Book')

urlpatterns = (
    url(r'^test$', views.test, name='test'),
    url(r'^', include(router.urls)),
)
