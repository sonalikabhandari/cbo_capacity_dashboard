<template>
  <v-navigation-drawer
    app
    clipped
    floating
    v-model="drawer"
  >
    <v-list dense>
      <v-list-item
        color="indigo"
        @click="setMainMenu"
        class="indigo darken-2"
      >
        <v-list-item-action>
          <v-icon small>arrow_back</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>Main Menu</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <v-list-item
        :to="{ name: 'roles', params: { type: 'department' }}"
        link
        color="primary"
      >
        <v-list-item-action>
          <v-icon small>group</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>Department Roles</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <v-list-item
        :to="{ name: 'roles', params: { type: 'user' }}"
        link
        color="primary"
      >
        <v-list-item-action>
          <v-icon small>person</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>User Roles</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { setSideMenu } from '@/util'

export default {
  props: ['value'],
  components: {

  },
  data () {
    return {
      drawer: undefined
    }
  },
  computed: {

  },
  methods: {
    setMainMenu () {
      setSideMenu('main')
    }
  },
  beforeMount () {
    if (this.value) this.drawer = this.value
    else this.drawer = false
  },
  watch: {
    value () {
      this.drawer = this.value
    }
  }
}
</script>
