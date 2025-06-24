import React, { useState } from 'react';
import { Box, Typography, Paper, Table, TableBody, TableCell, TableHead, TableRow, Tooltip } from '@mui/material';
import { motion } from 'framer-motion';

const fieldMappings = [
  { cs: 'Account Number', ubs: 'IBAN', status: 'mapped', logic: 'CS 16-digit → UBS IBAN' },
  { cs: 'Customer Name', ubs: 'Holder Name', status: 'mapped', logic: 'Direct copy' },
  { cs: 'Currency', ubs: 'Currency', status: 'mapped', logic: 'Direct copy' },
  { cs: 'Balance', ubs: 'Balance', status: 'partial', logic: 'Format normalization' },
  { cs: 'Risk Score', ubs: 'Risk Category', status: 'incompatible', logic: 'Requires transformation' },
];

const statusColor = {
  mapped: '#00ff00',
  partial: '#ffff00',
  incompatible: '#ff00ff',
};

const HarmonizationMatrix = () => {
  const [selected, setSelected] = useState(null);
  const [progress, setProgress] = useState(0);

  React.useEffect(() => {
    let prog = 0;
    const interval = setInterval(() => {
      prog = Math.min(100, prog + Math.random() * 10);
      setProgress(prog);
      if (prog >= 100) clearInterval(interval);
    }, 120);
    return () => clearInterval(interval);
  }, []);

  return (
    <Paper elevation={8} sx={{ background: 'rgba(10,10,10,0.95)', borderRadius: 4, p: 2, boxShadow: '0 0 32px #00ffff44', backdropFilter: 'blur(8px)', mb: 3 }}>
      <Typography variant="h6" sx={{ color: '#00ffff', mb: 2, fontFamily: 'monospace' }}>Harmonization Matrix</Typography>
      <Typography variant="body2" sx={{ color: '#fff', mb: 1 }}>
        This matrix helps you map fields between two services or data models. Click a cell to map a field from System A to System B. Green = mapped, gray = unmapped. Use this to ensure data consistency across systems.
      </Typography>
      <Box mb={1}>
        <Typography variant="caption" sx={{ color: '#00ff00', mr: 2 }}>Green: Mapped</Typography>
        <Typography variant="caption" sx={{ color: '#888', mr: 2 }}>Gray: Unmapped</Typography>
      </Box>
      <Box mb={2}>
        <motion.div animate={{ width: `${progress}%` }} style={{ height: 10, background: 'linear-gradient(90deg,#00ffff,#ff00ff,#00ff00)', borderRadius: 5, marginBottom: 8 }} />
        <Typography variant="body2" sx={{ color: '#fff' }}>Progress: {progress.toFixed(1)}%</Typography>
      </Box>
      <Table sx={{ background: 'rgba(20,20,20,0.7)', borderRadius: 2 }}>
        <TableHead>
          <TableRow>
            <TableCell sx={{ color: '#00ffff', fontWeight: 'bold' }}>CS Field</TableCell>
            <TableCell sx={{ color: '#00ffff', fontWeight: 'bold' }}>UBS Field</TableCell>
            <TableCell sx={{ color: '#00ffff', fontWeight: 'bold' }}>Status</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {fieldMappings.map((row, i) => (
            <Tooltip key={i} title={row.logic} arrow placement="top">
              <TableRow
                hover
                onClick={() => setSelected(i)}
                sx={{ cursor: 'pointer', background: selected === i ? '#222' : 'inherit' }}
              >
                <TableCell sx={{ color: '#fff' }}>{row.cs}</TableCell>
                <TableCell sx={{ color: '#fff' }}>{row.ubs}</TableCell>
                <TableCell sx={{ color: statusColor[row.status], fontWeight: 'bold' }}>
                  {row.status.charAt(0).toUpperCase() + row.status.slice(1)}
                </TableCell>
              </TableRow>
            </Tooltip>
          ))}
        </TableBody>
      </Table>
      {selected !== null && (
        <Box mt={2} p={2} sx={{ background: '#111', borderRadius: 2, color: '#fff', boxShadow: '0 0 16px #00ffff44' }}>
          <Typography variant="body2">Transformation Logic:</Typography>
          <Typography variant="body1" sx={{ color: '#00ffff' }}>{fieldMappings[selected].logic}</Typography>
        </Box>
      )}
      <Box mt={2}>
        <Typography variant="body2" sx={{ color: '#fff' }}>Summary: {fieldMappings.filter(f => f.status === 'mapped').length} mapped, {fieldMappings.filter(f => f.status === 'partial').length} partial, {fieldMappings.filter(f => f.status === 'incompatible').length} incompatible</Typography>
      </Box>
    </Paper>
  );
};

export default HarmonizationMatrix; 