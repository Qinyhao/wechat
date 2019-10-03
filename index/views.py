from django.shortcuts import render
from utils import restful
from utils.Tencentsdk.Tecent_sms_send import send_sms
from django.views.decorators.http import require_POST,require_GET


# Create your views here.

def wushu_introduce(request):
    return render(request,'wushu_introduce.html')

def company(request):
    return render(request,'company.html')

def course_booking(request):
    return render(request,'course_booking.html')

@require_POST
def send_booking_message(request):
    telephone = request.POST.get('telephone')
    username = request.POST.get('username')
    school = request.POST.get('school')

    try:
        result = send_sms(telephone,username,school)
    except Exception:
        print(result)
        return restful.params_error(message="参数错误")
    print(telephone,username,school)

    return restful.ok()
