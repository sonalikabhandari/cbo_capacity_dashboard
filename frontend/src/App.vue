<template>
  <div id="app">
    <v-app id="portal-home">
      <main-nav v-if="isAuth()"></main-nav>
      <pre-auth v-else></pre-auth>
      <v-content>
        <v-container fluid>
          <router-view />
        </v-container>
      </v-content>
      <v-footer app fixed>
        <span>
          <p class="text-xs-right right">
            &copy; {{ currentYear }} Service Reliability Engineering - Core and Backbone Operations - Charter Communications
          </p>
        </span>
      </v-footer>
    </v-app>
  </div>
</template>

<script>
import MainNav from '@/components/nav/MainNav'
import PreAuth from '@/components/nav/PreAuth'
import { mapState } from 'vuex'

export default {
  name: 'App',
  components: {
    MainNav,
    PreAuth
  },
  data () {
    return {
      drawer: true
    }
  },
  methods: {
    isAuth () {
      return this.isAuthenticated
    }
  },
  computed: {
    ...mapState({
      isAuthenticated: state => state.isAuthenticated,
      token: state => state.token
    }),
    currentYear () {
      return new Date().getFullYear()
    }
  },
  beforeMount () {
    if (this.token !== null) {
      this.$store.dispatch('inspectToken')
        .then((response) => {
          if (this.token !== null) {
            if (this.interval === undefined) {
              this.interval = setInterval(function () {
                this.$store.dispatch('inspectToken')
              }.bind(this), 300000)
            }
          }
        })
    }
  },
  watch: {
    token: function (val) {
      if (this.token == null) {
        this.$store.commit('setIsAuthenticated', { status: false })
        this.interval = clearInterval(this.interval)
        this.$router.push('/')
      } else {
        this.$store.commit('setIsAuthenticated', { status: true })
        this.interval = clearInterval(this.interval)
        this.interval = setInterval(function () {
          this.$store.dispatch('inspectToken')
        }.bind(this), 300000)
      }
    }
  }
}
</script>

<style>
.right {
  text-align: right;
}
html { overflow-y: auto }
</style>
