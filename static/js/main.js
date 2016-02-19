$(document).ready(function() {
	var table = $('#get_personal').dataTable({
		"columnDefs":[
		{"className":"center","targets":[0,6,7]}
		]
	});
	var table_personal = $('#table_personal').dataTable();
	var date = new Date();
	$.getJSON('/get_all_personal/',{"year": date.getFullYear(),"month":date.getMonth()}, function(json, textStatus) {
			table.fnClearTable();
			$.each(json,function(index, el) {
				var arr = [];
				arr.push('<a href="#personal_asis" data-toggle="modal" ><i class="fa fa-eye" data-id="'+el.id+'""></i></a>');
				arr.push('<a href="#personal_view" data-toggle="modal" ><i class="fa fa-eye" data-id="'+el.id+'""></i></a>');
				arr.push('<i class="fa fa-pencil" data-id="'+el.id+'""></i>');
				arr.push(el.cedula);
				arr.push(el.nombres);
				arr.push(el.apellidos);
				arr.push(el.telefono1);
				arr.push(el.direccion);
				arr.push('<a href="#motivos" data-toggle="modal" ><i class="fa fa-check"></i></a>');
				arr.push('<a href="#condicion" data-toggle="modal"><i class="fa fa-times"></i></a>');
				table.fnAddData(arr);
			});
	});
	
});