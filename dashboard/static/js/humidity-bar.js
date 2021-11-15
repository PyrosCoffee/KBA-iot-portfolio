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
              ticks: {beginAtZero: true}
          },
      ]},
    }

var myChartHumidity = new Chart(barChartCanvasHumidity, {
    type: 'bar',
    data: barData,
    options: barOptions,
});

async function getHumidity(){
    let link = 'http://127.0.0.1:5000/api/humidity';
    let result = await fetch(link);
    return await result.json();
}


async function updateHumidity(){
    let data = await getHumidity();
    myChartHumidity.data.datasets[0].data = [data.Humidity]
    myChartHumidity.update()

}

updateHumidity();