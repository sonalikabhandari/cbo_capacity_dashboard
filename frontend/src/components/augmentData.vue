<template>
<div id="app">
  <v-app id="inspire">
  <v-card-title class="blue-grey darken-2 white--text">
  Augment Dashboard
  </v-card-title>
    <v-card>
        <v-container fluid fill-height>
        <v-row>
          <v-layout align-start justify-start fill-height >
          <v-flex ml-4 pl-4 mt-3 md4>
            <augmentedCapacity/>
            </v-flex >
          <v-flex ml-4 pl-4 mt-3 md4>
            <capacity_count/>
            </v-flex>
            <v-flex ml-4 pl-4 mt-3 md4>
            <capacity_total/>
            </v-flex>
              </v-layout>
              </v-row>

           <v-row>
            <v-flex ml-0 pl-4 mt-3 xs2 >
            <v-text-field v-model="end_date_from" label="From date"></v-text-field>
          </v-flex>
          <v-flex ml-2 pl-4 mt-3 xs2>
          <v-text-field v-model="end_date_to" label="To date"></v-text-field>
        </v-flex>
        </v-row>
        </v-container>

  <v-data-table
  :headers="headers"
  :items="requests"
  item-key="path_id"
  v-model="selected"
  :items-per-page="5"
  class="elevation-1"
  :search="search"
  >
  <template v-slot:no-results>
    <v-alert :value="true" color="error" icon="warning">
      Found no results.
    </v-alert>
  </template>
  </v-data-table>
</v-card>
</v-app>
</div>
</template>

<script>
import { mapState } from 'vuex'
import { augmentview } from '@/api'
import augmentedCapacity from '@/components/barCapacityadded.vue'
import capacity_count from '@/components/capacityCount.vue'
import capacity_total from '@/components/totalcapacity.vue'

export default {

  components: {
    capacity_total,
    capacity_count,
    augmentedCapacity

  },

  props: ['requests'],
  data () {
    return {
      search: '',
      end_date_to: null,
      end_date_from: null,
      selected: [],
      headers: [

        {
          text: 'reporting_date',
          value: 'reporting_date',
          filter: value => {
            if (!this.end_date_from && !this.end_date_to) return true
            else {
              if (new Date(value) >= new Date(this.end_date_from) && new Date(value) <= new Date(this.end_date_to)) {
                return value
              }
            }
          }
        },
        { text: 'Seq', value: 'path_id' },
        { text: 'Legacy Company', value: 'legacy_company' },
        { text: 'A Location', value: 'a_location' },
        { text: 'Z Location', value: 'z_location' },
        { text: 'A Node', value: 'a_node' },
        { text: 'Z Node', value: 'z_node' },
        { text: 'Segment Type', value: 'segment_type' },
        { text: 'Leased', value: 'leased' },
        { text: 'Augmented Net Capacity(Gbps)', value: 'capacity_added_gbps' },
        { text: 'Monthly Start Capacity(Gbps)', value: 'ms_capacity_gbps' },
        { text: 'SSP(Gbps)', value: 'ssp_traffic_gbps' },
        { text: 'WCF(Gbps)', value: 'wcf_traffic_gbps' },
        { text: 'Pre Augment SSP Util%', value: 'pre_aug_ssp_util' },
        { text: 'Pre Augment WCF Util%', value: 'pre_aug_wcf_util' },
        { text: 'Post Augment SSP Util%', value: 'post_aug_ssp_util' },
        { text: 'Post Augment WCF Util%', value: 'post_aug_wcf_util' }
      ]
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
          return augmentview(this.token)
            .then((response) => {
              console.log('here1')
              const data = response.data
              this.requests = data.requests
              console.log(this.requests)
            })
        })
    },
  },
  beforeMount () {
    this.loadData()
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
