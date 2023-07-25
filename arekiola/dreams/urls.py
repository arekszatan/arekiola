from django.urls import path

from .views import (
    index,
    # NameColorText
)

urlpatterns = [
    path('dreams/', index, name='index'),
    # path('api/setting/textColor', NameColorText.as_view()),
]