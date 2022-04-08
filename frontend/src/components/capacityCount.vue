<template>
 <div>
 <capacitycount v-if="loaded" :chartData="count" :chartLabels="labels"></capacitycount>
</div>
</template>

<script>
// @ is an alias to /src

import capacitycount from '@/components/childCapacityCount.vue'

import { capacityCount } from '@/api'
import { mapState } from 'vuex'

export default {
  components: {
    capacitycount
  },
  props: {},
  data () {
    return {
      loaded: false,
      count: [],
      labels: []
    }
  },
  computed: {
    ...mapState({
      token: state => state.token,
      user: state => state.user
    })
  },
  methods: {
    loadData () {
      this.$store.dispatch('inspectToken')
        .then(() => {
          console.log('here1')
          return capacityCount(this.token)
            .then((response) => {
              console.log('here1')
              const events = response.data
              console.log('printing events')
              console.log(events)
              for (let i = 0; i < events.length; i++) {
                this.labels.push(events[i].month_year)
                this.count.push(events[i].Count_augment)
              }
              this.loaded = true
            })
          console.log(response.data)
        })
    }
  },
  beforeMount () {
    this.loadData()
  }

}
</script>
