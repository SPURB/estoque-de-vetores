$(document).ready(function(){ 
'use strict';
function makeReadOnly(div,descNome,sendindDiv,inputID,parserURL,postType){
	div.contentEditable = false;
	var fn = document.getElementById(descNome).value;
};

// edição de nome
$("#editarNome").click(function() {
	$("#nomeImagem").show( "normal" );
	$("#nomeSalvar").show( "normal" );
	$("#nomeCancelar").show( "normal" );
	$(".title").fadeOut( "normal" );
	$(this).fadeOut( "normal" );
});

function salvarEdicaoNome(){
ajax_post('nameStatus','nomeImagem','trataDados/nomeParser.php','nome=');
};

function cancelarEdicao(){
$("#nomeCancelar").click(function() {
	$("#nomeImagem").hide( "normal" );
	$("#nomeSalvar").hide( "normal" );
	$(this).hide( "normal" );
	$("#editarNome").fadeIn( "slow" );
	$(".title").fadeIn( "fast" );
});
};

// mouseover dos botões do menu
function appendActivePage(){
			$("#titulo" ).empty();
			$("#titulo" ).append(active_page);
};
$("#titulo" ).append('<p>'+active_page+'</p>');

$("#btn-pictogramas" ).mouseover(function() {
			$( "#titulo" ).empty();
			$( "#titulo" ).append( "Pictogramas" );
		})
		.mouseout(function(){
		appendActivePage();
		});

		$("#btn-infograficos" ).mouseover(function() {
			$("#titulo" ).empty();
			$("#titulo" ).append( "Infográficos" );
		})
		.mouseout(function(){
			appendActivePage();
		});

		$("#btn-blocos" ).mouseover(function() {
			$( "#titulo" ).empty();
			$( "#titulo" ).append( "Blocos" );
		})
		.mouseout(function(){
			appendActivePage();
		});

});//fim document ready