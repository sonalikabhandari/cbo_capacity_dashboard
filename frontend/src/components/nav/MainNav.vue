<template>
  <span>
    <!-- Side Navigation Options -->
    <side-nav
      v-model="drawer"
      v-if="sideMenu === 'main'"
    ></side-nav>
    <site-settings-side-nav
      v-model="drawer"
      v-else-if="sideMenu === 'settings'"
    ></site-settings-side-nav>
    <!-- End Side Navigation Options -->
    <!-- Top Navigation Options -->
    <top-nav
      v-model="drawer"
      v-if="topMenu === 'main'"
    ></top-nav>
    <!-- End Top Navigation Options -->
  </span>
</template>

<script>
/**
 * Controls content of side and top nav bars.
 * Current options:
 * Top:
 *      main - the main top navigation bar.  Has button to collapse side bar
 *             as well as shows version of FE, site name, and logout button
 *
 * Side:
 *      main - the main side bar giving options to drill into specific request
 *             types
 *      settings - admin functionality for whole site, roles.
 **/
import { mapState } from 'vuex'
import TopNav from '@/components/nav/TopNav'
import SideNav from '@/components/nav/SideNav'
import SiteSettingsSideNav from '@/components/nav/SiteSettingsSideNav'
import { setSideMenu } from '@/util'

export default {
  components: {
    SideNav,
    SiteSettingsSideNav,
    TopNav
  },
  data () {
    return {
      drawer: true
    }
  },
  computed: {
    ...mapState({
      user: state => state.profile,
      version: state => state.version,
      topMenu: state => state.topMenu,
      sideMenu: state => state.sideMenu
    })
  },
  /*
   * this code only exists while we are single use for this portal
   * after more non permission based routes are entered into the system
   * this beforeMount statement should be removed.
   */
  beforeMount () {
    if (this.user.permissions) {
      if (Object.keys(this.user.permissions).length > 0) return
    }
    setSideMenu('ports')
  }
}
</script>
