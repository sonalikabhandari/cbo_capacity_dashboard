import Vue from 'vue'
import Vuex from 'vuex'

import jwtDecode from 'jwt-decode'

// API calls
import {
  refreshToken,
  authenticate
} from './api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    available: JSON.parse(localStorage.getItem('available')),
    isAuthenticated: false,
    profile: localStorage.getItem('profile') ? JSON.parse(atob(localStorage.getItem('profile'))) : undefined,
    sideMenu: 'main',
    token: localStorage.getItem('profile') ? localStorage.getItem('token') : undefined,
    topMenu: 'main',
    version: process.env.VERSION
  },
  mutations: {
    removeToken (state) {
      localStorage.removeItem('token')
      localStorage.removeItem('profile')
      localStorage.removeItem('available')
      state.token = null
      state.profile = null
      state.isAuthenticated = false
    },
    setIsAuthenticated (state, payload) {
      state.isAuthenticated = payload.status
    },
    setSideMenu (state, menu) {
      state.sideMenu = menu
    },
    setTopMenu (state, menu) {
      state.topMenu = menu
    },
    updateToken (state, payload) {
      localStorage.removeItem('token')
      localStorage.removeItem('profile')
      localStorage.removeItem('available')

      localStorage.setItem('token', payload.data.token)

      if (payload.data.user) {
        localStorage.setItem('profile', btoa(JSON.stringify(payload.data.user)))
      }

      state.token = payload.data.token
      state.profile = payload.data.user

      if (state.token != null) {
        state.isAuthenticated = true
      } else {
        state.isAuthenticated = false
      }
    }
  },
  actions: {
    async inspectToken (context) {
      const token = this.state.token
      if (token) {
        const decoded = jwtDecode(token)
        const exp = decoded.exp
        const origIat = decoded.orig_iat
        const expTime = exp - (Date.now() / 1000)
        const maxExp = (Date.now() / 1000) - origIat
        if (expTime < 5400 && expTime > 0 && maxExp < 28800) {
          await this.dispatch('refreshToken')
        } else if (expTime > 5400) {
          // just make sure we are authenticated
          context.commit('setIsAuthenticated', { status: true })
        } else {
          context.commit('removeToken')
        }
      }
    },
    logout (context) {
      return context.commit('removeToken')
    },
    async obtainToken (context, cred) {
      const payload = {
        username: cred.username,
        password: cred.password
      }
      try {
        let response = await authenticate(payload)
        context.commit('updateToken', { data: response.data })
      } catch (error) {
        throw error
      }
    },
    async refreshToken (context) {
      const payload = {
        token: this.state.token
      }
      let response = await refreshToken(payload)
      context.commit('updateToken', { data: response.data })
    }
  }
})
