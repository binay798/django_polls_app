from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name="create"),
    path('result/',views.result,name='result'),
    path('view/',views.view,name="view"),
]