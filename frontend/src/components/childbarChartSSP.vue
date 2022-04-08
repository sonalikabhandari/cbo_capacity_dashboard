
<script>
import { HorizontalBar, mixins } from 'vue-chartjs'
import 'chartjs-plugin-datalabels'

const { reactiveProp } = mixins

export default {
  extends: HorizontalBar,
  mixins: [reactiveProp],

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
      barValue: [],
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
          text: 'SSP Utilization %',
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
        onClick: this.barClick,

        labels: {
          fontColor: 'white',
          fontStyle: 'bold'
        },
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  methods: {
    barClick (evt, array) {
      if (array.length != 0) {
        var position = array[0]._index
        var activeElement = array[0]._model.label
        this.barValue.push(activeElement)
        this.barValue = this.barValue.filter(function( item, index, inputArray ) {
           return inputArray.indexOf(item) == index;});
        this.$emit('bar-clicked', this.barValue)
        console.log(activeElement)
        console.log('helloji')
        console.log(this.barValue)
      } else {
        console.log('You selected the background!')
      }
    }
  },
  mounted () {
    this.renderChart({
      labels: this.chartLabels,
      datasets: [
        {
          label: 'SSP Utilizations %',
          backgroundColor: ['#66BB6A', '#FFF176', '#F57C00', '#F06292', '#E53935'],
          data: this.chartData
        }
      ]
    }, this.options)
  },
  watch: {
    chartData: function () {
      this._data._chart.destroy()
      this.renderChart({
        labels: this.chartLabels,
        datasets: [
          {
            label: 'SSP Utilizations %',
            backgroundColor: ['#66BB6A', '#FFF176', '#F57C00', '#F06292', '#E53935'],
            data: this.chartData
          }
        ]
      }, this.options)
    },
    deep: true
  }
}
</script>
