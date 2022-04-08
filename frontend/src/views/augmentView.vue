<template>
 <div>
  <augmentcomponent :requests="requests"
  ></augmentcomponent>
</div>
</template>

<script>
// @ is an alias to /src
import augmentcomponent from '@/components/augmentData.vue'
import { augmentview } from '@/api'
import { mapState } from 'vuex'

export default {
  components: {
    augmentcomponent
  },

  computed: {
    ...mapState({
      token: state => state.token,
      user: state => state.user
    })
  }
}
</script>
