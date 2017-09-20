<?php
//Debug
$time = microtime();
$time = explode(' ', $time);
$time = $time[1] + $time[0];
$start = $time;

//PARÂMETROS
$tudo = read_all_files();
$files = $tudo['files']; // array de todos os arquivos desta pasta
$dirs = $tudo['dirs']; // array de todos os diretórios desta pasta
$dataName='paraClosureDeArquivos.php';
$validDirs = array(); //apenas diretórios válidos 
$current = dirname(__DIR__); //pasta atual 

foreach ($dirs as $key => $value) {
	if (is_file($value.$dataName)) { 
		$value = str_replace('\\', '/', $value);
		array_push($validDirs, $value);
	}
}

//FUNÇÕES
/**  @author sreekumar @param string $root */
function read_all_files($root = '.'){ 
	global $subPastas;/* após include deste arquivo 'include functionsAndParameters.php' escrever '$subpastas = true' para ativar read_all_files() corretamente */

	$files = array('files'=>array(), 'dirs'=>array()); 
	$directories  = array(); 
	$last_letter  = $root[strlen($root)-1]; 
	$root  = ($last_letter == '\\' || $last_letter == '/') ? $root : $root.DIRECTORY_SEPARATOR; 

	$directories[] = $root; 

	while (sizeof($directories)) {
		$dir  = array_pop($directories);
		if ($subPastas == true) {
				if ($handle = opendir($dir)) {
					while (false !== ($file = readdir($handle))) {
						if ($file == '.' || $file == '..') { 
							continue; 
						}
						$file  = $dir.$file; 
						if (is_dir($file)) { 
							$directory_path = $file.DIRECTORY_SEPARATOR; 
							array_push($directories, $directory_path); 
							$files['dirs'][]  = $directory_path; 
						} elseif (is_file($file)) { 
							$files['files'][]  = $file; 
							}
					}
					closedir($handle); 
				}
		}

	}
return $files; 
};

/** valoresDePasta retorna valores de closure
$fKey = numérico, nº de itens de $validDirs - pode ser $key dentro de um foreach
$fPar = 'nome','descrição','publicações','diretório','tags' ou 'arquivos' 
se $fPar for igual a 'tags' ou 'arquivos' a função retornará um array
*/
function valoresDePastas($fKey, $fPar){
	global $validDirs, $dataName; 
	$dataArray = include $validDirs[$fKey].$dataName;

	switch ($fPar) {
		case 'nome':
			$comDir = $validDirs[$fKey].'/nome.txt';
			return file_get_contents($comDir);
			break;

		case 'descricao':
			$comDir = $validDirs[$fKey].'/descricao.txt';
			return file_get_contents($comDir);
			break;

		default:
			return 'variável $fPar inválida';
			break;
	}
}

/** RETORNA nome de arquivos de pasta sendo
$fKey = numérico, nº de itens de $validDirs - pode ser $key dentro de um foreach
$SfType = 'cad','jpg', 'png', 'gif' - apenas um item de cada tipo por pasta
$SfType = 'imagens' - retorna primeira imagem 
$SfType = 'thumb' - imagens com nome thumb independente da extensão 
*/
function arquivosPorTipo($fKey,$fType){
	global $validDirs, $dataName;
	$dataArray = include $validDirs[$fKey].$dataName;
	$todosArquivos = $dataArray['arquivos']();

	foreach ($todosArquivos as $arquivo) {
		$pathArquivo = pathinfo($validDirs[$fKey].$arquivo);
		$extension = $pathArquivo['extension'];
		$filename = $pathArquivo['filename'];
		$pngType = substr($filename, -2); //th

		if ($extension == $fType) {
				return $arquivo;
		}

		elseif ($fType == 'thumb' and $filename == 'thumb') {
				return $arquivo;
		}

		elseif ($fType == 'imagem') {
			if ($extension == 'jpg' or $extension == 'png' or $extension == 'gif') {
				return $arquivo;
			}
		}

		elseif ($fType = 'thumb' and $filename !== 'thumb') {
			if ($pngType == 'th') {
				return $arquivo;
			}
		}

	}
}

/*arquivosNapasta() RETORNA nome de arquivos de pasta sendo
$SfType = 'cad','jpg', 'png', 'gif' - apenas um item de cada tipo por pasta
$SfType = 'imagens' - retorna primeira imagem 
$SfType = 'thumb' - imagens com nome thumb independente da extensão */
function arquivosNapasta($fType){
	global $dataName;
	$dataArray = include $dataName;
	$todosArquivos = $dataArray['arquivos']();

	foreach ($todosArquivos as $arquivo) {
		$pathArquivo = pathinfo($arquivo);
		$extension = strtolower($pathArquivo['extension']);
		$filename = $pathArquivo['filename'];
		$detectTh = substr($filename, -2);//th 
		$pngType = substr($filename, -4); //full

		if ($extension !== 'th') {
			if ($extension == $fType) {
					return $arquivo;
			}

			elseif ($fType == 'thumb' and $filename == 'thumb') {
					return $arquivo;
			}

			elseif ($fType == 'thumb' and $filename !== 'thumb' and $pngType == 'full') {	
				return $arquivo;
			}

			elseif ($fType == 'imagem') {
				if ($extension == 'jpg' or 
						$extension == 'png' or 
						$extension == 'gif') {
					return $arquivo;
				}
			}
	}
	}
}

