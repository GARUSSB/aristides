$(document).ready(function() {
	var table = $('#get_personal').dataTable({
		"columnDefs":[
		{"className":"center","targets":[0,1,2,3,4]}
		],
		responsive: true
	});
	new $.fn.dataTable.Responsive( table );
	var table_personal = $('#table_personal').dataTable();
	var date = new Date();
	$.getJSON('/get_all_personal/',{"year": date.getFullYear(),"month":date.getMonth()}, function(json, textStatus) {
			table.fnClearTable();
			$.each(json,function(index, el) {
				var arr = [];
				arr.push('<a href="#personal_asis" data-toggle="modal" ><i class="fa fa-eye" data-id="'+el.id+'""></i></a>');
				arr.push('<a href="#personal_view" data-toggle="modal" ><i class="fa fa-calendar-plus-o" data-id="'+el.id+'""></i></a>');
				arr.push('<a href="#motivos" data-toggle="modal" ><i class="fa fa-check"></i></a>');
				arr.push('<a href="#condicion" data-toggle="modal"><i class="fa fa-times"></i></a>');
				arr.push('<i class="fa fa-pencil" data-id="'+el.id+'""></i>');
				arr.push(el.cedula);
				arr.push(el.nombres);
				arr.push(el.apellidos);
				arr.push(el.telefono1);
				arr.push(el.direccion);
				table.fnAddData(arr);
			});
	});
});
function set_person(){
	data = $('#new_person').serialize();
	console.log(data);
	$.ajax({
		url: 'crear_personal/',
		type: 'POST',
		data: data,
		beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
	})
	.done(function() {
		console.log("success");
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}