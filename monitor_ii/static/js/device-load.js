
var pieChartCanvasDeviceLoad = document.getElementById('Device-Load-Pie')


var pieOptions = {}

//pulls current cpu info from the api
//probably a better way to do this, update later
async function getCPUInfo(){
    let url = 'http://127.0.0.1:5000/api/cpu-load';
    let data = await fetch(url);
    return await data.json();

}
// mess of code that displays current cpu load and idle in a pie chart
//update later
async function loadData() {
    let data = await getCPUInfo();
    console.log("data", data);

    const cpu_load = data['CPU Load'];
    const cpu_idle = 100 - cpu_load;
    var pieData = {
        labels: ['CPU Load', 'Idle'],
        datasets: [{
            data: [cpu_load, cpu_idle],
            borderWidth: 2,
            borderAlign: 'inner',
            backgroundColor: ['rgba(57, 147, 221, 1)', 'rgba(64, 249, 155, 1)'],
            borderColor:['rgba(57, 147, 221, 1)','rgba(64, 249, 155, 1)'
            ],
        }],
    }

    var myPieChartDeviceLoad = new Chart(pieChartCanvasDeviceLoad, {
        type: 'pie',
        data: pieData,
        options: pieOptions,
    });

}

loadData();
