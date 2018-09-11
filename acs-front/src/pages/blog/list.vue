<i18n>
	{
		"ru": {
			"last": "Последние",
			"all_categories": "Все категории",
			"all": "Все",
			"all_tags": "Все теги"
		},
		"kz": {
			"last": "Songı",
			"all_categories": "Barlık sanattar",
			"all": "Bäri",
			"all_tags": "Barlık täkter"
		},
		"en": {
			"last": "Last",
			"all_categories": "All categories",
			"all": "All",
			"all_tags": "All tags"
		}
	}
</i18n>
<template>
  <div class="top container px-0">
  	<div class="row" data-sticky-container>
  		<div class="col-lg-9 col-md-8">
  			<h6 class="fw-300 blue">{{ $t("last") }}:</h6>
  			<ul class="list-unstyled mt-4" v-if="this.placeholder_posts">
  				<li>
  					<div class="animated-background w-100">
  					    <div class="background-masker after-date"></div>
  					    <div class="background-masker bottom-date"></div>
  					    <div class="background-masker between-headers"></div>
  					    <div class="background-masker after-header-1"></div>
  					    <div class="background-masker after-header-2"></div>
  					</div>
  				</li>
  				<li>
  					<div class="animated-background animated-background-thin w-100">
  					    <div class="background-masker after-date"></div>
  					    <div class="background-masker between-headers"></div>
  					    <div class="background-masker after-header-1"></div>
  					</div>
  				</li>
  				<li>
  					<div class="animated-background animated-background-3 w-100">
  					    <div class="background-masker after-date"></div>
  					    <div class="background-masker bottom-date"></div>
  					    <div class="background-masker between-headers"></div>
  					    <div class="background-masker after-header-1"></div>
  					    <div class="background-masker after-header-2"></div>
  					</div>
  				</li>
  				<!-- <li>
  					<div class="animated-background animated-background-thin animated-background-thin-2 w-100">
  					    <div class="background-masker after-date"></div>
  					    <div class="background-masker between-headers"></div>
  					    <div class="background-masker after-header-1"></div>
  					</div>
  				</li>
  				<li></li>
  				<li></li> -->
  			</ul>
				<ul class="list-unstyled mt-4 headlines" v-else>
					<li v-for="p in filtered_posts" class="d-sm-flex"><p class="fw-100 mr-4">{{ moment(p.created).format("MMM D, YYYY") }}</p><router-link class="link" :to="{ name: 'post', params: { id: p.id } }"><h5 class="fw-300">{{ p.title }}</h5></router-link></li>
				</ul>
  		</div>
  		<div class="col-lg-3 col-md-4">
  			<div class="selector" data-margin-top="40">
    			<div class="d-flex align-items-center search-blog mt-sm-4 mt-xs-5 mt-md-0">
		    		<div><icon name="search"></icon></div>
		    		<input class="fw-300" type="text" placeholder="Поиск по блогу" v-model="search">
	    		</div>
	    		<br>
	    		<div :class="{ 'mb-4': !this.categoriesCollapsed }">
		    		<h6 class="fw-300 blue button" @click="categoriesCollapsed=!categoriesCollapsed" v-if="!this.categorySelected">
		    			<u>
		    				{{ plusOrMinus(categoriesCollapsed) }} 
		    				{{ $t("all_categories") }}
		    			</u>
		    		</h6>
		    		<h6 class="fw-300 button category_selected change-icon" @click="categoriesCollapsed=!categoriesCollapsed" v-else>
		    				<span class="fa"><icon name="check-circle-o" scale="0.7"></icon> {{ category }}</span>
			    			<span class="fa red"><icon name="times-circle-o" scale="0.7"></icon> {{ category }}</span>
		    		</h6>
	    		</div>
	    		<transition @enter="toggleWidthAnimation" @leave="collapseWidthAnimation">
	    			<div class="w-100 d-flex flex-wrap tags overflow-hidden" v-if="!this.categoriesCollapsed">
	    				<div class="block">
                <input type="radio" id="category_all" name="categories" value="all" v-model="category">
                <label for="category_all">{{ $t("all") }}</label>
              </div>
	    				<div class="block" v-for="c in categories">
                <input type="radio" :id="`category_${c.name}`" name="categories" :value="c.name" v-model="category">
                <label :for="`category_${c.name}`">{{ c.name }}</label>
              </div>
	    				<br>
	    			</div>
    			</transition>

    			<h6 class="fw-300 blue button mt-3" :class="{ 'mb-4': !this.tagsCollapsed }"  @click="tagsCollapsed=!tagsCollapsed"><u>{{ plusOrMinus(tagsCollapsed) }} {{ $t("all_tags") }}</u></h6>

    			<transition @enter="toggleWidthAnimation" @leave="collapseWidthAnimation">
	    			<div class="w-100 d-flex flex-wrap tags overflow-hidden" v-if="!this.tagsCollapsed">
	    				<div class="block">
                <input type="radio" id="tag_all" name="tags" value="all" v-model="tag">
                <label for="tag_all">{{ $t("all") }}</label>
              </div>
	    				<div class="block" v-for="t in tags" :class="{ 'disabled': disable_tag(t.categories) }">
                <input type="radio" :id="`tag_${t.name}`" name="tags" :value="t.name" v-model="tag">
                <label :for="`tag_${t.name}`">{{ t.name }} <small class="small">{{ t.count }}</small></label>
              </div>
	    				<br>
	    			</div>
    			</transition>

    		</div>
  		</div>
  	</div>
  	<br>
  	<!-- <div class="row grid mt-3" data-masonry='{ "itemSelector": ".grid-item" }'>
      <div class="grid-item col-xs-12 col-sm-6 col-md-4 col-lg-3">
      	<h1 class="fw-300">Lorem ipsum dolor sit.</h1>
      </div>
      <div class="grid-item col-xs-12 col-sm-6 col-md-8 col-lg-6 tall">2</div>
      <div class="grid-item col-xs-12 col-sm-6 col-md-4 col-lg-3">3</div>
      <div class="grid-item col-xs-12 col-sm-6 col-md-4 col-lg-3 tall">4</div>
      <div class="grid-item col-xs-12 col-sm-6 col-md-4 col-lg-3 taller">5</div>
      <div class="grid-item col-xs-12 col-sm-6 col-md-4 col-lg-3">6</div>
      <div class="grid-item col-xs-12 col-sm-6 col-md-4 col-lg-3 tall">7</div>
      <div class="grid-item col-xs-12 col-sm-6 col-md-4 col-lg-3">8</div>
      <div class="grid-item col-xs-12 col-sm-6 col-md-4 col-lg-3">9</div>
      <div class="grid-item col-xs-12 col-sm-6 col-md-4 col-lg-3 taller">10</div>
  	</div> -->

  </div>
