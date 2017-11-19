window.idUltimaPeticion = 1;
//window.json = "{\"mensajes\":[{\"tension\":\"1\"}],\"idUltimaMedicion\":\"2\"}";
window.json = {"mensajes":[{"timestamp":"16:03","tension":"1","potencia":"2","corriente":"3","presion":"5","temperatura":"13","remitente":"pablo"}],"idUltimaPeticion":"2"};
$(document).ready(
    (function local(){
         alert(json.idUltimaPeticion);
         $.each(json.mensajes, function(key,value){
                alert ("tension" + value.tension);
                fila ="<tr>"+"<td>"+value.timestamp+"</td>"
                +"<td>"+value.remitente+"</td>"
                +"<td>"+value.temperatura+"</td>"
                +"<td>"+value.tension+"</td>"
                +"<td>"+value.corriente+"</td>"
                +"<td>"+value.potencia+"</td>"
                +"<td>"+value.presion+"</td>"
                +"</tr>";
                alert(fila);
                document.getElementById("demo").innerHTML = "Paragraph changed!";
                $("#demo").html('<p>chau</p>');
                $('#tabla tbody').append(fila);
            });
            idUltimaPeticion=json.idUltimaPeticion;//acá pensé q en el json que mandás sea con la estructura {"mensajes":[{"tension":"1",....}],"idUltimaPeticion":"1"}
                })(),
    (function llenarTabla(){
        $.ajax({
               url: 'D:\Facultad\QuintoAnio\TransmisionDeDatos\TP5\testData.json', //acá tiene que ir la url de la llamada para traer todos los datos
               dataType: "json",  // <---- For example
               success: function(data){
                 alert("exito");
                 $.each(data.mensajes, function(key,value){
                fila = "<tr>"+"<td>"+value.timestamp+"</td>"
                +"<td>"+value.remitente+"</td>"+
                +"<td>"+value.temperatura+"</td>"+
                +"<td>"+value.tension+"</td>"+
                +"<td>"+value.corriente+"</td>"+
                +"<td>"+value.potencia+"</td>"+
                +"<td>"+value.presion+"</td>"+
                "</tr>";
                $("#tabla").append(fila);
                });
                idUltimaPeticion=data.idUltimaPeticion;//acá pensé q en el json que mandás sea con la estructura {"mensajes":[{"tension":"1",....}],"idUltimaPeticion":"1"}
                },
               error: function(response){
                   alert("error al llenar tabla"); // <------ If errors occurs trigger an alert
               }
             })}                     
        )(),
    (function actualizar(){
        $.ajax({
                url: 'D:\Facultad\QuintoAnio\TransmisionDeDatos\TP5\testData.json', //acá tiene q ir la url de la llamada actualizar
                data: { 
                        idUltimaPeticion: window.idUltimaPeticion
                        },
                success: function(data){
                 alert("exito");
                 $.each(data.mensajes, function(key,value){
                fila = "<tr>"+"<td>"+value.timestamp+"</td>"
                +"<td>"+value.remitente+"</td>"+
                +"<td>"+value.temperatura+"</td>"+
                +"<td>"+value.tension+"</td>"+
                +"<td>"+value.corriente+"</td>"+
                +"<td>"+value.potencia+"</td>"+
                +"<td>"+value.presion+"</td>"+
                "</tr>";
                $("#tabla").append(fila);
                 });
                idUltimaPeticion=data.idUltimaPeticion;//guardo la última petición
             },
                error: function(data){
                    alert("error al actualizar: "+ window.idUltimaPeticion);
                },
                complete: function() {
                // Schedule the next request when the current one's complete
                setTimeout(actualizar, 5000);
                }
            });
        })()
        )