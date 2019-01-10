import Vue from 'vue'
import Vuex from 'vuex'
import api from './api'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		fetching: false,
		error: false
	},
	mutations: {
		FECHING: (state, status) => { state.fetching = status },
		ERROR: (state, status) => { state.error = status }
	},
	actions: {
		fetchHome: state => {
			state.commit('FECHING', true)
			api.get('')
				.then(response => { console.log(response) })
				.catch(error => { state.commit('ERROR', error) })
				.then(() => { state.commit('FECHING', false) })
		}
	}
})
