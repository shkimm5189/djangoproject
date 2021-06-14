$(function () {
    $("#signup_btn").on('click', function () {
        let userData = {
            id: $('#input_id').val(),
            password: $('#input_passwd').val(),
            nickname: $('#input_nickname').val()
        };

        $.ajax({
            type:'POST',
            url: '/api/auth/token/signup',
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify(userData),
            success:function () {
                window.location.assign("/testApp")
            },
            error: function () {
                alert("등록이 안된다. 이유는 니가 알겠지.")
            }
        })
    })
})(jQuery);