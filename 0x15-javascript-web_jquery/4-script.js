$(document).ready(function() {
	$('div#toggle_header').click(function() {
		if ($('header').hasClass('red')) {
			$('header').removeClass('red').addClass('green');
	a	} else {
			$('header').removeClass('green').addClass('red');
		}
	});
});
