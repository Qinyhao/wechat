
from django.urls import path
from . import views

app_name = "index"

urlpatterns = [
    path('wushu_introduce/',views.wushu_introduce,name = "wushu_introduce"),
path('company/',views.company,name = "company"),
path('course_booking/',views.course_booking,name = "course_booking"),
    path('send_booking_message/',views.send_booking_message,name = "send_booking_message"),
]