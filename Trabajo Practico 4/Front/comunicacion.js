window.idUltimaPeticion = 1;
$(document).ready(
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
                idUltimaPeticion=data.idUltimaPeticion;//acá pensé q en el json que mandás sea con la estructura {"mensaje":[{"tension":"1",....}],"idUltimaPeticion":"1"}
                },
               error: function(response){
                   alert("error al llenar tabla"); // <------ If errors occurs trigger an alert
               }
             })}                     
        ),
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
                    alert("error al actualizar: "+ idUltimaPeticion);
                },
                complete: function() {
                // Schedule the next request when the current one's complete
                setTimeout(actualizar, 5000);
                }
            });
        })()
        )