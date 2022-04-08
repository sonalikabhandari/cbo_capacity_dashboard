
<script>
import { Line } from 'vue-chartjs'
import { totalcapacity } from '@/api'
import 'chartjs-plugin-datalabels'

export default {
  extends: Line,
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
        layout: {
          padding: {
            left: 25,
            right: 25,
            top: 0,
            bottom: 0
          }
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
              display: true,
              color: '#616161'
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
          text: 'NBB Capacity Growth Trend, Monthly(Tbps)',
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
          backgroundColor: '#1DE9B6',
          borderColor: '#1DE9B6',
          borderWidth: 2,
          lineTension: 0,
          fill: false,
          pointBackgroundColor: '#1DE9B6',
          pointBorderColor: '#1DE9B6',

          data: this.chartData
        }
      ]
    }, this.options)
  }
}
</script>
