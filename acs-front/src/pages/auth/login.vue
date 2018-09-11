<i18n>
	{
	"en": {
		"username": "Username",
		"password": "Password",
		"signup": "Sign Up",
		"signin": "Sign In"
	},
	"ru": {
		"username": "Логин",
		"password": "Пароль",
		"signup": "Регистрация",
		"signin": "Вход"
	},
	"kz": {
		"username": "Логин",
		"password": "Құпиясөз",
		"signup": "Тіркелу",
		"signin": "Кіру"
	},
	"ja": {
		"username": "ユーザー名",
		"password": "パスワード",
		"signup": "サインアップ",
		"signin": "サインイン"
	},
	"ko": {
		"username": "사용자 이름",
		"password": "암호",
		"signup": "가입하기",
		"signin": "로그인"
	}
	}
</i18n>
<template>
    <div ref="login" class="container h-100">
		<div class="d-flex align-items-center h-100 login">
			<div class="row w-100 mx-0">
				<div class="col-xs-12 col-md-6 col-sm-8 offset-sm-2 col-lg-4 offset-lg-4 offset-md-3 px-4">
					<shadows intensity="11" class="p-4 w-100 mb-2" style="background-color: white;">
						<input type="username" class="w-100 mb-3" :placeholder="this.$t('username')" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" v-model="username" @keyup.13="login()" autofocus :disabled="loading">
						<div class="row m-0">
							<input type="password" class="col-md-11 col-sm-11 col-xs-11" :placeholder="this.$t('password')" v-model="password" @keyup.13="login()" :disabled="loading">
							<d-button markup="link" shadow="false" class="px-0 col-md-1 col-sm-1 col-xs-1 hidden-xs-down" style="color: #bdc3c7;">?</d-button>
						</div>
					</shadows>
				</div>
				<div class="col-xs-12 col-md-6 col-sm-8 offset-sm-2 col-lg-4 offset-lg-4 offset-md-3 px-4">
					<d-button markup="primary" class="mt-1 float-right" @click="login()" :loading="loading" :disabled="loading">{{ $t('signin') }}</d-button>
					<d-button markup="link" shadow="false" class="mt-1 float-right" @click="$store.state.authFormCurrent='register'">{{ $t('signup') }}</d-button>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	import shadows from "@/components/shadows.vue"
	export default{
		data(){
			return {
				username: '',
				password: '',
				loading: false
			}
		},
		components: {
			shadows
		},
		props: {
			after: {
				default: null
			}
		},
		methods: {
			shakeAnimation(element){
				TweenMax.to(element, .08, {
					x: -10,
					ease: Quad.easeInOut
				});
				TweenMax.to(element, .08, {
					repeat: 4,
					x: 10,
					yoyo: true,
					delay: .1,
					ease: Quad.easeInOut
				});
				TweenMax.to(element, .08, {
					x: 0,
					delay: .1 * 4
				});
			},
			login(){
				this.loading = true
				this.$http.post("auth/login", { 
					username: this.username, 
					password: this.password 
				}).then(response => {
					this.$auth.setToken(response.body.token)
					this.$router.push(this.after || '/webcampus')
					// this.$http.get("api/accounts/current?format=json", {
					// 	headers: {
					//         Authorization: `JWT ${this.$auth.getToken()}`
					//     }
					// }).then(response => {
					// 	console.log(response.body)
					// }, response => {
					// 	alert(response.body.detail)
					// })
					this.loading = false
					this.password = ""
				}, response => {
					console.log(response.statusText)
					this.shakeAnimation(this.$refs.login)
					this.loading = false
				})
			}
		}
	}
</script>

<style scoped>
	.login input{
		font-weight: 300;
		padding: 4px 0px;
		border: none;
		border-bottom: 1px solid white;
		/*border: none;*/
		-webkit-transition: border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;
	    transition: border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;
	    -o-transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s;
	    transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s;
	    transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;
	}
	.login input:hover{
		border-bottom: 1px solid rgba(0,0,0,.1);
	}
	.login input:focus{
		border-bottom: 1px solid #2ecc71;
	}
	::-webkit-input-placeholder {color:#bdc3c7;}
	::-moz-placeholder          {color:#bdc3c7;}
	:-moz-placeholder           {color:#bdc3c7;}
	:-ms-input-placeholder      {color:#bdc3c7;}
</style>
