from django.urls import path
from . import views

urlpatterns = [
    # path("january",views.january),
    # path("february",views.february)
    path("",views.index , name="index"), #challenge/
    path("<int:month>", views.dynamic_month_by_number),
    path("<str:month>", views.dynamic_month, name= "month-challenge"),
    ]
