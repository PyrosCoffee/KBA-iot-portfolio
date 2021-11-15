
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
              ticks: {beginAtZero: true,}
              },
              ]},
    }

async function getPressure(){
    let url = 'http://127.0.0.1:5000/api/pressure';
    let data = await fetch(url);
    return await data.json();

}

var myChartPressure = new Chart(barChartCanvasPressure, {
    type: 'bar',
    data: barData,
    options: barOptions,
});


async function updatePressure(){
    let data = await getPressure();
    myChartPressure.data.datasets[0].data = [data.Pressure]
    myChartPressure.update()

}



updatePressure()