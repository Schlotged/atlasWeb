
// ajax para aplicar api de cep criada usando rota do django
$(document).ready(function() {
    $('#buscar-cep').click(function() {
        var cep = $('#cepPrest').val();

        if (cep.length < 8) {

            return alert('Cep é obrigatório ter mais de 8 digitos')
        } else {
            $('#loadingModal').modal('show');

            if (cep) {
                $.ajax({
                    url: buscarCep,
                    type: "POST",
                    data: {
                        'cep': cep,
                        csrfmiddlewaretoken: csrfToken
                    },
                    success: function(response) {
                        
                    

                        if (response.erro) {
                            alert('CEP não localizado, verificar número');
                            return;
                        }

                        
                        
                        var cepHtml = `
                            <div class="form-group" style="width: 48%;">
                                <label for="logradouro">Logradouro:</label>
                                <input type="text" class="form-control" id="logradouro" name="endereco" value="${response.logradouro}">
                            </div>
                            <div class="form-group" style="width: 48%;">
                                <label for="bairro">Bairro:</label>
                                <input type="text" class="form-control" id="bairro" name="bairro" value="${response.bairro}">
                            </div>
                            <div class="form-group" style="width: 48%;">
                                <label for="localidade">Localidade:</label>
                                <input type="text" class="form-control" id="localidade" name="localidade" value="${response.localidade}">
                            </div>
                            <div class="form-group" style="width: 48%;">
                                <label for="uf">UF:</label>
                                <input type="text" class="form-control" id="uf" name="uf" value="${response.uf}">
                            </div>
                            <div class="form-group" style="width: 48%;">
                                <label for="ddd">Código IBGE:</label>
                                <input type="text" class="form-control" id="ddd" name="ddd" value="${response.ibge}">
                            </div>
                            <div class="form-group" style="width: 48%;">
                                <label>Número</label>
                                <input type="text" class="form-control" id="numeroCep" name="numeroCep" value="">
                            </div>

                            <div class="form-group" style="width: 48%;">
                                <label>Complemento</label>
                                <input type="text" class="form-control" id="complemento" name="complemento" value="">
                            </div>
                        `;

                        $('#cep-table').append(cepHtml);

                        setTimeout(function() {
                            $('#loadingModal').modal('hide');
                        }, 1000);

                        
                    },
                    error: function() {
                        alert('Erro ao buscar informações do CEP');
                        $('#loadingModal').modal('hide');
                    }
                });
            } else {
                alert('Campo CEP não pode ser nulo');
            }
        }
    });
});

// Função pra tirar qualquer letra do input
const inputs = document.querySelectorAll('.input-number');

        inputs.forEach(input => {
            input.addEventListener('input', function() {
                this.value = this.value.replace(/[^0-9]/g, '');
            });
        });

// Envio de requisição soap para SOC e posteriormente SENIOR
$(document).ready(function() {
    $('#prestadorSocSenior').submit(function(event) {
        event.preventDefault();

        var formDataArray = $(this).serializeArray();
        var allFieldsFilled = true;

        var camposParaValidar = [
            'usuario', 
            'nomePrestador', 
            'cpf', 
            'tipo-prestador', 
            'razaoSocial', 
            'tipo-pessoa', 
            'uf', 
            'representanteLegal', 
            'cep', 
            'telefonePrestador', 
            'emailPrestador', 
            'horaInicialAtendimento', 
            'horaFinalAtendimento', 
            'tipoAtendimento', 
            'comentarioPrestador', 
            'observacao-geral', 
            'prestadorAtivo', 
            'statusContrato',
            'diaDoPagamento',
            'condicaoPagamento',
            'codigoCondicaoFaturamento',
            'tipoPagamento',
            'dataPagamento',
            'tipoDocumento'
        ];

            formDataArray.forEach(function(field) {
                var inputElement = $('[name="' + field.name + '"]');
                
                // Verifica se o campo está na lista de campos para validar
                if (camposParaValidar.includes(field.name)) {
                    if (field.value.trim() === '') {
                        inputElement.css('border', '2px solid red');
                        allFieldsFilled = false;
                    } else {
                        inputElement.css('border', '');
                    }
                }
            });

        if (!allFieldsFilled) {
            alert('Por favor, preencha todos os campos obrigatórios.');
            return;
        }

        var formData = $(this).serialize();

        $.ajax({
            url: sendPrestador,
            type: "POST",
            data: formData,
            success: function(response) {

                $('#successModal').modal('show');
                $('#successModal').modal('hide');
                
                setTimeout(function() {
                    $('#successModal').modal('hide');
                    
                    setTimeout(function() {
                        window.location.href = windowPrestador;
                    }, 1000);
                }, 1000); // 1 segundo para o modal
                
                console.log('Dados enviados:', response);
                $('#successModal').modal('hide');

            },
            error: function(response) {
                alert('Erro ao enviar os dados');
            },
        });
    });
});

