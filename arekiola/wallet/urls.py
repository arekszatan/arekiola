from django.urls import path

from .views import (
    index,
    WalletListDbView,
    WalletListAddDbView,
    WalletListRemoveAllDbView
)

urlpatterns = [
    path('api/wallet/List/', WalletListDbView.as_view()),
    path('wallet/', index, name='index'),
    path('api/wallet/list/add/', WalletListAddDbView.as_view()),
    path('api/wallet/list/remove/', WalletListRemoveAllDbView.as_view())
]
