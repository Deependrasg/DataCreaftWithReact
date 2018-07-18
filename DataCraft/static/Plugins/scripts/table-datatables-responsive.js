var lang = window.location.pathname.split('/')[1];
var oTable;

var TableDatatablesResponsive = function () {

    var initDataListTable = function () {
        var table = $('.data_list_table');

        // switch (lang) {
        //     case "en":
        //         lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json";
        //         break;
        //     case "de":
        //         lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/German.json";
        //         break;
        //     case "ro":
        //         lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/Romanian.json";
        //         break;
        //     default:
        //         lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json";
        // }

        oTable = table.dataTable({
            // "language": {
            //    url: lang_url
            // },
            
            // setup buttons extentension: http://datatables.net/extensions/buttons/
            buttons: [],

            // setup responsive extension: http://datatables.net/extensions/responsive/
            responsive: {
                details: {
                   
                }
            },

            "order": [
                [0, 'asc']
            ],
            
            "lengthMenu": [
                [1, 5, 10, 15, 20, -1],
                [1, 5, 10, 15, 20, "All"] // change per page values here
            ],
            // set the initial value
            "pageLength": 5,

            "dom": "<'row' <'col-md-12'B>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r><'table-scrollable't><'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>", // horizobtal scrollable datatable

            // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
            // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/plugins/datatables/plugins/bootstrap/dataTables.bootstrap.js). 
            // So when dropdowns used the scrollable div should be removed. 
            //"dom": "<'row' <'col-md-12'T>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r>t<'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>",
        });
    }

     var relativeTable = function () {
        var table = $('.relative_table');

        switch (lang) {
            case "en":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json";
                break;
            case "de":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/German.json";
                break;
            case "ro":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/Romanian.json";
                break;
            default:
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json";
        }

        oTable = table.dataTable({
            "language": {
               url: lang_url
            },
            
            // setup buttons extentension: http://datatables.net/extensions/buttons/
            buttons: [],

            // setup responsive extension: http://datatables.net/extensions/responsive/
            responsive: {
                details: {
                   
                }
            },

            "order": [
                [0, 'asc']
            ],
            
            "lengthMenu": [
                [5, 10, 15, 20, -1],
                [5, 10, 15, 20, "All"] // change per page values here
            ],
            // set the initial value
            "pageLength": 5,

            "dom": "<'row' <'col-md-12'B>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r><'table-scrollable't><'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>", // horizobtal scrollable datatable

            // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
            // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/plugins/datatables/plugins/bootstrap/dataTables.bootstrap.js). 
            // So when dropdowns used the scrollable div should be removed. 
            //"dom": "<'row' <'col-md-12'T>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r>t<'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>",
        });
    }

    var staffTable = function () {
        var table = $('.staff_table');
  
        switch (lang) {
            case "en":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json";
                break;
            case "de":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/German.json";
                break;
            case "ro":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/Romanian.json";
                break;
            default:
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json";
        }

        oTable = table.dataTable({
            "language": {
               url: lang_url
            },
            
            // setup buttons extentension: http://datatables.net/extensions/buttons/
            buttons: [],

            // setup responsive extension: http://datatables.net/extensions/responsive/
            responsive: {
                details: {
                   
                }
            },

            "order": [
                [0, 'asc']
            ],
            
            "lengthMenu": [
                [5, 10, 15, 20, -1],
                [5, 10, 15, 20, "All"] // change per page values here
            ],
            // set the initial value
            "pageLength": 5,

            "dom": "<'row' <'col-md-12'B>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r><'table-scrollable't><'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>", // horizobtal scrollable datatable

            // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
            // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/plugins/datatables/plugins/bootstrap/dataTables.bootstrap.js). 
            // So when dropdowns used the scrollable div should be removed. 
            //"dom": "<'row' <'col-md-12'T>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r>t<'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>",
        });
    }
    
    var relativePatientTable = function () {
        var table = $('#relativePatientTable');

        switch (lang) {
            case "en":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json";
                break;
            case "de":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/German.json";
                break;
            case "ro":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/Romanian.json";
                break;
            default:
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json";
        }

        oTable = table.dataTable({
            "language": {
               url: lang_url
            },
            
            // setup buttons extentension: http://datatables.net/extensions/buttons/
            buttons: [],

            // setup responsive extension: http://datatables.net/extensions/responsive/
            responsive: {
                details: {
                   
                }
            },

            "order": [
                [0, 'asc']
            ],
            
            "lengthMenu": [
                [5, 10, 15, 20, -1],
                [5, 10, 15, 20, "All"] // change per page values here
            ],
            // set the initial value
            "pageLength": 5,

            "dom": "<'row' <'col-md-12'B>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r><'table-scrollable't><'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>", // horizobtal scrollable datatable

            // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
            // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/plugins/datatables/plugins/bootstrap/dataTables.bootstrap.js). 
            // So when dropdowns used the scrollable div should be removed. 
            //"dom": "<'row' <'col-md-12'T>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r>t<'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>",
        });
    }
    
    var doctorPatientTable = function () {
        var table = $('.doctorPatientTable');
   
        switch (lang) {
            case "en":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json";
                break;
            case "de":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/German.json";
                break;
            case "ro":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/Romanian.json";
                break;
            default:
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json";
        }

        oTable = table.dataTable({
            "language": {
               url: lang_url
            },
            
            // setup buttons extentension: http://datatables.net/extensions/buttons/
            buttons: [],

            // setup responsive extension: http://datatables.net/extensions/responsive/
            responsive: {
                details: {
                   
                }
            },

            "order": [
                [0, 'asc']
            ],
            
            "lengthMenu": [
                [5, 10, 15, 20, -1],
                [5, 10, 15, 20, "All"] // change per page values here
            ],
            // set the initial value
            "pageLength": 5,

            "dom": "<'row' <'col-md-12'B>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r><'table-scrollable't><'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>", // horizobtal scrollable datatable

            // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
            // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/plugins/datatables/plugins/bootstrap/dataTables.bootstrap.js). 
            // So when dropdowns used the scrollable div should be removed. 
            //"dom": "<'row' <'col-md-12'T>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r>t<'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>",
        });
    }

    var doctorAddressTable = function () {
        var table = $('.address_table');
  
        switch (lang) {
            case "en":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json";
                break;
            case "de":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/German.json";
                break;
            case "ro":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/Romanian.json";
                break;
            default:
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json";
        }

        oTable = table.dataTable({
            "language": {
               url: lang_url
            },
            
            // setup buttons extentension: http://datatables.net/extensions/buttons/
            buttons: [],

            // setup responsive extension: http://datatables.net/extensions/responsive/
            responsive: {
                details: {
                   
                }
            },

            "order": [
                [0, 'asc']
            ],
            
            "lengthMenu": [
                [5, 10, 15, 20, -1],
                [5, 10, 15, 20, "All"] // change per page values here
            ],
            // set the initial value
            "pageLength": 5,

            "dom": "<'row' <'col-md-12'B>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r><'table-scrollable't><'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>", // horizobtal scrollable datatable

            // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
            // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/plugins/datatables/plugins/bootstrap/dataTables.bootstrap.js). 
            // So when dropdowns used the scrollable div should be removed. 
            //"dom": "<'row' <'col-md-12'T>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r>t<'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>",
        });
    }

    var hospitalTable = function () {
        var table = $('.hospital_table');
 
        switch (lang) {
            case "en":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json";
                break;
            case "de":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/German.json";
                break;
            case "ro":
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/Romanian.json";
                break;
            default:
                lang_url = "//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json";
        }

        oTable = table.dataTable({
            "language": {
               url: lang_url
            },
            
            // setup buttons extentension: http://datatables.net/extensions/buttons/
            buttons: [],

            // setup responsive extension: http://datatables.net/extensions/responsive/
            responsive: {
                details: {
                   
                }
            },

            "order": [
                [0, 'asc']
            ],
            
            "lengthMenu": [
                [5, 10, 15, 20, -1],
                [5, 10, 15, 20, "All"] // change per page values here
            ],
            // set the initial value
            "pageLength": 5,

            "dom": "<'row' <'col-md-12'B>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r><'table-scrollable't><'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>", // horizobtal scrollable datatable

            // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
            // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/plugins/datatables/plugins/bootstrap/dataTables.bootstrap.js). 
            // So when dropdowns used the scrollable div should be removed. 
            //"dom": "<'row' <'col-md-12'T>><'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r>t<'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>",
        });
    }
    
    return {

        //main function to initiate the module
        init: function () {

            if (!jQuery().dataTable) {
                return;
            }

            initDataListTable();
            relativePatientTable();
            doctorPatientTable();
            doctorAddressTable();
            hospitalTable();
            relativeTable();
            staffTable();
        }
    };
}();

jQuery(document).ready(function() {
    TableDatatablesResponsive.init();
});
