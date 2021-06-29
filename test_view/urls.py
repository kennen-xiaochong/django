from django.urls import path
from . import views
urlpatterns={
    path('login/',views.login),
    path('index/',views.index),
    path('add_person/',views.add_person),
    path('del_person/<int:personid>/',views.del_person),
    path('edit_person/<int:personid>/',views.edit_person),
}