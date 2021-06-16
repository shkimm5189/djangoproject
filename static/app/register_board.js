$(function () {
     function getCookie(name) {
        var value = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
        return value? value[2] : null;
    }

    function create_by() {
        let name = getCookie('nickname')
        if (name == null) {
            return "AnonymousUser"
        } else {
            return name;
        }
    }
    $("#register_btn").on("click",function (e) {
        let myData = {
            subject: $("#input_subject").val(),
            content: $("#textarea_content").val(),
            create_by: create_by(),
        };
        $.ajax({
            type: 'POST',
            url: '/api/boards/',
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify(myData),
            success:function (myData) {

                window.location.assign("/testApp");
            },
            error:function () {
                alert("아 몰랑 뭔가 틀렸엉");
                console.log(myData)
            },
        });
    });

})(jQuery);