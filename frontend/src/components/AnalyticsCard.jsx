import { useEffect, useState } from "react";
import api from "../services/api";

function AnalyticsCard() {

  const [data, setData] = useState({
    documents: 0,
    chunks: 0,
    questions: 0,
    avg_response: "0.00 s",
    vector_store: "Offline"
  });

  useEffect(() => {

    api.get("/analytics/")
      .then(res => setData(res.data))
      .catch(console.error);

  }, []);

  return (

    <div className="card analytics-card">

      <h2>📊 Analytics Dashboard</h2>

      <div className="stats-grid">

        <div className="stat-box">
          <h3>{data.documents}</h3>
          <p>Documents</p>
        </div>

        <div className="stat-box">
          <h3>{data.chunks}</h3>
          <p>Chunks</p>
        </div>

        <div className="stat-box">
          <h3>{data.questions}</h3>
          <p>Questions</p>
        </div>

        <div className="stat-box">
          <h3>{data.avg_response}</h3>
          <p>Avg Response</p>
        </div>

        <div className="stat-box">
          <h3>{data.vector_store}</h3>
          <p>Vector Store</p>
        </div>

      </div>

    </div>

  );
}

export default AnalyticsCard;