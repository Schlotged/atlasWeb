function mascaraCNPJ(cnpj) {
    cnpj.value = cnpj.value
        .replace(/\D/g, '')
        .replace(/^(\d{2})(\d)/, '$1.$2')
        .replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3')
        .replace(/\.(\d{3})(\d)/, '.$1/$2')
        .replace(/(\d{4})(\d)/, '$1-$2')
        .replace(/(-\d{2})\d+?$/, '$1');
}


function mascaraMoeda(campo) {
    let valor = campo.value.replace(/\D/g, '');
    valor = valor.replace(/(\d{1,})(\d{2})$/, '$1,$2');
    valor = valor.replace(/(\d)(?=(\d{3})+(\D|$))/g, '$1.');
    campo.value = valor;
}

$(document).ready(function() {
    $('#datEmi').on('change', function() {
        var dataInicial = $(this).val();

        // Define a data mínima para o input de data final
        $('#datPag').attr('min', dataInicial);
    });
});


$(document).ready(function() {

    function calcularValorTotal() {

        var quantidade = parseFloat($('input[name="quantidade-produto"]').val()) || 0;
        var valorUnitario = parseFloat($('input[name="valor_unitario"]').val().replace(/\./g, '').replace(',', '.')) || 0;

        var valorTotal = quantidade * valorUnitario;

        $('input[name="valor-total-produto"]').val(valorTotal.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
    }

    $('input[name="quantidade-produto"], input[name="valor_unitario"]').on('input', function() {
        calcularValorTotal();
    });
});


// Busca prestador
$(document).ready(function() {
    // Função para buscar prestador
    $('#buscar-prestador-btn').click(function() {
        var cnpj = $('#cnpj-input').val();

        if (cnpj){

            $('#loadingModal').modal('show');
            $.ajax({
                url: buscarPrestadorUrl,
                type: "POST",
                data: {
                    'cnpj': cnpj,
                    csrfmiddlewaretoken: csrfToken
                },
                success: function(response) {
                    if (response.options && response.options.length > 1) {
                        // Preenche a tabela com as opções
                        var optionsHtml = response.options.map(function(option) {
                            return `
                                <tr>
                                    <td>${option.nome}</td>
                                    <td>${option.codigo}</td>
                                    <td>${option.cnpj}</td>
                                    <td><button class="btn btn-primary select-option-prestador" data-codigo="${option.codigo}" data-nome="${option.nome}">Selecionar</button></td>
                                </tr>
                            `;
                        }).join('');
                        
                        $('#optionsModalBody').html(optionsHtml);
                        $('#optionsModal').modal('show');
                    } else if (response.nome_prestador) {
                        // Atualiza o input com nome e código
                        $('#prestador-input').val(`${response.codigo} - ${response.nome_prestador}`);
                        $('#loadingModal').modal('hide');
                        $('#successModal').modal('show');
                        setTimeout(function() {
                            $('#successModal').modal('hide');
                        }, 1000);
                    }
                },
                error: function() {
                    $('#loadingModal').modal('hide');
                    alert('Erro ao buscar prestador');
                }
            });
        } else {
            alert('Campo CNPJ prestador não pode ser nulo');
        }
    });

    $(document).on('click', '.select-option-prestador', function(event) {
        event.preventDefault();
        $('#loadingModal').modal('hide');
        var codigo = $(this).data('codigo');
        var nome = $(this).data('nome');
        $('#prestador-input').val(`${codigo} - ${nome}`);
        
        $('#optionsModal').modal('hide');
    });
});


// Busca cliente
$(document).ready(function() {
    // Função para buscar cliente
    $('#buscar-cliente-btn').click(function() {
        var cnpj = $('#cnpj-input-cliente').val();

        if (cnpj){

            $('#loadingModal').modal('show');
            $.ajax({
                url: buscarClienteUrl,
                type: "POST",
                data: {
                    'cnpj': cnpj,
                    csrfmiddlewaretoken: csrfToken
                },
                success: function(response) {
                    if (response.options && response.options.length > 1) {
                        // Preenche a tabela com as opções
                        var optionsHtml = response.options.map(function(option) {
                            return `
                                <tr>
                                    <td>${option.nome}</td>
                                    <td>${option.codigo}</td>
                                    <td>${option.cnpj}</td>
                                    <td><button class="btn btn-primary select-option-cliente" data-codigo="${option.codigo}" data-nome="${option.nome}">Selecionar</button></td>
                                </tr>
                            `;
                        }).join('');
                        
                        $('#optionsModalBody').html(optionsHtml);
                        $('#optionsModal').modal('show');
                    } else if (response.nome_cliente) {
                        // Atualiza o input com nome e código
                        $('#cliente-input').val(`${response.codigo} - ${response.nome_cliente}`);
                        
                        $('#loadingModal').modal('hide');
                        $('#successModal').modal('show');
                        setTimeout(function() {
                            $('#successModal').modal('hide');
                        }, 1000);
                    }
                },
                error: function() {
                    $('#loadingModal').modal('hide');
                    alert('Erro ao buscar cliente');
                }
            });
        } else {
            alert('Campo CNPJ cliente não pode ser nulo');
        }
    });

    // Manipula a seleção de uma opção da tabela para cliente
    $(document).on('click', '.select-option-cliente', function(event) {
        event.preventDefault();
        $('#loadingModal').modal('hide');
        var codigo = $(this).data('codigo');
        var nome = $(this).data('nome');
        $('#cliente-input').val(`${codigo} - ${nome}`);
        
        $('#optionsModal').modal('hide');
    });
});

// Envia requisição senior
$(document).ready(function() {
    $('#ordemCompraForm').submit(function(event) {
        event.preventDefault();

        var formDataArray = $(this).serializeArray();
        var allFieldsFilled = true;

        formDataArray.forEach(function(field) {
            var inputElement = $('[name="' + field.name + '"]');
            
            if (field.name !== 'csrfmiddlewaretoken' && field.value.trim() === '') {
                inputElement.css('border', '2px solid red');
                allFieldsFilled = false;
            } else {
                inputElement.css('border', ''); // Remove a borda vermelha se o campo estiver preenchido
            }
        });

        if (!allFieldsFilled) {
            alert('Por favor, preencha todos os campos obrigatórios.');
            return;
        }

        var formData = $(this).serialize();
        console.log(formData);

        $.ajax({
            url: sendOrdemCompra,
            type: "POST",
            data: formData,
            success: function(response) {

                // Exibe o modal de sucesso
                $('#successModal').modal('show');

                setTimeout(function() {
                    $('#successModal').modal('hide');
                    
                    // Aguarda 3 segundos antes de redirecionar
                    setTimeout(function() {
                        window.location.href = windowOrdemCompra;
                    }, 1000); // 3 segundos
                }, 1000); // 1 segundo para o modal
                
                console.log('Dados enviados:', response);

            },
            error: function(response) {
                alert('Erro ao enviar os dados');
            },
        });
    });
});

$(document).ready(function() {
    $('#add-select-btn').on('click', function() {
        // Clona a primeira linha da tabela
        var $originalRow = $('#table-body tr:first');
        var $newRow = $originalRow.clone();

        // Remove o ID do botão na nova linha para evitar duplicados
        $newRow.find('#add-select-btn').removeAttr('id');

        // Altera o botão "Incluir" para "Excluir" na nova linha
        var $newButton = $newRow.find('button');
        $newButton.text('Excluir');
        $newButton.removeClass('btn-primary');
        $newButton.addClass('btn-danger btn-sm');

        // Adiciona um evento de clique ao botão "Excluir" na nova linha
        $newButton.on('click', function() {
            // Remove a linha atual da tabela
            $newRow.remove();
        });

        // Adiciona a nova linha ao corpo da tabela
        $('#table-body').append($newRow);
    });
});