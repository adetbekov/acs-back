<template>
	<div class="bg">
		<div class="container">
			<Navbar :hideElements="this.hideElements" class="bottom"></Navbar>
			<list v-if="this.hideElements" :flipping="this.hideElements"></list>
	    	<keep-alive v-else><router-view></router-view></keep-alive>
		</div>
	</div>
</template>

<script>
	// import Navbar from '../.././components/Navbar.vue'
	import Masonry from 'masonry-layout'
	import list from './list.vue'

	export default {
		props: {
			hideElements: {
				type: Boolean,
				default: false
			}
		},
		components: {
			list,
		}
	}
</script>

<style scoped>
	.bg {
		height: 100%;
		color: #2c3e50;
		background-color: white;
	}
	.bottom {
		margin-bottom: 15px;
	}
</style>






