import moment from 'moment'

export default function(Vue){
	Vue.auth = {
		setToken(token){
			var today = new Date()
			localStorage.setItem('token', token)
			localStorage.setItem('time', new Date().setDate(today.getDate()+15))
		},
		getToken(){
			return localStorage.getItem('token') || null
		},
		getExpirationTime(){
			return localStorage.getItem('time')
		},
		removeToken(){
			localStorage.removeItem('token')
			localStorage.removeItem('time')
		},
		isAuthenticated(){
			return Boolean(this.getToken())
		}
	}
	Object.defineProperties(Vue.prototype, {
		$auth: {
			get(){
				return Vue.auth
			}
		}
	})
}