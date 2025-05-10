fetch("http://localhost:5000/api/crime_by_district")
  .then(res => res.json())
  .then(data => {
    const width = 800;
    const height = 400;
    const margin = { top: 20, right: 30, bottom: 60, left: 60 };

    const svg = d3.select("#bar-district-chart")
      .append("svg")
      .attr("width", width)
      .attr("height", height);

    const x = d3.scaleBand()
      .domain(data.map(d => d.district))
      .range([margin.left, width - margin.right])
      .padding(0.5);

    const y = d3.scaleLinear()
      .domain([0, 100])
      .nice()
      .range([height - margin.bottom, margin.top]);

    svg.append("g")
      .attr("fill", "#34495E")
      .selectAll("rect")
      .data(data)
      .join("rect")
      .attr("x", d => x(d.district))
      .attr("y", d => y(d.arrest_rate))
      .attr("height", d => y(0) - y(d.arrest_rate))
      .attr("width", x.bandwidth());

    // x轴
    const xAxis = svg.append("g")
      .attr("transform", `translate(0,${height - margin.bottom})`)
      .call(d3.axisBottom(x));

    // 在x轴标签后面加上“区”
    xAxis.selectAll("text")
      .text(d => `${d}区`);

    svg.append("g")
      .attr("transform", `translate(${margin.left},0)`)
      .call(d3.axisLeft(y));
  });
