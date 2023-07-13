// Load the map data from map.json
d3.json("map.json").then(function(mapData) {
    // Create the SVG container
    var svg = d3.select("#map")
      .append("svg")
      .attr("width", "100%")
      .attr("height", "100%");
  
    // Create a path generator using a projection
    var path = d3.geoPath();
  
    // Render the map features
    svg.selectAll("path")
      .data(mapData.features)
      .enter()
      .append("path")
      .attr("d", path)
      .style("fill", "lightgray")
      .style("stroke", "white")
      .style("stroke-width", "0.5px");
  });
  