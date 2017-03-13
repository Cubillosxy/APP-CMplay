
var CancionesPage = {
	init: function() {
		this.bindEvents();
	},

	bindEvents: function() {
		$('.btn-canciones').on('click', function(e) {
			e.preventDefault();  //evitamos que se abra el link

			var self = $(this);
			var url = $(this).attr('href');
			$.getJSON(url, function(result) {
                //solo la llamamos para recuperar el valor.
			});

			return false;
		});
	}
};

$(document).ready(function() {
    CancionesPage.init();
});