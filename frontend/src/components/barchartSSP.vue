<template>
 <div>
 <barchartSSP v-if="loaded" :chartData="ssp_data" :chartLabels="sspLabels" @bar-clicked="onClickChild"></barchartSSP>
</div>
</template>

<script>
// @ is an alias to /src

import barchartSSP from '@/components/childbarChartSSP.vue'

import { sspFilter } from '@/api'
import { mapState } from 'vuex'

export default {
  components: {
    barchartSSP
  },
  props: {
    sspMonth: {
      type: String,
      required: false
    },
    sspYear: {
      type: String,
      required: false
    }
  },
  data () {
    return {
      loaded: false,
      ssp_Jan: [],
      sspLabels: [],
      userMonth: this.sspMonth,
      userYear: this.sspYear,
      ssp_all: [],
      request: [],
    }
  },
  computed: {
    ...mapState({
      token: state => state.token,
      user: state => state.user
    }),

    ssp_data () {
    if (this.sspMonth == null) {
    return this.ssp_Jan
    }
    else if (this.sspMonth == '' && this.sspYear == '') {
      return this.ssp_Jan
    }
    else return this.gettingsspdata()
    },
  },
  methods: {
    loadDataSSP () {
      this.$store.dispatch('inspectToken')
        .then(() => {
          console.log('here1')
          return sspFilter(this.token)
            .then((response) => {
              console.log('here1')
              const events = response.data
              this.request = response.data
              this.sspLabels.push('<40%', '40-49%', '50-59%', '60-69%', '>70%')
              for (let i = 0; i < events.length; i++) {
                if (events[i].months == 'January' && events[i].years == 2019) {
                  this.ssp_Jan.push(events[i].count_lt_forty)
                  this.ssp_Jan.push(events[i].count_lt_fortynine)
                  this.ssp_Jan.push(events[i].count_lt_fiftynine)
                  this.ssp_Jan.push(events[i].count_lt_sixtynine)
                  this.ssp_Jan.push(events[i].count_gt_seventy)
                }
              }
              this.loaded = true
            })

          console.log(this.ssp_Jan)
          console.log(this.ssp_Feb)
          console.log(this.sspMonth)
          console.log(this.labels_data_Jan)
          console.log(this.labels_data_Feb)
          console.log(this.barValue)
        })
    },

    gettingsspdata () {

    for (let i = 0; i < this.request.length; i++) {
      if (this.request[i].months == this.userMonth && this.request[i].years == this.userYear){
      this.ssp_all = [];
      this.ssp_all.push(this.request[i].count_lt_forty)
      this.ssp_all.push(this.request[i].count_lt_fortynine)
      this.ssp_all.push(this.request[i].count_lt_fiftynine)
      this.ssp_all.push(this.request[i].count_lt_sixtynine)
      this.ssp_all.push(this.request[i].count_gt_seventy)
      return this.ssp_all
      }
    }
    },

    onClickChild (value) {
      this.$emit('ClickedBar', value)
    },

  },
  beforeMount () {
    this.loadDataSSP()
  },
  watch: {
    sspMonth: function () {
    this.userMonth = this.sspMonth
    },
    sspYear: function () {
    this.userYear = this.sspYear
    }
    }

}
</script>
