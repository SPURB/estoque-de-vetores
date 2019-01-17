<template>
	<div class="home">
		<main>
			<h1>Estoque de vetores</h1>
			<ul id="secoes">
				<li v-for="(route, index) in home" :key="index">
					<router-link :to="route.name">
						<img v-for="(image, index) in route.images" :key="index"
							:src="route.folder + '/' + image.file"
							:alt="alt(image.file)">
						<h2>{{ route.name }}</h2>
					</router-link>
				</li>
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

<style lang="scss" scoped>
* { box-sizing: border-box; }
body, html, main {
	display: grid;
	font-family: 'Roboto', helvetica, san-serif;
	color: #333;
	height: 100vh
}

main { margin: 0 }

h1, h2 {
	border: 0;
	margin: 0
}

h1 {
	margin: auto;
	font-size: 5em;
	font-weight: 100
}

h2 {
	font-weight: 300
}

a {
	text-decoration: none;
	color: #333
}

ul, li {
	list-style-type: none;
	margin: 0;
	padding: 0;
	border: 0
}

ul {
	display: grid;
	grid-template-columns: 1fr 1fr 1fr
}

li {
	text-align: center
}

li > a {
	opacity: .35;
	transition: opacity ease-in .15s
}

li > a:hover{
	opacity: 1
}

</style>
