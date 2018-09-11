<template>
	<div class="bg" v-if="activated">
		<div class="container px-0" v-if="this.post">
			<!-- <BlogHeader :title="post.title"></BlogHeader> -->
    		<!-- <h2 class="mb-4">{{ post.title }}</h2> -->
    		<Dynamic class="full-width" :template="post.content" :post="post"></Dynamic>
			<div class="w-100 d-flex flex-wrap tags overflow-hidden">
				<a :href="`/${t.name}`" class="active" v-for="t in post.tags">{{ t.name }}</a>
			</div>
		</div>
	</div>
</template>

<script>
	import Vue from 'vue'
	// import BlogHeader from '../.././components/blog/BlogHeader'

	var Dynamic = {
	  props: ['template', 'post'],
	  data() {
	    return {
	      templateRender: null,
	    };
	  },
	  render(h) {
	    if (!this.templateRender) {
	      return h('div', 'loading...')
	    } else { 
	      return this.templateRender()
	    }
	  },
	  watch: {
	  	template:{
	    	immediate: true,
	      handler() {
	        var res = Vue.compile(this.template);
	        this.templateRender = res.render;
	        this.$options.staticRenderFns = []
	        this._staticTrees = []
	        for (var i in res.staticRenderFns) {
	          this.$options.staticRenderFns.push(res.staticRenderFns[i])
	        }
	      }
	    }
	  },
	}

	export default {
		props: ['id'],
		data: () => ({
			post: null,
			activated: false
		}),
		components: {
			Dynamic,
			// BlogHeader
		},
		activated() {
			var self = this
			this.$http.get(`api/blog/${ this.id }/`).then(response => {
		    this.post = response.body
		    this.activated = true
		  }, response => {
		    console.log("Post loading error")
		  }) 
		},
		deactivated() {
			this.activated = false
		}
	}
</script>

<style scoped>
	.bg {
		/*height: 100vh;*/
		color: #2c3e50;
		background-color: white;
	}
	.top {
		margin-top: 60px;
	}
	.content {
		font-size: 20px;
	}
	.tags a {
		display: block;
		max-height: 27px;
		color: #2c3e50;
		font-size: 13px;
	    letter-spacing: 0;
	    text-decoration: none;
	    background: #f1f1f1;
	    border-radius: 3px;
	    line-height: 1.1;
	    padding: 6px 10px 7px;
	    margin: 0px 10px 10px 0px;
	    vertical-align: middle;
	}
	.tags a:hover {
		background-color: #ebebeb;
	}
	ul > li {
		margin-bottom: 25px;
	}
	.blue {
		color: #3498db;
	}
	.full-width {
	  width: 100vw;
	  height: 100%;
	  position: relative;
	  left: 50%;
	  margin-left: -50vw;
	}
</style>