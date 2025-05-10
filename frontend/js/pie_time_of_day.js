fetch("http://localhost:5000/api/crime_by_time_of_day")
  .then(res => res.json())
  .then(data => {
    // 转换 count 为数字
    data.forEach(d => d.count = +d.count);

    const width = 800;
    const height = 400;
    const margin = { top: 20, right: 30, bottom: 40, left: 50 };

    const svg = d3.select("#pie-time-of-day-chart")
      .append("svg")
      .attr("width", width)
      .attr("height", height);

    const radius = Math.min(width, height) / 2 - margin.top;

    // 使用三种颜色：蓝色、橙色、绿色
    const color = d3.scaleOrdinal()
      .domain(data.map(d => d.time_of_day))  // 以时间为依据
      .range(["#4c79ff", "#00bfff", "#8a2be2"]);  // 蓝色，橙色，绿色

    const pie = d3.pie()
      .value(d => d.count)
      .sort(null);  // 保持原始顺序

    const arc = d3.arc()
      .outerRadius(radius)
      .innerRadius(0);

    const labelArc = d3.arc()
      .outerRadius(radius - 40)
      .innerRadius(radius - 40);

    svg.append("g")
      .attr("transform", `translate(${width / 2},${height / 2})`)
      .selectAll(".arc")
      .data(pie(data))
      .join("g")
      .attr("class", "arc")
      .append("path")
      .attr("d", arc)
      .attr("fill", (d, i) => color(d.data.time_of_day));  // 使用三种颜色

    // 外部标签
    svg.append("g")
      .attr("transform", `translate(${width / 2},${height / 2})`)
      .selectAll(".arc")
      .data(pie(data))
      .join("g")
      .attr("class", "arc")
      .append("text")
      .attr("transform", d => `translate(${labelArc.centroid(d)})`)
      .attr("dy", ".35em")
      .attr("text-anchor", "middle")
      .text(d => d.data.time_of_day + "时")  // 添加“时”字
      .style("font-size", "14px")
      .style("fill", "#fff");
  });
