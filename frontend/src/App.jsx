import { useEffect, useState } from "react";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import UploadCard from "./components/UploadCard";
import UploadedFiles from "./components/UploadedFiles";
import AnalyticsCard from "./components/AnalyticsCard";
import SearchPanel from "./components/SearchPanel";
import ChatBox from "./components/ChatBox";

import "./App.css";

function App() {
  const [darkMode, setDarkMode] = useState(() => {
    return localStorage.getItem("theme") === "dark";
  });

  useEffect(() => {
    if (darkMode) {
      document.body.classList.add("dark-theme");
      localStorage.setItem("theme", "dark");
    } else {
      document.body.classList.remove("dark-theme");
      localStorage.setItem("theme", "light");
    }
  }, [darkMode]);

  return (
    <div className={`app ${darkMode ? "dark" : ""}`}>
      <Navbar
        darkMode={darkMode}
        setDarkMode={setDarkMode}
      />

      <div className="layout">
        <Sidebar />

        <main className="main-content">

          {/* Upload PDF */}
          <UploadCard />

          {/* Uploaded Documents */}
          <div style={{ marginTop: "20px" }}>
            <UploadedFiles />
          </div>

          {/* Analytics */}
          <div style={{ marginTop: "20px" }}>
            <AnalyticsCard />
          </div>

          {/* Semantic Search */}
          <div style={{ marginTop: "20px" }}>
            <SearchPanel />
          </div>

          {/* AI Chat */}
          <div style={{ marginTop: "20px" }}>
            <ChatBox />
          </div>

        </main>
      </div>
    </div>
  );
}

export default App;