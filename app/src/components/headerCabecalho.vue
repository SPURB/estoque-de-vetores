<template>
	<div class="headercabecalho">
		<div class="pesquisar">
			<input type="text" name="pesquisa" placeholder="Pesquise" class="search">
			<div class="busca"></div>
		</div>
		<h1>{{ thisPageTitle(this.$route.fullPath) }}</h1>
		<div class="icones">
			<router-link
				v-for="(section, index) in home"
				:to="'../' + section.name"
				:key="index"
				tag="a"> {{ section.name }}</router-link>
		</div>
	</div>
</template>

<script>
import { mapState } from 'vuex'
export default {
	name: 'headercabecalho',
	data () {
		return {
			section: 'section'
		}
	},
	computed: {
		...mapState([
			'home',
			'fetching'
		])
	},
	methods: {
		thisPageTitle (path) { return path.replace('/', '') }
	}
}
</script>
