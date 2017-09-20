<?php 
if ($_POST) {
	$value = $_POST["nome"];
	$myfile = $_POST["directory"].'/'.'nome.txt'; 

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