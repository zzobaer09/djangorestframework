from django.urls import path
from .apis import *
urlpatterns = [
    path("register/" , RegisterApi.as_view(),name="register"),
]
