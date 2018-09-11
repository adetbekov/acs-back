<template>
	<div class="bg">
		<div class="container px-0" v-if="this.course">
    		<h2 class="mb-4">{{ course.name }}</h2>
		</div>
	</div>
</template>

<script>
	export default {
		data: () => ({
			course: null
		}),
		props: {
			course_slug: {
				type: String,
				default: ""
			}
		},
		mounted() {
			this.$http.get(`api/webcampus/${ this.course_slug }/`).then(response => {
				this.course = response.body
			}, response => {
				console.log("Course loading error")
			}) 
		}
	}
</script>