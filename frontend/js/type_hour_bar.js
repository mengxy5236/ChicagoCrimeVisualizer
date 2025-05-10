fetch("http://localhost:5000/api/type_hour_bar")
  .then(res => res.json())
  .then(data => {
    const width = 800;
    const height = 400;
    const margin = { top: 20, right: 30, bottom: 40, left: 60 };

    const svg = d3.select("#bar-type-hour-chart")
      .append("svg")
      .attr("width", width)
      .attr("height", height);

    const types = Object.keys(data[0]).filter(k => k !== "hour");
    const x = d3.scaleBand()
      .domain(data.map(d => d.hour))
      .range([margin.left, width - margin.right])
      .padding(0.1);

    const y = d3.scaleLinear()
      .domain([0, d3.max(data, d => d3.sum(types, t => d[t]))])
      .nice()
      .range([height - margin.bottom, margin.top]);

    const color = d3.scaleOrdinal()
      .domain(types)
      .range([
        "#2A3D66", // 深蓝色
        "#4C6B8B", // 中等蓝色
        "#6A8FBF", // 浅蓝色
        "#8DA6D9", // 非常浅的蓝色
        "#B7C5E3"  // 最浅的蓝色
      ]);

    const stack = d3.stack()
      .keys(types)
      (data);

    svg.append("g")
      .selectAll("g")
      .data(stack)
      .join("g")
      .attr("fill", d => color(d.key))
      .selectAll("rect")
      .data(d => d)
      .join("rect")
      .attr("x", d => x(d.data.hour))
      .attr("y", d => y(d[1]))
      .attr("height", d => y(d[0]) - y(d[1]))
      .attr("width", x.bandwidth());

    svg.append("g")
      .attr("transform", `translate(0,${height - margin.bottom})`)
      .call(d3.axisBottom(x).tickFormat(d => `${d}时`));

    svg.append("g")
      .attr("transform", `translate(${margin.left},0)`)
      .call(d3.axisLeft(y));

    // 图例
    const legend = svg.append("g")
      .attr("transform", `translate(${width - margin.right - 100}, ${margin.top})`);

    types.forEach((t, i) => {
      const g = legend.append("g").attr("transform", `translate(0,${i * 20})`);
      g.append("rect").attr("width", 12).attr("height", 12).attr("fill", color(t));
      g.append("text").text(t).attr("x", 16).attr("y", 10).style("font-size", "12px");
        
    });
  });
