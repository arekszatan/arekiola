from django.urls import path

from .views import (
    # TodoListApiView,
    index
    # RemoveRow,
    # UpdateRow
)

urlpatterns = [
    # path('api/', TodoListApiView.as_view()),
    # path('api/remove', RemoveRow.as_view()),
    # path('api/update', UpdateRow.as_view()),
    path('wallet/', index, name='index'),
]
