// ajax를 사용한 데이터 가져오기
var count = 1; // 전역변수
let total = 0;
let avg = 0;
let id_num;
let temp = 0; // 수정버튼클릭확인
$(function(){

  $.ajax({
    url: "js/stuData.json",
    type: "get",
    data: "",
    dataType: "json",
    success: function(data){
     let stu_data = "";
      for(i = 0; i < data.length; i++){
        count++

        total= data[i].kor + data[i].eng + data[i].math;
        avg = (total/3).toFixed(2);

        stu_data += `<tr id="${data[i].no}">`;
        stu_data += `<td>${data[i].no}</td>`;
        stu_data += `<td>${data[i].name}</td>`;
        stu_data += `<td>${data[i].kor}</td>`;
        stu_data += `<td>${data[i].eng}</td>`;
        stu_data += `<td>${data[i].math}</td>`;
        stu_data += `<td>${total}</td>`;
        stu_data += `<td>${avg}</td>`;
        stu_data += `<td><button class="updateBtn">수정</button><button class="delBtn">삭제</button></td>`;
        stu_data += `</tr>`;
      };
      $("#tbody").html(stu_data);
    },
    error:function(){
      alert("실패");
    }
  }); // ajax

  // 입력버튼
    $(document).on("click", "#create", function(){
      let name = $("#name").val();
      let kor = Number($("#kor").val());
      let eng = Number($("#eng").val());
      let math = Number($("#math").val());
      total = kor + eng + math;
      avg = (total/3).toFixed(2);

      //입력된 데이터가 있는지 확인
      if($("#name").val.length < 1 || $("#kor").val().length < 1 || $("#eng").val().length < 1 || $("#math").val().length < 1){
        alert("데이터를 저장하셔야합니다.");
        return false;
      };

      // 표 만들기
      let stu_data = "";
        stu_data += `<tr id="${count}">`;
        stu_data += `<td>${count}</td>`;
        stu_data += `<td>${name}</td>`;
        stu_data += `<td>${kor}</td>`;
        stu_data += `<td>${eng}</td>`;
        stu_data += `<td>${math}</td>`;
        stu_data += `<td>${total}</td>`;
        stu_data += `<td>${avg}</td>`;
        stu_data += `<td><button class="updateBtn">수정</button><button class="delBtn">삭제</button></td>`;
        stu_data += `</tr>`;
      

      $("#tbody").prepend(stu_data);

      $("#name").val("");
      $("#kor").val("");
      $("#eng").val("");
      $("#math").val("");

      count++

    });

  // 수정버튼
    $(document).on("click", ".updateBtn", function(){
      
      //수정버튼이 클릭이 되어 있는지 확인
      if(temp==1){
        alert("수정완료 또는 수정취소 버튼을 클릭하셔야 합니다.");
        return false;
      }
      $(this).css({"color":"blue", "font-weight:":"700"});
      alert("수정을 진행합니다.");

      //데이터 가져오기
      id_num = $(this).closest("tr").attr("id");
      let new_data = $(this).closest("tr");

      console.log(new_data.children("td:eq(1)").text());
      console.log(new_data.children("td:eq(2)").text());
      console.log(new_data.children("td:eq(3)").text());
      console.log(new_data.children("td:eq(4)").text());

      $("#name").val(new_data.children("td:eq(1)").text());
      $("#kor").val(new_data.children("td:eq(2)").text());
      $("#eng").val(new_data.children("td:eq(3)").text());
      $("#math").val(new_data.children("td:eq(4)").text());

      $("#create, #update, #updateCancel").toggle();

      temp = 1;
    });


  // 수정완료 버튼
    $(document).on("click", "#update", function(){
      $(".updateBtn").css({"color":"black", "font-weight:":"400"});
      let name = $("#name").val();
      let kor = Number($("#kor").val());
      let eng = Number($("#eng").val());
      let math = Number($("#math").val());
      total = kor + eng + math;
      avg = (total/3).toFixed(2);

      //입력된 데이터가 있는지 확인
      if($("#name").val.length < 1 || $("#kor").val().length < 1 || $("#eng").val().length < 1 || $("#math").val().length < 1){
        alert("데이터를 저장하셔야합니다.");
        return false;
      };
      // 표 만들기
      let stu_data = "";
        stu_data += `<td>${id_num}</td>`;
        stu_data += `<td>${name}</td>`;
        stu_data += `<td>${kor}</td>`;
        stu_data += `<td>${eng}</td>`;
        stu_data += `<td>${math}</td>`;
        stu_data += `<td>${total}</td>`;
        stu_data += `<td>${avg}</td>`;
        stu_data += `<td><button class="updateBtn">수정</button><button class="delBtn">삭제</button></td>`;
      

      $("#"+id_num).html(stu_data);

      $("#name").val("");
      $("#kor").val("");
      $("#eng").val("");
      $("#math").val("");

      alert("수정이 완료되었습니다.");

      $("#create, #update, #updateCancel").toggle();

      temp = 0;
    })

  // 수정취소 버튼
    $(document).on("click", "#updateCancel", function(){
      $(".updateBtn").css({"color":"black", "font-weight:":"400"});
      alert("수정이 취소되었습니다.");
      $("#name").val("");
      $("#kor").val("");
      $("#eng").val("");
      $("#math").val("");

      $("#create, #update, #updateCancel").toggle();

      temp = 0;
    })

  // 삭제버튼
    $(document).on("click", ".delBtn", function(){
      let id_num = $(this).closest("tr").attr("id");
      if(confirm(id_num+"번의 학생 데이터를 삭제하시겠습니까?")){
        $("#"+id_num).remove();
        alert(id_num + "번의 학생 데이터가 삭제되었습니다.")
      }
    })

}); //제이쿼리