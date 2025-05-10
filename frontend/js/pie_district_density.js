fetch("http://localhost:5000/api/crime_density_by_district")
  .then(res => res.json())
  .then(data => {
    const width = 450;
    const height = 400;
    const radius = Math.min(width, height) / 2;

    const svg = d3.select("#pie-district-density-chart")
      .append("svg")
      .attr("width", width)
      .attr("height", height)
      .append("g")
      .attr("transform", `translate(${width / 2}, ${height / 2})`);

    const color = d3.scaleOrdinal()
      .domain(data.map(d => d.district))
      .range(["#1f77b4", "#5dade2", "#7d3c98", "#2874a6", "#48c9b0"]);

    const pie = d3.pie()
      .value(d => d.density);

    const arc = d3.arc()
      .innerRadius(0)
      .outerRadius(radius - 10);

    const arcs = svg.selectAll("path")
      .data(pie(data))
      .join("path")
      .attr("d", arc)
      .attr("fill", d => color(d.data.district))
      .attr("stroke", "#fff")
      .style("stroke-width", "2px");

    // 添加标签
    const labelArc = d3.arc().outerRadius(radius + 20).innerRadius(radius + 20);

    svg.selectAll("text")
  .data(pie(data))
  .join("text")
  .attr("transform", d => `translate(${arc.centroid(d)})`)
  .style("text-anchor", "middle")
  .style("font-size", "16px")
  .style("fill", "white")  // 设置白色字体更容易在深色扇形上可见
  .text(d => `D${d.data.district}`);
  });
