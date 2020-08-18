// Only execute when page is loaded completely
$(document).ready(function() {
    //function to auto set the height of the text area when query length increases
	$('textarea').on('input', function () { 
		this.style.height = 'auto'; 
		  
		this.style.height =  
				(this.scrollHeight) + 'px'; 
	}); 

//function which handles the generate new text button by sending ajax post request
	$('#gen').on('click', function(event) {
        // making post request with the value of textarea  to /gen route
		$.ajax({
			data : {
				text:$('#textarea1').val()
			},
			type : 'POST',
			url : '/gen'
		})
		.done(function(data) {
        //   when the post request is succesful displayng the more button and the output
            if(data.text)
            {   $("#textdiv").show()
                $("#textoutput").text(data.text);
                $("#more").show()
            }

		});

		event.preventDefault();

	});
	// function which handles the generate new text button by sending ajax post request
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
            {   
                $("#textoutput").text(data.text);
                $("#more").show()
            }

		});

		event.preventDefault();

	});

});