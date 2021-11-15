// i think this was supposed to be on a separate page? oops

let lineChartCanvasTemperature = document.getElementById("Temperature-Bar")

let lineData = {
    labels: ["Celsius", "Time"],
    datasets: [{
         label: "Temperature",
         line: "",
         data: [35, 100],
         borderWidth: 1,
         lineTension: 0.2,
         fill: false,
         backgroundColor: ["rgba( 167, 117, 77, 1)"],
         borderColor: ["rgba( 33, 26, 29, 1)"],
         }],
    }

let lineOptions = {
    legend: {display: false},
    title: {display: true, text: "Temperature"},
    Scales: {
        xAxes: [{
            scaleLabel: {display: true, labelString: "Time",
            }
        }],
        yAxes: [{
            scaleLabel: {display: true, labelString: "Celsius",
            },
            ticks: {beginAtZero: true, suggestedMin: 0, suggestedMax: 100,
            },
        }]
    }
}

let tempLineChartTemperature = new Chart(lineChartCanvasTemperature, {
    type: "line",
    data: lineData,
    options: lineOptions
});


//less messy code for showing data?
async function updateTemp(){
    let data = await getTemp();
    tempLineChartTemperature.data.datasets[0].data = [data.temp]
    tempLineChartTemperature.update()

}


async function getTemp(){
    let link = 'http://127.0.0.1:5000/api/temperature';
    let result = await fetch(link);
    return await result.json();
}

updateTemp()
