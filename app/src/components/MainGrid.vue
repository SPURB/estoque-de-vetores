<template>
	<div class="grid">
		<ul>
			<mainGridCard
				v-for="(item, index) in section.content"
				:key="index"
				:contentItems="item">
			</mainGridCard>
		</ul>
	</div>
</template>
<script>
import { mapState } from 'vuex'
import mainGridCard from '@/components/MainGridCard'

export default {
	name: 'mainGrid',
	components: { mainGridCard },
	computed: {
		...mapState([
			'section'
		])
	}
}
</script>
