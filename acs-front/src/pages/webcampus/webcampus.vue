<template>
	<div class="bg">
		<div class="container">
			<Navbar :hideElements="this.hideElements" logo="webcampus" class="bottom">
				<ul style="position: relative; left: -50%;" v-if="$route.path.split('/')[1] == 'webcampus'" class="list-unstyled d-flex align-items-center text-gray m-0 p-0 hidden-sm-down">
			  		<li class="pr-2">
					  	<router-link :to="{ name: 'dashboard' }" class="d-flex flex-column align-items-center" :class="{ 'active': $route.name == 'dashboard'}">
					  		<icon name="dashboard" scale="1.2"></icon>
					  		<small style='line-height:0.8'><span class="small">Основная</span></small>
					  	</router-link>
				  	</li>
				  	<li class="px-3">
						<router-link :to="{ name: 'webcampus' }" class="d-flex flex-column align-items-center" :class="{ 'active': $route.name == 'webcampus'}">
					  		<icon name="store" scale="1.2"></icon>
					  		<small style='line-height:0.8'><span class="small">Магазин курсов</span></small>
					  	</router-link>
					</li>
					<li class="pl-2">
					  	<router-link :to="{ name: 'webcampus' }" class="d-flex flex-column align-items-center" :class="{ 'active': $route.name == 'purchased'}">
					  		<icon name="purchased" scale="1.2"></icon>
					  		<small style='line-height:0.8'><span class="small">Мои курсы</span></small>
					  	</router-link>
				  	</li>
			  	</ul>
			</Navbar>
			<store v-if="this.hideElements" :flipping="this.hideElements"></store>
	    	<keep-alive v-else><router-view></router-view></keep-alive>
		</div>
	</div>
</template>

<script>
	import store from './store.vue'
	import { mapGetters }  from 'vuex'

	export default {
		props: {
			hideElements: {
				type: Boolean,
				default: false
			}
		},
		components: {
			store,
		},
		computed: {
			...mapGetters([
			    'getUser'
			])
		}
	}
</script>

<style scoped>
	.bottom {
		margin-bottom: 15px;
	}
	.bg {
		min-height: 100vh;
		color: #2c3e50;
		background-color: #f7f7f7;
		overflow: hidden;
	}
	.active * {
		color: #3498db;
	}
	a {
	  color: #7e7f81;
	  text-decoration: none;
	}

	a:focus, a:hover {
	  color: #3498db;
	  text-decoration: none;
	}
</style>