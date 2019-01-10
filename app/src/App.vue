<template>
	<div id="app">
		<div id="nav" v-if="!isHome">
			<router-link to="/pictogramas">Pictogramas</router-link> |
			<router-link to="/blocos">Blocos</router-link> |
			<router-link to="/infograficos">Infograficos</router-link>
		</div>
		<router-view/>
	</div>
</template>

<script>
export default {
	name: 'app',
	computed: {
		isHome () {
			if (this.$route.name === 'home') return true
			else return false
		}
	},
	mounted () {
		this.$store.dispatch('fetchHome')
	}
}
</script>

<style lang="scss">
</style>