//Retorna e escreve (para arquivos em branco) nome ou descrição 
function getValues($parametro){//'nome' ou 'descricao'
$directory = getcwd();
$scan = scandir($directory);

$nameFile='nome.txt';
$myDescricaoFile='descricao.txt';

if (is_file($myDescricaoFile)) {$existeArquivoDescricao=true;}
else{	$existeArquivoDescricao=false;}

foreach ($scan as $key => $value) {
	if ($value == $nameFile) {
		$existeArquivoNome = true;
}
	elseif ($value == $myDescricaoFile) {
		$existeArquivoDescricao  = true;
	}
}
	if ($parametro=='nome') {
		if (is_file($nameFile)==false) {
			$fp = fopen($nameFile, 'w');
			$myData = 'Atribua um nome';
			fwrite($fp, $myData);
			fclose($fp);
			}
			elseif(is_file($nameFile)){ 
			$myData = file_get_contents($nameFile);
			}
	}

	if ($parametro=='descricao') {
		if (is_file($myDescricaoFile)==false) {
		$fp=fopen($myDescricaoFile, 'w');
		$myData = 'nenhuma descrição';
		fwrite($fp, $myData);
		fclose($fp);
		}
		elseif(is_file($myDescricaoFile)){
		$myData = file_get_contents($myDescricaoFile);
		}
	}
	return $myData;
}

function returnFileNames(){
	global $validos, $extensoes;
	foreach ($validos as $key => $value) {
		switch ($extensoes[$key]) {
			case 'jpg':
				echo '.jpg<br>
				arquivo não editável (usável no powerpoint)<br><br>';
				break;
			case 'png':
				echo '.png<br>
				arquivo não editável (usável no powerpoint)<br><br>';
				break;
			case 'gif':
				echo '.gif<br>
				arquivo não editável (usável no powerpoint)<br><br>';
				break;
			case 'pdf':
				echo '.pdf<br>
				arquivo editável no illustrator<br><br>';
				break;
			case 'svg':
				echo '.svg<br>
				arquivo editável no illustrator<br><br>';
				break;
			case 'eps':
				echo '.eps<br>
				arquivo editável no illustrator e photoshop<br><br>';
				break;
			case 'ai':
				echo '.ai&nbsp;<br>
				arquivo editável no illustrator<br><br>';
				break;
			case 'psd':
				echo '.psd<br>
				arquivo editável no photoshop<br><br>';
				break;
			case 'skp':
				echo '.skp<br>
				arquivo editável no sketchup<br><br>';
				break;
			case 'dwg':
				echo '.dwg<br>
				arquivo editável no autocad<br><br>';
				break;
			case 'dxf':
				echo '.dxf<br>
				arquivo editável no autocad<br><br>';
				break;
		}
	}
} 

//variáveis desta página
function getArquivos(){
	global $directory, $currenFolderName, $validos, 
				 $extensoes, $insideArquivos; //variáveis definidas em "inside.php"

	foreach ($insideArquivos as $arquivo) {//identifica extensões de arquivos existentes
			if (is_file($arquivo)) {
				$pathArquivo = pathinfo($arquivo);
				$extension = strtolower($pathArquivo['extension']);
				$filename = $pathArquivo['filename'];
				$pngType = substr($filename, -2); //th
				$validExtensions = array('jpg','png','gif','pdf','ai','skp','dwg','dxf','psd','eps','svg');
			foreach ($validExtensions as $value) {
				if ($extension==$value) {
					if ($pngType !== 'th') {
						array_push($validos,$arquivo);
						array_push($extensoes,$extension);
					}
				}
			}
		}
	}
}

function montaLista() {
global $validDirs, $activePage;

foreach ($validDirs as $key => $value) {
	$imageURL = arquivosPorTipo($key,'thumb');
	$nomeImagem = valoresDePastas($key,'nome');
	$descricaoImagem = valoresDePastas($key,'descricao');
	list($width, $height) = getimagesize($value.$imageURL);
	$newHeight = round(356*$height/$width).'px';
	$width = $width.'px';
	$height = $height.'px';

		if ($activePage !== "pictogramas") {
		echo 
		"<li class='$activePage'>
			<div class='li-wrapper'>
				<a href='$value'>
					<img src='../_elementos/load_index.gif' data-async-load='$value$imageURL' style='width:356px; height:$newHeight'>
				</a>
				<div class='info'>
					<p class='nome'>$nomeImagem</p>
					<div class='descricao'>
						<p>$descricaoImagem</p>
					</div>
				</div>
			</div>
		</li>";
		}
		elseif ($activePage ==="pictogramas"){
		echo
		"<li class='$activePage'>
			<div class='li-wrapper-pictogramas'>
				<div class='wrap-wrapper-pictogramas'>
					<a href='$value'>
					<img data-async-load='$value/$imageURL' style='width: $width; height: $height'>
					</a>
					<div class='info'>
						<p class='nome'>$nomeImagem</p>
					</div>
				</div>
			</div>
		</li>";
		}
	}
}
?>