from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name="create"),
    path('result/<int:poll_id>',views.result,name='result'),
    path('vote/<int:poll_id>',views.vote,name="vote"),
]