<template>
 <div>
  <dashboardcomponent/>
</div>
</template>

<script>
// @ is an alias to /src
import dashboardcomponent from '@/components/dashboardData.vue'

import { dashboard } from '@/api'
import { mapState } from 'vuex'

export default {
  components: {
    dashboardcomponent
  },

  computed: {
    ...mapState({
      token: state => state.token,
      user: state => state.user
    })
  }
}
</script>
