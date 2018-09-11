<template lang="jade">
	button(
		class="d-btn", 
		:id="id", 
		:class="customClass", 
		:name="name", 
		:disabled="disabled", 
		:small="small",
		:large="large", 
		:markup="markup", 
		:outline="outline", 
		:transition="transition", 
		:rectangular="rectangular", 
		:shadow="shadow", 
		:block="block", 
		:circle="circle", 
		:to="to",
		:style="{ 'min-width': this.width+'px' }",
		:loading="loading"
		@click="handleClick") 
			svg(v-if="loading" height="10" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 683.3 383.7" xml:space="preserve")
				path(id="st0" d="M479.6,42.3c80.8,0,146.2,65.5,146.2,146.2s-65.5,146.2-146.2,146.2c-80.8,0-123-61.8-138.6-144.8v1.5 c-13.2-74.5-57-146.2-137.8-146.2S57,110.7,57,191.4s65.5,146.2,146.2,146.2")
				path(id="st1" d="M479.6,42.3c80.8,0,146.2,65.5,146.2,146.2s-65.5,146.2-146.2,146.2c-80.8,0-123-61.8-138.6-144.8v1.5 c-13.2-74.5-57-146.2-137.8-146.2S57,110.7,57,191.4s65.5,146.2,146.2,146.2")
			slot(v-else)
</template>

<script>
	export default {
		data(){
			return {
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
		    name: {
				type: String,
				default: null
		    },
		    disabled: {
				type: Boolean,
				default: false
		    },
		    loading: {
				type: Boolean,
				default: false
		    },
		    large: {
				type: Boolean,
				default: false
		    },
		    small: {
				type: Boolean,
				default: false
		    },
		    transition: {
				type: Boolean,
				default: true
		    },
		    rectangular: {
				type: Boolean,
				default: false
		    },
		    outline: {
				type: Boolean,
				default: false
		    },
		    block: {
				type: Boolean,
				default: false
		    },
		    markup: {
				type: String,
				default: 'default'
		    },
		    shadow: {
		    	type: String,
		    	default: "true"
		    },
		    circle: {
		    	type: String,
		    	default: "false"
		    },
		    to: {
				type: String,
				default: ''
		    },
		},
		methods:{
			handleClick (e) {
		      this.$emit('click', e)
		      this.$router.push(this.to)
		    }
		},
		mounted() {
			if(this.markup!="link")
				this.width = this.$el.offsetWidth
		}
	}
</script>

<style lang="sass?indentedSyntax=true">
	$default-color: #AAB6BD
	$default-hover-color: #bdc3c7
	$primary-color: #25b964
	$primary-hover-color: #2ecc71
	$info-color: #45576A
	$info-hover-color: #5E6C7B
	$success-color: #3ca2d9
	$success-hover-color: #54b3e6
	$warning-color: #E9BB00
	$warning-hover-color: #F7CB19
	$danger-color: #E15D4F
	$danger-hover-color: #ED776B
	$disabled-color: #bdc3c7

	@mixin button-color($color, $hover-color) 
		background-color: $color
		color: white
		&[outline="true"] 
			color: $color
			background: 0 0
		box-shadow: 0 0 0 1.25px $color inset
		&:enabled
			&:hover 
				background-color: $hover-color
				color: white
				box-shadow: 0 0 0 1.25px $hover-color inset
				&[shadow="true"]
					box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)
	.d-btn 
		cursor: pointer
		border: none
		background: 0 0
		border-radius: 3.5px
		font-family: 'Roboto', Helvetica, Arial, sans-serif
		font-weight: 300
		font-size: 1rem
		text-align: center
		display: block
		white-space: nowrap
		vertical-align: middle
		padding: 6px 18px
		text-decoration: none
		text-transform: none
		outline: 0
		-webkit-touch-callout: none 
		-webkit-user-select: none
		-khtml-user-select: none
		-moz-user-select: none
		-ms-user-select: none
		user-select: none
	
		
		&:disabled
			opacity: .65;
			cursor: not-allowed
			
		&[block="true"] 
			width: 100%
			padding: 6px auto

		&[circle="true"] 
			padding: 8px auto
			border-radius: 50%

		&[large="true"] 
			font-size: 1.4rem

		&[small="true"] 
			font-size: 1rem
			padding: 0px 5px

		&[transition="true"]
			transition: 0.2s 

		&[rectangular="true"] 
			border-radius: 0px

		&[markup="default"] 
			@include button-color($default-color, $default-hover-color)
		
		&[markup="primary"] 
			@include button-color($primary-color, $primary-hover-color)

		&[markup="info"] 
			@include button-color($info-color, $info-hover-color)
		
		&[markup="success"] 
			@include button-color($success-color, $success-hover-color)
		
		&[markup="warning"] 
			@include button-color($warning-color, $warning-hover-color)
		
		&[markup="danger"] 
			@include button-color($danger-color, $danger-hover-color)

		&[markup="link"] 
			color: $primary-color
			&:hover
				color: $primary-hover-color
				/*text-decoration: underline*/
			box-shadow: none
		&[shadow="true"]
			box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)
			transition: all 0.3s cubic-bezier(.25,.8,.25,1)
			
</style>
<style>
    #st0{fill:none;stroke:#D9D9D9;stroke-width:85;stroke-miterlimit:10;display: none}
    #st1{fill:none;stroke:white;stroke-width:85;stroke-miterlimit:10;
      stroke-dasharray: 1000;
      stroke-dashoffset: 1000;
      -webkit-animation: dash 1s linear forwards infinite;
      -moz-animation: dash 1s linear forwards infinite;
      -o-animation: dash 1s linear forwards infinite;
      animation: dash 1s linear forwards infinite;
    }
    @-webkit-keyframes dash{
      from{
        stroke-dashoffset: -2000;
      }
      to{
        stroke-dashoffset: 0;
      }
    }
  </style>
