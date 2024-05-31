<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recebe dados</title>
</head>
<body>
    
<?php
$conexao=mysqli_connect("localhost","root","","comerciantes");
//checar conexao
if($conexao){
echo"NÃO CONECTADO";
}

echo"CONECTADO AO BANCO>>>>>>>>>>";

$produto = $_POST['produto'];
$descricao = $_POST['descricao'];
$preco_normal = $_POST['preco_normal'];
$preco_promocional = $_POST['preco_promocional'];
$comercio  = $_POST['comercio'];
$endereco = $_POST['enderco'];
$telefone = $_POST['telefone'];
$validade_promocao =$_POST['validade_promocao'];

$sql="INSERT INTO bdprodutos.cadastro_produtos(produto,descricao,preco_normal,preco_promocional,comercio,endereco,telefone,validade_promocao)
values('$produto','$descricao','$preco_normal','$preco_promocional','$comercio','$endereco','$telefone',$validade_promocao')";
// Executar a query
if (mysqli_query($conexao, $sql)) {
    echo "PRODUTO CADASTRADO COM SUCESSO!";
} else {
    echo "Erro: " . $sql . "<br>" . mysqli_error($conexao);
}

// Fechar a conexão
mysqli_close($conexao);$resultado = mysqli_query($conexao,$sql);
echo">PRODUTO CADASTRADO COM SUCESSO!";

?>



</body>

</html>