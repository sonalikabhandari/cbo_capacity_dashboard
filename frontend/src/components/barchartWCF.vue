<template>
 <div>
 <barchartWCF v-if="loaded" :chartData="getwcfData" :chartLabels="wcfLabels" @bar-clicked="onClickChild"></barchartWCF>
</div>
</template>

<script>
import { mapState } from 'vuex'
import { wcfFilter } from '@/api'
import barchartWCF from '@/components/childbarChartWCF.vue'

export default {
  components: {
    barchartWCF
  },
  props: {
    wcfMonth: {
      type: String,
      required: false
    },
    wcfYear: {
      type: String,
      required: false
    }
  },
  data () {
    return {
      loaded: false,
      months: null,
      years: '',
      userMonth: this.wcfMonth,
      userYear: this.wcfYear,
      requests: [],
      wcfLabels: [],
      wcf_Jan: [],
      wcf_all: [],
      request: [],
    }
  },
  computed: {

    ...mapState({
      token: state => state.token,
      user: state => state.user
    }),

    month_year () {
      for (let i = 0; i < this.requests.length; i++) {
        this.months.push(requests[i].path_month)
        this.years.push(requests[i].path_year)
        console.log(this.months)
        console.log(this.years)
      }
    },

    getwcfData () {
    if (this.wcfMonth == null) {
    return this.wcf_Jan
    }
    else if (this.wcfMonth == '' && this.wcfYear == '') {
      return this.wcf_Jan
    }
    else return this.gettingwcfdata()
    },
  },

  methods: {

    loadDatawcf () {

      this.$store.dispatch('inspectToken')
        .then(() => {

          return wcfFilter(this.token)
            .then((response) => {
              console.log('here1')
              this.request = response.data
              const events = response.data
              console.log(this.userMonth)
              this.wcfLabels.push('<70%', '70-79%', '80-89%', '90-99%', '>100%')
              for (let i = 0; i < events.length; i++) {
                if (events[i].months == 'January' && events[i].years == 2019) {
                  this.wcf_Jan.push(events[i].count_lt_seventy)
                  this.wcf_Jan.push(events[i].count_lt_seventynine)
                  this.wcf_Jan.push(events[i].count_lt_eightynine)
                  this.wcf_Jan.push(events[i].count_lt_ninetynine)
                  this.wcf_Jan.push(events[i].count_gt_hundred)
                }
              }
              this.loaded = true
            })
          console.log(this.wcf_Jan)
          console.log(this.wcf_Feb)
          console.log(this.months)
          console.log(this.labels_data_Jan)
          console.log(this.labels_data_Feb)
        })
    },

    gettingwcfdata () {

    for (let i = 0; i < this.request.length; i++) {
      if (this.request[i].months == this.userMonth && this.request[i].years == this.userYear){
      this.wcf_all = [];
      this.wcf_all.push(this.request[i].count_lt_seventy)
      this.wcf_all.push(this.request[i].count_lt_seventynine)
      this.wcf_all.push(this.request[i].count_lt_eightynine)
      this.wcf_all.push(this.request[i].count_lt_ninetynine)
      this.wcf_all.push(this.request[i].count_gt_hundred)
      return this.wcf_all
      }
    }
    },

    onClickChild (value) {
      this.$emit('ClickedBar', value)
    },
  },
  beforeMount () {
    this.loadDatawcf()
  },
  watch: {
    wcfMonth: function () {
    this.userMonth = this.wcfMonth
    },
    wcfYear: function () {
    this.userYear = this.wcfYear
    }
    }
}
</script>

<style>
th {
  font-size: 24px;
}

  table tr + tr {
  font-family: Arial;
  }

  thead {
    background-color: #455A64;
    color: #FFFFFF;
  }

</style>
