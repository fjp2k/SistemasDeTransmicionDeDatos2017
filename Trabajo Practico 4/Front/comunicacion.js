$(document).ready(
    (function(){
        alert("hola");
        alert("chau");
    $.ajax({
               url: "C:\Users\Facundo Ciancio\Desktop\prueba.txt", 
               datatype: "text",  // <---- For example
               success: function(response){ // response is returned by server 
                   alert("ajax");  // <------ Here you add rows updated on table
               },
               error: function(response){
                   alert("error"); // <------ If errors occurs trigger an alert
               },
             });
            
        }))