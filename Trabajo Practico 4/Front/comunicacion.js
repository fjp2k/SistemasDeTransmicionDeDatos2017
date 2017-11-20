window.idUltimaTrama = 0;
window.reintentar = true;
//window.json = "{\"mensajes\":[{\"tension\":\"1\"}],\"idUltimaMedicion\":\"2\"}";
$(document).ready(
    (function llenarTabla() {
        console.log("Llenando tabla...");
        $.ajax({
            url: 'http://localhost:5000/getTramas',
            type: "GET",
            headers: {
                'Access-Control-Allow-Origin': '*'
            },
            success: function (data) {
                console.log("(Llenar tabla)Llamada exitosa");
                $.each(data, function (key, value) {
                    fila = "<tr>"
                        + "<td>" + value.timestamp + "</td>"
                        + "<td>" + value.remitente + "</td>"
                        + "<td>" + value.temperatura + "</td>"
                        + "<td>" + value.tension + "</td>"
                        + "<td>" + value.corriente + "</td>"
                        + "<td>" + value.potencia + "</td>"
                        + "<td>" + value.presion + "</td>"
                        + "</tr>";
                    if (value.id > idUltimaTrama) {
                        idUltimaTrama = value.id;
                        console.log("(Llenar tabla)Ultimo id actualizado con: " + value.id);
                    }
                    console.log("(Llenar tabla)Imprimiendo trama con id: " + window.idUltimaTrama);
                    $("#tabla").append(fila);
                })
                filtrarTabla()
                actualizar();
            },
            error: function (response) {
                console.error("(Llenar tabla)Error obtieniendo datos iniciales");
                var r = confirm("Error al cargar datos. Desea re intentar?");
                if (r == true) {
                    llenarTabla();
                }
            }
        })
    })()
)

function actualizar() {
    console.log("Actualizando tabla. Ultimo id: " + window.idUltimaTrama);
    $.ajax({
        url: 'http://localhost:5000/getUltimasTramas', //acá tiene q ir la url de la llamada actualizar
        dataType: "json",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            "id": window.idUltimaTrama
        }),
        success: function (data) {
            console.log("(Actualizar datos)Llamada exitosa");
            $.each(data, function (key, value) {
                fila = "<tr>"
                    + "<td>" + value.timestamp + "</td>"
                    + "<td>" + value.remitente + "</td>"
                    + "<td>" + value.temperatura + "</td>"
                    + "<td>" + value.tension + "</td>"
                    + "<td>" + value.corriente + "</td>"
                    + "<td>" + value.potencia + "</td>"
                    + "<td>" + value.presion + "</td>"
                    + "</tr>";
                if (value.id > idUltimaTrama) {
                    idUltimaTrama = value.id;
                    console.log("(Actualizar datos)Ultimo id actualizado con: " + value.id);
                }
                console.log("(Actualizar datos)Imprimiendo trama con id: " + window.idUltimaTrama);
                $("#tabla").append(fila);
            });
            filtrarTabla()
        },
        error: function (data) {
            console.error("(Actualizar datos)Error actualizando tabla");
            window.reintentar = confirm("Error al actualizar datos. Desea re intentar?");
        },
        complete: function () {
            // Schedule the next request when the current one's complete
            if (window.reintentar == true) {
                setTimeout(actualizar, 5000);
            }
        }
    });
}

function filtrarTabla() {
    // Declarar las variables
    var input, filter, table, tr, td, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("tabla");
    tr = table.getElementsByTagName("tr");
    console.log("Filtrando tabla con datos: " + filter);
    // Recorrer todas las filas y eliminar las que no corresponden
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}