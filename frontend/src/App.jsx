// App.jsx

import { Route, Routes } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import LiveMonitoring from "./pages/LiveMonitoring";
import Evidence from "./pages/Evidence";
import Analytics from "./pages/Analytics";
import { MainLayout } from "./layouts/MainLayout";

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          <Route index element={<Dashboard />} />
          <Route path="/live-monitoring" element={<LiveMonitoring />} />
          <Route path="/evidence" element={<Evidence />} />
          <Route path="/analytics" element={<Analytics />} />
          {/* <Route path="*" element={<Dashboard />} /> */}
        </Route>
      </Routes>
    </>
  );
}
export default App;
