// Inicie a reinicialização dinâmica assim que a página for carregada
$(document).ready(function() {
    reiniciarPaginaDinamicamente();
});

function reiniciarPaginaDinamicamente() {
    // Simule uma requisição AJAX para obter novos dados do servidor
    $.ajax({
        url: 'http://localhost:5000/temperatura/avg',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            console.log('Página atualizada: ', data)

            // Defina um temporizador para reiniciar dinamicamente após 5 segundos (ajuste conforme necessário)
            setTimeout(reiniciarPaginaDinamicamente, 1000);
        }
    }).then(result => {
        google.charts.load('current',{packages:['corechart']});
        google.charts.setOnLoadCallback(drawChart(result));
    });
}

function drawChart(result) {
    valores = [
        ['Temperaturas', 'Temp']
    ]

    for(i =0; i < result.length; i++) {
        var temp = result[i]
        valores.push([temp.data, Number(temp.temperatura)])
    }
    
    console.log(valores)
    const options = {
        title: 'Temperaturas'
    };

    const chart = new google.visualization.BarChart(document.getElementById('myChart'));

    const dataObjects = google.visualization.arrayToDataTable(valores)
    chart.draw(dataObjects, options);
    
    valoresDataGraph = [
        ['Dia', 'Temperatura Máxima', 'Temperatura Mínima']
    ]

    for(i =0; i < result.length; i++) {
        var temp = result[i]
        valoresDataGraph.push([temp.data, Number(temp.temperaturamax), Number(temp.temperaturamin)])
    }

    const dataGraphObjects = google.visualization.arrayToDataTable(valoresDataGraph)

    // var dataGraph =  google.visualization.arrayToDataTable([
    //     ['Dia', 'Temperatura Média', 'Temperatura Máxima'],
    //     ['24/09/2023',  22,      28],
    //     ['25/09/2023',  21,      26],
    //     ['27/10/2023',  22,      29],
    //     ['24/11/2023',  25,      31]
    //   ]);

    var options2 =  {
        title: 'Gráfico de crescimento de temperaturas',
        hAxis: {title: 'Temperatura',  titleTextStyle: {color: '#333'}},
        vAxis: {minValue: 0}
        };
    const chart2 = new google.visualization.AreaChart(document.getElementById('myChart2'));
    chart2.draw(dataGraphObjects, options2);
}