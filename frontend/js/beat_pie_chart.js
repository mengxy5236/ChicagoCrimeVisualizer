fetch("http://localhost:5000/api/crime_by_beat")
  .then(res => res.json())
  .then(data => {
    const width = 400;
    const height = 360;
    const radius = Math.min(width, height) / 2 - 20;

    const color = d3.scaleOrdinal()
      .domain(data.map(d => d.beat))
      .range(["#4c79ff", "#00bfff", "#8a2be2", "#6495ed", "#1e90ff"]);

    const svg = d3.select("#pie-beat-chart")
      .append("svg")
      .attr("width", width)
      .attr("height", height + 40)
      .append("g")
      .attr("transform", `translate(${width / 2},${height / 2})`);

    const pie = d3.pie()
      .value(d => d.count);

    const arc = d3.arc()
      .innerRadius(0)
      .outerRadius(radius);

    const arcs = svg.selectAll("arc")
      .data(pie(data))
      .join("g");

    arcs.append("path")
      .attr("d", arc)
      .attr("fill", d => color(d.data.beat))
      .attr("stroke", "white")
      .attr("stroke-width", "2px");

    // 添加文字标签：Beat + Count
    arcs.append("text")
      .attr("transform", d => `translate(${arc.centroid(d)})`)
      .attr("text-anchor", "middle")
      .attr("fill", "white")
      .style("font-size", "14px")
      .text(d => `${d.data.beat}区: ${d.data.count}`);
  });
