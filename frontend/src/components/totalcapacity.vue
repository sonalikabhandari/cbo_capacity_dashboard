<template>
 <div>
 <capacitytotal v-if="loaded" :chartData="total" :chartLabels="labels"></capacitytotal>
</div>
</template>

<script>
// @ is an alias to /src

import capacitytotal from '@/components/childtotalcapacity.vue'

import { totalcapacity } from '@/api'
import { mapState } from 'vuex'

export default {
  components: {
    capacitytotal
  },
  props: {},
  data () {
    return {
      loaded: false,
      total: [],
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
          return totalcapacity(this.token)
            .then((response) => {
              console.log('here1')
              const events = response.data
              console.log('printing events')
              console.log(events)
              for (let i = 0; i < events.length; i++) {
                this.labels.push(events[i].path_date)
                this.total.push(events[i].TotalValue)
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
