$(document).ready(function(){ 
// switcher de descrição
$("#switchBtn").delay(1500).attr("style", "display:flex");
$("#inlcludeDesc").click(function(){
	$(".descricao").toggleClass("active_descricao"); 
	if (checked==true){
		options['valueNames']=['nome'];
		var updatedList = new List('my-list', options);
		checked=true;
		}

		else if (checked==false){
			options['valueNames']=['nome','descricao'];
			var originalList = new List('my-list', options);
			checked=false;
			}
		}); 
	checked = false;

// mouseover dos botões
function appendActivePage(){
			$( "#titulo" ).empty();
			$( "#titulo" ).append(active_page);
};

$("#titulo" ).append('<p>'+active_page+'</p>');
	$( "#btn-pictogramas" ).mouseover(function() {
		$( "#titulo" ).empty();
		$( "#titulo" ).append( "Pictogramas" );
	})
	.mouseout(function(){
		appendActivePage();
	});
	$( "#btn-infograficos" ).mouseover(function() {
		$( "#titulo" ).empty();
		$( "#titulo" ).append( "Infográficos" );
	})
	.mouseout(function(){
		appendActivePage();
	});
	$( "#btn-blocos" ).mouseover(function() {
		$( "#titulo" ).empty();
		$( "#titulo" ).append( "Blocos" );
	})
	.mouseout(function(){
		appendActivePage();
	});


// load de imagens dinâmico 
//fonte: https://zachalam.com/using-ajax-and-jquery-to-load-images-asynchronously/
load_images_in_view();
$(window).scroll(load_images_in_view); 

function load_images_in_view(){
	$("img").each(function() {
		var object_bottom = $(this).offset().top + ($(this).outerHeight()/2);
		var window_bottom = $(window).scrollTop() + $(window).height();

		if (window_bottom > object_bottom){	
			if ($(this).data("image-loaded") != true){
					var image_source = $(this).data("async-load");
					$(this).data("image-loaded",true);
					$(this).attr("src",image_source);
			}
		}
	}); // end $("img").each()	
}

//listjs: ordena por nome
mylist.sort('nome', {
	order:"asc",
	alphabet: "AaÀàÁáÂâÃãBbCcDdEeÉéÊêFfGgHhIiÍíJjKkLlMmNnOoÓóÔôÕõPpQqRrSwTtUuÚúÜüVvXxYyZz"
});

});//fim document ready

//parâmetros para listjs
var options = {
	valueNames: ['nome']
};
var mylist = new List('my-list', options);


//volta ao topo
var timeOut;
function scrollToTop() {
	if (document.body.scrollTop!=0 || document.documentElement.scrollTop!=0){
		window.scrollBy(0,-50);
		timeOut=setTimeout('scrollToTop()',10);
	}
	else clearTimeout(timeOut);
}
var btn = document.getElementById('voltarTopo');
btn.addEventListener('click',scrollToTop, false);

// function displayArquivos(){
// 	$(".cjtoArquivos").toggleClass("active_cjtoArquivos");
// };