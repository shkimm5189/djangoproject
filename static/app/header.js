$(function () {
    checkNickname();

    function checkNickname() {
        if(getCookie('Token') != null){
            let changeName = "<li id='logout_btn' class='nav-item'><a href='logout' class='nav-link'>Logout</a></li>"
            $("#nav_header").children().last().replaceWith(changeName)
        }
    }

    function getCookie(name) {
        var value = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
        return value? value[2] : null;
    }

    $('#logout_btn').on('click', function () {
        $.ajax({
            type: 'GET',
            url: '/api/auth/token/logout',
            success:function () {
                alert("로그아웃 되었습니다.")
                window.location.assign("/testApp");
            }
        })
    })


})(jQuery);