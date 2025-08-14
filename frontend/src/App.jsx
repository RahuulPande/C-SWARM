import React, { useState, useEffect } from 'react';
import { Box, CssBaseline, AppBar, Toolbar, Typography, Tabs, Tab, Button, Select, MenuItem, FormControl, InputLabel, Paper, Chip, IconButton, Dialog, DialogTitle, DialogContent, DialogContentText, DialogActions, Tooltip, Divider } from '@mui/material';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';
import ServiceMeshVisualizer from './ServiceMeshVisualizer.js';
import TestingDashboard from './TestingDashboard.js';
import HarmonizationMatrix from './HarmonizationMatrix.js';
import PerformanceMonitor from './PerformanceMonitor.js';
import RiskHeatmap from './RiskHeatmap.js';

const neon = {
  color: '#00ffff',
  textShadow: '0 0 8px #00ffff, 0 0 16px #00ffff',
};

const scenarios = [
  { label: 'Cross-Border Payment Test', value: 'payment_flow' },
  { label: 'Risk Calculation Storm', value: 'risk_storm' },
  { label: 'Complete System Harmonization', value: 'full_harmonization' },
];

const businessValue = [
  { label: 'Test Coverage', value: '99.7%' },
  { label: 'Faster Integration', value: '3x' },
  { label: 'Risk Mitigation', value: '$5M+' },
  { label: 'Compliance Ready', value: 'Yes' },
];

const scenarioConfig = {
  payment_flow: { testCount: 1200, serviceCount: 7, flowName: 'Cross-Border Payment Test' },
  risk_storm: { testCount: 2000, serviceCount: 9, flowName: 'Risk Calculation Storm' },
  full_harmonization: { testCount: 1500, serviceCount: 12, flowName: 'Complete System Harmonization' },
};

