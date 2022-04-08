import Vue from 'vue'
import Router from 'vue-router'
import store from './store'
import { userHasPermission } from './util'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes: [
    // non authentication based routes
    {
      path: '/',
      name: 'home',
      component: () => import(
        /* webpackChunkName: "home" */ './views/Home.vue'
      )
    },
    {
      path: '/logout',
      name: 'logout',
      component: () => import(
        /* webpackChunkName: "logout" */ './views/Logout.vue'
      )
    },
    {
      path: '/dashboardview',
      name: 'dashboardview',
      component: () => import(
        /* webpackChunkName: "dashboardview" */ './views/capacitydashboard.vue'
      )
    },
    {
      path: '/augmentview',
      name: 'augmentview',
      component: () => import(
        /* webpackChunkName: "dashboardview" */ './views/augmentView.vue'
      )
    },
    {
      path: '/dashboardview/:pID',
      name: 'dashboardviewID',
      // pass the 'id' param as a prop to the 'Post' component
      // props: (route) => ({ pID: route.query.pID, id_data: route.query.id_data }),
      props: true,
      component: () => import('@/components/pathID.vue')
    },

    {
      path: '/test',
      name: 'test',
      component: () => import(
        /* webpackChunkName: "dashboardview" */ './views/testfilters.vue'
      )
    },

    // authentication based routes

    // admin only views

    // site admin views
    {
      path: '/roles/:type',
      name: 'roles',
      component: () => import(
        /* webpackChunkName: "roles" */ './views/PermissionEditor.vue'
      ),
      meta: {
        requiresAuth: true,
        isAdmin: true
      },
      props: true
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.state.token === undefined || store.state.token === null) {
      next('/')
    } else {
      if (store.state.isAuthenticated === true) {
        if (to.matched.some(record => record.meta.requiresMRTG)) {
          if (userHasPermission('MRTG')) {
            next()
          } else {
            next('/')
          }
        } else if (to.matched.some(record => record.meta.isAdmin)) {
          if (userHasPermission('ADMIN')) {
            next()
          } else {
            next('/')
          }
        } else if (to.matched.some(record => record.meta.isStaff)) {
          if (store.state.profile.is_staff) {
            next()
          } else {
            next('/')
          }
        } else {
          next()
        }
      } else {
        next('/')
      }
    }
  } else {
    next()
  }
})

export default router
