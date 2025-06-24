import React, { useRef, useEffect } from 'react';
import { Box, Typography, Paper } from '@mui/material';
import * as d3 from 'd3';

const baseServices = [
  'account', 'payment', 'risk', 'compliance', 'trading', 'customer', 'ledger', 'notification', 'fx', 'reporting', 'auth', 'audit'
];

const baseLinks = [
  { source: 'account', target: 'customer' },
  { source: 'account', target: 'ledger' },
  { source: 'payment', target: 'account' },
  { source: 'payment', target: 'fx' },
  { source: 'risk', target: 'trading' },
  { source: 'compliance', target: 'risk' },
  { source: 'trading', target: 'ledger' },
  { source: 'customer', target: 'auth' },
  { source: 'ledger', target: 'reporting' },
  { source: 'notification', target: 'customer' },
  { source: 'fx', target: 'account' },
  { source: 'reporting', target: 'audit' },
  { source: 'auth', target: 'compliance' },
  { source: 'audit', target: 'compliance' },
];

const ServiceMeshVisualizer = ({ testing }) => {
  const ref = useRef();

  useEffect(() => {
    const width = 600;
    const height = 350;
    const svg = d3.select(ref.current)
      .attr('width', width)
      .attr('height', height)
      .style('background', '#111')
      .style('borderRadius', '16px');
    svg.selectAll('*').remove();

    // Deep copy to avoid mutating original arrays
    const services = baseServices.map(s => ({ id: s }));
    const links = baseLinks.map(l => ({ ...l }));

    const color = d3.scaleOrdinal(d3.schemeCategory10);
    const highlightColor = '#ff00ff';

    const simulation = d3.forceSimulation(services)
      .force('link', d3.forceLink(links).id(d => d.id).distance(90))
      .force('charge', d3.forceManyBody().strength(-400))
      .force('center', d3.forceCenter(width / 2, height / 2));

    const link = svg.append('g')
      .attr('stroke', '#00ffff')
      .attr('stroke-width', 2)
      .selectAll('line')
      .data(links)
      .enter().append('line')
      .attr('stroke', d => testing ? highlightColor : '#00ffff')
      .attr('stroke-width', d => testing ? 4 : 2)
      .attr('opacity', 0.7);

    const node = svg.append('g')
      .selectAll('circle')
      .data(services)
      .enter().append('circle')
      .attr('r', 22)
      .attr('fill', d => testing ? highlightColor : color(d.id))
      .attr('stroke', '#fff')
      .attr('stroke-width', 2)
      .call(d3.drag()
        .on('start', dragstarted)
        .on('drag', dragged)
        .on('end', dragended));

    const label = svg.append('g')
      .selectAll('text')
      .data(services)
      .enter().append('text')
      .text(d => d.id)
      .attr('fill', '#fff')
      .attr('font-size', 13)
      .attr('font-family', 'monospace')
      .attr('text-anchor', 'middle')
      .attr('dy', 5);

    simulation.on('tick', () => {
      link
        .attr('x1', d => d.source.x)
        .attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x)
        .attr('y2', d => d.target.y);
      node
        .attr('cx', d => d.x)
        .attr('cy', d => d.y);
      label
        .attr('x', d => d.x)
        .attr('y', d => d.y);
    });

    function dragstarted(event, d) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }
    function dragged(event, d) {
      d.fx = event.x;
      d.fy = event.y;
    }
    function dragended(event, d) {
      if (!event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    }
    return () => simulation.stop();
  }, [testing]);

  return (
    <Paper elevation={8} sx={{ background: 'rgba(10,10,10,0.95)', borderRadius: 4, p: 2, boxShadow: '0 0 32px #00ffff44', backdropFilter: 'blur(8px)', mb: 3 }}>
      <Typography variant="h6" sx={{ color: '#00ffff', mb: 2, fontFamily: 'monospace' }}>Service Mesh Visualizer</Typography>
      <Typography variant="body2" sx={{ color: '#fff', mb: 1 }}>
        This graph shows all microservices and their dependencies. Use it to understand the flow of data and spot critical connections. When testing starts, the mesh animates to highlight the active path.
      </Typography>
      <Box mb={1}>
        <Typography variant="caption" sx={{ color: '#00ffff', mr: 2 }}>Cyan: Normal</Typography>
        <Typography variant="caption" sx={{ color: '#ff00ff', mr: 2 }}>Magenta: Active/Tested</Typography>
      </Box>
      <Box sx={{ width: 600, height: 350, mx: 'auto', borderRadius: 4, overflow: 'hidden', background: '#111' }}>
        <svg ref={ref} />
      </Box>
    </Paper>
  );
};

export default ServiceMeshVisualizer; 