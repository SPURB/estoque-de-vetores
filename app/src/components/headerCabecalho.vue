<template>
	<div class="headerCabecalho">
		<div id="icones">
			<router-link to="/">Voltar</router-link>
			<router-link  v-for="(section, index) in home" :to="section.name" :key="index"> {{section.name}}</router-link>
		</div>
	</div>
</template>

<script>
import { mapState } from 'vuex'
export default {
	name: 'headerCabecalho',
	computed: {
		...mapState([
			'home',
			'fetching'
		])
	}
}
</script>
