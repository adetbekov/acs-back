<template>
	<div class="fullbg">
	<div class="container h-100 d-flex flex-column justify-content-center" ref="container">
		<Navbar></Navbar>
		<div  class="w-100 mt-5 pt-md-5">
		  <transition name="component-fade" mode="out-in">
		    <keep-alive>
		      <div :is="$store.state.authFormCurrent"></div>
		    </keep-alive>
		  </transition>
		  </div>
		</div>	
	</div>
	</div>
</template>

<script>
	import login from "@/pages/auth/login.vue"
	import register from '@/pages/auth/register.vue'

	export default {
		components: {
			login,
			register
		}
	}
</script>

<style scoped>
	.bg {
		min-height: 100vh;
		color: #2c3e50;
		background-color: #f7f7f7;
		overflow: hidden;
	}
	.component-fade-enter-active, .component-fade-leave-active {
		transition: all 0.15s ease-in-out;
	}
	.component-fade-enter, .component-fade-leave-to{
		opacity: 0;
		transform: scale(2);
	}
</style>