<?php 
if ($_POST) {
	$value = $_POST["descricao"];
	$myfile = $_POST["directory"].'/'.'descricao.txt'; 
	if (isset($value)) {
		$handle = fopen($myfile, "w");
		fwrite($handle, $value);
		fclose($handle);
	}
}
?>
<script type="text/javascript">
history.back();
</script>