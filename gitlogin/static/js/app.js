// Nav hamburger menu
  $(function() {
    $( ".icn" ).click(function() {
      $( ".men" ).toggleClass( "ladi", 500 );
    });
  });
  // Nav dropdown menu
$(function() {
    $( ".drop" ).click(function() {
      $( ".lss" ).toggleClass( "mre", 500 );
    });
  });


OAuth.initialize('HDdOYzwEsvFqqzg0LJYoVGFAE0E');
OAuth.popup('github')
   .done(function(result) {
       result.get('/me')
           .done(function (response) {
               //this will display "John Doe" in the console
               console.log(response.name);
           })
           .fail(function (err) {
               //handle error with err
           });
   })
   .fail(function (err) {
       //handle error with err
   });





OAuth.popup(provider)
    .done(function(result) {
        result.get('/me')
            .done(function (response) {
                //this will display "John Doe" in the console
                console.log(response.name);
            })
            .fail(function (err) {
                //handle error with err
            });
    })
    .fail(function (err) {
        //handle error with err
    });

//provider can be 'facebook', 'twitter', 'github', or any supported
//provider that contain the fields 'firstname' and 'lastname'
//or an equivalent (e.g. "FirstName" or "first-name")
var provider = 'github';

OAuth.popup(provider)
    .done(function(result) {
        result.me()
            .done(function (response) {
                console.log('FirstName: ', response.firstname);
                console.log('LastName: ', response.lastname);
            })
            .fail(function (err) {
                //handle error with err
            });
    })
    .fail(function (err) {
        //handle error with err
    });

result.me(['firstname', 'lastname', 'email'/*, ...*/]);