import Vue from 'vue'
import Vuex from 'vuex'
import api from './api'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		fetching: false,
		error: false,
		home: undefined,
		section: undefined,
		validSections: false
	},
	mutations: {
		FECHING: (state, status) => { state.fetching = status },
		ERROR: (state, status) => { state.error = status },
		SET_HOME: (state, data) => { state.home = data },
		SET_SECTION_CONTENT: (state, data) => { state.section = data },
		SET_VALID_SECTIONS: (state, data) => {	state.validSections = data }
	},
	actions: {
		getHome: state => {
			state.commit('FECHING', true)
			api.get('')
				.then(response => {
					state.commit('SET_HOME', response.data.content)
				})
				.catch(error => { state.commit('ERROR', error) })
				.then(() => { state.commit('FECHING', false) })
		},
		getSection: (state, section) => {
			if (section.isValid) {
				state.commit('FECHING', true)
				api.get(section.path)
					.then(response => {
						const output = {
							'content': response.data.content
						}
						state.commit('SET_SECTION_CONTENT', output)
					})
					.catch(error => { state.commit('ERROR', error) })
					.then(() => { state.commit('FECHING', false) })
			} else { console.log(section.path + ' invalid') }
		},
		getValidSections: (state) => {
			state.commit('FECHING', true)
			api.get('/valid-sections')
				.then(response => {
					state.commit('SET_VALID_SECTIONS', response.data.content)
				})
				.catch(error => { state.commit('ERROR', error) })
				.then(() => { state.commit('FECHING', false) })
		}
	}
})
