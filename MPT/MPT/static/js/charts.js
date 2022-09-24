var xValues = [
  "Engg. Maths 1",
  "Engg. Physics 1",
  "Engg. Chemistry 1",
  "Basic Elec. Engg.",
  "Mechanics",
];
var ia1Values = [5, 8, 6, 8, 4];
var ia2Values = [7, 5, 8, 8, 6];
var eseValues = [66, 47, 35, 39, 40];

var ia1Color = ["#FA1E0E", "#FFCA03", "#42E6A4", "#3EDBF0", "#C355F5"];
var ia2Color = ["#BD2000", "#FF5403", "#02A8A8", "#77ACF1", "#AA26DA"];
var eseColor = ["#8C0000", "#F90716", "#018383", "#04009A", "#851DE0"];

// horizontal bar chart 1
new Chart("barGraphSem1", {
  type: "horizontalBar",
  data: {
    labels: xValues,
    datasets: [
      {
        backgroundColor: ia1Color,
        data: ia1Values,
      },
      {
        backgroundColor: ia2Color,
        data: ia2Values,
      },
      {
        backgroundColor: eseColor,
        data: eseValues,
      },
    ],
  },
  options: {
    responsive: true,
    legend: { display: false },
    title: {
      position: "bottom",
      display: true,
      text: "Semester 1",
    },
    scales: {
      xAxes: [
        {
          stacked: true,
          ticks: { min: 0, max: 100 },
        },
      ],
      yAxes: [
        {
          display: false,
          stacked: true,
        },
      ],
    },
  },
});

// doughtnut 1
var xValues = [
  "Engg. Maths 1",
  "Engg. Physics 1",
  "Engg. Chemistry 1",
  "Basic Elec. Engg.",
  "Mechanics",
];
var yValues = [55, 49, 44, 24, 15];
var barColors = ["#8C0000", "#F90716", "#018383", "#04009A", "#851DE0"];

var stackedText = {
  id: "stackedText",
  afterDatasetsDraw(chart, args, options) {
    const {
      ctx,
      data,
      chartArea: { top, bottom, left, right, width, height },
    } = chart;
    ctx.save();
    ctx.font = "bolder 13px Arial";
    // ctx.fillStyle = localStorage.getItem('theme') == 'dark' ?"#e5e9f0":"#111318";
    ctx.textAlign = "center";
    ctx.fillText("5.56", (left + right) / 2, (bottom + top) / 2 - 5);
    ctx.restore();

    ctx.font = "bold 8px Arial";
    // ctx.fillStyle = localStorage.getItem('theme') == 'dark' ?"#e5e9f0":"#111318";
    ctx.textAlign = "center";
    ctx.fillText("CGPA", (left + right) / 2, (bottom + top) / 2 + 5);
  },
};

new Chart("donutGraphSem1", {
  type: "doughnut",
  data: {
    labels: xValues,
    datasets: [
      {
        backgroundColor: barColors,
        data: yValues,
      },
    ],
  },
  maintainAspectRatio: false,
  // legend: {
  //   display: true,
  //   position: "right",
  // },
  plugins: [stackedText],
});

// Sem 2
var xValues = [
  "Engg. Maths 2",
  "Engg. Physics 2",
  "Engg. Chemistry 2",
  "Pro. Comm. Ethics",
  "Engg. Drawing",
];
var ia1Values = [5, 8, 6, 8, 4];
var ia2Values = [7, 5, 8, 8, 6];
var eseValues = [56, 67, 65, 45, 60];

var ia1Color = ["#FA1E0E", "#FFCA03", "#42E6A4", "#3EDBF0", "#C355F5"];
var ia2Color = ["#BD2000", "#FF5403", "#02A8A8", "#77ACF1", "#AA26DA"];
var eseColor = ["#8C0000", "#F90716", "#018383", "#04009A", "#851DE0"];

// bar chart 2
new Chart("barGraphSem2", {
  type: "horizontalBar",
  data: {
    labels: xValues,
    datasets: [
      {
        backgroundColor: ia1Color,
        data: ia1Values,
      },
      {
        backgroundColor: ia2Color,
        data: ia2Values,
      },
      {
        backgroundColor: eseColor,
        data: eseValues,
      },
    ],
  },
  options: {
    responsive: true,
    legend: {
      display: false,
    },
    title: {
      position: "bottom",
      display: true,
      text: "Semester 2",
    },
    scales: {
      xAxes: [
        {
          stacked: true,
          ticks: { min: 0, max: 100 },
        },
      ],
      yAxes: [
        {
          display: false,
          stacked: true,
        },
      ],
    },
  },
});

var stackedText = {
  id: "stackedText",
  afterDatasetsDraw(chart, args, options) {
    const {
      ctx,
      data,
      chartArea: { top, bottom, left, right, width, height },
    } = chart;
    ctx.save();
    ctx.font = "bolder 13px Arial";
    // ctx.fillStyle = localStorage.getItem('theme') == 'dark' ?"#e5e9f0":"#111318";
    ctx.textAlign = "center";
    ctx.fillText("7.01", (left + right) / 2, (bottom + top) / 2 - 7);
    ctx.restore();

    ctx.font = "bold 12px Arial";
    // ctx.fillStyle = localStorage.getItem('theme') == 'dark' ?"#e5e9f0":"#111318";
    ctx.textAlign = "center";
    ctx.fillText("CGPA", (left + right) / 2, (bottom + top) / 2 + 7);
  },
};

// doughnut 2
var xValues = [
  "Engg. Maths 2",
  "Engg. Physics 2",
  "Engg. Chemistry 2",
  "Pro. Comm. Ethics",
  "Engg. Drawing",
];
var yValues = [56, 70, 80, 68, 55];
var barColors = ["#8C0000", "#F90716", "#018383", "#04009A", "#851DE0"];

new Chart("donutGraphSem2", {
  type: "doughnut",
  data: {
    labels: xValues,
    datasets: [
      {
        backgroundColor: barColors,
        data: yValues,
      },
    ],
  },
  maintainAspectRatio: false,
  legend: {
    display: false,
  },
  plugins: [stackedText],
});
