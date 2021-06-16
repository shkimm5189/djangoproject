$(function () {
    getAllData();
    var key;
    let myData = {};
    let idToIdx = {

    };

    function addBoardRow(row,i) {
        var boardRow = "<tr id="+i+" data-toggle=\"modal\" data-target=\"#detail_Modal\">";
        boardRow += "<td>"+ i +"</td>";
        for (k in row){
            if(k == 'id'){
                idToIdx[i] = row[k];
                continue;
            }
            if(k == 'create_at'){
                date = row[k].split('T');
                days = date[0].split('-');
                dateformat = days[1]+"월"+days[2]+"일 ";
                times = date[1].substr(0,5).split(':');
                timeformat = times[0]+":"+times[1];
                boardRow += "<td>" + dateformat + timeformat + "</td>";
                continue
            }
            if(k== 'content'){
                continue
            }

            boardRow += "<td>" + row[k]+"</td>";
        }
        boardRow += "</tr>";
        return boardRow;
    }
    function getAllData() {
        $.ajax({
            type:'GET',
            url:'/api/boards',
            dataType:'json',
            success:function (data) {
                var tableList = data;
                if(tableList.length > 0){
                    for(var i = 0, val ; val = tableList[i] ;i++){
                        $('#main_table').append(addBoardRow(tableList[i],i+1))
                    }
                }
            }
        })
    }
     function getCookie(name) {
        var value = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
        return value? value[2] : null;
    }

    function update_by() {
        let name = getCookie('nickname')
        if (name == null) {
            return "AnonymousUser"
        } else {
            return name;
        }
    }

    $("#registerBtn").on("click",function (e) {
        window.location.href="register";
    });

    // $("#detail_Modal").on('show.bs.modal',function (e) {
    //     console.log($(this).parents());
    //    $.ajax({
    //        type:'GET',
    //        url:'/api/boards/',
    //        success:function (data) {
    //
    //        }
    //    })
    // });


    $("#update_btn").on('click', function (e) {
        let myData = {
            subject: $("#input_modal_subject").val(),
            content: $("#textarea_modal_content").val(),
            update_by : update_by()
        };
        $.ajax({
            type:'PUT',
            url: '/api/boards/'+idToIdx[key],
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify(myData),
            success: function (myData) {

            },
            error: function () {
                alert("업데이트가 안된다!");
            }
        })
    });
    
    $("#delete_btn").on('click', function (e) {
        $.ajax({
            type:'DELETE',
            url: '/api/boards/'+idToIdx[key],
            success:function () {
                
            },
            error:function () {
                alert("안지워진다!")
            }
        })
    });

    $("#main_table").on('click','tr',function (e) {
       key = $(this).attr('id');
        $.ajax({
            type: 'GET',
            url: '/api/boards/'+idToIdx[key],
            dataType: 'json',
            success: function (data) {
                $("#input_modal_subject").val(data.subject);
                $("#textarea_modal_content").text(data.content);
            },
            error:function () {
                alert("안되지롱 다시 생각해")
            }
        })

    })


})(jQuery);

