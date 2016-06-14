var phone;

$( document ).ready(function() {
  $( "#target1" ).focus(); //puts cursor on first entry field
  $(".text-entry").on("click", function() { //selects value on click of input field
    this.select(); 
  });
  $("#target11").on("click", function() {
    
    phone = "+1-" + $("#target1").val() + $("#target2").val() + $("#target3").val() + "-" + $("#target4").val() + $("#target5").val() + $("#target6").val() + "-" + $("#target7").val() + $("#target8").val() + $("#target9").val() + $("#target10").val();
        document.callerid.entry.value = phone;
        $(".lookup-form").submit();
  });
  $(".clear").on("click", function() { //listener for clear button
    $('body').find('form')[0].reset(); 
    $('#target1').focus();
  });
});


function check(obj){ //automatically moves focus to next entry field when max is met
  if(obj.value.length +1 <=1) { 
  } else {
    var current = $(obj).attr("id"); //finds current entry field
    var num = parseInt(current.slice(6)); //picks the target number out of the field's id
    num = num + 1;
    $( "#target" + num ).focus().select();
  }
}