</template>

<script>
	import Sticky from 'sticky-js'
	export default {
		props: {
			flipping: {
				type: Boolean,
				default: false
			}
		},
		data() {
			return {
				tagsCollapsed: true,
				categoriesCollapsed: false,
				categorySelected: false,
				posts: [],
				categories: [],
				tags: [],
				category: 'all',
				tag: 'all',
				loading_posts: true,
				loading_categories: true,
				loading_tags: true,
				search: ""
			}
		},
		watch: {
			category(c) {
				this.categoriesCollapsed = true
				this.tagsCollapsed = false
				this.categorySelected = true
				this.tag = "all"
				if (c == "all") {
					this.categorySelected = false
					this.categoriesCollapsed = false
					this.tagsCollapsed = true
				}
			}
		},
		computed: {
			placeholder_posts() {
				return this.flipping || this.loading_posts
			},
			placeholder_categories() {
				return this.flipping || this.loading_categories
			},
			filteredByCategory() {
				return _.filter(this.posts, (el) => { 
					return this.category == "all"
						? true 
						: el.category.name === this.category
				})
			},
			filteredByTag() {
				return _.filter(this.filteredByCategory, (el) => {
					return this.tag == "all"
						? true
						: _.some(el.tags, { name: this.tag })
				})
			},
			filtered_posts() {
				return _.filter(this.filteredByTag, (el) => {
					return _.includes(_.toLower(el.title), _.toLower(this.search))
				})
			}
		},
		methods: {
			plusOrMinus(b) {
				return b ? "+" : "−"
			},
			collapseWidthAnimation(el, done){
				let tl = new TimelineLite()
				tl.set(el, { y: 23 }).to(el, 0.4, { opacity: 0, height: 0, ease: Power2.easeOut, onComplete: done })
			},
			toggleWidthAnimation(el, done){
				let tl = new TimelineLite()
				tl.from(el, 0.4, { opacity: 0, height: 0, ease: Power2.easeOut, onComplete: done })
			},
			disable_tag(c) {
				return this.category == "all"
					? 0
					: _.indexOf(c, this.category)
			}
		},
		mounted(){
			if(!this.flipping){

				this.$http.get('api/blog/posts').then(response => {
			    this.posts = response.body
			    this.loading_posts = false
			  }, response => {
			    console.log("Posts loading error")
			  })

			  this.$http.get('api/blog/categories').then(response => {
			    this.categories = response.body
			    this.loading_categories = false
			  }, response => {
			    console.log("Categories loading error")
			  })

			  this.$http.get('api/blog/tags').then(response => {
			    this.tags = response.body
			    this.loading_tags = false
			  }, response => {
			    console.log("Tags loading error")
			  })

			}
		  var sticky = new Sticky('.selector')
		}
	}
