<template>
	<div class="blog-caption">
		<div :id="this.id" :class="this.captionClass">
			<div class="container">
				<div class="row">
					<div :class="this.containerStyle" class="py-3">
						<h1 class="hidden-sm-down m-0" :style="this.captionStyle(1)">{{ caption }}</h1>
						<h2 class="hidden-md-up hidden-xs-down m-0" :style="this.captionStyle(2)">{{ caption }}</h2>
						<h3 class="hidden-sm-up m-0" :style="this.captionStyle(3)">{{ caption }}</h3>
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
	    template: {
				type: Number,
				default: 0
	    },
	    color: {
				type: String,
	    }
		},
		methods: {
			captionStyle(h) {
				return { 'font-size': this.getStyles[this.template][4][h-1] + "px" }
			},
		},
		computed: {
			caption() {
				return this.$slots.default[0].text;
			},
			getColor() {
				return { 'color': this.color }
			},
			getStyles() {
				return [
					[ 0, null, null, [ "mt-3" ], [ 45, 40, 35 ] ],
					[ 1, null, null, [ "col-12", "text-center", "mt-3" ], [ 55, 50, 45 ] ],
					[ 2, null, null, [ "playfair", "mt-3" ], [ 50, 45, 40 ]],
					[ 3, null, null, [ "playfair", "mt-3" ], [ 45, 40, 35 ] ],
					[ 4, null, null, [ "playfair", "col-12", "text-center", "mt-3" ], [ 55, 50, 45 ] ],
					[ 5, null, null, [ "lobster", "mt-3" ], [ 45, 40, 35 ]],
					[ 6, null, null, [ "lobster", "mt-3", "text-center" ], [ 45, 40, 35 ] ],
					[ 7, null, null, [ "amatic-sc", "col-12", "text-center", "mt-3" ], [ 55, 50, 45 ] ],
					[ 8, null, null, [ "amatic-sc", "mt-3" ], [ 50, 45, 40 ]]
				]
			},
			captionClass() {
				return this.getStyles[this.template][1]
			},
			headerStyle() {
				return [ this.getStyles[this.template][2], this.getColor ]
			},
			containerStyle() {
				return this.getStyles[this.template][3]
			}
		}
	}
</script>


<style scoped>
	.blog-caption {
		position: relative;
		padding-top: 0px;
		width: 100%;
		font-family: 'BebasNeue';
		z-index: 0;
	}

	.playfair {
		font-family: 'Playfair Display';
	}

	.lobster {
		font-family: 'Lobster';
	}

	.amatic-sc {
		font-family: 'Amatic SC';
	}

	.bold {
		font-weight: bold;
	}

	h1, h2, h3 {
		position: inherit;
 		z-index: 2;
	}

</style>