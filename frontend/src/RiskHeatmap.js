import React, { useRef, useEffect } from 'react';
import { Box, Typography, Paper } from '@mui/material';
import * as THREE from 'three';

const RiskHeatmap = () => {
  const mountRef = useRef(null);

  useEffect(() => {
    const mountElement = mountRef.current;
    if (!mountElement) return;
    // Scene setup
    const width = 600;
    const height = 350;
    const scene = new THREE.Scene();
    scene.background = new THREE.Color('#0a0a0a');
    const camera = new THREE.PerspectiveCamera(60, width / height, 0.1, 1000);
    camera.position.set(0, 0, 20);
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(width, height);
    mountElement.appendChild(renderer.domElement);

    // Create risk cubes
    const cubes = [];
    for (let i = 0; i < 12; i++) {
      const risk = Math.random();
      const color = risk > 0.7 ? '#ff00ff' : risk > 0.4 ? '#ffff00' : '#00ff00';
      const geometry = new THREE.BoxGeometry(2, 2, 2);
      const material = new THREE.MeshPhongMaterial({ color, emissive: color, transparent: true, opacity: 0.85 });
      const cube = new THREE.Mesh(geometry, material);
      cube.position.x = (i % 4) * 3 - 4.5;
      cube.position.y = Math.floor(i / 4) * 3 - 3;
      cube.userData = { risk, id: i };
      cubes.push(cube);
      scene.add(cube);
    }

    // Lighting
    const light = new THREE.PointLight('#00ffff', 2, 100);
    light.position.set(0, 0, 20);
    scene.add(light);

    // Animation
    let frame = 0;
    function animate() {
      frame++;
      cubes.forEach((cube, i) => {
        // Animate risk propagation
        cube.scale.z = 1 + Math.abs(Math.sin(frame / 40 + i)) * cube.userData.risk * 2;
        if (cube.userData.risk > 0.7 && frame % 60 < 30) {
          cube.material.emissive.set('#ff00ff');
        } else if (cube.userData.risk > 0.4) {
          cube.material.emissive.set('#ffff00');
        } else {
          cube.material.emissive.set('#00ff00');
        }
      });
      renderer.render(scene, camera);
      requestAnimationFrame(animate);
    }
    animate();

    // Cleanup
    return () => {
      if (mountElement && renderer.domElement) {
        mountElement.removeChild(renderer.domElement);
      }
    };
  }, []);

  return (
    <Paper elevation={8} sx={{ background: 'rgba(10,10,10,0.95)', borderRadius: 4, p: 2, boxShadow: '0 0 32px #00ffff44', backdropFilter: 'blur(8px)', mb: 3 }}>
      <Typography variant="h6" sx={{ color: '#00ffff', mb: 2, fontFamily: 'monospace' }}>Risk Heatmap</Typography>
      <Typography variant="body2" sx={{ color: '#fff', mb: 1 }}>
        This 3D heatmap shows risk levels for each service/module based on the last test run. Magenta = high risk, green = low risk. Use this to spot critical paths and areas needing attention.
      </Typography>
      <Box ref={mountRef} sx={{ width: 600, height: 350, mx: 'auto', borderRadius: 4, overflow: 'hidden', background: '#111' }} />
      <Box mt={2}>
        <Typography variant="body2" sx={{ color: '#fff' }}>Critical paths highlighted in magenta. Animated risk propagation. Drill-down by clicking cubes (to be implemented).</Typography>
      </Box>
    </Paper>
  );
};

export default RiskHeatmap; 