</script>

<style scoped>

 .grid [class*='col-'] {
  /*background-color: white;*/
  background-clip: content-box;
  min-height: 120px;
  margin-bottom: 30px;
}

.tall {
  height: 160px;
}
.taller {
  height: 200px;
}
	.tags label, .tags a {
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
	    cursor: pointer;
	    user-select: none;
	}
	.tags label,.tags  a:hover {
		background-color: #ebebeb;
	}
	.tags input[type="radio"] {
	  display: none;
	}
	.tags input[type="radio"]:checked+label {
	  color: #3498db;
	}
	ul > li {
		margin-bottom: 25px;
	}
	.blue {
		color: #3498db;
	}
	.red {
		color: #e74c3c;
	}
</style>
<style scoped>
	.search-blog {
		color: #AAB6BD;
		border-bottom: 1px solid rgba(0, 0, 0, 0.3);
		/*width: 100%;*/
		transition: all 0.3s ease-in-out;
	}
	.search-blog input {
		/*width: 100%;*/
		background: none;
		/*padding-left: 10px;*/
		padding: 0px 0px 3px 10px;
		font-size: 18px;
		border: none;
		transition: all 0.2s ease-in-out;
	}
	.headlines p{
		min-width: 100px;
	}
	.top {
		margin-top: 60px;
	}
	@media screen and (max-width: 576px){
		.headlines p {
		  font-size: 12px;
		  margin-bottom: 6px;
		}
		.headlines li {
			margin-bottom: 40px;
		}
		.top {
			margin-top: 35px;
		}
	}
	u {
		text-decoration: none;
	}
	.button {
		cursor: pointer;
		margin-bottom: 0px;
		user-select: none;
	}
	.button u:hover {
		border-bottom: 1px solid #3498db;
	}
	.overflow-hidden {
		overflow: hidden;
	}
	.link {
		color: #2c3e50!important;
		text-decoration: none;
	}
	.link:hover {
		color: #3498db!important;
	}
	.category_selected {
		color: #27ae60;
	}
	.change-icon > .fa + .fa,
	.change-icon:hover > .fa {
	  display: none;
	}
	.change-icon:hover > .fa + .fa {
	  display: inherit;
	}
</style>
<style scoped>

	@keyframes placeHolderShimmer {
	  0%{ background-position: -400px 0; }
	  100%{ background-position: 400px 0; }
	}

	.animated-background {
	  animation-duration: 1.2s;
	  animation-fill-mode: forwards;
	  animation-iteration-count: infinite;
	  animation-timing-function: linear;
	  animation-name: placeHolderShimmer;
	  background: #f6f7f8;
	  background: linear-gradient(to right, #eeeeee 8%, #dddddd 18%, #eeeeee 33%);
	  background-size: 800px 104px;
	  height: 44px;
	  position: relative;
	}
	.animated-background {
		margin-bottom: 35px;
	} 

	.animated-background-thin {
		height: 17px;
	}

	.background-masker {
	  background: #fff;
	  position: absolute;
	}

	/* Every thing below this is just positioning */
	.background-masker.after-date {
		left: 95px;
		top: 0px;
		width: 30px;
		height: 44px;
	}
	.background-masker.bottom-date {
		top: 17px;
		left: 0;
		width: 95px;
		height: 27px;
	}
	.background-masker.between-headers {
		top: 17px;
		left: 95px;
		width: 100%;
		height: 10px;
	}
	.background-masker.after-header-1 {
		width: auto;
		left: 90%;
		right: 0;
		height: 17px;
	}
	.background-masker.after-header-2 {
		width: auto;
		top: 27px;
		left: 60%;
		right: 0;
		height: 17px;
	}
	.animated-background-thin .after-header-1 {
		left: 80%;
	}

	.animated-background-3 .after-header-1 {
		left: 85%;
	}
	.animated-background-3 .after-header-2 {
		left: 50%;
	}
	.animated-background-thin-2 .after-header-1 {
		left: 87%;
	}
	
	.disabled {
		opacity: 0.4;
		pointer-events: none;
	}
</style>