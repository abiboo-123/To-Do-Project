from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('update_item/<int:pk>', views.ubdateTask, name='update'),
]