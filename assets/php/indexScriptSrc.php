<!--[if !IE]> -->
<script src="../assets/js/jquery-3.0.0.min.js" defer></script>
<!-- <![endif]-->
<!--[if IE]>
<script src="../assets/js/jquery-1.11.3.js" defer></script>
<![endif]-->
<script src="../assets/js/list.min.js" defer></script>
<script src="../assets/js/respond.min.js" defer></script>

<script src="../assets/js/script_geral.js" defer></script>
<script src="../assets/js/script_index.js" defer></script>


<?php
$time = microtime();
$time = explode(' ', $time);
$time = $time[1] + $time[0];
$finish = $time;
$total_time = round(($finish - $start), 4);
echo 'página gerada em '.$total_time.' segundos';
?>