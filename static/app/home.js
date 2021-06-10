$(function () {
    getAllData();

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
            boardRow += "<td>" + row[k]+"</td>";
        }
        boardRow += "</tr>"
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
            content: $("#textarea_modal_content").val()
        };
        $.ajax({
            type:'PUT',
            url: '/api/boards'
        })
    });
    
    $("#delete_btn").on('click', function (e) {
        $.ajax({
            type:'DELETE',
            url:'/api/boards',
            success:function () {
                
            },
            error:function () {
                
            }
        })
    })

})(jQuery);

