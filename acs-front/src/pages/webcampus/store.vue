<template>
	<div class="top container px-0" id="container">
  		<div class="row">
	  		<div class="col-lg-12">
	  			<h5 class="fw-300 blue mb-3">Фильтр:</h5>
	  			<swiper :options="swiperOption" class="categories" id="filter_slider">
  			        <swiper-slide v-for="subject in subjects" :key="subject.icon_name" class="li">
  			        	<shadows intensity="9" hoverIntensity="-1" radius="8px" class="w-100">	
		  					<div class="card">
		  						<div class="info">
		  							<h5 class="mb-0 pb-0"><b>{{ subject.name }}</b></h5>
		  							<span class="text-gray"><small>{{ subject.count }} курсов</small></span>
		  						</div>
		  						<div class="icon">
		  							<icon :name="subject.icon_name" scale="1.3" :color="subject.color"></icon>	
		  						</div>
		  					</div>
	  					</shadows>
  			        </swiper-slide>
  			    </swiper>
  			    
	  			<div class="row">
	  			<div class="col-md-4">
		  			<h5 class="fw-300 blue mb-3 top">Популярно: <span class="small float-right text-gray">Еще</span></h5>
		  			<ul class="popular list-unstyled">
		  				<li class="big-popular">
							<shadows intensity="12" radius="8px">	
			  					<div class="card">
			  						<div class="info">
			  							<h5 class="mb-0 pb-0"><b>Python</b></h5>
			  							<span class="text-gray"><small>12345</small></span>
			  						</div>
			  						<div class="icon">
			  							<icon name="book" scale="1.3" color="#e74c3c"></icon>	
			  						</div>
			  					</div>
		  					</shadows>
		  				</li>
		  			</ul>
		  			<ul class="popular list-unstyled">
		  				<li>
							<shadows intensity="7" radius="8px">	
			  					<div class="card">
			  						<div class="info">
			  							<h5 class="mb-0 pb-0"><b>OpenCV</b></h5>
			  							<span class="text-gray"><small>12345</small></span>
			  						</div>
			  						<div class="icon">
			  							<icon name="folder" scale="1.3" color="#2ecc71"></icon>	
			  						</div>
			  					</div>
		  					</shadows>
		  				</li>
		  				<li>
							<shadows intensity="7" radius="8px">	
			  					<div class="card">
			  						<div class="info">
			  							<h5 class="mb-0 pb-0"><b>C++</b></h5>
			  							<span class="text-gray"><small>12345</small></span>
			  						</div>
			  						<div class="icon">
			  							<icon name="magic" scale="1.3" color="#3498db"></icon>	
			  						</div>
			  					</div>
		  					</shadows>
		  				</li>
		  			</ul>	
	  			</div>
	  		</div>
	  		</div>
		</div>
	</div>
</template>

<script>
	import shadows from "@/components/shadows.vue"

	export default {
		data() {
			return {
				subjects: [],
				loading_subjects: true,
				swiperOption: {
		          slidesPerView: 5,
		          spaceBetween: 25,
		          // init: false,
		          // pagination: {
		          //   el: '.swiper-pagination',
		          //   clickable: true
		          // },
		          mousewheel: true,
		          grabCursor: true,
		          // loop: true,
		          // loopFillGroupWithBlank: true,
		          breakpoints: {
		            576: {
		              slidesPerView: 1.5,
		              spaceBetween: 25
		            },
		            768: {
		              slidesPerView: 2.5,
		              spaceBetween: 25
		            },
		            992: {
		              slidesPerView: 3,
		              spaceBetween: 25
		            },
		            1200: {
		              slidesPerView: 4,
		              spaceBetween: 25
		            },
		          }
		        }
			}
		},
		components: {
			shadows,
		},
		props: {
			flipping: {
				type: Boolean,
				default: false
			}
		},
		methods: {
			// resize() {
			// 	let container = document.getElementById("container")
			// 	let filter_slider = document.getElementById("filter_slider")
				// filter_slider.style.width = (window.innerWidth - container.clientWidth)/2 + container.clientWidth + "px"
			// }
		},
		mounted(){
			if(!this.flipping){
				this.$http.get('api/webcampus/subjects').then(response => {
				    this.subjects = response.body
				    this.loading_posts = false
				}, response => {
					console.log("Subjects loading error")
				})
				// this.$http.get('http://localhost:8000/api/blog/categories').then(response => {
				// 	this.categories = response.body
				// 	this.loading_categories = false
				// }, response => {
				// 	console.log("Categories loading error")
				// })
				// this.$http.get('http://localhost:8000/api/blog/tags').then(response => {
				// 	this.tags = response.body
				// 	this.loading_tags = false
				// }, response => {
				// 	console.log("Tags loading error")
				// })
			}
			// window.addEventListener("resize", () => { this.resize() })
			// this.resize()
		}
	}
</script>

<style scoped>
	.top {
		margin-top: 50px;
	}
	.categories {
		/*display: flex;*/
		overflow: visible;
		min-width: 100%;
	}
	.categories .card {
		display: flex;
		padding: 18px 18px 16px 16px;
		border-radius: 8px;
		/*min-width: 1680px;*/
		height: 66px;
		justify-content: space-between;
		background-color: white;
		align-items: stretch;
	}
	.li {
		/*min-width: 200px;*/
	}
	.categories .card .info {
		align-self: flex-end;
		padding: 5px 0 0 0;
	}
	.categories .card .info * {
		line-height: 0.6;
	}
	.categories .card .info {
		white-space: nowrap;
		max-width: 100%;
	  	overflow-x: hidden;
	  	text-overflow: ellipsis;
	}
	.popular {
		display: flex;
		min-width: 100%;
	}
	.popular li {
		margin-right: 25px;
		margin-bottom: 10px;
	}
	.popular .card {
		display: flex;
		padding: 18px 18px 16px 16px;
		border-radius: 8px;
		/*min-width: 180px;*/
		height: 100px;
		justify-content: space-between;
	}
	.popular .card .info {
		align-self: flex-end;
	}
	.popular .card .info * {
		line-height: 0.6;
	}
	.big-popular .card {
		/*min-width: 385px;*/
		height: 200px;
	}
</style>