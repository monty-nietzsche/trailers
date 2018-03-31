 $('#trailer').click(function(event) {
  event.stopPropagation();
});
 
 
 // Pause the video when the modal is closed
 $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function(event) {
     // Remove the src so the player itself gets removed, as this is the only
     // reliable way to ensure the video stops playing in IE
     $("#trailer-video-container").empty();
	 $("#trailer").modal('hide');
	 
 });
 // Start playing the video whenever the trailer modal is opened
 $(document).on('click', '.movie-tile', function(event) {
     var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
     var movieTitle = $(this).attr('data-title')
     var movieDirector = $(this).attr('data-director')
     var movieStoryline = $(this).attr('data-storyline')
     var movieGenres = $(this).attr('data-genres')
     var movieImdb = $(this).attr('data-imdb')
     var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
     $("#movie-title").html('<div class=\"movie-title-info\">' + movieTitle + '</div> by : <span class=\"movie-director-info\">' + movieDirector + '</span> <h5>' + movieStoryline + '</h5> <h5>' + movieGenres +
         '</h5><div class=\"imdb\"><a  href=\"http://www.imdb.com/title/' + movieImdb + '/\" target="_blank">More on the movie on IMDB &nbsp; &nbsp; </a></div>');
     $("#trailer-video-container").empty().append($("<iframe></iframe>", {
         'id': 'trailer-video',
         'type': 'text-html',
         'src': sourceUrl,
         'frameborder': 0
     }));
 });
 // Animate in the movies when the page loads
 $(document).ready(function() {
     $('.movie-tile').hide().first().show("fast", function showNext() {
         $(this).next("div").show("fast", showNext);
     });
 });