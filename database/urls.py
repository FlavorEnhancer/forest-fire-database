# database urls for django app


from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.database_directions),

]
