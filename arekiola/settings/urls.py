from django.urls import path

from .views import (
    index,
    NameColorText
)

urlpatterns = [
    path('settings/', index, name='index'),
    path('api/setting/textColor', NameColorText.as_view()),
]