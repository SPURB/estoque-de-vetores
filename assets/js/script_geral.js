var gifDiv = document.getElementById('page_loader');
function gifLoader() {
	gifDiv.style.display="block";
}

// topping
if (active_page==='Blocos'){
	$("#btn-blocos").removeClass("btnz").addClass('btn-base');
};
if (active_page==='Infográficos'){
	$("#btn-infograficos").removeClass("btnz").addClass('btn-base');
};
if(active_page==='Pictogramas'){
	$("#btn-pictogramas").removeClass("btnz").addClass('btn-base');
}


