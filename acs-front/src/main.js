import Vue from 'vue'
import VueResource from 'vue-resource'
import router from './router'
import store from './store'
import i18n from './i18n'
import { TweenMax, TimelineLite } from 'gsap'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import './assets/toolkit.css'
import 'vue-awesome/icons'
// import Icon from 'vue-awesome/components/Icon'

import VueAwesomeSwiper from 'vue-awesome-swiper'	
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.css'
import App from './App'
import moment from 'moment'
import lodash from 'lodash'
import HTML from 'vue-html'

import Auth from './packages/auth/Auth.js'
import Navbar from '@/components/Navbar.vue'
import BlurShadow from '@/components/BlurShadow.vue'
import BlogHeader from '@/components/blog/BlogHeader.vue'
import Caption from '@/components/blog/Caption.vue'
import buttons from '@/components/buttons.vue'
import "@/icon.js"

Vue.use(VueAwesomeSwiper)
Vue.use(Auth)
Vue.use(VueResource)
Vue.use(HTML)

Vue.config.productionTip = false
Vue.prototype.TweenMax = TweenMax
Vue.prototype.TimelineLite = TimelineLite
Vue.prototype._ = lodash
Vue.prototype.moment = moment
Vue.http.options.root = "http://localhost:8000"
Vue.http.interceptors.push(function(request, next) {
	let self = this
	if(Vue.auth.isAuthenticated() && Vue.auth.getExpirationTime() >= new Date() )
		request.headers.set('Authorization', `JWT ${Vue.auth.getToken()}`)
	if( Vue.auth.getExpirationTime() >= new Date() && Vue.auth.isAuthenticated() && Vue.auth.getExpirationTime() - new Date() <= 432000){
		this.$http.post("auth/reload", { 
			token: Vue.auth.getToken(),  
		}).then(response => {
			Vue.auth.removeToken()
			this.$auth.setToken(response.body.token)
			console.log("Token reloaded")
		}, response => {
			console.log(response.statusText)
		})
	}
	next(response => {
		if(response.status == 401 || response.status == 403) {
			Vue.auth.removeToken()
			location.reload()
		}
	})
})

Vue.component('dBlurShadow', BlurShadow)
Vue.component('Navbar', Navbar)
Vue.component('BlogHeader', BlogHeader)
Vue.component('Caption', Caption)
Vue.component('dButton', buttons)

new Vue({
  el: '#app',
  router,
  store,
  i18n,
  render: h => h(App),
  components: {
  	swiper,
  	swiperSlide
  }
})