// Funcao temporaria para buscar codigo do usuario na tela
$(document).ready(function() {

    $('#buscar-usuario-btn').click(function() {
        var login_user = $('#usuario-input').val();

        if (login_user) {

            $('#loadingModal').modal('show');
            $.ajax({
                url: sendBuscaUsuario, // Certifique-se de que a URL esteja correta
                type: "POST",
                data: {
                    'login_user': login_user,
                    csrfmiddlewaretoken: csrfToken
                },
                success: function(response) {

                    if (response.nome_user) {

                        var cepHtml = `
                            <div class="form-group" style="width: 48%;" >
                                <label>Login</label>
                                <input type="text" name="usuario-login" class="form-control" id="login-input" value="${response.codigo_user}"/>
                            </div>
                        `;

                        $('#user-table').append(cepHtml);

                        $('#loadingModal').modal('hide');
                        $('#successModal').modal('show');
                        setTimeout(function() {
                            $('#successModal').modal('hide');
                        }, 1000);
                    } else {
                        $('#loadingModal').modal('hide');
                        alert('Usuário não encontrado');
                    }
                },
                error: function(xhr, textStatus, errorThrown) {
                    var statusCode = xhr.status; // Acessa o código de status
                    console.log('Status Code:', statusCode);
                    $('#loadingModal').modal('hide');
            
                    if (statusCode === 404) {

                        alert('Recurso não encontrado.')
                        console.log('Recurso não encontrado.');

                    } else if (statusCode === 500) {
                        $('#loadingModal').modal('hide');
                        console.log('Erro interno do servidor.');
                    }
                }
            });
        } else {
            alert('Campo de login não pode ser nulo');
        }
    });
});

//Função para aplicar mascara do tipo data no input texto
$(document).ready(function() {
    function formatarData(input) {
        var valor = input.value;

        valor = valor.replace(/\D/g, '');

        if (valor.length <= 2) {
            valor = valor.replace(/(\d{2})/, '$1');
        } else if (valor.length <= 4) {
            valor = valor.replace(/(\d{2})(\d{2})/, '$1/$2');
        } else {
            valor = valor.replace(/(\d{2})(\d{2})(\d{4})/, '$1/$2/$3');
        }

        input.value = valor;
    }

    $('#dataContratacao').on('input', function() {
        formatarData(this);
    });

    $('#dataPagamento').on('input', function() {
        formatarData(this);
    });
});


//Função para aplicar mascara do tipo data
document.addEventListener('DOMContentLoaded', function() {
    function formatarDocumento() {
        var campoCpf = document.getElementById('cpf');
        var valor = campoCpf.value.replace(/\D/g, ''); // Remove caracteres não numéricos

        if (valor.length > 11) {
            // Formata como CNPJ (xx.xxx.xxx/xxxx-xx)
            valor = valor.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})$/, '$1.$2.$3/$4-$5');
        } else {
            // Formata como CPF (xxx.xxx.xxx-xx)
            valor = valor.replace(/^(\d{3})(\d{3})(\d{3})(\d{2})$/, '$1.$2.$3-$4');
        }

        campoCpf.value = valor;
    }

    // Adiciona o evento de formatação ao campo CPF para cada alteração
    document.getElementById('cpf').addEventListener('input', formatarDocumento);
});

// Função para validar campo tipoPessoa e cpf/cnpj
document.addEventListener('DOMContentLoaded', function() {
    function validarDocumento() {
        var tipoPessoa = document.getElementById('tipoPessoa').value;
        var documento = document.getElementById('cpf').value.replace(/\D/g, '');
        var documentoValido = false;

        if (tipoPessoa === 'JURIDICA') {

            documentoValido = documento.length === 14;
        } else if (tipoPessoa === 'FISICA') {

            documentoValido = documento.length === 11;
        }

        if (documento !== '') {

            if (!documentoValido) {
                document.getElementById('cpf').style.border = '2px solid red';
                document.getElementById('documentoErro').style.display = 'block';
            } else {
                document.getElementById('cpf').style.border = '';
                document.getElementById('documentoErro').style.display = 'none';
            }
        } else {

            document.getElementById('cpf').style.border = '';
            document.getElementById('documentoErro').style.display = 'none';
        }
    }

    document.getElementById('tipoPessoa').addEventListener('change', validarDocumento);
    document.getElementById('cpf').addEventListener('keyup', validarDocumento);
});