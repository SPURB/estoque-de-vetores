<template>
	<div id="app">
		<headerCabecalho v-if="!isHome"></headerCabecalho>
		<router-view/>
	</div>
</template>

<script>
import { mapState } from 'vuex'
import headerCabecalho from '@/components/headerCabecalho'

export default {
	name: 'app',
	components: { headerCabecalho },
	computed: {
		isHome () {
			if (this.$route.name === 'home') return true
			else return false
		},
		...mapState([
			'validSections'
		])
	},
	created () {
		this.$store.dispatch('getValidSections')
		this.$store.dispatch('getHome')
	}
}
</script>

<style lang="scss">
</style>
