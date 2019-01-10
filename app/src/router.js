import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
	routes: [
		{
			path: '/',
			name: 'home',
			component: Home
		},
		{
			path: '/pictogramas',
			name: 'pictogramas',
			component: () => import('./views/Pictogramas.vue')
		},
		{
			path: '/blocos',
			name: 'blocos',
			component: () => import('./views/Blocos.vue')
		},
		{
			path: '/Infograficos',
			name: 'infograficos',
			component: () => import('./views/Infograficos.vue')
		}
	]
})
