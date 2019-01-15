import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
	routes: [
		{
			path: '/',
			name: 'home',
			component: () => import(/* webpackChunkName: "home" */ './views/Home.vue')
		},
		{
			path: '/:section',
			component: () => import(/* webpackChunkName: "section" */ './views/Sections.vue')
		}
	]
})
