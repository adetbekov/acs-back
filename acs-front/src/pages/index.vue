<i18n>
	{
		"ru": {
			"hello": "Привет!",
			"welcoming": "Добро пожаловать в Adetbekov Creative Studio.",
			"blog": "Блог",
			"blog-inner": "Почему UX это важно",
			"academy": "Академия",
			"academy-inner": "Курс Vue.js essentials",
			"projects": "Проекты",
			"projects-inner": "Upgradeland intranet"
		},
		"kz": {
			"hello": "Sälem",
			"welcoming": "Adetbekov Creative Studio jobasına koc keldińiz.",
			"blog": "Blog",
			"blog-inner": "UX nege mańızdı",
			"academy": "Kädem",
			"academy-inner": "Vue.js essentials kürsi",
			"projects": "Jobalar",
			"projects-inner": "Upgradeland intraneti"
		},
		"en": {
			"hello": "Hello",
			"welcoming": "Welcome to Adetbekov Creative Studio.",
			"blog": "Blog",
			"blog-inner": "UX importance",
			"academy": "Academy",
			"academy-inner": "Vue.js essentials course",
			"projects": "Projects",
			"projects-inner": "Upgradeland intranet"
		}
	}	
</i18n>

<template>
	<div class="fullbg">
	<div class="container h-100 d-flex flex-column justify-content-center" ref="container">
		<Navbar></Navbar>
		<div class="hidden-md-up mt-5">
			<img src="../assets/Face-index.png" alt="Face-index" class="img-fluid mainimg" width="539" height="505">
		</div>
		<div class="row">
			<div class="offset-lg-1 offset-md-0 col-lg-4 col-md-6 d-flex flex-column justify-content-center toTop">
				<h1 class="fw-100 stagger1 mb-4">{{ $t("hello") }}</h1>
				<h4 class="fw-100 stagger1">{{ $t("welcoming") }}</h4>
				<!--<p class="fw-100 stagger1">Меня зовут Елдос. Я Fullstack Веб-Разработчик. Вдохновляют красивые UI/UX.</p>-->	
				<div class="row mt-2 stagger1 mt-3">
					<div class="col-6 col-xl-4 pb-4" :class="{ 'toTop': this.toTop(1) }">
							<div class="card-container h-100">
								<div class="card" ref="tale1" url="blog">
									<div class="side" :class="{ 'overflow-hidden': this.hiddenbg }">
										<dBlurShadow class="h-100" :hiddenbg="this.hiddenbg">
											<button class="heading" @click="flip(1)">
												<p class="m-0">{{ $t("blog") }}</p>
												<p class="m-0 small fw-300 content">{{ $t("blog-inner") }}</p>
											</button>
										</dBlurShadow>
									</div>
									<div class="side back overflow-hidden">
										<div is="blog" :hideElements="true"></div>
									</div>
								</div>
							</div>
					</div>
					<div class="col-6 col-xl-4 pb-4" :class="{ 'toTop': this.toTop(2) }">
							<div class="card-container h-100">
								<div class="card" ref="tale2" url="webcampus">
									<div class="side" :class="{ 'overflow-hidden': this.hiddenbg }">
										<dBlurShadow class="h-100" :hiddenbg="this.hiddenbg">
											<button class="heading" @click="flip(2)">
												<p class="m-0">{{ $t("academy") }}</p>
												<p class="m-0 small fw-300 content">{{ $t("academy-inner") }}</p>
											</button>
										</dBlurShadow>
									</div>
									<div class="side back overflow-hidden">
										<div is="webcampus" :hideElements="true"></div>
									</div>
								</div>
							</div>
					</div>
					<div class="col-6 col-xl-4 pb-4" :class="{ 'toTop': this.toTop(3) }">
							<div class="card-container h-100">
								<div class="card" ref="tale3" url="/">
									<div class="side" :class="{ 'overflow-hidden': this.hiddenbg }">
										<dBlurShadow class="h-100" :hiddenbg="this.hiddenbg">
											<button class="heading" @click="flip(3)">
												<p class="m-0">{{ $t("projects") }}</p>
												<p class="m-0 small fw-300 content">{{ $t("projects-inner") }}</p>
											</button>
										</dBlurShadow>
									</div>
									<div class="side back overflow-hidden">
										<div is="blog" :hideElements="true"></div>
									</div>
								</div>
							</div>
					</div>
				</div>
			</div>
			<div class="col-md-6 hidden-sm-down">
				<img src="../assets/Face-index.png" alt="Face-index" class="img-fluid mainimg" width="539" height="505">
			</div>
		</div>
	</div>
	</div>
