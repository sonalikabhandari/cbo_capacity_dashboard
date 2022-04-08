
<script>
import { Bar } from 'vue-chartjs'
import { capacityAdded } from '@/api'
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
    }
  },

  data () {
    return {
      options: {
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
              display: true

            }
          }]
        },
        legend: {
          display: false
        },
        title: {
          display: true,
          text: 'Total Capacity Added (Backbone), Monthly(Tbps)',
          fontColor: 'white',
          fontSize: 15,
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
          label: 'WCF Utilizations %',
          backgroundColor: '#fc6c71',
          data: this.chartData
        }
      ]
    }, this.options)
  }
}
</script>
