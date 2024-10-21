$(function(){

  $("#searchBtn").click(function(){
    alert("검색");
    let surl= "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=jRdaYR86wEkj5USok7LxRDgo9yflcgxyPLqiuNZ5x%2B%2Bvo%2F5va5kLiFX6EdQGuJCEFcwCA0Ai%2B%2FQ6xpUIGmLowQ%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    surl += searchWord;
    $.ajax({
      url: surl,
      type: "get",
      data: "",
      dateType: "json",
      success: function(data){
        alert("성공");
        //console.log(data)
        var g_item = data.response.body.items.item;

        var h_data = "";
        for(var i = 0; i < g_item.length; i++){
          h_data += `<tr id="id">`;
          h_data += `<td>${g_item[i].galContentId}</td>`;
          h_data += `<td>${g_item[i].galTitle}</td>`;
          h_data += `<td>${g_item[i].galPhotographer}</td>`;
          h_data += `<td>${g_item[i].galModifiedtime}</td>`;
          h_data += `<td><img src= '${g_item[i].galWebImageUrl}'></td>`;
          h_data += `<td><button class='delBtn'>삭제</button></td>`;
          h_data += `</tr>`;
        }
        $("#tbody").html(h_data);
      },
      error:function(){
        alert("실패");
      }
  }); // ajax
  });//searchBtn
    $(document).on("click", ".delBtn", function(){
      let id_num = $(this).closest("tr").attr("id");
      console.log(id_num);
      $("#"+id_num).remove();
    });
}); // 제이쿼리