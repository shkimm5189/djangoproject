$(function () {

    $("#register_btn").on("click",function (e) {
    //     let subject = $("#input_subject").val();
    // let content = $("#textarea_content").val();
    // let myData = {};
    // myData.subject = subject;
    // myData.content = content;
    // myData.author = "kimSungHyun";
    // myData.create_at="KimSungHyun";
    // myData.update_at="KimSungHyun";


        let myData = {
            subject: $("#input_subject").val(),
            content: $("#textarea_content").val(),
            create_by: "kimsunghyun"
        };
        $.ajax({
            type: 'POST',
            url: '/api/boards/',
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify(myData),
            success:function (data) {
                window.location.assign("/testApp")
            },
            error:function () {
                alert("아 몰랑 뭔가 틀렸엉")
                console.log(myData)
            },


            });
    });
})(jQuery);