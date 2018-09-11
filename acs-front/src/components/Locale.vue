<template>
	<div class="radio-toolbar d-flex justify-content-center w-100 align-items-center list-inline m-0" v-if="locale">
      <input type="radio" id="kz" name="lang" value="kz" v-model="locale">
      <label for="kz">kz</label>
      <input type="radio" id="ru" name="lang" value="ru" v-model="locale">
      <label for="ru">ru</label>
      <input type="radio" id="en" name="lang" value="en" v-model="locale">
      <label for="en">en</label>
    </div>
</template>

<script>
	export default {
		data() {
			return {
				locale: null
			}
		},
		watch:{
		  locale(val){
		    this.$i18n.locale = val
		  },
		  getLocale(val){
		    this.locale = val
		  }
		},
		computed: {
		  getLocale(){
		    return this.$i18n.locale
		  },
		},
		mounted() {
			this.locale = this.getLocale
		}
	}
</script>

<style scoped>
	.radio-toolbar input[type="radio"] {
	  display: none;
	}

	.radio-toolbar label {
	  user-select: none;
	  padding: 0 5px;
	  margin: 0;
	  cursor: pointer;
	  transition: all 0.2s ease-in-out;
	}

	.radio-toolbar input[type="radio"]:checked+label {
	  color: #cecece;
	}
</style>