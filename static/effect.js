$(document).ready(function() {
	$('textarea').on('input', function () { 
		this.style.height = 'auto'; 
		  
		this.style.height =  
				(this.scrollHeight) + 'px'; 
	}); 

	$('#gen').on('click', function(event) {
        
		$.ajax({
			data : {
				text:$('#textarea1').val()
			},
			type : 'POST',
			url : '/gen'
		})
		.done(function(data) {
          
            if(data.text)
            {   $("#textdiv").show()
                $("#textoutput").text(data.text);
                $("#more").show()
            }

		});

		event.preventDefault();

    });
    $('#more').on('click', function(event) {
        
		$.ajax({
			data : {
				text:$('#textoutput').text()
			},
			type : 'POST',
			url : '/gen'
		})
		.done(function(data) {
       
            if(data.text)
            {   data.text=data.text.replace('<|endoftext|>','');
                $("#textoutput").text(data.text);
                $("#more").show()
            }

		});

		event.preventDefault();

	});

});