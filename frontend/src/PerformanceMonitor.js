import React, { useEffect, useState } from 'react';
import { Box, Typography, Paper } from '@mui/material';
import { motion } from 'framer-motion';

const services = ['account', 'payment', 'risk', 'compliance', 'trading', 'customer', 'ledger', 'notification', 'fx', 'reporting', 'auth', 'audit'];

const PerformanceMonitor = () => {
  const [latencies, setLatencies] = useState(Array(12).fill(100));
  const [throughput, setThroughput] = useState(Array(12).fill(100));
  const [errorRates, setErrorRates] = useState(Array(12).fill(0.01));
  const [bottleneck, setBottleneck] = useState(0);

  useEffect(() => {
    // This animation is currently mock/random. With real data, update these states from backend.
    const interval = setInterval(() => {
      setLatencies(l => l.map(() => 80 + Math.random() * 120));
      setThroughput(t => t.map(() => 80 + Math.random() * 200));
      setErrorRates(e => e.map(() => Math.random() * 0.05));
      setBottleneck(Math.floor(Math.random() * 12));
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <Paper elevation={8} sx={{ background: 'rgba(10,10,10,0.95)', borderRadius: 4, p: 2, boxShadow: '0 0 32px #00ffff44', backdropFilter: 'blur(8px)', mb: 3 }}>
      <Typography variant="h6" sx={{ color: '#00ffff', mb: 2, fontFamily: 'monospace' }}>Performance Monitor</Typography>
      <Typography variant="body2" sx={{ color: '#fff', mb: 1 }}>
        This panel shows real-time latency, throughput, and error rates for all microservices involved in the selected flow. Use it to spot slowdowns, bottlenecks, and reliability issues.
      </Typography>
      <Box display="flex" gap={2}>
        <Box flex={1}>
          <Typography variant="body2" sx={{ color: '#fff', mb: 1 }}>Latency Heatmap (ms)</Typography>
          <Box sx={{ display: 'flex', gap: 1, alignItems: 'end', overflowX: 'auto', minWidth: 350 }}>
            {latencies.map((lat, i) => (
              <Box key={i} display="flex" flexDirection="column" alignItems="center">
                <motion.div animate={{ background: i === bottleneck ? '#ff00ff' : `rgba(0,255,255,${1 - lat / 300})` }} style={{ width: 24, height: 60, borderRadius: 6, margin: 2, display: 'flex', alignItems: 'flex-end', justifyContent: 'center' }}>
                  <Typography variant="caption" sx={{ color: '#fff' }}>{Math.round(lat)}</Typography>
                </motion.div>
                <Typography variant="caption" sx={{ color: '#00ffff' }}>{services[i].toUpperCase()}</Typography>
              </Box>
            ))}
          </Box>
        </Box>
        <Box flex={1}>
          <Typography variant="body2" sx={{ color: '#fff', mb: 1 }}>Throughput</Typography>
          <Box sx={{ display: 'flex', gap: 1, alignItems: 'end', overflowX: 'auto', minWidth: 350 }}>
            {throughput.map((tp, i) => (
              <Box key={i} display="flex" flexDirection="column" alignItems="center">
                <motion.div animate={{ height: tp / 2, background: '#00ff00' }} style={{ width: 24, borderRadius: 6, margin: 2, display: 'flex', alignItems: 'flex-end', justifyContent: 'center' }}>
                  <Typography variant="caption" sx={{ color: '#111' }}>{Math.round(tp)}</Typography>
                </motion.div>
                <Typography variant="caption" sx={{ color: '#00ff00' }}>{services[i].toUpperCase()}</Typography>
              </Box>
            ))}
          </Box>
        </Box>
        <Box flex={1}>
          <Typography variant="body2" sx={{ color: '#fff', mb: 1 }}>Error Rate</Typography>
          <Box sx={{ display: 'flex', gap: 1, alignItems: 'end', overflowX: 'auto', minWidth: 350 }}>
            {errorRates.map((er, i) => (
              <Box key={i} display="flex" flexDirection="column" alignItems="center">
                <motion.div animate={{ height: Math.min(er * 200 + 10, 70), background: er > 0.03 ? '#ff00ff' : '#00ffff' }} style={{ width: 24, borderRadius: 6, margin: 2, display: 'flex', alignItems: 'flex-end', justifyContent: 'center' }}>
                  <Typography variant="caption" sx={{ color: '#111' }}>{(er * 100).toFixed(1)}%</Typography>
                </motion.div>
                <Typography variant="caption" sx={{ color: '#ff00ff' }}>{services[i].toUpperCase()}</Typography>
              </Box>
            ))}
          </Box>
        </Box>
        <Box flex={1}>
          <Typography variant="body2" sx={{ color: '#fff', mb: 1 }}>Bottleneck</Typography>
          <Box display="flex" gap={1}>
            {services.map((svc, i) => (
              <Box key={i} sx={{ width: 24, height: 24, borderRadius: 6, background: i === bottleneck ? '#ff00ff' : '#222', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                <Typography variant="caption" sx={{ color: '#fff', fontWeight: i === bottleneck ? 'bold' : 'normal' }}>{svc.charAt(0).toUpperCase()}</Typography>
              </Box>
            ))}
          </Box>
        </Box>
      </Box>
    </Paper>
  );
};

export default PerformanceMonitor; 