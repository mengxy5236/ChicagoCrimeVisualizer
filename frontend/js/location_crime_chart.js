fetch("http://localhost:5000/api/crime_by_location")
  .then(res => res.json())
  .then(data => {
    const width = 450;
    const height = 400;
    const radius = Math.min(width, height) / 2;

    const svg = d3.select("#pie-location-chart")
      .append("svg")
      .attr("width", width)
      .attr("height", height) // 多留空间显示下方文字
      .append("g")
      .attr("transform", `translate(${width / 2},${height / 2})`);

    const color = d3.scaleOrdinal()
      .domain(data.map(d => d.location))
      .range(["#4c79ff", "#00bfff", "#8a2be2", "#7b68ee", "#4682b4"]);

    const pie = d3.pie()
      .value(d => d.count);

    const arc = d3.arc()
      .innerRadius(0)
      .outerRadius(radius-10);

    const arcs = svg.selectAll("arc")
      .data(pie(data))
      .enter()
      .append("g");

    arcs.append("path")
      .attr("d", arc)
      .attr("fill", d => color(d.data.location));

    arcs.append("text")
      .attr("transform", d => `translate(${arc.centroid(d)})`)
      .attr("text-anchor", "middle")
      .attr("font-size", "12px")
      .style("fill", "white")  // 设置字体颜色为白色
      .text(d => d.data.location);
  });
