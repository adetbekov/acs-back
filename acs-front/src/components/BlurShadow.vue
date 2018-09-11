<!-- <template>
	<div class="d-blur" :id="id" :class="customClass" :style="customStyle">
		<div class="bg w-100" ref="slot"><slot><div class="hello"></div></slot></div>
		<div class="head w-100"><slot></slot></div>
	</div>
</template> -->
<!-- :style="{ 'width': this.width + 'px', 'height': this.height +'px'}" -->
<script>
	export default{
		render(h) {
	    return h('div', {
	      'class': [
	        'd-blur'
	      ],
	      ':id': this.id,
	      ':class': this.customClass,
	      'style': this.getStyle
	    }, [
	      h('div',{ 'class': { 'bg':1, 'less': 1, 'w-100':1, 'h-100':1, 'hidden': this.hiddenbg }, 'style': this.getSize }, this.$slots.default),
	      h('div',{ 'class': ['head', 'w-100', 'h-100'], 'style': this.getSize }, this.$slots.default)
	    ])
	  },
		data(){
			return {
				height: 0,
				width: 0
			}
		},
		props: {
			id: {
				type: String,
				default: null
		    },
			customClass: {
				type: String,
				default: null
			},
			customStyle: {
				type: String,
				default: null
			},
			hiddenbg: {
				type: Boolean,
				default: false
			}
		},
		methods: {
			resizeWindow(){
				this.height = this.$slots.default[0].elm.innerHeight
				this.width = this.$slots.default[0].elm.innerWidth
			}
		},
		computed: {
			getSize(){
				return { 'min-height': this.height +'px', 'min-width': this.width +'px'}
			}
		},
		mounted() {
			this.resizeWindow()
			window.addEventListener('resize', ()=>{this.resizeWindow()})
		}
	}
</script>

<style scoped>
	.d-blur {
		position: relative;
		display: block;
	}
	.d-blur div {
		position: absolute;
	}
	.hidden {
		display: none;
	}
	.bg {
		pointer-events: none;
		padding-top: 10px;
		opacity: 0.9;
		transform: scale(0.9);

		-webkit-filter: blur(13px) brightness(110%) saturate(3);
		-moz-filter: blur(13px) brightness(110%) saturate(3);
		-o-filter: blur(13px) brightness(110%) saturate(3);
		-ms-filter: blur(13px) brightness(110%) saturate(3);
		filter: blur(13px) brightness(110%) saturate(3);
	}
	.less {
		-webkit-filter: blur(13px) brightness(95%) saturate(2);
		-moz-filter: blur(13px) brightness(95%) saturate(2);
		-o-filter: blur(13px) brightness(95%) saturate(2);
		-ms-filter: blur(13px) brightness(95%) saturate(2);
		filter: blur(13px) brightness(95%) saturate(2);
	}
</style>