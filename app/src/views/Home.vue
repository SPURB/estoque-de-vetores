<template>
	<div class="home">
		<main>
			<h1>Estoque de vetores</h1>
				<!-- <ul id="secoes">
					<li><a href="./pictogramas/"><img src="assets/img/home_pictogramas.png" alt="Pictogramas"><h2>Pictogramas</h2></a></li>
					<li><a href="./infograficos/"><img src="assets/img/home_infograficos.png" alt="Infográficos"><h2>Infográficos</h2></a></li>
					<li><a href="./blocos"><img src="assets/img/home_blocos.png" alt="Blocos"><h2>Blocos</h2></a></li>
				</ul> -->
				<ul class="secoes">
					<li><router-link to="/pictogramas">Pictogramas</router-link></li>
					<li><router-link to="/blocos">Blocos</router-link></li>
					<li><router-link to="/infograficos">Infograficos</router-link></li>
				</ul>				
		</main>
	</div>
</template>

<script>
export default {
	name: 'home'
}
</script>
