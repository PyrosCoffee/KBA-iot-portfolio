var barChartCanvasPressure = document.getElementById("Pressure-Bar")

var barData = {
    labels: ["Current"],
    datasets: [{
         label: "Pressure",
         data: [32],
         borderWidth: 2,
         backgroundColor: ["rgba( 57, 147, 221, 1)"],
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

var myChartPressure = new Chart(barrChartCanvasPressure,) {
    type: 'bar'
    data: barData,
    options: barOptions,
    })