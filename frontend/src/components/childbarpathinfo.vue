
<script>
import { Bar } from 'vue-chartjs'
import 'chartjs-plugin-datalabels'

export default {
  extends: Bar,
  props: {
    chartData: {
      type: Array | Object,
      required: false
    },
    chartLabels: {
      type: Array,
      required: true
    },
    chartcolors: {
      type: Array,
      required: false
    },
    charttitle: {
      type: String,
      required: false
    },
    legenddata: {
      type: String,
      required: false
    }
  },

  data () {
    return {
      htmlLegend: null,
      options: {
        legendCallback: function (chart) {
          var legendHtml = []
          legendHtml.push('<div><div class="box red" style="float: left; margin-bottom: 20px;  clear: both; background-color: #EF5350; width:15px; height:15px; left: 10px; top: 15px;"></div>Unsafe</div>')
          legendHtml.push('<br>')
          legendHtml.push('<div><div class="box green" style="float: left; margin-bottom: 20px;  clear: both; background-color: #FDD835; width:15px; height:15px; left: 10px; top: 15px;"></div>Above Threshold</div>')
          legendHtml.push('<br>')
          legendHtml.push('<div><div class="box blue" style="float: left; margin-bottom: 20px;  clear: both; background-color: #43A047; width:15px; height:15px; left: 10px; top: 15px;"></div>Below Threshold</div>')
          return legendHtml
        },
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true,
              fontSize: 15,
              fontColor: 'white',
              fontStyle: 'bold'
            },
            gridLines: {
              display: true
            },
            scaleLabel: {
              display: true,
              labelString: 'WCF Utilization %',
              fontSize: 15,
              fontColor: 'white',
              fontStyle: 'bold'
            }
          }],
          xAxes: [{
            ticks: {
              beginAtZero: true,
              fontSize: 15,
              fontColor: 'white',
              fontStyle: 'bold'
            },
            gridLines: {
              display: false
            }
          }]
        },
        legend: {
          display: false
        },
        title: {
          display: true,
          text: this.charttitle,
          fontColor: 'white',
          fontSize: 20,
          fontStyle: 'bold'
        },
        plugins: {
          datalabels: {
            align: 'end',
            anchor: 'end',
            color: 'white',
            fontSize: 15,
            fontStyle: 'bold'
          }
        },

        labels: {
          fontColor: 'white',
          fontStyle: 'bold'
        },
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  mounted () {
    this.renderChart({
      labels: this.chartLabels,
      datasets: [
        {
          label: 'SSP Utilizations %',
          backgroundColor: this.chartcolors,
          data: this.chartData
        }
      ]
    }, this.options)
    this.htmlLegend = this.$data._chart.generateLegend()
  }
}
</script>
