<!DOCTYPE html>
<html lang="pt">
<head> 
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="../assets/css/base.css">
<!--[if IE]>
<link rel="stylesheet" type="text/css" href="../assets/css/ie.css">
<![endif]-->

<title>Estoque de vetores</title>
<?php
	$subPastas = true;
	$activePage = "pictogramas";
	include '../assets/php/functionsAndParamaters.php';
?>
</head>
<body>
<div id="page_loader">
	<img src="../_elementos/loading.gif">
</div>

<div id="indexContainer">
<div id="my-list">
<div id="indexHeader">

<div class='voltarHome'>
	<a href='../'><img src="../_elementos/BTN_voltar-01.svg"></a>
</div>

<div id="searchBox">
<label>Pesquisar<input class="search" placeholder="Pesquisar"/></label>
</div>

<?php include("../assets/php/indexNav.php");?>

</div>

<div class='separador'></div>
	<div id="result">
		<ul class='list' id="ulList"><!-- estrutura de lista -->
			<?php montaLista();?>
		</ul>
	</div><!-- result -->
</div><!-- list.js -->

</div><!-- container -->

<?php include("../assets/php/footer.php");?>

<script>
var active_page = "Pictogramas";
</script>
<?php include '../assets/php/indexScriptSrc.php' ?>
</body>
</html>
