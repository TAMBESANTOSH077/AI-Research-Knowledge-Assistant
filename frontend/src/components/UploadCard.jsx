import { useState } from "react";
import api from "../services/api";

function UploadCard() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const uploadFile = async () => {
    if (!file) {
      setStatus("⚠ Please select a PDF.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

   try {
  setStatus("Uploading...");

  const response = await api.post("/upload/", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  console.log("SUCCESS RESPONSE:", response);
  console.log("DATA:", response.data);

  setStatus("✅ Upload Successful");
} catch (error) {
  console.error("FULL ERROR:", error);

  if (error.response) {
    console.log("Status:", error.response.status);
    console.log("Data:", error.response.data);
    setStatus(`❌ ${error.response.status}`);
  } else if (error.request) {
    console.log("Request:", error.request);
    setStatus("❌ Cannot connect to FastAPI server");
  } else {
    console.log("Message:", error.message);
    setStatus(`❌ ${error.message}`);
  }
}
  };

  return (
    <div className="card upload-card">
      <h2>📄 Upload Research Document</h2>

      <p className="upload-subtitle">
        Upload a PDF and start chatting with your AI assistant.
      </p>

      <label className="upload-box">
        ☁️

        <h3>Drag & Drop PDF</h3>

        <p>or click here to browse</p>

        <input
          type="file"
          accept=".pdf"
          hidden
          onChange={(e) => {
            setFile(e.target.files[0]);
            setStatus("");
          }}
        />
      </label>

      {file && (
        <div className="selected-file">
          📄 {file.name}
        </div>
      )}

      <button className="upload-btn" onClick={uploadFile}>
        🚀 Upload Document
      </button>

      <p className="upload-status">{status}</p>
    </div>
  );
}

export default UploadCard;