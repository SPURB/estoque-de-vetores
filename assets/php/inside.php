<?php 
$directory = getcwd();
$currenFolderName = substr(str_replace(dirname(__FILE__), '', $directory), 1);
$validos = array(); //array de arquivos válidos para download
$extensoes = array(); //array de extensões arquivos válidos para download
$insideArquivos = $dataArray['arquivos']();//todos os arquivos dentro de cada pasta 
getArquivos();
?>
<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<title>Estoque de vetores</title>
<meta name='description' content='O Estoque de Vetores é dividido em: pictogramas, infográficos, blocos. Contém desenhos vetoriais com bases axonométricas, cortes e ilustrações'>
<!-- caminhos relativos à index.php da pasta da imagem -->
<link rel="stylesheet" type="text/css" href="../../../assets/css/base.css">
<!--[if IE]>
<link rel="stylesheet" type="text/css" href="../../../assets/css/ie.css">
<![endif]-->
</head>
<body>
<div id="page_loader" style="">
	<img src="../../../_elementos/loading.gif">
</div>
<div id="insideContainer"> 
	<div id='insideHeader'> 
		<div id="insideNome">
			<div class='voltar'>
				<a href='../../' onclick="window.history.back()"><img src="../../../_elementos/BTN_voltar-01.png"></a><!--BTN_voltar-01.svg -->
			</div>
			<form id="conteudoNome" action='../../../assets/php/processName.php' method='post'>
				<textarea id="nomeAparente" name="nome"><?php echo getValues('nome')?></textarea>
				<input class="submit" id="nomeInput" type='submit' value='Salvar Nome'>
				<input type='hidden' name='directory' value=<?php echo $directory;?>>
			</form>
		</div>

<?php include "../../../assets/php/insideNav.php"; ?>

</div>
<div class='separador'></div>
<div id='insideMain'>
	<div id="mainImg">
		<img src=<?php echo "'".arquivosNaPasta('thumb')."'";?>> 
	</div>

	<div id='mainArquivos'>
		<div id='imgArquivos'>
			<h3>Arquivos</h3>
			<div id='arquivosContainer'>
			<?php 
				foreach ($validos as $key => $value) {
				echo "<a class='arquivosExt' href='".$validos[$key]."' title='.".$extensoes[$key]." desta imagem' download>";
				echo file_get_contents("../../../_elementos/1_2_baixar_branco.svg");
				echo "<h3>";
				echo '.'.$extensoes[$key]."</h3></a>";
				}
			?>
			</div>
			<div style='clear:both'></div>
			<p>
			<br>
			<?php returnFileNames();?>
			<!--[if IE]>
			<hr style='margin-right:20px'><br>
			Para salvar o arquivo no seu computador: <br>
			Clique com o botão direito na opção de arquivo e selecione "Salvar Destino Como..."
			<![endif]-->

			</p>
		</div>
	</div>
</div>

<div id="mainDescricao">
<div id='conteudoDescricao'>
<form action='../../../assets/php/processComment.php' method='post'>
<textarea id="descricao" name='descricao' cols='5' rows='5'>
<?php echo getValues('descricao');?>
</textarea>
<input id="descricaoInput" class="submit" type='submit' value='Salvar Descricao'>
<input type='hidden' name='directory' value=<?php echo getcwd();?>>
</form>
</div>
</div>
</div><!-- insideContainer -->
</body>
</html>
