<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recebe dados</title>
</head>
<body>

<?php
// Conectar ao banco de dados
$conexao = mysqli_connect("localhost", "root", "", "comerciantes");

// Checar a conexão
if (!$conexao) {
    die("Falha na conexão: " . mysqli_connect_error());
}

echo "CONECTADO AO BANCO DE DADOS";

// Obter dados do formulário
$produto = mysqli_real_escape_string($conexao, $_POST['produto']);
$descricao = mysqli_real_escape_string($conexao, $_POST['descricao']);
$preco_normal = mysqli_real_escape_string($conexao, $_POST['preco_normal']);
$preco_promocional = mysqli_real_escape_string($conexao, $_POST['preco_promocional']);
$comercio = mysqli_real_escape_string($conexao, $_POST['comercio']);
$endereco = mysqli_real_escape_string($conexao, $_POST['endereco']);
$telefone = mysqli_real_escape_string($conexao, $_POST['telefone']);
$validade_promocao = mysqli_real_escape_string($conexao, $_POST['validade_promocao']);

// Preparar a query SQL
$sql = "INSERT INTO cadastro_produtos (produto, descricao, preco_normal, preco_promocional, comercio, endereco, telefone, validade_promocao)
VALUES ('$produto', '$descricao', '$preco_normal', '$preco_promocional', '$comercio', '$endereco', '$telefone', '$validade_promocao')";

// Executar a query
if (mysqli_query($conexao, $sql)) {
    echo "PRODUTO CADASTRADO COM SUCESSO!";
} else {
    echo "Erro: " . $sql . "<br>" . mysqli_error($conexao);
}

// Fechar a conexão
mysqli_close($conexao);
?>

</body>
</html>
