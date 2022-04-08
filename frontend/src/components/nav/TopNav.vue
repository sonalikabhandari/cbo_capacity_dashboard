<template>
  <v-app-bar app clipped-left dense color="grey darken-4">
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    <!--v-toolbar-title>CBO Datacenter - Firewall Intake Request Tool</v-toolbar-title-->
    <v-toolbar-title>
      <v-img :src="require('@/assets/logo.png')" height="50" width="350">
      </v-img>
    </v-toolbar-title>
    <v-flex class="text" mt-4 ml-3>version: {{ version }}</v-flex>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-btn text disabled>Hello {{ user.firstname }}</v-btn>
      <v-btn text icon to='/logout'>
        <v-icon>logout</v-icon>
      </v-btn>
    </v-toolbar-items>
  </v-app-bar>
</template>

<script>
import { mapState } from 'vuex'

export default {
  props: ['value'],
  components: {

  },
  data () {
    return {
      drawer: undefined
    }
  },
  computed: mapState({
    user: state => state.profile,
    version: state => state.version
  }),
  watch: {
    drawer () {
      this.$emit('input', this.drawer)
    }
  },
  beforeMount () {
    if (this.value) this.drawer = this.value
    else this.drawer = false
  }
}
</script>
