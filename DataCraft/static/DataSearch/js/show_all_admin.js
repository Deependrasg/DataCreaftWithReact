$(document).ready(function() {
    $.ajax({
        type: "GET",
        url:"show-all-admin/",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(result) {
            var userlist = result;
            var dataTab = $.parseJSON(JSON.stringify(userlist));
            $('#max_page').val(dataTab.max_page)
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
           var innerArray = [value.id,full_name,value.user_role,value.email, Staff,actions,value.department,
                               value.is_active,value.is_active];
           outterArray.push(innerArray);
       });
       $('#contact_table').dataTable({
           "destroy":true,
           "aaData": outterArray,
           "aoColumns": [
               { "sTitle": "ID" },
               { "sTitle": "Full Name"},
               { "sTitle": "User Role" },
               { "sTitle": "Email" },
               { "sTitle": "Is Staff" },
               { "sTitle": "Action"},
               { "sTitle": "Department" },
               { "sTitle": "Active" },
               { "sTitle": "Active1" },   

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


function deleteUser(id){
    swal({
        title: "Are you sure ",
        text: "You want to delete User ?",
        type: "info",
        showCancelButton: true,
        },
        function(){
            $.ajax({
                  type: "GET",
                  url:"delete-admin/"+id+"/",
                  contentType: "application/json; charset=utf-8",
                  dataType: "json",
                  success: function(result) {
                    if (result.status=='success'){
                      setTimeout(function() {
                            swal({
                                title: "Removed Successfully.",
                                type: "success",
                                showCancelButton: false,
                                showConfirmButton: false,
                                closeOnConfirm: false,
                                timer: 2000,
                            });
                        }, 500);
                    show_value(result)
                    }
                    else{
                      setTimeout(function() {
                            swal({
                                title: "Permission denied.",
                                type: "error",
                                showCancelButton: false,
                                showConfirmButton: false,
                                closeOnConfirm: false,
                                timer: 2000,
                            });
                        }, 500);


                    }
                },
        })
    }); 
}





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