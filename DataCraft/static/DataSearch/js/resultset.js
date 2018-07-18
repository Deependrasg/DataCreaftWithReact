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
});

  $('.search-btn').click(function(){
      if ($('#search').val() != ''){
            $.ajax({
              type: "GET",
              url:"searching/",
              data:{'val':$('#search').val()},
              contentType: "application/json; charset=utf-8",
              dataType: "json",
              success: function(result) {
                  if (result.status='success'){
                    $('.result-data').text('')
                    $('.pagination-data').text('')
                    $.each(result.data, function (index, value) {
                      $(".result-data").append('<div class="row member-box">\
                        <div class="col-md-9 col-sm-8 col-xs-12">\
                        <a href="/service-data/'+value.id+'"/">\
                        <h1 class="cyan heading">'+value.title+'</h1>\
                        </a>\
                        <h3>'+value.description+'</h3>\
                        <p>Tags<span class="cyan"> business</span></p></div>\
                        <div class="col-md-3 col-sm-4 col-xs-12">\
                        <div class="inner-box">\
                        <span class="cyan">Dataset</span><br>\
                        <h4>Updated</h4>\
                        <h4 class="cyan">February 15,2018</h4><br>\
                        <h4>views</h4><h4 class="cyan">84,403</h4>\
                        </div></div>\
                        <div class="clearfix"></div>\
                        </div>');
                    })
                  }
                      
              },
              error: function(){},
          });
      }
      
      });