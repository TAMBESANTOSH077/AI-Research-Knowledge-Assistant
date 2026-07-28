import { useState } from "react";

function Navbar({ darkMode, setDarkMode }) {
  const [showSettings, setShowSettings] = useState(false);

  return (
    <>
      <nav className="navbar">
        <div className="logo">
          🤖 <span>AI Research & Knowledge Assistant</span>
        </div>

        <div className="nav-actions">
          <button
            className="nav-btn"
            onClick={() => setDarkMode(!darkMode)}
          >
            {darkMode ? "☀️ Light Mode" : "🌙 Dark Mode"}
          </button>

          <button
            className="nav-btn"
            onClick={() => setShowSettings(true)}
          >
            ⚙ Settings
          </button>
        </div>
      </nav>

      {showSettings && (
        <div className="modal-overlay">
          <div className="settings-modal">
            <h2>⚙ Settings</h2>

            <div className="setting-item">
              <label>Theme</label>
              <button
                className="nav-btn"
                onClick={() => setDarkMode(!darkMode)}
              >
                {darkMode ? "Light Mode" : "Dark Mode"}
              </button>
            </div>

            <div className="setting-item">
              <label>AI Model</label>
              <select>
                <option>Gemini</option>
                <option>OpenAI</option>
              </select>
            </div>

            <div className="setting-item">
              <label>Temperature</label>
              <input
                type="range"
                min="0"
                max="1"
                step="0.1"
                defaultValue="0.3"
              />
            </div>

            <div className="setting-item">
              <label>Chunk Size</label>
              <input type="number" defaultValue="500" />
            </div>

            <div className="setting-item">
              <label>Top K Results</label>
              <input type="number" defaultValue="4" />
            </div>

            <div className="modal-buttons">
              <button
                className="nav-btn"
                onClick={() => setShowSettings(false)}
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}

export default Navbar;