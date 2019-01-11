<template>
	<div class="headerCabecalho">
		<div id="icones">
			<a href="/">voltar </a>
				<router-link  v-for="(section, index) in home" :to="section.url" :key="index"> {{section.name}} </router-link>
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
