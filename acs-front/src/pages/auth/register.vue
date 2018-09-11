<i18n>
	{
	"en": {
		"firstname": "First name",
		"secondname": "Second name",
		"username": "Username",
		"emailorphone": "E-mail of phone",
		"password": "Password",
		"female": "Female",
		"male": "Male",
		"signup": "Sign Up",
		"signin": "Sign In"
	},
	"ru": {
		"firstname": "Имя",
		"secondname": "Фамилия",
		"username": "Логин",
		"emailorphone": "E-mail или телефон",
		"password": "Пароль",
		"female": "Женщина",
		"male": "Мужчина",
		"signup": "Регистрация",
		"signin": "Вход"
	},
	"kz": {
		"firstname": "Есіміңіз",
		"secondname": "Тегіңіз",
		"username": "Логин",
		"emailorphone": "E-mail немесе телефон",
		"password": "Құпиясөз",
		"female": "Әйел",
		"male": "Ер",
		"signup": "Тіркелу",
		"signin": "Кіру"
	},
	"ja": {
		"firstname": "名前",
		"secondname": "姓",
		"username": "ユーザー名",
		"emailorphone": "電子メールまたは電話",
		"password": "パスワード",
		"female": "女性",
		"male": "男性",
		"signup": "サインアップ",
		"signin": "サインイン"
	},
	"ko": {
		"firstname": "이름",
		"secondname": "성",
		"username": "사용자 이름",
		"emailorphone": "전화 이메일",
		"password": "암호",
		"female": "여자",
		"male": "남성",
		"signup": "가입하기",
		"signin": "로그인"
	}
	}
</i18n>
<template>
	<div class="container h-100">
		<div class="d-flex align-items-center h-100 login">
			<div class="row w-100 mx-0">
				<div class="col-xs-12 col-md-6 col-sm-8 offset-sm-2 col-lg-4 offset-lg-4 offset-md-3 px-4">
					<shadows intensity="12" class="p-4 w-100 mb-2" style="background-color: white;">
						<div class="row m-0 mb-3 w-100">
							<div class="col-md-6 col-sm-6 col-xs-6 pl-0 pr-xs-0 mb-xs-3">
								<input type="text" :placeholder="this.$t('firstname')" class="w-100 mr-0" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false">
							</div>
							<div class="col-md-6 col-sm-6 col-xs-6 pl-0 pr-0 mr-0">
								<input type="text" :placeholder="this.$t('secondname')" class="w-100 mr-0" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false">
							</div>
						</div>
						<input type="username" class="w-100 mb-3" :placeholder="this.$t('username')" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false">
						<input type="text-field" class="w-100 mb-3" :placeholder="this.$t('emailorphone')" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false">
						<input type="text-field" class="w-100 mb-3" :placeholder="this.$t('password')">
						<div class="float-left">
							<input type="radio" id="one" value="One" v-model="picked" class="mr-2"><label for="one" class="mr-2">{{ $t('female') }}</label>
						</div>
						<div class="float-left">
							<input type="radio" id="two" value="Two" v-model="picked" class="mr-2"><label for="two">{{ $t('male') }}</label>
						</div>
					</shadows>
				</div>
				<div class="col-xs-12 col-md-6 col-sm-8 offset-sm-2 col-lg-4 offset-lg-4 offset-md-3 px-4">
					<d-button markup="primary" class="mt-1 float-right">{{ $t('signup') }}</d-button>
					<d-button markup="link" shadow="false" class="mt-1 float-right" @click="$store.state.authFormCurrent='login'">{{ $t('signin') }}</d-button>
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
				picked: ''
			}
		},
		components: {
			shadows
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
	.login label {
		font-weight: 300;
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