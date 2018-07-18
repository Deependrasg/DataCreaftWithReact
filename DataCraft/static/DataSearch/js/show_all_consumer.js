$(document).ready(function() {
    $.ajax({
        type: "GET",
        url:"show-all-consumer/",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(result) {
            var userlist = result;
            var dataTab = $.parseJSON(JSON.stringify(userlist));
            show_value(dataTab)
                
        },
        error: function(){},
    });
});


function show_value(result,contact_type){

   if (result != "[]") {
       var userlist = result;
       var dataTab = $.parseJSON(JSON.stringify(userlist));
       var outterArray = [];
       
       $.each(dataTab.data, function (index, value) {
           var actions = "<ul class='action-icon' >\
                       <li><a href='javascript:void(0);' onclick='deleteUser("+value.id+")'\
                               class='btn' title='Remove Client From Database'><i class='fa fa-trash-o' ></i></a>\</li>\
                       <li><a href='javascript:void(0);' onclick='EditClient("+value.id+")' class='btn' title='Edit Client Detail'><i class='fa fa-edit' ></i></a></li>\
                       </ul>";
           var full_name=value.first_name+" "+value.last_name;
           if(value.email){
               email="<a href='#' title='"+value.email+"' class='btn default btn-xs purple tooltip'>\
               <i class='fa fa-envelope'></i> Email </a"
           }

           var Staff
           if (value.is_staff==false){
            var Staff= "<label class='switch' ><input type='checkbox' >\
                    <span class='slider round'></span></label>"
                    }
            else{
              var Staff= "<label class='switch' ><input type='checkbox' checked>\
                    <span class='slider round'></span></label>"
            }


          var super_consumer
           if (value.Super_consumer==false){
            var super_consumer= "<label class='switch' ><input type='checkbox' href='javascript:void(0);' onclick='consumer("+value.id+','+value.Super_consumer+")'>\
                    <span class='slider round'></span></label>"
                    }
            else{
              var super_consumer= "<label class='switch'><input type='checkbox'  href='javascript:void(0);' onclick='consumer("+value.id+','+value.Super_consumer+")' checked>\
                    <span class='slider round'></span></label>"
            }

           var innerArray = [value.id,full_name,value.user_role,super_consumer, Staff,actions,value.department,
                               value.email,value.is_active];
           outterArray.push(innerArray);
       });
       $('#contact_table').dataTable({
           "destroy":true,
           "aaData": outterArray,
           "aoColumns": [
               { "sTitle": "ID" },
               { "sTitle": "Full Name"},
               { "sTitle": "User Role" },
               { "sTitle": "Super Consumer" },
               { "sTitle": "Is Staff" },
               { "sTitle": "Action"},
               { "sTitle": "Department" },
               { "sTitle": "Email" },
               { "sTitle": "Active" },   

            ],
           "fnRowCallback": function( nRow, aData, iDisplayIndex, iDisplayIndexFull ) {
               // $(nRow).attr('data-href', "general-"+contact_type+"");
           },
           "pageLength": 5,
           "lengthMenu": [
                   [1, 5, 10, 15, 20, -1],
                   [1, 5, 10, 15, 20, "All"] // change per page values here
               ],
           })
   }
}

function consumer(id,parameter){
  $.ajax({
        type: "GET",
        url:"manage-consumer-type/",
        contentType: "application/json; charset=utf-8",
        data:{'parameter':parameter,'id':id},
        dataType: "json",
        success: function(result) {
            if(result.status='success')
            {
              setTimeout(function() {
                swal({
                      title: "Consumer Type Change Successfully.",
                      type: "success",
                      showCancelButton: false,
                      showConfirmButton: false,
                      closeOnConfirm: false,
                      timer: 2000,
                  });
              }, 500);
            }
            else{

            }           
        },
        error: function(){},
  });
}

// $('.switch input[type=checkbox]').change(function() { 
// alert('sadfadsf')
//    });

// function deleteUser(id) {
//     $.ajax({
//         type: "GET",
//         url:"delete-user/"+id+"/",
//         contentType: "application/json; charset=utf-8",
//         dataType: "json",
//         success: function(result) {
//             if (status='success'){
//                 var userlist = result;
//                 var dataTab = $.parseJSON(JSON.stringify(userlist));
//                 $('#max_page').val(dataTab.max_page)
//                 show_value(dataTab)
//                 }
//             else{
//               alert('Data Not found')
//             }
//         },
//         error: function(){},
//     });
// }


// function EditClient(id){
//   $("#userid").val(id);
//   $('#myModal').modal('show')
// }

// $('#form1').submit(function (e){
//    var user_role=$('#sel1').val()
//    var user_id=$('#userid').val()
//    var form=$('#form1').val()
//    if (user_role != "Select User Role"){
//         $.ajax({
//         type: "GET",
//         url:"user-role/",
//         contentType: "application/json; charset=utf-8",
//         data:{'user_role':user_role,'id':user_id},
//         dataType: "json",
//         success: function(result) {
//             if (status='success'){
//                 var userlist = result;
//                 var dataTab = $.parseJSON(JSON.stringify(userlist));
//                 $('#max_page').val(dataTab.max_page)
//                 show_value(dataTab)
//                 }
//             else{
//               alert('Data Not found')
//             }
//         },
//         error: function(){},
//     });
    
//    }else{
//     return false;
//    }
// });


// function validate_user(id){
//       $.ajax({
//         type: "GET",
//         url:"validate-user/"+id+"/",
//         contentType: "application/json; charset=utf-8",
//         dataType: "json",
//         success: function(result) {
//             if (status='success'){
//                 var userlist = result;
//                 var dataTab = $.parseJSON(JSON.stringify(userlist));
//                 $('#max_page').val(dataTab.max_page)
//                 show_value(dataTab)
//                 }
//             else{
//               alert('Data Not found')
//             }
//         },
//         error: function(){},
//     });
// }