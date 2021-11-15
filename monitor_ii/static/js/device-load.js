var pieChartCanvasDeviceLoad = document.getElementById('Device-Load-Pie')
var pieData = {
    labels: ['CPU Load', 'Idle'],
    datasets: [{
        data: [36, 64],
        borderWidth: 2,
        borderAlign: 'inner',
        backgroundColor: ['rgba(57, 147, 221, 1)', 'rgba(64, 249, 155, 1)'],
        borderColor:['rgba(57, 147, 221, 1)','rgba(64, 249, 155, 1)'
        ],
    }],
}

var pieOptions = {}

var myPieChartDeviceLoad = new Chart(pieChartCanvasDeviceLoad, {
    type: 'pie',
    data: pieData,
    options: pieOptions,
})


async function getCPUInfo(){
    let link = 'http://127.0.0.1:5000/api/cpu-load';
    let result = await fetch(link);
    return await result.json();

}

getCPUInfo()