<template>
	<div class="blog-header">
		<div :id="this.id" :class="this.headerClass" :style="this.headerStyle" :fullTop="this.fullTop" :overlay="this.overlay" :overlayTop="this.overlayTop">
			<div class="container">
				<div class="row">
					<div :class="this.containerStyle" class="py-3">
						<h1 class="t hidden-sm-down m-0" :style="this.titleStyle(1)">{{ title }}</h1>
						<h2 class="t hidden-md-up hidden-xs-down m-0" :style="this.titleStyle(2)">{{ title }}</h2>
						<h3 class="t hidden-sm-up m-0" :style="this.titleStyle(3)">{{ title }}</h3>
						<p class="t m-0 p-0">{{ moment(this.created).format("MMM D, YYYY HH:MM") }}</p>
					</div>
				</div>
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
	    post: {
				type: Object,
				required: true
	    },
	    template: {
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
	    overlay: {
				type: Boolean,
				default: false
	    },
	    overlayTop: {
				type: Boolean,
				default: false
	    }
		},
		methods: {
			titleStyle(h) {
				return { 'font-size': this.getStyles[this.template][4][h-1] + "px" }
			},
			animation(c) {
				let tl = new TimelineLite()
				if (c) tl.from('.blog-header', 0.8, { opacity: 0, ease: Power3.easeOut }, 0.3)
					.staggerFrom('.t', 2, { y: -10, scale: 0.95, ease: Elastic.easeOut, opacity: 0 }, 0.1)
			}
		},
		computed: {
			title() {
				return this.post.title
			},
			created() {
				return this.post.created
			},
			getBackground() {
				return { 'background-image': 'url('+this.post.image_url+')' }
			},
			getColor() {
				return { 'color': this.color }
			},
			getStyles() {
				return [
					[ 0, null, null, [ "mt-5" ], [ 45, 45, 45 ] ],
					[ 1, null, null, [ "col-12", "text-center", "mt-3" ], [ 55, 50, 45 ] ],
					[ 2, [ "hf", "bg" ], this.getBackground, [ "col-12", "text-center" ], [ 65, 60, 55 ] ],
					[ 3, [ "hf", "bg" ], this.getBackground, [ "col-6" ], [ 55, 45, 40 ] ],
					[ 4, [ "hh", "bg" ], this.getBackground, [ "col-12", "text-center" ], [ 60, 50, 45 ] ],
					[ 5, [ "hh", "bg" ], this.getBackground, [ "col-6" ], [ 45, 35, 35 ] ],
					[ 6, [ "hf", "bg", "bottom", "pb-md-3" ], this.getBackground, [ "col-12" ], [ 45, 35, 35 ] ]
					[ 7, [ "hh", "bg", "bottom", "pb-md-3" ], this.getBackground, [ "col-12" ], [ 45, 35, 35 ] ]
				]
			},
			headerClass() {
				return this.getStyles[this.template][1]
			},
			headerStyle() {
				return [ this.getStyles[this.template][2], this.getColor ]
			},
			containerStyle() {
				return this.getStyles[this.template][3]
			}
		},
		mounted(){
			this.animation(this.getStyles[this.template][2])
		}
	}
</script>


<style scoped>
	.blog-header {
		position: relative;
		padding-top: 0px;
		width: 100%;
		font-family: 'BebasNeue';
		z-index: 0;
	}

	.bg {
		text-shadow: 2px 4px 3px rgba(0,0,0,0.5);
		display: flex;
		flex-direction: column;
		justify-content: center;
		background-position: center;
		background-size: cover;
	}

	.bottom {
		justify-content: flex-end;
	}

	.hf {
		min-height: calc( 100vh - 75px );
	}

	.hf[fulltop="true"] {
		min-height: 100vh;
		margin-top: -75px;
	}

	.hh {
		min-height: calc( 60vh - 75px );
	}

	.hh[fulltop="true"] {
		min-height: 60vh;
		margin-top: -75px;
	}

	.bg[overlay="true"]:after {
	  content:'';
	  position: absolute;
	  left: 0;
	  width: 100%;
	  min-height: 150px;
	  bottom: 0;
	  background: linear-gradient(
	    to bottom,
	    rgba(0,0,0,0),
	    rgba(0,0,0,1)
	  );
	  z-index:1;
	}

	.bg[overlaytop="true"]:before {
	  content:'';
	  position: absolute;
	  left: 0;
	  width: 100%;
	  min-height: 120px;
	  top: 0;
	  background: linear-gradient(
	    to top,
	    rgba(0,0,0,0),
	    rgba(0,0,0,1)
	  );
	  z-index: 1;
	}

	h1, h2, h3 {
		position: inherit;
 		z-index: 2;
	}

</style>