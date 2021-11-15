var barChartCanvasHumidity = document.getElementById("Humidity-Bar")

var barData = {
    labels: ["Current"],
    datasets: [{
         label: "Humidity",
         data: [32],
         borderWidth: 2,
         backgroundColor: ["rgba( 157, 105, 163, 1)"],
         borderColor: ["rgba( 33, 26, 29, 1)"],
         }],
    }

var barOptions = {
    Scales: {
         yAxes: [{
              ticks: {beginAtZero: True,}
              },
              ]},
    }

var myChartHumidity = new Chart(barrChartCanvasHumidity,) {
    type: 'bar'
    data: barData,
    options: barOptions,
    })