
<template>
<div id="app">
  <v-app id="inspire">
  <v-card-title class="blue-grey darken-2 white--text">
  Capacity Dashboard
  </v-card-title>
   <v-card>
    <v-container fluid>
         <v-row>

          <v-layout align-start justify-start fill-height row wrap>

          <v-flex ml-4 pl-4 mt-3 xs2>
          <barchartWCF :wcfMonth="months" :wcfYear="years" @ClickedBar="onWCFClickbar"></barchartWCF>
          </v-flex>

          <v-flex ml-4 pl-4 mt-3 xs2>
          <barchartSSP  :sspMonth="months" :sspYear="years" @ClickedBar="onSSPClickbar"></barchartSSP>
          </v-flex>

        <v-spacer></v-spacer>

          <v-row>
         <v-flex ml-4 pl-4 mt-3 xs2>
            <v-select
            multiple
           label="legacy Company"
           :items="['L-TWC','L-CHTR']"
           v-model="LegacyType"
         ></v-select>
            </v-flex>

            <v-flex ml-4 pl-4 mt-3 xs2>
            <v-select
            multiple
            label="Segment Type"
            :items="['BBR - BBR','BBR - CRR','BBR - PRR']"
           v-model="SegmentType"
            ></v-select>
            </v-flex>

            <v-flex ml-4 pl-4 mt-3 xs2>
            <v-select
            label="Month"
            :items="['January','February','March','April','May','June','July','August','September','October','November','December',]"

           v-model="months"
            ></v-select>
            </v-flex>

            <v-flex ml-4 pl-4 mt-3 xs2>
            <v-select
            label="Year"
            :items="[' 2019 ', '2020','2021',]"
           v-model="years"
            ></v-select>
            </v-flex>

            <v-flex ml-4 pl-4 mt-3 xs2>
             <v-btn small color="#0097A7" v-on:click="resetOptions">Reset</v-btn>
            </v-flex>

            </v-row>

          </v-layout>
          </v-row>
        </v-container>
        </v-card>

      <v-data-table
        ref="capacity_data"
        :headers="headers"
        :items="requests"
        item-key="path_id"
        success
        class="elevation-10"
        >
        <template v-slot:items="props">
          <td class="text-xs-left">{{ props.item.id}}</td>
          <td class="text-xs-left">{{ props.item.reporting_date}}</td>
          <td class="text-xs-left">{{ props.item.path_name}}</td>
          <td class="text-xs-left">{{ props.item.legacy_company }}</td>
          <td class="text-xs-left">{{ props.item.a_location}}</td>
          <td class="text-xs-left">{{ props.item.z_location}}</td>
          <td class="text-xs-left">{{ props.item.a_node}}</td>
          <td class="text-xs-left">{{ props.item.segment_type}}</td>
          <td class="text-xs-left">{{ props.item.leased}}</td>
          <td class="text-xs-left">{{ props.item.current_capacity_gbps}}</td>
          <td class="text-xs-left">{{ props.item.capacity_gbps}}</td>
          <td class="text-xs-left">{{ props.item.current_ssp_util}}</td>
          <td class="text-xs-left">{{ props.item.current_wcf_util}}</td>
          <td class="text-xs-left">{{ props.item.path_month}}</td>
          <td class="text-xs-left">{{ props.item.path_year}}</td>
          <td class="text-xs-left">{{ props.item.path_info_id}}</td>
          <div>

          <router-link :to="{name: 'dashboardviewID', params: {pID: props.item.path_info_id}}"></router-link>

          </div>
        </template>
        <template v-slot:no-results>
          <v-alert :value="true" color="error" icon="warning">
            Found no results.
          </v-alert>
        </template>
        <template v-slot:item.path_name="{ item }">
          <a :href="get_url(item.path_info_id)" target="_blank" @click = postData(item.id)>
          {{ item.path_name}}
        </a>
        </template>
      </v-data-table>
    </v-card>
  </v-app>
</div>
</template>

<script>
import { mapState } from 'vuex'
import { dashboardviewmy } from '@/api'
import { postdashboard } from '@/api'
import barchartSSP from '@/components/barchartSSP.vue'
import barchartWCF from '@/components/barchartWCF.vue'


