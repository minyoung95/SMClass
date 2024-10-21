$(function(){

  let name_pattern = /^[가-힣]{2,4}$/
  let id_pattern = /^[a-zA-z0-9_]{4,16}$/
  let pw_pattern = /^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*]).{8,}$/

  $("#mem_ship").click(function(){
    
    if(!(name_pattern.test($("#name").val())) || !(id_pattern.test($("#id").val())) || !(pw_pattern.test($("#pw1").val()))){
      alert("이름, 아이디 또는 비밀번호 입력 안댐");
      return false;
    }else{
      alert("성공");
    }
  });
}); //제이쿼리

