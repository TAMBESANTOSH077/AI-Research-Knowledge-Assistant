import { useEffect, useState } from "react";
import api from "../services/api";

function UploadedFiles() {
  const [documents, setDocuments] = useState([]);

  const loadFiles = async () => {
    try {
      const res = await api.get("/upload/files");
      setDocuments(res.data.files);
    } catch (err) {
      console.error("Error loading files:", err);
    }
  };

  const deleteFile = async (filename) => {
    const confirmDelete = window.confirm(
      `Delete "${filename}"?`
    );

    if (!confirmDelete) return;

    try {
      await api.delete(`/upload/files/${filename}`);

      // Refresh file list
      loadFiles();
    } catch (err) {
      console.error("Delete failed:", err);
    }
  };

  useEffect(() => {
    loadFiles();
  }, []);

  return (
    <div className="card uploaded-files">
      <h2>📂 Uploaded Documents</h2>

      <p>Total Documents: {documents.length}</p>

      {documents.length === 0 ? (
        <p>No documents uploaded.</p>
      ) : (
        <ul className="document-list">
          {documents.map((doc) => (
            <li key={doc.name} className="document-item">
              <div>
                <strong>📄 {doc.name}</strong>
                <br />
                <small>{doc.size_kb} KB</small>
              </div>

              <button
                className="delete-btn"
                onClick={() => deleteFile(doc.name)}
              >
                🗑 Delete
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default UploadedFiles;