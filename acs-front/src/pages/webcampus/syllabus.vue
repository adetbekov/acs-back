<template>
	<div class="container px-0" id="container">
  		<div class="row">
	  		<div class="col-lg-12" v-if="syllabus">
	  			<h5 class="fw-300 my-4">Силлабус:</h5>
				<div class="row">
				<ul class="list-unstyled col-lg-8 col-md-12">
					<li v-for="(chapter, i) in chapters" class="w-100 mb-3">
						<div @click="clickCard(i)">
						<shadows class="card d-flex align-items-center" intensity="1" :hoverIntensity="(opened == i) ? '0' : '1'" radius="5px" :block="true">	
							<!-- <icon label="Play">	
								<icon name="circle" scale="2.5" style="color: #3498db;"></icon>
								<icon name="play" class="text-white" scale="1" width="15"></icon>	
							</icon>
							<icon label="Lock">	
								<icon name="circle" scale="2.5" style="color: #BDC3C7;"></icon>
								<icon name="lock" class="text-white" scale="1.09"></icon>	
							</icon> -->
							<icon label="Done" class="syllabus-icon">	
								<icon name="circle" scale="2.5" style="color: #26C281;"></icon>
								<icon name="check" class="text-white" scale="1.09"></icon>	
							</icon>
							<div class="text d-flex flex-column">
								<small>LESSON {{ i }}</small>
								<h5><b>{{ chapter.name }}</b></h5>
							</div>
							<icon name="caret-down" class="ml-auto" style="color: #BDC3C7;"></icon>	
						</shadows>
						</div>
						<transition @enter="toggleWidthAnimation" @leave="collapseWidthAnimation">
							<ul class="list-unstyled inner-list overflow-hidden" v-if="opened == i"  style="height: auto;">
								<li v-for="step in chapter.steps" class="w-100 mb-0">
									<router-link :to="{ name: 'lesson', params: { course_slug: course_slug, chapter_slug: chapter.slug, step_slug: step.slug } }">
										<shadows class="step d-flex align-items-center" intensity="1" :block="true" radius="0">
											<icon label="Done" class="syllabus-icon">	
												<icon name="circle" scale="1.8" style="color: #26C281;"></icon>
												<icon name="check" class="text-white" scale="0.7"></icon>	
											</icon>
											<div class="text d-flex flex-column">
												{{ step.title }}
											</div>
										</shadows>
									</router-link>
								</li>
							</ul>
						</transition>
					</li>
				</ul>
				</div>
	  		</div>
	  	</div>
	</div>
</template>

<script>
	import shadows from "@/components/shadows.vue"

	export default {
		data: () => ({
			syllabus: null,
			opened: null
		}),
		props: {
			course_slug: {
				type: String,
				default: ""
			}
		},
		components: {
			shadows,
		},
		methods: {
			clickCard(i) {
				if (i != this.opened) { 
					this.opened = i 
				} else { 
					this.opened = null 
				}
			},
			collapseWidthAnimation(el, done){
				let tl = new TimelineLite()
				tl.set(el, { y: 0 }).to(el, 0.4, { opacity: 0, height: 0, ease: Power2.easeInOut, onComplete: done })
			},
			toggleWidthAnimation(el, done){
				let tl = new TimelineLite()
				tl.from(el, 0.4, { opacity: 0, height: 0, ease: Power2.easeOut, onComplete: done })
			}
		},
		computed: {
			chapters() { 
				return this.syllabus.chapters
			}
		},
		mounted() {
			this.$http.get(`api/webcampus/${ this.course_slug }/syllabus`).then(response => {
			    this.syllabus = response.body
			}, response => {
				console.log("Syllabus loading error")
			})
		}
	}
</script>

<style scoped>
	.top {
		margin-top: 50px;
	}
	.card {
		background-color: white;
		width: 100%;
		padding: 25px 30px 25px 25px;
		border-radius: 5px;
		transition: all 0.35s;
	}
	.card:hover {
		transform: scale(1.01);
		cursor: pointer;
	}
	.syllabus-icon {
		margin-right: 20px;
	}
	.text small {
		color: #BDC3C7;
		font-weight: bold;
		margin-bottom: 2px;
	}
	.text h5 {
		font-size: 20px;
		margin: 0;
		padding: 0;
	}
	.step {
		background-color: white;
		width: 100%;
		padding: 10px 22px;
		border-radius: 0px;
		border-top: 1px solid rgba(0,0,0,0.1);
	}
	.step:hover{
		background-color: rgba(149,165,166 ,0.10);
		cursor: pointer;
	}
	.step .syllabus-icon{
		margin-right: 25px;
	}
	.inner-list {
		/*margin-left: 1.5%;
		width: 97%;*/
		padding: 0 8px;
	}
	a {
		color: #2c3e50;
		text-decoration: none;
	}
	.overflow-hidden {
		overflow: hidden;
	}
</style>