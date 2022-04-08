<template>
  <span>
    <v-navigation-drawer
      app
      clipped
      floating
      permanent
    >
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-card class="elevation-0">
            <v-card-text>
              <v-form>
                <v-text-field
                  prepend-icon="person"
                  name="username"
                  id="username"
                  autocomplete="username"
                  label="Login"
                  type="text"
                  v-model="username"
                  v-on:keyup.enter.native="login()"
                ></v-text-field>
                <v-text-field
                  id="password"
                  prepend-icon="lock"
                  name="password"
                  autocomplete="current-password"
                  label="Password"
                  type="password"
                  v-model="password"
                  v-on:keyup.enter.native="login()"
                ></v-text-field>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click.stop="login()" fixed right>Login</v-btn>
              </v-form>
            </v-card-text>
          </v-card>
        </v-layout>
      </v-container>
    </v-navigation-drawer>
    <v-app-bar app clipped-left dense color="grey darken-4">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      <v-toolbar-title>
        <v-img :src="require('@/assets/logo.png')" height="50" width="350">
        </v-img>
      </v-toolbar-title>
    </v-app-bar>
    <v-dialog v-model="dialog" max-width="400">
      <v-card>
        <v-card-title class="error">
          Login Failed
        </v-card-title>
        <v-card-text>
          Incorrect Username or Password. Please try again.
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="dialog = false">
            OK
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </span>
</template>

<script>
export default {
  components: {

  },
  data () {
    return {
      dialog: false,
      username: undefined,
      password: undefined
    }
  },
  methods: {
    async login () {
      /**this.$store.dispatch(
        'obtainToken',
        { username: this.username, password: this.password }
      ).then(() => {
        this.$router.push({ name: 'home' })
      }).catch((error) => {
        console.debug(error)
        console.log('in catch')
        this.dialog = true
      })
    }*/
      try {
        await this.$store.dispatch('obtainToken', { username: this.username, password: this.password })
        this.$router.push({ name: 'home' })
      } catch(error)  {
        console.debug(error)
        this.dialog = true
      }
    }
  }
}
</script>

<style>
.stretch {
  min-height: 100%
}
</style>
