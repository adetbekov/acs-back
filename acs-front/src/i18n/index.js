import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n)

const messages = {
  en: {
    navbar: {
      search: 'Search',
      language: 'Language',
      signup: 'Sign Up',
      logout: 'Log Out'
    }
  },
  ru: {
    navbar: {
      search: 'Поиск',
      language: 'Язык',
      signup: 'Регистрация',
      logout: 'Выход'
    }
  },
  kz: {
    navbar: {
      search: 'Iздеу',
      language: 'Тіл',
      signup: 'Тіркеу',
      logout: 'Шығу'
    }
  },
  ja: {
    navbar: {
      search: 'サーチ',
      language: '言語',
      signup: 'サインアップ',
      logout: 'ログアウト'
    }
  },
  ko: {
    navbar: {
      search: '수색',
      language: '언어',
      signup: '가입하기',
      logout: '로그 아웃'
    }
  }
}

const i18n = new VueI18n({
  locale: 'ru', 
  fallbackLocale: 'en',
  messages
})

export default i18n