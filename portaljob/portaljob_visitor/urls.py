from django.urls import path

from . import views

app_name='portaljob_visitor'

urlpatterns = [
    path('', views.index, name='index'),
    path('recruitment',views.recruitment, name='recruitment')
]
