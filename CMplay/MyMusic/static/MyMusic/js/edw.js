
var CancionesPage = {
	init: function() {
		this.$container = $('.canciones-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},

	bindEvents: function() {
		$('.btn-canciones', this.$container).on('click', function(e) {
			e.preventDefault();

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