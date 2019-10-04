
from django.conf.urls import url
from . import views

app_name = "index"

urlpatterns = [
    url(r'wushu_introduce/',views.wushu_introduce,name = "wushu_introduce"),
    url(r'company/',views.company,name = "company"),
    url(r'course_booking/',views.course_booking,name = "course_booking"),
    url(r'send_booking_message/',views.send_booking_message,name = "send_booking_message"),
]
