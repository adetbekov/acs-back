<template>
	<div class="top container px-0" id="container">
		<div class="row" v-if="lesson && current_step">
			<div class="col-lg-8">
				<h6 class="fw-300 mb-3"><router-link :to="{ name: 'syllabus' }">Силлабус</router-link> &ensp;/&ensp; {{ lesson.name }} &ensp;/&ensp; <b>{{ current_step.title }}</b></h6>
				<div v-for="i in current_step.content">
					<div class="card" v-if="i.type == 'text'">
						{{ i.content }}
					</div>
					<div class="embed-responsive embed-responsive-16by9" v-if="i.type == 'video'">
						<iframe class="embed-responsive-item" allowfullscreen :src="i.uri" frameborder="0"></iframe>
					</div> 
					<div class="card" v-if="i.type == 'html'" v-html="i.content">
					</div>
				</div>
			</div>
			<div class="col-lg-4">
				<ul class="list-unstyled rounded steps">
					<li v-for="step in lesson.steps" class="w-100 mb-0">
						<router-link :to="{ name: 'lesson', params: { course_slug: course_slug, chapter_slug: chapter_slug, step_slug: step.slug } }">
							<div class="step d-flex align-items-center" :class="{ 'active': step_slug == step.title }">
								<icon label="Done" class="syllabus-icon">	
									<icon name="circle" scale="1.8" style="color: #26C281;"></icon>
									<icon name="check" class="text-white" scale="0.7"></icon>	
								</icon>
								<div class="text d-flex flex-column">
									{{ step.title }}
								</div>
							</div>
						</router-link>
					</li>
				</ul>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		data: () => ({
			lesson: null,
			current_step: null
		}),
		props: {
			course_slug: {
				type: String,
				default: ""
			},
			chapter_slug: {
				type: String,
				default: ""
			},
			step_slug: {
				type: String,
				default: ""
			},
		},
		mounted() {
			this.load_lesson()
			this.load_step()
		},
		watch: {
			step_slug: function(val, oldVal) {
				if (val != oldVal) {
					this.load_step()
				}
			},
			chapter_slug: function(val, oldVal) {
				if (val != oldVal) {
					this.load_lesson()
				}
			}
		},
		methods: {
			load_lesson() {
				this.$http.get(`api/webcampus/${ this.course_slug }/${ this.chapter_slug }`).then(response => {
				    this.lesson = response.body
				}, response => {
					console.log("Lesson loading error")
				})
			},
			load_step() {
				this.$http.get(`api/webcampus/${ this.course_slug }/${ this.chapter_slug }/${ this.step_slug }`).then(response => {
				    this.current_step = response.body
				}, response => {
					console.log("Step loading error")
				})
			}
		}
	}
</script>

<style scoped>
	.top {
		margin-top: 30px;
	}
	.card {
		background-color: white;
		width: 100%;
		padding: 20px 25px;
	}
	.step {
		background-color: white;
		width: 100%;
		padding: 10px 22px;
	}
	.step .syllabus-icon{
		margin-right: 25px;
	}
	.inner-list {
		/*margin-left: 1.5%;
		width: 97%;*/
		padding: 0 8px;
	}
	.steps a {
		color: #2c3e50;
		text-decoration: none;
	}
	.active {
		background-color: rgba(149,165,166 ,0.10);
	} 
</style>