window.idUltimaTrama = 0;
//window.json = "{\"mensajes\":[{\"tension\":\"1\"}],\"idUltimaMedicion\":\"2\"}";
$(document).ready(
    (function llenarTabla(){
        $.ajax({
               url: 'http://localhost:5000/getTramas', 
               type: "GET",
               headers: {
                    'Access-Control-Allow-Origin': '*'
                },
               success: function(data){
                 alert("exito");
                 $.each(data, function(key,value){
                fila = "<tr>"+"<td>"+value.timestamp+"</td>"
                +"<td>"+value.remitente+"</td>"+
                +"<td>"+value.temperatura+"</td>"+
                +"<td>"+value.tension+"</td>"+
                +"<td>"+value.corriente+"</td>"+
                +"<td>"+value.potencia+"</td>"+
                +"<td>"+value.presion+"</td>"+
                "</tr>";
                if (value.id > idUltimaTrama){
                        idUltimaTrama = value.id;
                }
                alert(idUltimaTrama);
                $("#tabla").append(fila);
                })
                },
               error: function(response){
                   alert("error al llenar tabla"); // <------ If errors occurs trigger an alert
               }
             })}                     
        )(),
    (function actualizar(){
        $.ajax({
                url: 'http://localhost:5000/getUltimasTramas', //acá tiene q ir la url de la llamada actualizar
                dataType:"json",
                type: "POST",
                data: { 
                        id: window.idUltimaTrama
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
                idUltimaTrama=data.idUltimaTrama;//guardo la última petición
             },
                error: function(data){
                    alert("error al actualizar: "+ window.idUltimaTrama);
                },
                complete: function() {
                // Schedule the next request when the current one's complete
                setTimeout(actualizar, 5000);
                }
            });
        })()
        )