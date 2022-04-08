<template>
  <v-navigation-drawer
    app
    clipped
    floating
    v-model="drawer"
  >
    <v-list dense>
      <!--v-list-item link color="primary" @click="setPortMenu">
        <v-list-item-action>
          <v-icon small>security</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>Port Requests</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <div v-if="hasMRTG">
        <v-list-item link color="primary" @click="setMRTGMenu">
          <v-list-item-action>
            <v-icon small>build</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>MRTG Requests</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
      </div ! Just leaving this here for example how to use...!-->
      <div v-if="hasAdmin">
        <v-list-item link color="primary" @click="setSettingsMenu">
          <v-list-item-action>
            <v-icon small>settings_applications</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Site Settings</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider dark></v-divider>
      </div>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapState } from 'vuex'
import { userHasPermission, setSideMenu } from '@/util'

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
    ...mapState({
      user: state => state.profile
    }),
    hasAdmin () {
      return userHasPermission('ADMIN')
    }
    /**hasMRTG () {
      return userHasPermission('MRTG')
    } Just examples... */
  },
  methods: {
    /**setMRTGMenu () {
      setSideMenu('mrtg')
    },
    setPortMenu () {
      setSideMenu('ports')
    }, just examples...*/
    setSettingsMenu () {
      setSideMenu('settings')
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
