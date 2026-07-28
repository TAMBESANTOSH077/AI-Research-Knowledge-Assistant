import { useState } from "react";
import api from "../services/api";

function SearchPanel() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const search = async () => {
    if (!query.trim()) return;

    try {
      const res = await api.post("/search/", {
        query
      });

      setResults(res.data.results);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="card">

      <h2>🔍 Semantic Search</h2>

      <div className="search-row">
        <input
          type="text"
          placeholder="Search uploaded documents..."
          value={query}
          onChange={(e)=>setQuery(e.target.value)}
        />

        <button onClick={search}>
          Search
        </button>
      </div>

      <div className="search-results">
        {results.map((item,index)=>(
          <div className="search-card" key={index}>
            <h4>📄 {item.document}</h4>
            <p>{item.content}</p>
          </div>
        ))}
      </div>

    </div>
  );
}

export default SearchPanel;