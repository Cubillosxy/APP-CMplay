$(document).ready(function() {
	//$(html), '. todas las clases con ese tag'
	$('.btn-canciones').on('click', function(e) {
	//$('.btn-canciones').click(function(e){
		e.preventDefault();  //evitamos que se abra el link

		var self = $(this);
		var url = $(this).attr('href');
		$.getJSON(url, function(res) {
				if (res.success) {
					//$('.glyphicon-star-empty', self).toggleClass('active');
					$('.glyphicon-star-empty',self).remove();
					for (var i = 0; i < res.ratin; i = i + 1) {
						$( "#start" ,self).append('<span class="glyphicon glyphicon-star"> </span>');
					}
				}
			});

		return false;
	});
});