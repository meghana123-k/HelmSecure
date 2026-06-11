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
          <Route index path="/" element={<LiveMonitoring />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/evidence" element={<Evidence />} />
          <Route path="/analytics" element={<Analytics />} />
          {/* <Route path="*" element={<Dashboard />} /> */}
        </Route>
      </Routes>
    </>
  );
}
export default App;
