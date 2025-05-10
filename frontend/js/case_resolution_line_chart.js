fetch("http://localhost:5000/api/case_resolution_time_by_year")
  .then(res => res.json())
  .then(data => {
    const width = 800;
    const height = 400;
    const margin = { top: 20, right: 30, bottom: 60, left: 60 };

    const svg = d3.select("#line-case-resolution-chart")
      .append("svg")
      .attr("width", width)
      .attr("height", height);

    const x = d3.scaleLinear()
      .domain(d3.extent(data, d => d.year))
      .range([margin.left, width - margin.right]);

    const y = d3.scaleLinear()
      .domain([0, d3.max(data, d => d.avg_days)])
      .nice()
      .range([height - margin.bottom, margin.top]);

    const line = d3.line()
      .x(d => x(d.year))
      .y(d => y(d.avg_days));

    svg.append("path")
      .datum(data)
      .attr("fill", "none")
      .attr("stroke", "#4c79ff")
      .attr("stroke-width", 2)
      .attr("d", line);

    svg.append("g")
      .attr("transform", `translate(0,${height - margin.bottom})`)
      .call(d3.axisBottom(x).tickFormat(d3.format("d")));

    svg.append("g")
      .attr("transform", `translate(${margin.left},0)`)
      .call(d3.axisLeft(y));

    
  });
