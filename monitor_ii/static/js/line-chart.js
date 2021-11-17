// this code is an absolute mess because i rewrote the structure and functions multiple times

let lineChartCanvasTemp = document.getElementById("Temp-Chart")


let lineOptions = {
    legend: {display: false},
    titles: {display: true,
             text: "Temperature"
    },
    Scales: {
         xAxes: [{
             scaleLabel: {
                 display: true,
                 labelString: "Time",
             },
         }],
         yAxes: [{
             scaleLabel: {
                 display: true,
                 labelString: "Temperature",
             },
              // ticks: {
              //    beginAtZero: true,
              //    suggestedMin: 0,
              //    suggestedMax: 100,
              // },
         },
         ]},
    }


// updates the temperature
async function updateTemperature(){

    let data = await getTemperature();



let lineData = {
    labels: ["Celsius"],
    datasets: [{
         label: "Celsius",
         // data: data.map(_i => new Date(_i.Date )),
         borderWidth: 2,
         lineTension: 0.2,
         fill: false,
         borderColor: ["rgba( 33, 26, 29, 1)"],
         }],
    }
    //creates the chart and places the API data into their respective axes
let myChartTemperature = new Chart(lineChartCanvasTemp, {
    type: 'line',
    data: {
      labels: data.x,
      datasets: [{
        label: 'Temperature (Celsius)',
        data: data.y,
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
      }]},
        // options: lineOptions,
});
    // myChartTemperature.data.datasets[0].data = data
    myChartTemperature.update()

}

async function getTemperature(){
    let url = 'http://127.0.0.1:5000/api/temperature/-25';
    let data = await fetch(url);
    return await data.json();

}

updateTemperature()