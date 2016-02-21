$(document).ready(function() {
	window.table = $('#get_personal').dataTable({
		dom: 'Bfrtip',
		 buttons: [
            'excel', 'pdf', 'print'
        ],
		"columnDefs":[
		{"className":"center","targets":[0,1,2,3,4]}
		],
		responsive: true,
	});
	window.jobs = $('#get_job').dataTable({
		responsive: true,
	});
	window.filter = $('#get_asis_filter').dataTable({
		dom: 'Bfrtip',
		 buttons: [
            'excel', 'pdf', 'print'
        ],
		responsive: true,
	});
	window.personal_asis = $('#get_personal_asis').dataTable({
		responsive: true,
		dom: 'Bfrtip',
		 buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
	});
	get_all_personal();
	new $.fn.dataTable.Responsive( personal_asis );
	new $.fn.dataTable.Responsive( jobs );
	$('.asistencia').on('click', function() {
		var $val = $(this).data('value');
		set_personal_asis($val);
	});
	$('#personal_asis').on('show.bs.modal',get_personal_asis);
	$('#job').on('show.bs.modal',get_cargo);
	$('select').select2();
	$('.date-picker').datepicker();
	$('#edit_cargo').on('show.bs.modal', set_input_job);
});
function set_input_job () {
	$.getJSON('/get_job', {id: jobid}, function(json) {
		$('#nombre_cargo').val(json.name);
	});
}
function set_person(){
	data = $('#new_person input,#new_person select').serialize();
	console.log(data);
	$.ajax({
		url: '/crear_personal/',
		type: 'POST',
		data: data,
		beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
	})
	.done(function() {
		OmegaNotify.success('Guardado Exitoso','');
		get_all_personal();
	})
	.fail(function() {
		OmegaNotify.fail('Error al guardar','');
	})
	.always(function() {
		$('#profile_set').modal('hide');
	});
	
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
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
function get_all_personal(){
	new $.fn.dataTable.Responsive( table );
	$.getJSON('/get_all_personal/', function(json, textStatus) {
			table.fnClearTable();
			$.each(json,function(index, el) {
				var arr = [];
				arr.push('<a href="#" data-toggle="modal" ><i class="fa fa-eye" data-id="'+el.id+'"></i></a>');
				arr.push('<a href="#personal_asis" data-toggle="modal" onclick="set_id('+el.id+')" id="'+el.id+'" data-name="'+el.nombres+'"><i class="fa fa-calendar-plus-o" data-id="'+el.id+'""></i></a>');
				arr.push('<a href="#motivos" data-toggle="modal" onclick="set_id('+el.id+')" ><i class="fa fa-check"></i></a>');
				arr.push('<a href="#condicion" data-toggle="modal" onclick="set_id('+el.id+')" ><i class="fa fa-times"></i></a>');
				arr.push('<a href="#profile_edit" data-toggle="modal" onclick="set_id('+el.id+')"><i class="fa fa-pencil"></i></a>');
				arr.push('<a href="#" onclick="drop_person('+el.id+')"><i class="fa fa-trash"></i></a>');
				arr.push(el.cedula);
				arr.push(el.nombres);
				arr.push(el.apellidos);
				arr.push(el.telefono1);
				arr.push(el.telefono2);
				arr.push(el.direccion);
				arr.push(el.email);
				arr.push(el.sexo);
				arr.push(el.cargo);
				arr.push(el.fecha_de_nacimiento);
				table.fnAddData(arr);
			});
	}).fail(function(){
		OmegaNotify.fail('Error al cargar datos','');
	});
}
function get_personal_asis(){
	var name = $('#'+personalid).data('name');
	$('#nombre_personal').text(name);
	$.getJSON('/get_personal_inacistencia/', {id_personal: personalid}, function(json, textStatus) {
		personal_asis.fnClearTable();
		$.each(json,function(index, el) {
			var arr = [],
				condicion = el.tipo.split(' ');
			arr.push(el.fecha);
			arr.push(condicion[0]);
			arr.push(condicion[1]);
			personal_asis.fnAddData(arr);
		});
	});
}
function set_personal_asis(val){
	$.ajax({
		url: '/crear_inacistencia/',
		type: 'POST',
		data: {
				id_personal: personalid,
				tipo:val
			},
		beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
	})
	.done(function() {
		$('#condicion').modal('hide');
		$('#motivos').modal('hide');
		OmegaNotify.success('Guardado Exitoso','');
	})
	.fail(function() {
		OmegaNotify.fail('Error al guardar','');
	})
	.always(function() {
		$('#condicion').modal('hide');
		$('#motivos').modal('hide');
	});
	
}
function set_id(id){
	window.personalid= id;
}
function job_id(id){
	window.jobid= id;
}
function set_job(){
	data = $('#new_job').serialize();
	$.ajax({
			url: 'crear_cargos/',
			type: 'POST',
			data: data,
			beforeSend: function(xhr) {
	            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	        }
		})
		.done(function() {
			$('#set_cargo').modal('hide');
			OmegaNotify.success('Guardado Exitoso','');
		})
		.fail(function() {
			$('#set_cargo').modal('hide');
			OmegaNotify.fail('Error al Guardar','');
		})
		.always(function() {
		});
}
function edit_job () {
	
}
function edit_person () {
	
}
function get_cargo(){
	$.getJSON('/get_cargos', function(json, textStatus) {
		jobs.fnClearTable();
		$.each(json, function(index, val) {
			var arr= [];
			arr.push('<a href="#edit_cargo" onclick="job_id('+val.id+')" data-dismiss="modal" data-toggle="modal" ><i class="fa fa-pencil"></i></a>');
			arr.push('<i onclick="drop_job('+val.id+')" class="fa fa-trash"></i>');
			arr.push(val.id);
			arr.push(val.cargo);
			jobs.fnAddData(arr);
		});
	});
}
function drop_job(id){
	$.ajax({
		url: '/drop_cargos/',
		type: 'POST',
		data: {id: id},
		beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
	})
	.done(function() {
		get_cargo();
	})
	.fail(function() {
		OmegaNotify.fail('Error al borrar','');
	})
	.always(function() {
		get_cargo();
	});
	
}
function drop_person(id){
	OmegaNotify.confirm({
			message:"",
			description:"¿Seguro que desea eliminar esta persona?",
			action:function(){
				$.ajax({
					url: '/drop_person/',
					type: 'POST',
					data: {id: id},
					beforeSend: function(xhr) {
		            	xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		        	},
				})
				.done(function() {
					get_all_personal();
				});
			}
		});
}