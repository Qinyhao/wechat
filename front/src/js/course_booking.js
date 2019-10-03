function Coursebooking() {

}

Coursebooking.prototype.run = function () {
    this.ListenBookingEvent();
}

Coursebooking.prototype.ListenBookingEvent = function(){
    var self = this;
    var commitBtn = $('.commit');
    commitBtn.click(function () {
        var telephone = $(".form-control[name='telephone']").val()
        var username = $(".form-control[name='username']").val()
        var school = $(".form-control[name='school']").val()
        xfzajax.post({
            'url':'/wechat/send_booking_message/',
            'data':{
                'telephone':telephone,
                'username':username,
                'school':school
            },
            'success':function (result) {
                if(result['code'] === 200){
                    window.messageBox.showSuccess("恭喜您预约成功！")
                }else{
                    window.messageBox.showError("预约失败，请重新预约！")
                }
            },
            'fail':function (error) {
                console.log(error)
            }

        })
    })
}


$(function () {
    cb = new Coursebooking();
    cb.run();
})