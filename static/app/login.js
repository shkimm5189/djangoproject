$(function () {
    $("#login_btn").on('click',function () {
        let myInfo = {
            id: $("#input_id").val(),
            password: $("#input_passwd").val()
        };
        $.ajax({
            type:'POST',
            url:'/api/auth/token/login',
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify(myInfo),
            success:function (data) {
                window.location.assign("/testApp")
                alert("로그인 완료")
            },
            error:function (e) {
                alert("로그인 error")
            }
        })
    })
})(jQuery);