<template>
 <div>
 <barchartCapacityAdded v-if="loaded" :chartData="capAdded" :chartLabels="labels"></barchartCapacityAdded>
</div>
</template>

<script>
// @ is an alias to /src

import barchartCapacityAdded from '@/components/childbarCapacityAdded.vue'

import { capacityAdded } from '@/api'
import { mapState } from 'vuex'

export default {
  components: {
    barchartCapacityAdded
  },
  props: {},
  data () {
    return {
      loaded: false,
      capAdded: [],
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
          return capacityAdded(this.token)
            .then((response) => {
              console.log('here1')
              const events = response.data
              console.log('printing events')
              console.log(events)
              for (let i = 0; i < events.length; i++) {
                this.labels.push(events[i].month_year)
                this.capAdded.push(events[i].total_augment)
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
