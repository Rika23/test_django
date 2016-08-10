$(document).ready(function(){
	$( "#add-another" ).click(function() {
		var formCount = parseInt($("[name='form-TOTAL_FORMS']").val());
		var newForm = $('form').find('div').last().clone();
		newForm.find('input').each(function(index, elem){
		    elem.id = elem.id.replace(/\d/g, formCount) 
		    elem.name = elem.name.replace(/\d/g, formCount)
		    elem.value = ""
		});
		$("[name='form-TOTAL_FORMS']").val(formCount + 1);
		$('form').find('div').last().after(newForm)
	});
});