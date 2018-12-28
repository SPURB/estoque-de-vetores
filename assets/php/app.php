<?php
	echo 
	'<div id="app">
		<headercabecalho v-on:updatepesquisa="input($event)"></headercabecalho>
		<grid :pesquisa="pesquisa"></grid>
	</div>';