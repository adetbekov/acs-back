import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
	state: {
		authFormCurrent: 'login',
		currentUser: null,
		locale: 'ru'
	},
	getters: {
		getUser: state => {
			return state.currentUser
		},
		getUsername: (state, getters) => {
			return getters.getUser
				? getters.getUser.username
				: ''
		},
		getId: (state, getters) => {
			return getters.getUser
				? getters.getUser.id
				: ''
		},
		getLocale: state => {
			return state.locale
		}
	},
	mutations: {
		FETCH_USER(state, user) {
		    state.currentUser = user
		},
		CHANGE_LOCALE(state, locale) {
			state.locale = locale
		}
	},
	actions: {
		fetchUser({ commit }) {
			return new Promise((resolve, reject) => {
			    Vue.http.get("api/accounts/current?format=json").then((response) => {
			        commit("FETCH_USER", response.body)
			        resolve()
			    }, response => {
					console.log(response.statusText)
					reject()
				})
			})
		},
		changeLocale({ commit }, locale ) {
			commit("CHANGE_LOCALE", locale)
			localStorage.setItem('locale', locale)
		}
	}
})

export default store