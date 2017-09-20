<html>
<head>
	<title>teste</title>
</head>
<body>
<pre>
<?php

include '../../../../assets/php/functionsAndParamaters.php';

$teste = array(
"arquivos" => function (){
	$parent = dirname(__FILE__);

	$scan = scandir($parent);

	return $parent;
	// return $scan;
}
);


var_dump($teste);
print_r($teste['arquivos']());

?>
</pre>
?>
</body>
</html>