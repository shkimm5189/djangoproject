$(function () {
    getAllData();

    let myData = {};
    function addBoardRow(row,i) {
        var boardRow = "<tr>";
        boardRow += "<td>"+ i +"</td>";
        for (k in row){
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
})(jQuery);

