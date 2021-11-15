var barChartCanvasTemperature = document.getElementById("Temperature-Bar")

var barData = {
    labels: ["Celsius"],
    datasets: [{
         label: "Current",
         data: [],
         borderWidth: 1,
         backgroundColor: ["rgba(167, 117, 77, 1)"],
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


var myChartTemperature = new Chart(barChartCanvasTemperature, {
    type: 'bar',
    data: barData,
    options: barOptions,
});


async function updateTemperature(){
    let data = await getTemperature();
    myChartTemperature.data.datasets[0].data = [data.Temperature]
    myChartTemperature.update()

}

async function getTemperature(){
    let url = 'http://127.0.0.1:5000/api/temperature';
    let data = await fetch(url);
    return await data.json();

}


updateTemperature()