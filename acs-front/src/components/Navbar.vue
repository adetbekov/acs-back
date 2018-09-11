<template>
	<div>
		<div class="header container d-flex justify-content-between hidden-xs-down px-0">
		  <router-link :to="getLogoUrl">
		  <dBlurShadow>
		    <div class="d-flex">
			      <img :src="getLogoImage" :alt="getLogoAlt" :height="getLogoHeight" class="mr-1">
			      <img :src="getLogoText" :alt="getLogoAlt+'-text'" :height="getLogoHeight">
		    </div>
		  </dBlurShadow>
		  </router-link>
		  <div style="position: absolute; left: 50%;">
			<slot></slot>
		  </div>
		  <div class="d-flex align-items-center">
			  <ul class="list-inline text-gray mb-0 d-flex justify-content-center align-items-center">
			  	<li class="list-inline-item pr-3"><icon name="search" scale="0.9"></icon></li>
			    <li v-if="this.routeIndex" class="pr-4 overflow-hidden" style="margin-top: -3.5px;">
			    	<Locale></Locale>
			    </li>
			    <li class="list-inline-item"><icon name="bars" scale="0.9"></icon></li>
			    <li class="list-inline-item pl-3" style="margin-top: -3.5px;" v-if="isAuthenticated">{{ getUser.first_name }} <icon name="sort-down" scale="0.9"></icon></li>
			    <li class="list-inline-item" style="margin-top: -3px;" v-else><d-button to="auth" markup="link" shadow="0">Вход</d-button></li>
			  </ul>
		  </div>
		</div>
		<div class="header container hidden-sm-up d-flex justify-content-between px-0">
		    <router-link :to="getLogoUrl">
		    <dBlurShadow>
			      <img :src="getLogoImage" :alt="getLogoAlt" :height="getLogoHeight">
		    </dBlurShadow>
		    </router-link>
			<div class="d-flex align-items-center">
			  <ul class="list-inline text-gray mb-0 d-flex justify-content-center">
			  	<li class="list-inline-item pr-3"><icon name="search" scale="1.2"></icon></li>
			    <li class="list-inline-item"><icon name="bars" scale="1.2"></icon></li>
			  </ul>
			</div>
		</div>
	</div>
</template>

<script>
	import Locale from "@/components/Locale.vue"
	import dButton from "@/components/buttons.vue"
	import { mapGetters }  from 'vuex'

	export default {
		data() {
			return {
				logos: {
					acs: {
						img: "acs-logo.svg",
						text: "acs-logo-text.svg",
						alt: "ACS",
						height: 40,
						url: "/"
					},
					webcampus: {
						img: "webcampus-logo.svg",
						text: "webcampus-logo-text.svg",
						alt: "WebCampus",
						height: 30,
						url: "/webcampus"
					}
				}
			}
		},
		components: {
			Locale,
			dButton
		},
		props: {
			hideElements: {
				type: Boolean,
				default: false
			},
			logo: {
				type: String,
				default: "acs"
			}
		},
		computed: {
			getLogoImage() {
				return require('.././assets/' + this.logos[this.logo].img)
			},
			getLogoText() {
				return require('.././assets/' + this.logos[this.logo].text)
			},
			getLogoAlt() {
				return this.logos[this.logo].alt
			},
			getLogoHeight() {
				return this.logos[this.logo].height
			},
			getLogoUrl() {
				return this.logos[this.logo].url
			},
			routeIndex() {
				return this.$route.name=='index' && !this.hideElements
			},
			isAuthenticated() {
				return this.$auth.isAuthenticated() && this.getUser
			},
			...mapGetters([
			    'getUser'
			])
		},
		methods: {
			collapseWidthAnimation(el, done){
				TweenMax.to(el, 0.4, { opacity: 0, width: 0, ease: Power2.easeOut, onComplete: done })
			}
		}
	}
</script>

<style scoped>
	.overflow-hidden {
		overflow: hidden;
	}
	.header {
		z-index: 10;
	}
</style>

