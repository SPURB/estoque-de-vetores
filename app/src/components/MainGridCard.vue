<template>
	<li class="card">
		{{ contentItems }}
	</li>
</template>
<script>

export default {
	name: 'mainGridCard',
	props: {
		contentItems: {
			required: true,
			type: Object
		}
	}
}
</script>
