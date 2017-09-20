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
	//para debug
	$subPastas = true;
	$activePage = "blocos";
	include '../assets/php/functionsAndParamaters.php';
	?>
</head>

<body>
<div id="page_loader">
	<img src="../_elementos/loading.gif">
</div>

<div id="indexContainer">
<div id="my-list">
<?php include("../assets/php/indexHeader.php");?>

<div class='separador'></div>
	<div id="result">
		<ul class='list'><!-- estrutura de lista -->
			<?php montaLista();?>
		</ul>
		<ul class='pagination'></ul>
	</div><!-- result -->
</div><!-- list.js -->
</div><!-- container -->

<?php include("../assets/php/footer.php");?>

<script type="text/javascript">
	var active_page = "Blocos";
</script>
<?php include("../assets/php/indexScriptSrc.php");?>
</body>
</html>

