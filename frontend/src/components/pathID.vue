<template>

 <div>
 <v-card-title class="blue-grey darken-2 white--text">
  Path - {{pathinfo}}
 </v-card-title>
 <v-container>
<v-layout column align-center justify-center >
 <v-card-title class="grey darken-2 white--text">
  Growth Projections
 </v-card-title>
 <v-subheader class="white--text font-size:20px;" >
 <div><div style="float: left; margin-bottom: 10px; clear: both; background-color:#EF5350; width:15px; height:15px; left: 10px; top: 15px;"></div>Unsafe</div>
 <br>
 <div><div style="float: left; margin-bottom: 10px;  clear: both; background-color:#FDD835; width:15px; height:15px; left: 10px; top: 15px;"></div>Above Threshold</div>
 <br>
 <div><div style="float: left; margin-bottom: 10px;  clear: both; background-color: #43A047; width:15px; height:15px; left: 10px; top: 15px;"></div>Below Threshold</div>
 </v-subheader>
 </v-layout>
 </v-container>
 <v-card>
     <v-container>
       <v-layout align-center justify-center fill-height>
       <v-col>
         <barchartpathinfo v-if="loaded" :chartData="wcf" :chartLabels="rep_date"
         :chartcolors="path_colors" :charttitle="pathinfo"></barchartpathinfo>
         </v-col>
         </v-layout>
 </v-container>
 </v-card>
 <v-container>
<v-layout column align-center justify-center >
 <v-card-title class="grey darken-2 white--text">
 Growth Projection,if 2020 End State is complete
 </v-card-title>
 <v-subheader class="white--text font-size:20px;" >
 <div><div style="float: left; margin-bottom: 10px; clear: both; background-color:#EF5350; width:15px; height:15px; left: 10px; top: 15px;"></div>Unsafe</div>
 <br>
 <div><div style="float: left; margin-bottom: 10px;  clear: both; background-color:#FDD835; width:15px; height:15px; left: 10px; top: 15px;"></div>Above Threshold</div>
 <br>
 <div><div style="float: left; margin-bottom: 10px;  clear: both; background-color: #43A047; width:15px; height:15px; left: 10px; top: 15px;"></div>Below Threshold</div>
 </v-subheader>
 </v-layout>
 </v-container>
  <v-card>
 <v-container>
   <v-layout align-center justify-center fill-height>
   <v-col>
         <endstatepathinfo v-if="loaded" :chartData="es_wcf" :chartLabels="rep_date"
         :chartcolors="es_path_colors" :charttitle="pathinfo" :legenddata="es_legend_labels"></endstatepathinfo>
         </v-col>
         </v-layout>
 </v-container>
 </v-card>
</div>
</template>

<script>
// @ is an alias to /src

import barchartpathinfo from '@/components/childbarpathinfo.vue'
import endstatepathinfo from '@/components/childbarpathinfo.vue'

import { dashboardviewpathinfo } from '@/api'
import { mapState } from 'vuex'
import axios from "axios";
import Vue from 'vue'

export default {
  name: 'dashboardviewID',
  props: {
    pID: {
      type: Number,
      required: true
    }
  },
  components: {
    barchartpathinfo,
    endstatepathinfo
  },
  data () {
    return {
      loaded: false,
      rep_date: [],
      es_wcf: [],
      es_path_colors: [],
      wcf: [],
      path_colors: [],
      pathinfo: '',
      legend_labels: [],
      trial: [],
      es_trial: [],
      es_legend_labels: []

    }
  },
  computed: {
    ...mapState({
      token: state => state.token,
      user: state => state.user
    })
  },
  methods: {
    postData () {
    const headers = {
      'Content-Type': 'application/json'
    }
   Vue.axios.post(
      'http://localhost:8000/path',
      {
         Pthid: 'sona',
      },
    { headers: headers }
    )
    .then(response => {
      this.resp = response;
      console.log(response+"this is axios post")
    })
    .catch(e => {
      console.error(e);
    });
    },
    loadData () {
      this.$store.dispatch('inspectToken')
        .then(() => {
          console.log('here1')
          return dashboardviewpathinfo(this.token)
            .then((response) => {
              console.log('here2')
              console.log("path-id is here"+this.pID)
              const events = response.data

              for (let i = 0; i < events.length; i++) {
                if (events[i].path_info_id == this.pID) {
                  this.rep_date.push(events[i].path_date)
                  this.wcf.push(events[i].current_wcf_util)
                  this.es_wcf.push(events[i].end_state)
                  this.pathinfo = events[i].path_name

                  if (events[i].current_wcf_util >= 100) {
                    this.path_colors.push('#EF5350')
                  } else if (events[i].current_wcf_util >= 80 && events[i].current_wcf_util < 100) {
                    this.path_colors.push('#FDD835')
                  } else {
                    this.path_colors.push('#43A047')
                  }

                  if (events[i].end_state >= 100) {
                    this.es_path_colors.push('#EF5350')
                  } else if (events[i].end_state >= 80 && events[i].end_state < 100) {
                    this.es_path_colors.push('#FDD835')
                  } else {
                    this.es_path_colors.push('#43A047')
                  }
                }
              }

              console.log(this.legend_labels)
              this.loaded = true
              console.log(this.rep_date)
              console.log(this.wcf)
              console.log(this.path_colors)
              console.log(this.pathinfo)

              console.log(this.es_legend_labels)
            })
        })
    }
  },
  beforeMount () {
    this.postData()
    this.loadData()
  }

}
</script>
