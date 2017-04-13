$(document).ready(function(){
    var sendMessage = function(){
    	data = $('#message').val().trim();
    	$('#message').val('');	

    	if (data != '')
    		socket.onopen = function() {
    		    socket.send(data);
    		}

    	// Call onopen directly if socket is already open
    	if (socket.readyState == WebSocket.OPEN) socket.onopen();
    };	

    socket.onmessage = function(e) {
    	message = '';
        message = message + '<div class="row"><div class="col-lg-12"><div class="media"><a class="pull-left" href="#"><img class="media-object img-circle" src="http://lorempixel.com/30/30/people/1/" alt=""></a><div class="media-body"><p>'+ e.data +'</p></div></div></div></div><hr>';
        $('.chat-box').append(message);
    }

    $('#send').click(function(){
    	sendMessage()
    });

    $('#message').keypress(function(e){
    	if (e.which == 13){
    		e.preventDefault();
    		sendMessage();
    	}
    });
});