</template>

<script>
	import blog from './blog/blog.vue'
	import Navbar from '.././components/Navbar.vue'
	import webcampus from './webcampus/webcampus.vue'

	export default {
		components: {
			blog,
			Navbar,
			webcampus
		},
		data(){
			return { 
				hiddenbg: false,
				flipped: null
			}
		},
		methods: {
			toTop(card){
				return this.flipped == card
			},
			cumulativeOffset(element) {
			    var top = 0, left = 0
			    do {
			        top += element.offsetTop  || 0
			        left += element.offsetLeft || 0
			        element = element.offsetParent;
			    } while(element)

			    return {
			        top: top,
			        left: left
			    }
			},
			flip(t){
				this.flipped = t
				let tale = 'tale'+t
				let tl = new TimelineLite()
				let box = this.cumulativeOffset(this.$refs[tale])
				tl.set(this.$refs[tale], { transition: 'none', position:'absolute'})
					.to(this.$refs[tale], 1, { left: -box.left, top: -box.top, width: "100vw", height: "100vh", transform: 'rotate3d(0,1,0,180deg)', borderRadius: 0, ease: Power4.easeInOut, onStart: () => { this.hiddenbg = true }, onComplete: () => { this.$router.push(this.$refs[tale].getAttribute("url")) } })
			}
		},
		mounted(){
			let tl = new TimelineLite()
			tl.from('.mainimg', 1, { opacity: 0, ease: Power1.easeInOut }, 0.6)
				.staggerFrom('.stagger1', 0.4, { x: 130, scale: 0.7, ease: Power1.easeInOut, opacity: 0 }, 0.1)
		}
	}
</script>

<style scoped>
	.fullbg {
		min-height: 100vh;
		background-color: #181818;
		/*#1e1f24;*/
	}
	* {
		color: white;
	}
	h1 {
		white-space: nowrap;
		text-overflow: ellipsis;
		font-size: 72px;
		color: white;
	}
	.heading {
		border: none;
		text-align: left;
		cursor: pointer;
		line-height: 1.4;
		padding: 5px 10px 10px;
		/*min-width: 96px;*/
		min-height: 100%;
		position: absolute;
		width: 100%;
		background: linear-gradient(to top right, #3498db, #9b59b6);
		border-radius: 12px;
		transform: rotate3d(-180,0,0,0deg);
		transition: all 0.1s ease-in-out;
	}
	.small {
		line-height: 1.1;
	}
	.stagger1 {
		/*min-height: 65px;*/
	}
	.content {
	   overflow: hidden;
	   display: -webkit-box;
	   -webkit-box-orient: vertical;
	   -webkit-line-clamp: 2; 
	}
	/*.minheight {
		min-height: 85px;
	}*/
	.card-container {
		min-height: 65px;
	  /*cursor: pointer;*/
	  perspective: 600;
	  position: relative;
	}
	.card {
	  height: 100%;
	  position: absolute;
	  overflow: visible !important;
    transform-style: preserve-3d;
	  transition: all 1s ease-in-out;
	  width: 100%;
	}
	.card .side {
		transform: rotateY(0deg);
	  backface-visibility: hidden;
	  /*border-radius: 6px;*/
	  height: 100%;
	  position: absolute;
	  width: 100%;
	}
	.overflow-hidden {
		overflow: hidden;
	}
	.card .back {
	  transform: rotateY(180deg);
	}
	.toTop{
		z-index: 1000;
	}
</style>