export default {
  components: {
    barchartWCF,
    barchartSSP
  },
  data () {
    return {
      loaded: false,
      barlabelSSP: [],
      barlabelWCF: [],
      LegacyType: [],
      SegmentType: [],
      months: null,
      years: '',
      path_link: '',
      selected: [],
      getpathid: '',
      getID: '',

      headers: [
        { text: 'ID', value: 'id' },
        { text: 'Date', value: 'reporting_date', width: '15%',
        filter: value => {
          if (!this.months ) return true
          else {
            if (this.month_name(value) === this.months) {
              return value
            }
          }
        }
        },
        { text: 'Path', value: 'path_name', width: '15%' },
        {
          text: 'Legacy Company',
          value: 'legacy_company',
          filter: value => {
            if (this.LegacyType.length == 0) {
              return true
            }
            else {
            if (this.LegacyType.includes(value)) {
              return value
            }
            }
            }

          },
        { text: 'A Location', value: 'a_location' },
        { text: 'Z Location', value: 'z_location' },
        { text: 'A Node', value: 'a_node' },
        { text: 'Z Node', value: 'z_node' },
        {
          text: 'Segment Type',
          value: 'segment_type',
          filter: value => {
            if (this.SegmentType.length == 0) {
              return true
            }
            else {
            if (this.SegmentType.includes(value)) {
              return value
            }
            }
            }

        },
        { text: 'Leased', value: 'leased' },
        { text: 'Current Capacity(Gbps)', value: 'current_capacity_gbps' },
        { text: 'Capacity(Gbps)', value: 'capacity_gbps' },
        { text: 'SSP Traffic(Gbps)', value: 'ssp_traffic_gbps' },
        { text: 'WCF Traffic(Gbps)', value: 'wcf_traffic_gbps' },
        {
          text: 'SSP Utilization %',
          value: 'current_ssp_util',
          filter: value => {
            if (this.barlabelSSP.length == 0) return true
            else {
              if (this.barlabelSSP.includes('<40%')) {
                if (value < 40) {
                  return value
                }
              }
              if (this.barlabelSSP.includes('40-49%')) {
                if (value >= 40 && value <= 49) {
                  return value
                }
              }
              if (this.barlabelSSP.includes('50-59%')) {
                if (value >= 50 && value <= 59) {
                  return value
                }
              }
              if (this.barlabelSSP.includes('60-69%')) {
                if (value >= 60 && value <= 69) {
                  return value
                }
              }
              if (this.barlabelSSP.includes('>70%')) {
                if (value > 70) {
                  return value
                }
              }
            }
          }
        },
        {
          text: 'WCF Utilization %',
          value: 'current_wcf_util',
          filter: value => {
            if (this.barlabelWCF.length == 0) return true
            else {
              if (this.barlabelWCF.includes('<70%')) {
                if (value < 70) {
                  return value
                }
              }
              if (this.barlabelWCF.includes('70-79%')) {
                if (value >= 70 && value <= 79) {
                  return value
                }
              }
              if (this.barlabelWCF.includes('80-89%')) {
                if (value >= 80 && value <= 89) {
                  return value
                }
              }
              if (this.barlabelWCF.includes('90-99%')) {
                if (value >= 90 && value <= 99) {
                  return value
                }
              }
              if (this.barlabelWCF.includes('>100%')) {
                if (value > 100) {
                  return value
                }
              }
            }
          }
        },
        {
            text: 'Year',
            value: 'path_year',
            filter: value => {
              if (!this.years) return true
              else {
                if (value === Number(this.years)) {
                  return value
                }
              }
            }

          },
        { text: 'Path_info_ID', value: 'path_info_id' }
      ],
      requests: []
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


  },
  methods: {

    loadData () {
      this.$store.dispatch('inspectToken')
        .then(() => {
          console.log('here1')
          return dashboardviewmy(this.token)
            .then((response) => {
              console.log('here1')
              const data = response.data
              this.requests = data
              console.log(this.requests)
              console.log('chao')
            })
        })
    },

    postData (id) {
    this.$store.dispatch('inspectToken')
      .then(() => {
        console.log("Sona sending data to teh backend "+ id)
        return postdashboard(this.token, id)
          .then((response) => {
            this.requests = this.data.requests
          }).catch((error) => {
            console.debug(error)
          })

      })


    },

    month_name (dt) {
    if (dt) {
    let regex = /^(\d{4})-(\d{2})-(\d{2})$/;
    let match = regex.exec(dt);
    let month = +match[2] -1;
    let mlist = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ];
    return mlist[month];
    }
    },



    year_name (dt) {
    if (dt) {
    let d = new Date(dt);
    return d.getFullYear();
    }
    },

    onSSPClickbar (value) {
      for (let i = 0; i < value.length; i++) {
        this.barlabelSSP.push(value[i])
        this.barlabelSSP = this.barlabelSSP.filter(function( item, index, inputArray ) {
           return inputArray.indexOf(item) == index;});
      }
      console.log(value+"Sonaji")
      console.log(this.barlabelSSP+" SonajiAgain ")
    },

    onWCFClickbar (value) {
    for (let i = 0; i < value.length; i++) {
      this.barlabelWCF.push(value[i])
      this.barlabelWCF = this.barlabelWCF.filter(function( item, index, inputArray ) {
         return inputArray.indexOf(item) == index;});
    }
    console.log(value+"Sonaji")
    console.log(this.barlabelWCF+" SonajiAgain ")
    },

    get_url (path_info_id) {
      this.path_link = 'http://localhost:8000/dashboardview/'
      return ''.concat(this.path_link,path_info_id)
    },

    resetOptions () {
      this.LegacyType = []
      this.SegmentType = []
      this.months = ''
      this.years = ''
    },

  },
  beforeMount () {
    this.loadData()
  },

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
