let num = 0;
let num2 = 0;
$(function(){
  $("#right").click(function(){
    if(num >= 900){
      alert("오른쪽 끝에 도달했습니다. 우측 이동은 불가합니다.");
      return false;
    }
    $("#box").stop();
    num += 100;
    num2 += 360;
    $("#box").animate({
      left:num, "rotate" : num2+"deg"
    }, 1000);
  });
  $("#left").click(function(){
    if(num <= 0){
      alert("오른쪽 끝에 도달했습니다. 우측 이동은 불가합니다.");
      return false;
    }
    $("#box").stop();
    num -= 100;
    num2 -= 360;
    $("#box").animate({
      left:num, "rotate" : num2+"deg"
    }, 1000);
  });
});