const App = () => {
  const [tab, setTab] = useState(0);
  const [wsConnected, setWsConnected] = useState(false);
  const [scenario, setScenario] = useState('payment_flow');
  const [testing, setTesting] = useState(false);
  const [helpOpen, setHelpOpen] = useState(false);

  useEffect(() => {
    // WebSocket connection indicator - Demo mode for Vercel deployment
    let ws = null;
    function connect() {
      // Check if we're in production (Vercel) or development
      const isProduction = window.location.hostname !== 'localhost';
      
      if (isProduction) {
        // Demo mode - simulate WebSocket connection
        setWsConnected(true);
        // Simulate real-time updates for demo
        const interval = setInterval(() => {
          // Simulate test results for demo
          if (testing) {
            // This will be handled by the testing state
          }
        }, 2000);
        return () => clearInterval(interval);
      } else {
        // Development mode - real WebSocket
        ws = new window.WebSocket('ws://localhost:8001/ws');
        ws.onopen = () => setWsConnected(true);
        ws.onclose = () => setWsConnected(false);
        ws.onerror = () => setWsConnected(false);
      }
    }
    connect();
    return () => { ws && ws.close(); };
  }, [testing]);

  return (
    <Box sx={{ minHeight: '100vh', background: '#0a0a0a', pb: 6 }}>
      <CssBaseline />
      <AppBar position="static" sx={{ background: 'rgba(10,10,10,0.95)', boxShadow: '0 0 32px #00ffff44', backdropFilter: 'blur(8px)' }}>
        <Toolbar>
          <Typography variant="h5" sx={{ ...neon, flexGrow: 1, fontFamily: 'monospace' }}>
            UBS-CS Integration Control Tower
          </Typography>
          <Chip label={wsConnected ? 'WebSocket: Connected' : 'WebSocket: Disconnected'} sx={{ background: wsConnected ? '#00ff00' : '#ff00ff', color: '#111', fontWeight: 'bold', mr: 2 }} />
          <FormControl variant="outlined" size="small" sx={{ minWidth: 220, mr: 2 }}>
            <InputLabel sx={{ color: '#00ffff' }}>Scenario</InputLabel>
            <Select
              value={scenario}
              onChange={e => setScenario(e.target.value)}
              label="Scenario"
              sx={{ color: '#00ffff', '.MuiOutlinedInput-notchedOutline': { borderColor: '#00ffff' } }}
            >
              {scenarios.map(s => <MenuItem key={s.value} value={s.value}>{s.label}</MenuItem>)}
            </Select>
          </FormControl>
          <Button
            variant="contained"
            sx={{ background: testing ? '#ff00ff' : 'linear-gradient(90deg,#00ffff,#ff00ff,#00ff00)', color: '#111', fontWeight: 'bold', boxShadow: '0 0 16px #00ffff44', mr: 2 }}
            onClick={() => setTesting(t => !t)}
          >
            {testing ? 'Stop Testing' : 'Start Testing'}
          </Button>
          <Button
            variant="outlined"
            sx={{ color: '#00ffff', borderColor: '#00ffff', fontWeight: 'bold', mr: 2 }}
            onClick={() => document.documentElement.requestFullscreen()}
          >
            Full Screen
          </Button>
          <Tooltip title="What is this?">
            <IconButton color="info" onClick={() => setHelpOpen(true)}>
              <InfoOutlinedIcon sx={{ color: '#00ffff' }} />
            </IconButton>
          </Tooltip>
        </Toolbar>
      </AppBar>
      {/* Business Value Panel */}
      <Paper elevation={8} sx={{ maxWidth: 1200, mx: 'auto', mt: 2, mb: 2, borderRadius: 4, background: 'rgba(20,20,20,0.8)', boxShadow: '0 0 32px #00ffff44', p: 2, backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <Box display="flex" gap={3} alignItems="center">
          {businessValue.map((item, i) => (
            <Box key={i} sx={{ color: '#00ffff', fontFamily: 'monospace', fontWeight: 'bold', fontSize: 18, display: 'flex', alignItems: 'center' }}>
              {item.label}: <span style={{ color: '#fff', marginLeft: 8 }}>{item.value}</span>
            </Box>
          ))}
        </Box>
        <Box sx={{ color: '#fff', fontFamily: 'monospace', fontWeight: 'bold', fontSize: 16 }}>
          <span style={{ color: '#ff00ff' }}>AI-Powered Test Automation</span>
        </Box>
      </Paper>
      
      {/* Developer Contact Panel */}
      <Paper elevation={8} sx={{ maxWidth: 1200, mx: 'auto', mt: 2, mb: 2, borderRadius: 4, background: 'rgba(20,20,20,0.8)', boxShadow: '0 0 32px #00ffff44', p: 3, backdropFilter: 'blur(8px)' }}>
        <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <Box sx={{ color: '#fff', fontFamily: 'monospace' }}>
            <Typography variant="h6" sx={{ color: '#00ffff', fontWeight: 'bold', mb: 1 }}>
              Developed by Rahuul Pande
            </Typography>
            <Typography variant="body2" sx={{ color: '#ccc', mb: 2 }}>
              Test Automation Engineer | AI Enthusiast
            </Typography>
            <Typography variant="body2" sx={{ color: '#ccc', fontSize: 14 }}>
              Keenly Looking for AI-Powered Solutions | Test Automation | Banking Integration
            </Typography>
          </Box>
          <Box sx={{ display: 'flex', gap: 2 }}>
            <Button
              variant="contained"
              href="https://www.linkedin.com/in/rahuulpande/"
              target="_blank"
              rel="noopener noreferrer"
              sx={{ 
                background: '#0077b5', 
                color: '#fff', 
                fontWeight: 'bold',
                '&:hover': { background: '#005885' },
                minWidth: 100
              }}
            >
              LinkedIn
            </Button>
            <Button
              variant="contained"
              href="https://github.com/rahuulpande"
              target="_blank"
              rel="noopener noreferrer"
              sx={{ 
                background: '#333', 
                color: '#fff', 
                fontWeight: 'bold',
                '&:hover': { background: '#555' },
                minWidth: 100
              }}
            >
              GitHub
            </Button>
            <Button
              variant="contained"
              href="mailto:rahuulpande@gmail.com"
              sx={{ 
                background: '#00a651', 
                color: '#fff', 
                fontWeight: 'bold',
                '&:hover': { background: '#008a44' },
                minWidth: 100
              }}
            >
              Email
            </Button>
          </Box>
        </Box>
      </Paper>
      
      {/* Color Legend */}
      <Box sx={{ maxWidth: 1200, mx: 'auto', mb: 1, display: 'flex', alignItems: 'center', gap: 2, pl: 2 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
          <Box sx={{ width: 18, height: 18, borderRadius: '50%', background: '#00ff00', mr: 0.5, border: '2px solid #222' }} />
          <Typography variant="caption" sx={{ color: '#00ff00', fontWeight: 'bold', mr: 2 }}>Healthy</Typography>
          <Box sx={{ width: 18, height: 18, borderRadius: '50%', background: '#00ffff', mr: 0.5, border: '2px solid #222' }} />
          <Typography variant="caption" sx={{ color: '#00ffff', fontWeight: 'bold', mr: 2 }}>Testing</Typography>
          <Box sx={{ width: 18, height: 18, borderRadius: '50%', background: '#ff00ff', mr: 0.5, border: '2px solid #222' }} />
          <Typography variant="caption" sx={{ color: '#ff00ff', fontWeight: 'bold' }}>Failing</Typography>
        </Box>
      </Box>
      <Paper elevation={8} sx={{ maxWidth: 1200, mx: 'auto', mt: 2, borderRadius: 4, background: 'rgba(20,20,20,0.8)', boxShadow: '0 0 32px #00ffff44', p: 2, backdropFilter: 'blur(8px)' }}>
        <Tabs value={tab} onChange={(_, v) => setTab(v)} textColor="inherit" TabIndicatorProps={{ style: { background: '#00ffff' } }} sx={{ mb: 2 }}>
          <Tab label="Service Mesh" sx={{ color: '#00ffff', fontWeight: 'bold' }} />
          <Tab label="Testing Dashboard" sx={{ color: '#00ff00', fontWeight: 'bold' }} />
          <Tab label="Harmonization" sx={{ color: '#ff00ff', fontWeight: 'bold' }} />
          <Tab label="Performance" sx={{ color: '#00ffff', fontWeight: 'bold' }} />
          <Tab label="Risk Heatmap" sx={{ color: '#ffff00', fontWeight: 'bold' }} />
        </Tabs>
        <Box>
          {tab === 0 && <ServiceMeshVisualizer testing={testing} />}
          {tab === 1 && (
            <TestingDashboard
              testing={testing}
              testCount={scenarioConfig[scenario]?.testCount || 1500}
              serviceCount={scenarioConfig[scenario]?.serviceCount || 12}
              flowName={scenarioConfig[scenario]?.flowName || 'Selected Flow'}
            />
          )}
          {tab === 2 && <HarmonizationMatrix />}
          {tab === 3 && <PerformanceMonitor />}
          {tab === 4 && <RiskHeatmap />}
        </Box>
      </Paper>
      {/* Help Dialog */}
      <Dialog open={helpOpen} onClose={() => setHelpOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle sx={{ color: '#00ffff', fontFamily: 'monospace', background: '#111' }}>What is the UBS-CS Integration Control Tower?</DialogTitle>
        <DialogContent sx={{ background: '#111' }}>
          <DialogContentText sx={{ color: '#00ffff', fontSize: 16, mb: 2 }}>
            <b style={{ color: '#fff' }}>This dashboard is your mission control for digital banking integration and health.</b><br /><br />
            <ul style={{ color: '#fff' }}>
              <li><b>Service Mesh:</b> See how all your banking services are connected and communicating.</li>
              <li><b>Testing Dashboard:</b> Watch live test results and system health in real time.</li>
              <li><b>Harmonization:</b> Ensure data from old and new systems is mapped and transformed correctly.</li>
              <li><b>Performance:</b> Monitor speed, errors, and bottlenecks across all services.</li>
              <li><b>Risk Heatmap:</b> Visualize risk and critical paths in 3D.</li>
            </ul>
            <Divider sx={{ my: 2, background: '#00ffff' }} />
            <b style={{ color: '#fff' }}>Business Value:</b>
            <ul style={{ color: '#fff' }}>
              <li>Faster, safer integration of UBS and CS systems</li>
              <li>Automated risk and compliance checks</li>
              <li>Instant visibility for management and auditors</li>
              <li>Reduces outages, saves time and money</li>
            </ul>
            <Divider sx={{ my: 2, background: '#00ffff' }} />
            <b style={{ color: '#fff' }}>How to use:</b>
            <ul style={{ color: '#fff' }}>
              <li>Select a scenario to simulate a real business flow</li>
              <li>Click 'Start Testing' to launch automated tests</li>
              <li>Watch the dashboard for live results and alerts</li>
              <li>Use the tabs to explore service health, data harmonization, performance, and risk</li>
            </ul>
          </DialogContentText>
        </DialogContent>
        <DialogActions sx={{ background: '#111' }}>
          <Button onClick={() => setHelpOpen(false)} sx={{ color: '#00ffff', fontWeight: 'bold' }}>Close</Button>
        </DialogActions>
      </Dialog>
      
      {/* Footer */}
      <Box sx={{ mt: 4, py: 3, textAlign: 'center', borderTop: '1px solid #333' }}>
        <Typography variant="body2" sx={{ color: '#666', fontFamily: 'monospace' }}>
          © 2024 Rahuul Pande | Test Automation Engineer & AI Enthusiast | UBS-CS Integration Control Tower | Built with React, FastAPI & D3.js
        </Typography>
        <Box sx={{ mt: 1, display: 'flex', justifyContent: 'center', gap: 2 }}>
          <Typography variant="caption" sx={{ color: '#666' }}>
            <a href="https://www.linkedin.com/in/rahuulpande/" target="_blank" rel="noopener noreferrer" style={{ color: '#00ffff', textDecoration: 'none' }}>
              LinkedIn
            </a>
          </Typography>
          <Typography variant="caption" sx={{ color: '#666' }}>|</Typography>
          <Typography variant="caption" sx={{ color: '#666' }}>
            <a href="https://github.com/rahuulpande" target="_blank" rel="noopener noreferrer" style={{ color: '#00ffff', textDecoration: 'none' }}>
              GitHub
            </a>
          </Typography>
          <Typography variant="caption" sx={{ color: '#666' }}>|</Typography>
          <Typography variant="caption" sx={{ color: '#666' }}>
            <a href="mailto:rahuulpande@gmail.com" style={{ color: '#00ffff', textDecoration: 'none' }}>
              Email
            </a>
          </Typography>
        </Box>
      </Box>
    </Box>
  );
};

export default App;
