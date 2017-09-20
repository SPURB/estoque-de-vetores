<?php
return array(
"arquivos" => function (){
	$current = dirname(__FILE__);
	$scan = scandir($current);
	return $scan;
}
);
?>