<template>
  <div class="sections">
	<h1>{{this.$route.fullPath}}</h1>
	<ul v-if="validSection">
		<li v-for="(item, index) in section" :key="index">{{item}}</li>
	</ul>
  </div>
</template>
<script>
import { mapState } from 'vuex'
export default {
	name: 'sections',
	computed: {
		...mapState([
			'validSections',
			'section',
			'fetching'
		]),
		validSection () {
			const sectionName = this.$route.fullPath.replace('/', '')
			let valid = this.validSections.find(el => el === sectionName)
			return valid !== undefined
		}
	},
	mounted () { this.$store.dispatch('getSection', { 'path': this.$route.fullPath, 'isValid': this.validSection }) },
	watch: {
		'$route' (to) {
			this.$store.dispatch('getSection', { 'path': to.fullPath, 'isValid': this.validSection })
		}
	}
}
</script>
