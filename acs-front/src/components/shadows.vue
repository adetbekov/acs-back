<template lang="jade">
	div(
	class="d-shdw", 
	:id="id", 
	:class="customClass", 
	:intensity="intensity", 
	:hoverIntensity="hoverIntensityValue", 
	:radius="radius", 
	:block="block", 
	:style="customStyle")
		slot
</template>

<script>
	export default{
		props: {
			id: {
				type: String,
				default: null
		    },
		    customClass: {
				type: String,
				default: null
		    },
			intensity: {
				type: String,
				default: "2"
			},
			hoverIntensity: {
				type: String,
				default: null
			},
			block: {
				type: Boolean,
				default: false
		    },
			radius: {
				type: String,
				default: "3.5px"
			},
		},
		computed: {
			customStyle(){
				return { borderRadius: this.radius }  
			},
			hoverIntensityValue(){
				if(this.hoverIntensity)
					return parseFloat(this.intensity)+parseFloat(this.hoverIntensity)
				if(!this.hoverIntensity)
					return parseFloat(this.intensity)
			}
		}
	}
</script>

<style lang="sass?indentedSyntax=true">
	.d-shdw
		display: inline-block

		&[block="true"] 
			width: 100%
		
		&[intensity="0"]
			box-shadow: none
		&[intensity="1"]
			box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)
		&[intensity="2"]
			box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)
		&[intensity="3"]
			box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23)
		&[intensity="4"]
			box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22)
		&[intensity="5"]
			box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22)
		&[intensity="6"]
			-webkit-box-shadow: 0px 43px 243px -40px rgba(0,0,0,0.6);
			-moz-box-shadow: 0px 43px 243px -40px rgba(0,0,0,0.6);
			box-shadow: 0px 43px 243px -40px rgba(0,0,0,0.6);
		&[intensity="7"]
			-webkit-box-shadow: 0px 10px 200px -35px rgba(0,0,0,0.7);
			-moz-box-shadow: 0px 10px 200px -35px rgba(0,0,0,0.7);
			box-shadow: 0px 10px 200px -35px rgba(0,0,0,0.7);
		&[intensity="8"]
			box-shadow: 0 5px 15px -2px rgba(10, 16, 34, .4);
		&[intensity="9"]
			box-shadow: 0 10px 30px -5px rgba(10, 16, 34, .2);
		&[intensity="11"]
			-webkit-box-shadow: 0px 0px 300px -46px rgba(0,0,0,0.71);
			-moz-box-shadow: 0px 0px 300px -46px rgba(0,0,0,0.71);
			box-shadow: 0px 0px 300px -46px rgba(0,0,0,0.71);
		&[intensity="12"]
			-webkit-box-shadow: 0px 0px 200px -60px rgba(0,0,0,0.71);
			-moz-box-shadow: 0px 0px 200px -60px rgba(0,0,0,0.71);
			box-shadow: 0px 0px 200px -60px rgba(0,0,0,0.71);

		&:hover
			&[hoverIntensity="0"]
				box-shadow: none
			&[hoverIntensity="1"]
				box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)
			&[hoverIntensity="2"]
				box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)
			&[hoverIntensity="3"]
				box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23)
			&[hoverIntensity="4"]
				box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22)
			&[hoverIntensity="5"]
				box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22)
			&[hoverIntensity="6"]
				-webkit-box-shadow: 0px 43px 243px -40px rgba(0,0,0,0.6);
				-moz-box-shadow: 0px 43px 243px -40px rgba(0,0,0,0.6);
				box-shadow: 0px 43px 243px -40px rgba(0,0,0,0.6);
			&[hoverIntensity="7"]
				-webkit-box-shadow: 0px 10px 200px -35px rgba(0,0,0,0.7);
				-moz-box-shadow: 0px 10px 200px -35px rgba(0,0,0,0.7);
				box-shadow: 0px 10px 200px -35px rgba(0,0,0,0.7);
			&[hoverIntensity="8"]
				box-shadow: 0 5px 15px -2px rgba(10, 16, 34, .4);
			&[hoverIntensity="9"]
				box-shadow: 0 10px 30px -5px rgba(10, 16, 34, .2);
			&[hoverIntensity="11"]
				-webkit-box-shadow: 0px 0px 300px -46px rgba(0,0,0,0.71);
				-moz-box-shadow: 0px 0px 300px -46px rgba(0,0,0,0.71);
				box-shadow: 0px 0px 300px -46px rgba(0,0,0,0.71);
		
		transition: all 0.3s cubic-bezier(.25,.8,.25,1)
</style>