import { Route, Routes } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import LiveMonitoring from './pages/LiveMonitoring';
import Evidence from './pages/Evidence';
import Analytics from './pages/Analytics';

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/live-monitoring" element={<LiveMonitoring />} />
        <Route path="/evidence" element={<Evidence />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </>
  );
}
export default App;
