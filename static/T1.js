const initCharts = async () => {
  const chart1 = echarts.init(document.getElementById("chart1"));
  const chart2 = echarts.init(document.getElementById("chart2"));

  // Dados reais (substitua pelos seus dados)
  const responseOrigem = await fetch("http://127.0.0.1:5000/api/origem/data");
  const dataOrigem = await responseOrigem.json();
  console.log(dataOrigem);

  const responseDestino = await fetch("http://127.0.0.1:5000/api/destino/data");
  const dataDestino = await responseDestino.json();
  console.log(dataDestino);

  const opcoesChart1 = {
    xAxis: {
      type: "category",
      data: dataOrigem.map((item) => {
        return item[0];
      }),
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        name: "Repetições",
        type: "bar",
        data: dataOrigem.map((item) => {
          return item[1];
        }),
      },
    ],
  };

  const opcoesChart2 = {
    xAxis: {
      type: "category",
      data: dataDestino.map((item) => {
        return item[0];
      }),
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        name: "Repetições",
        type: "bar",
        data: dataDestino.map((item) => {
          return item[1];
        }),
      },
    ],
  };


  chart1.setOption(opcoesChart1);
  chart2.setOption(opcoesChart2);
};

export default initCharts;
