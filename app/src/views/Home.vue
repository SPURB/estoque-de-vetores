<template>
	<div class="home">
		<main>
			<h1>Estoque de vetores</h1>
				<ul id="secoes">
					<li v-for="(route, index) in home"
						:key="index"><router-link
						:to="route.name"><img
						:src="concatImagePath(route.name, route.images[0].filename)"
						:alt="alt(route.name)"><h2>{{ route.name }}</h2></router-link></li>
				</ul>
		</main>
	</div>
</template>

<script>
import { mapState } from 'vuex'
export default {
	name: 'home',
	computed: {
		...mapState([
			'home',
			'fetching',
			'imagesHostBaseUrl'
		])
	},
	created () { this.$store.dispatch('getHome') },
	methods: {
		alt (name) { return 'Image of "' + name + '" section' },
		concatImagePath (folder, file) { return this.imagesHostBaseUrl + folder + '/' + file }
	}
}
</script>
