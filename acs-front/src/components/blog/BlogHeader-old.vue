<template>
	<div class="header" :id="id" :class="customClass">

		<div v-if="this.layout == 1">
			<div class="header-1" :style="{ 'background-image': 'url('+this.post.image_url+')' }" :fullTop="this.fullTop">
				<div class="container">
					<div class="row">
						<div class="col-12 text-center" :style="{ 'color': this.color }">
							<h1 class="hidden-sm-down">{{ title }}</h1>
							<h2 class="hidden-md-up hidden-xs-down">{{ title }}</h2>
							<h3 class="hidden-sm-up">{{ title }}</h3>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div v-if="this.layout == 11">
			<div class="header-2" :style="{ 'background-image': 'url('+this.post.image_url+')' }" :fullTop="this.fullTop">
				<div class="container">
					<div class="row">
						<div class="col-6" :style="{ 'color': this.color }">
							<h1 class="hidden-md-down">{{ title }}</h1>
							<h2 class="hidden-xs-down hidden-lg-up">{{ title }}</h2>
							<h3 class="hidden-sm-up">{{ title }}</h3>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div v-if="this.layout == 12">
			<div class="header-2" :style="{ 'background-image': 'url('+this.post.image_url+')' }" :fullTop="this.fullTop">
				<div class="container">
					<div class="row">
						<div class="col-6" :style="{ 'color': this.color }">
							<h1 class="hidden-md-down">{{ title }}</h1>
							<h2 class="hidden-xs-down hidden-lg-up">{{ title }}</h2>
							<h3 class="hidden-sm-up">{{ title }}</h3>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div v-if="this.layout == 2">
			<div class="header-3" :style="{ 'background-image': 'url('+this.post.image_url+')' }" :fullTop="this.fullTop">
				<div class="container">
					<div class="row">
						<div class="col-12 text-center" :style="{ 'color': this.color }">
							<h1 class="hidden-sm-down">{{ title }}</h1>
							<h2 class="hidden-md-up hidden-xs-down">{{ title }}</h2>
							<h3 class="hidden-sm-up">{{ title }}</h3>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div v-if="this.layout == 21">
			<div class="header-4" :style="{ 'background-image': 'url('+this.post.image_url+')' }" :fullTop="this.fullTop">
				<div class="container">
					<div class="row">
						<div class="col-6" :style="{ 'color': this.color }">
							<h1 class="hidden-md-down">{{ title }}</h1>
							<h2 class="hidden-xs-down hidden-lg-up">{{ title }}</h2>
							<h3 class="hidden-sm-up">{{ title }}</h3>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div v-if="this.layout == 3">
			<div class="header-5 mt-5">
				<h1 class="hidden-md-down">{{ title }}</h1>
				<h2 class="hidden-xs-down hidden-lg-up">{{ title }}</h2>
				<h3 class="hidden-sm-up">{{ title }}</h3>
			</div>
		</div>

		<div v-if="this.layout == 0">
			<div class="header-0">
				<h2 class="mt-5">{{ title }}</h2>
			</div>
		</div>

	</div>
</template>

<script>
	export default {
		props: {
		    id: {
					type: String,
					default: null
		    },
		    customClass: {
					type: String,
					default: null
		    },
		    post: {
					type: Object,
					required: true
		    },
		    overlay: {
					type: Boolean,
					default: false
		    },
		    layout: {
					type: Number,
					default: 0
		    },
		    color: {
					type: String,
		    },
		    fullTop: {
					type: Boolean,
					default: false
		    },
		},
		computed: {
			title() {
				return this.post.title
			}
		}
	}
</script>

<style scoped>
	.header {
		padding-top: 0px;
		width: 100%;
	}
	.header-1, .header-3 {
		min-height: calc( 100vh - 75px );
		display: flex;
		flex-direction: column;
		justify-content: center;
		background-position: center;
		background-size: cover;
		font-family: 'BebasNeue';

		text-shadow: 2px 4px 3px rgba(0,0,0,0.4);
	}
	.header-1[fulltop="true"] {
		min-height: 100vh;
		margin-top: -75px;
	}
	.header-1 h1 {
		font-size: 65px;
	}
	.header-1 h2 {
		font-size: 60px;
	}
	.header-1 h3 {
		font-size: 55px;
	}

	.header-3 {
		min-height: calc( 60vh - 75px );
	}

	.header-3[fulltop="true"] {
		min-height: 60vh;
		margin-top: -75px;
	}

	.header-3 h1 {
		font-size: 60px;
	}

	.header-3 h2 {
		font-size: 50px;
	}

	.header-3 h3 {
		font-size: 45px;
	}

	.header-2 {
		min-height: calc( 100vh - 75px );
		display: flex;
		flex-direction: column;
		justify-content: center;
		background-position: center;
		background-size: cover;
		font-family: 'BebasNeue';

		text-shadow: 2px 4px 3px rgba(0,0,0,0.4);
	}
	.header-2[fulltop="true"] {
		min-height: 100vh;
		margin-top: -75px;
	}
	.header-2 h1 {
		font-size: 55px;
	}
	.header-2 h2 {
		font-size: 45px;
	}
	.header-2 h3 {
		font-size: 40px;
	}

	.header-0 {
		font-family: 'BebasNeue';
	}

	.header-0 h2 {
		font-size: 50px;
	}

	.header-5 {
		text-align: center;
		font-family: 'BebasNeue';
	}

	.header-5 h1 {
		font-size: 55px;
	}
	.header-5 h2 {
		font-size: 45px;
	}
	.header-5 h3 {
		font-size: 40px;
	}
</style>