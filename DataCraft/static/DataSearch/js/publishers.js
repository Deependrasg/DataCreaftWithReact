$(document).ready(function($){
$('.slider .owl-carousel').owlCarousel({
  loop:true,
  autoplay:true,
  margin:0,
  nav:false,
  items: 1
})       

$(".back-top").click(function(){
  $('html, body').animate({scrollTop:0},500);  
});


// add department according to sub department
$("#id_subdepartment").find('option').remove()
$("#id_subdepartment").append('<option value="">Select </option>');
$("#id_department").change(function(){
      $.ajax({
        type: "GET",
        url:"get-sub-department/"+$('#id_department').val()+"/",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(result) {
          $("#id_subdepartment").find('option').remove()
          $("#id_subdepartment").append('<option value="">Select </option>');
          
          if(result.status='success'){
                $.each(result.data, function (index, value) {
                $("#id_subdepartment").append('<option value="'+value.id+'">'+value.name+'</option>');
                    })
                }                  
            },
            error: function(){},
        });
    });

$("#id_subdepartment").change(function(){
      $.ajax({
        type: "GET",
        url:"get-sub-department-code/"+$('#id_subdepartment').val()+"/",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(result) {
          if(result.status='success'){
                $('#id_inventory_ID').val(result.code)    
                }               
          },
          error: function(){},
      });
    });
  });