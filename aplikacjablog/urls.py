from django.urls import path

from aplikacjablog import views

app_name = 'aplikacjablog'

urlpatterns = [
    path('', views.post_list, name='post_list')
]