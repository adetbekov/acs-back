import Vue from 'vue'
import Router from 'vue-router'
import index from '@/pages/index.vue'
import blog from '@/pages/blog/blog.vue'
import post from '@/pages/blog/post.vue'
import list from '@/pages/blog/list.vue'
import authenticate from '@/pages/auth/authenticate.vue'
import webcampus from '@/pages/webcampus/webcampus.vue'
import course from '@/pages/webcampus/course.vue'
import market from '@/pages/webcampus/store.vue'
import syllabus from '@/pages/webcampus/syllabus.vue'
import lesson from '@/pages/webcampus/lesson.vue'
import store from '@/store'

Vue.use(Router)

const routes = [
  {
    path: '/',
    name: 'index',
    component: index,
    meta: { 
      title: "Main", 
      forVisitors: true 
    } 
  },
  {
    path: '/auth',
    name: 'auth',
    component: authenticate,
    meta: { 
      title: "Auth", 
      forVisitors: true 
    } 
  },
  {
    path: '/blog',
    component: blog,
    children: [
      {
        path: ':id',
        name: 'post',
        component: post,
        props: true,
        meta: { 
          title: "Post", 
          forVisitors: true 
        }
      },
      {
        path: '',
        name: 'blog',
        component: list,
        props: true,
        meta: { 
          title: "Blog", 
          forVisitors: true 
        }
      }
    ]
  },
  {
    path: '/webcampus',
    component: webcampus,
    children: [
      {
        path: ':course_slug',
        name: 'course',
        component: course,
        props: true,
        meta: { 
          title: "Course", 
          forAuth: true 
        }
      },
      {
        path: ':course_slug/syllabus',
        name: 'syllabus',
        component: syllabus,
        props: true,
        meta: { 
          title: "Syllabus", 
          forAuth: true 
        }
      },
      {
        path: ':course_slug/:chapter_slug/:step_slug',
        name: 'lesson',
        component: lesson,
        props: true,
        meta: { 
          title: "Lesson", 
          forAuth: true 
        }
      },
      {
        path: '',
        name: 'webcampus',
        component: market,
        props: true,
        meta: { 
          title: "Webcampus", 
          forVisitors: true 
        }
      }
    ]
  },
]


const router = new Router({
  mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  document.title = to.meta.title     
  if(to.meta.forAuth){
    if(!Vue.auth.isAuthenticated()){
      next({
        path: '/auth',
      })
    }else next()
  }else next()
  if (Vue.auth.isAuthenticated() && !store.getters.getUser) {
    store.dispatch("fetchUser")
  }
})

export default router