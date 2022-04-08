
<script>
import { Line } from 'vue-chartjs'
import { capacityCount } from '@/api'
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
          text: 'Total # of Augments Completed,Monthly',
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
          backgroundColor: '#3949AB',
          borderColor: '#3949AB',
          borderWidth: 2,
          lineTension: 0,
          fill: false,
          pointBackgroundColor: '#3949AB',
          pointBorderColor: '#3949AB',

          data: this.chartData
        }
      ]
    }, this.options)
  }
}
</script>
