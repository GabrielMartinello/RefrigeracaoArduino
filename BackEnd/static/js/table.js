$(document).ready(function() {
    montaDadosTable();
});

function montaDadosTable() {
    $.ajax({
        url: 'http://localhost:5000/temperatura',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            // Limpar e destruir a DataTable antes de adicionar novas linhas
            tabela = $('#table').DataTable()

            paginaAtiva = tabela.page();
            console.log('Pag: ', paginaAtiva)

            tabela.clear();

            for (let i = 0; i < data.length; i++) {
                var temp = data[i];
                tabela.row.add([
                    temp.id,
                    '<p class="status ' +
                        (temp.temperatura >= 25 ? 'cancelled' : (temp.temperatura >= 20 && temp.temperatura <= 24 ? 'delivered' : 'shipped')) +
                        '">' + temp.temperatura + '</p>',
                    temp.umidade,
                    temp.data,
                    '<button id="botaoExcluir" class="myButton" onclick="excluirRegistro(' + temp.id + ')">Excluir</button>'
                ]).draw();

                tabela.page(paginaAtiva).draw(false)
            }
            setTimeout(montaDadosTable, 10000);
        }
    });

}

function excluirRegistro(id) {
    $.ajax({
        url: 'http://localhost:5000/temperaturas/' + id,
        type: 'DELETE',
        dataType: 'json',
        success: function () {
            montaDadosTable()
        }
    });
}