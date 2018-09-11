<template lang="jade">
	div(
	class="d-loadarea", 
	:id="id", 
	:loading="loading",
	:class="customClass", 
	:style="customStyle")
		div(class="h-100 w-100 d-flex justify-content-center align-items-center" v-if="loading")
			svg( height="20" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 683.3 383.7" xml:space="preserve")
				path(id="st0" d="M479.6,42.3c80.8,0,146.2,65.5,146.2,146.2s-65.5,146.2-146.2,146.2c-80.8,0-123-61.8-138.6-144.8v1.5 c-13.2-74.5-57-146.2-137.8-146.2S57,110.7,57,191.4s65.5,146.2,146.2,146.2")
				path(id="st1" d="M479.6,42.3c80.8,0,146.2,65.5,146.2,146.2s-65.5,146.2-146.2,146.2c-80.8,0-123-61.8-138.6-144.8v1.5 c-13.2-74.5-57-146.2-137.8-146.2S57,110.7,57,191.4s65.5,146.2,146.2,146.2")
		slot(v-else)
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
		    customStyle: {
				type: String,
				default: null
		    },
		    loading: {
				type: Boolean,
				default: true
		    }
		}
	}
</script>

<style lang="sass?indentedSyntax=true">
	/*.d-loadarea
		height: calc(100vh - 106.19px)*/
		/*display: block*/
</style>
<style>
    #st0{fill:none;stroke:white;stroke-width:70;stroke-miterlimit:10;display: none}
    #st1{fill:none;stroke:#2ecc71;stroke-width:70;stroke-miterlimit:10;
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
