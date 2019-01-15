<template>
	<div id="app">
		<router-view/>
	</div>
</template>

<script>
import { mapState } from 'vuex'

export default {
	name: 'app',
	computed: {
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
