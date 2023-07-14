from django.urls import path

from .views import (
    TodoListApiView,
    index,
    RemoveRow,
    UpdateRow
)

urlpatterns = [
    path('api/', TodoListApiView.as_view()),
    path('api/remove', RemoveRow.as_view()),
    path('api/update', UpdateRow.as_view()),
    path('', index, name='index'),
    path('shopping/', index, name='index'),
    path('test/', index, name='index'),
]