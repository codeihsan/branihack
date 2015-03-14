$('.btn').on('click', function() {
	$.get( "/image", function( data ) {
		console.log(data);
		// var a = $('<img>').attr('src', data);
		// console.log(a);
		// $('#results').append(a);
	});
});
