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
              ticks: {beginAtZero: True,}
              },
              ]},
    }

var myChartTemperature = new Chart(chartCanvasTemperature,); {
    type: "bar"
    data: barData,
    options: barOptions;

})


async function updateTemp(){
    let temps = await getTemp();
    myChartTemperature.data.datasets[0].data = [temps.temperature]
    myChartTemperature.update()

}


async function getTemp(){
    let link = 'http://127.0.0.1:5000/api/temperature';
    try {
        let result = await fetch(link);
        return await result.json();
        }catch(error){
            console.log(error);
        }
}

updateTemp()
