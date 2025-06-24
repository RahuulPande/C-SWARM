import React, { useEffect, useState } from 'react';
import { Box, Typography, Paper, LinearProgress, List, ListItem, ListItemText } from '@mui/material';
import { motion, useAnimation } from 'framer-motion';

const neon = {
  color: '#00ffff',
  textShadow: '0 0 8px #00ffff, 0 0 16px #00ffff',
};

const TestingDashboard: React.FC = () => {
  const [coverage, setCoverage] = useState(0);
  const [testsPerSec, setTestsPerSec] = useState(0);
  const [successRate, setSuccessRate] = useState([0.99]);
  const [failedTests, setFailedTests] = useState<string[]>([]);
  const [progress, setProgress] = useState(0);
  const [timeSaved, setTimeSaved] = useState(0);
  const controls = useAnimation();

  useEffect(() => {
    // Animate coverage
    controls.start({ coverage: 99.7, transition: { duration: 2 } });
    setTimeout(() => setCoverage(99.7), 2000);
    // Animate tests/sec
    let tps = 0;
    const tpsInterval = setInterval(() => {
      tps = Math.min(1000, tps + Math.random() * 200);
      setTestsPerSec(Math.floor(tps));
      if (tps >= 1000) clearInterval(tpsInterval);
    }, 80);
    // Animate progress
    let prog = 0;
    const progInterval = setInterval(() => {
      prog = Math.min(100, prog + Math.random() * 10);
      setProgress(prog);
      if (prog >= 100) clearInterval(progInterval);
    }, 120);
    // Animate time saved
    let ts = 0;
    const tsInterval = setInterval(() => {
      ts = Math.min(5000000, ts + Math.random() * 100000);
      setTimeSaved(ts);
      if (ts >= 5000000) clearInterval(tsInterval);
    }, 100);
    // Animate success rate
    let sr = 0.99;
    const srInterval = setInterval(() => {
      sr = Math.min(0.997, sr + Math.random() * 0.0005);
      setSuccessRate(s => [...s, sr]);
      if (sr >= 0.997) clearInterval(srInterval);
    }, 60);
    // Animate failed tests
    let fails = 0;
    const failInterval = setInterval(() => {
      if (fails < 5) {
        setFailedTests(f => [...f, `Test ${1000 + fails} failed`]);
        fails++;
      } else {
        clearInterval(failInterval);
      }
    }, 700);
    return () => {
      clearInterval(tpsInterval);
      clearInterval(progInterval);
      clearInterval(tsInterval);
      clearInterval(srInterval);
      clearInterval(failInterval);
    };
  }, [controls]);

  return (
    <Paper elevation={8} sx={{ background: 'rgba(10,10,10,0.95)', borderRadius: 4, p: 2, boxShadow: '0 0 32px #00ffff44', backdropFilter: 'blur(8px)', mb: 3 }}>
      <Typography variant="h6" sx={{ ...neon, mb: 2, fontFamily: 'monospace' }}>Testing Dashboard</Typography>
      <Box display="flex" gap={4} alignItems="center" mb={2}>
        <Box>
          <Typography variant="body2" sx={{ color: '#fff', mb: 1 }}>Test Coverage</Typography>
          <motion.div animate={{ scale: [1, 1.1, 1] }} transition={{ repeat: Infinity, duration: 2 }}>
            <Typography variant="h3" sx={{ ...neon }}>{coverage.toFixed(1)}%</Typography>
          </motion.div>
        </Box>
        <Box>
          <Typography variant="body2" sx={{ color: '#fff', mb: 1 }}>Tests/sec</Typography>
          <motion.div animate={{ scale: [1, 1.1, 1] }} transition={{ repeat: Infinity, duration: 1.5 }}>
            <Typography variant="h3" sx={{ color: '#00ff00', textShadow: '0 0 8px #00ff00' }}>{testsPerSec}</Typography>
          </motion.div>
        </Box>
        <Box>
          <Typography variant="body2" sx={{ color: '#fff', mb: 1 }}>Time Saved</Typography>
          <Typography variant="h5" sx={{ color: '#ff00ff', textShadow: '0 0 8px #ff00ff' }}>
            ${Math.floor(timeSaved).toLocaleString()}
          </Typography>
        </Box>
        <Box flex={1}>
          <Typography variant="body2" sx={{ color: '#fff', mb: 1 }}>Test Generation Progress</Typography>
          <LinearProgress variant="determinate" value={progress} sx={{ height: 10, borderRadius: 5, background: '#222', '& .MuiLinearProgress-bar': { background: 'linear-gradient(90deg,#00ffff,#ff00ff,#00ff00)' } }} />
        </Box>
      </Box>
      <Box mb={2}>
        <Typography variant="body2" sx={{ color: '#fff', mb: 1 }}>Success Rate</Typography>
        <svg width={300} height={60} style={{ background: 'rgba(0,0,0,0.2)', borderRadius: 8 }}>
          <polyline
            fill="none"
            stroke="#00ff00"
            strokeWidth={3}
            points={successRate.map((v, i) => `${i * 10},${60 - v * 60}` ).join(' ')}
          />
        </svg>
      </Box>
      <Box>
        <Typography variant="body2" sx={{ color: '#fff', mb: 1 }}>Failed Tests</Typography>
        <List dense sx={{ maxHeight: 100, overflow: 'auto', background: 'rgba(20,20,20,0.7)', borderRadius: 2 }}>
          {failedTests.map((fail, i) => (
            <ListItem key={i} sx={{ color: '#ff00ff' }}>
              <ListItemText primary={fail} />
            </ListItem>
          ))}
        </List>
      </Box>
    </Paper>
  );
};

export default TestingDashboard; 