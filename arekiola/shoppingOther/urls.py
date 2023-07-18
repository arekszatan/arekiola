from django.urls import path

from .views import (
    index,
    ShoppingOtherView,
    ShoppingOtherUpdate,
    ShoppingOtherRemove
)

urlpatterns = [
    path('shoppingOther/', index, name='index'),
    path('api/shoppingOther/', ShoppingOtherView.as_view()),
    path('api/shoppingOther/remove', ShoppingOtherRemove.as_view()),
    path('api/shoppingOther/update', ShoppingOtherUpdate.as_view()),
]
