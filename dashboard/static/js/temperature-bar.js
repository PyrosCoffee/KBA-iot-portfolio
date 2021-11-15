var barChartCanvasTemperature = document.getElementById("Temperature-Bar")

var barData = {
    labels: ["Current"],
    datasets: [{
         label: "Temperature",
         data: [15],
         borderWidth: 1,
         backgroundColor: ["rgba( 167, 117, 77, 1)"],
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
    type: "bar",
    data: barData,
    options: barOptions
});

//less messy code for showing data?
async function updateTemp(){
    let data = await getTemp();
    myChartTemperature.data.datasets[0].data = [data.Temperature]
    myChartTemperature.update()

}


async function getTemp(){
    let link = 'http://127.0.0.1:5000/api/temperature';
    let result = await fetch(link);
    return await result.json();
}

updateTemp()
