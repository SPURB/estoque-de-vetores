<template>
	<div class="sections">
		<headerCabecalho v-if="validSection"></headerCabecalho>
		<mainGrid v-if="validSection"></mainGrid>
	<div v-else>
		<img src="https://httpstatusdogs.com/img/404.jpg" alt="404">
		<p>Voltar para <router-link to='/' tag="a">Home</router-link>?</p>
	</div>
	</div>
</template>
<script>
import { mapState } from 'vuex'
import headerCabecalho from '@/components/HeaderCabecalho'
import mainGrid from '@/components/MainGrid'

export default {
	name: 'sections',
	components: {
		headerCabecalho,
		mainGrid
	},
	computed: {
		...mapState([
			'validSections',
			'section',
			'fetching'
		])
	},
	methods: {
		validSection () {
			try {
				const sectionName = this.$route.fullPath.replace('/', '')
				let valid = this.validSections.find(el => el === sectionName)
				return valid
			} catch (error) {
				console.log(error)
				this.$router.push('/')
			}
		}
	},
	mounted () {
		this.$store.dispatch('getSection', { 'path': this.$route.fullPath, 'isValid': true })
	},
	watch: {
		'$route' (to) {
			this.$store.dispatch('getSection', { 'path': to.fullPath, 'isValid': this.validSection })
		}
	}
}
</script>
