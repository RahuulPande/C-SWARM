import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';
import { Box, Typography, Paper } from '@mui/material';

interface Node {
  id: string;
  name: string;
  status: 'healthy' | 'testing' | 'failing';
  importance: number;
}

interface Edge {
  source: string;
  target: string;
  traffic: number;
}

interface ServiceMeshVisualizerProps {
  nodes: Node[];
  edges: Edge[];
  focusNodeId?: string;
  onNodeClick?: (node: Node) => void;
}

const statusColor = {
  healthy: '#00ff00',
  testing: '#00ffff',
  failing: '#ff00ff',
};

const ServiceMeshVisualizer: React.FC<ServiceMeshVisualizerProps> = ({ nodes, edges, focusNodeId, onNodeClick }) => {
  const ref = useRef<SVGSVGElement>(null);

  useEffect(() => {
    if (!ref.current) return;
    const width = 800;
    const height = 500;
    d3.select(ref.current).selectAll('*').remove();
    const svg = d3.select(ref.current)
      .attr('width', width)
      .attr('height', height)
      .style('background', 'rgba(10,10,10,0.95)')
      .style('borderRadius', '24px')
      .style('backdropFilter', 'blur(8px)')
      .style('boxShadow', '0 0 32px #00ffff44');

    const simulation = d3.forceSimulation(nodes as any)
      .force('link', d3.forceLink(edges as any).id((d: any) => d.id).distance(180))
      .force('charge', d3.forceManyBody().strength(-600))
      .force('center', d3.forceCenter(width / 2, height / 2));

    // Draw links
    const link = svg.append('g')
      .attr('stroke', '#fff2')
      .selectAll('line')
      .data(edges)
      .enter().append('line')
      .attr('stroke-width', d => Math.max(2, d.traffic / 20))
      .attr('stroke', '#00ffff88');

    // Draw nodes
    const node = svg.append('g')
      .selectAll('circle')
      .data(nodes)
      .enter().append('circle')
      .attr('r', d => 24 + d.importance * 8)
      .attr('fill', d => statusColor[d.status])
      .attr('stroke', d => focusNodeId === d.id ? '#fff' : '#222')
      .attr('stroke-width', d => focusNodeId === d.id ? 4 : 2)
      .style('filter', 'drop-shadow(0 0 12px #00ffff)')
      .on('mouseover', function (event, d) {
        d3.select(this).attr('stroke', '#fff').attr('stroke-width', 4);
        // Tooltip
        svg.append('text')
          .attr('id', 'hover-label')
          .attr('x', d.x)
          .attr('y', d.y - 30)
          .attr('text-anchor', 'middle')
          .attr('fill', '#fff')
          .attr('font-size', 18)
          .attr('font-family', 'monospace')
          .text(`${d.name} (${d.status})`);
      })
      .on('mouseout', function (event, d) {
        d3.select(this).attr('stroke', focusNodeId === d.id ? '#fff' : '#222').attr('stroke-width', focusNodeId === d.id ? 4 : 2);
        svg.select('#hover-label').remove();
      })
      .on('click', function (event, d) {
        if (onNodeClick) onNodeClick(d);
      });

    // Animate particles on edges
    const particleCount = 30;
    const particles = Array.from({ length: particleCount }, () => ({ t: Math.random(), edge: edges[Math.floor(Math.random() * edges.length)] }));
    const particleGroup = svg.append('g');

    function animateParticles() {
      particleGroup.selectAll('circle').remove();
      particles.forEach(p => {
        p.t += 0.01 + Math.random() * 0.01;
        if (p.t > 1) {
          p.t = 0;
          p.edge = edges[Math.floor(Math.random() * edges.length)];
        }
        const source = nodes.find(n => n.id === p.edge.source);
        const target = nodes.find(n => n.id === p.edge.target);
        if (source && target) {
          const x = source.x + (target.x - source.x) * p.t;
          const y = source.y + (target.y - source.y) * p.t;
          particleGroup.append('circle')
            .attr('cx', x)
            .attr('cy', y)
            .attr('r', 4)
            .attr('fill', '#00ffff')
            .attr('opacity', 0.7);
        }
      });
    }

    simulation.on('tick', () => {
      link
        .attr('x1', d => (d.source as any).x)
        .attr('y1', d => (d.source as any).y)
        .attr('x2', d => (d.target as any).x)
        .attr('y2', d => (d.target as any).y);
      node
        .attr('cx', d => (d as any).x)
        .attr('cy', d => (d as any).y);
      animateParticles();
    });

    return () => {
      simulation.stop();
    };
  }, [nodes, edges, focusNodeId, onNodeClick]);

  return (
    <Paper elevation={8} sx={{ background: 'rgba(10,10,10,0.95)', borderRadius: 4, p: 2, boxShadow: '0 0 32px #00ffff44', backdropFilter: 'blur(8px)' }}>
      <Typography variant="h6" sx={{ color: '#00ffff', mb: 2, fontFamily: 'monospace' }}>Service Mesh Visualizer</Typography>
      <Box display="flex" justifyContent="center">
        <svg ref={ref} style={{ width: 800, height: 500, display: 'block' }} />
      </Box>
    </Paper>
  );
};

export default ServiceMeshVisualizer; 