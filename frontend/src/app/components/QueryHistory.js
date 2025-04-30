'use client';

import { useEffect, useState } from "react";
import {formatResponse} from './utils'

const QueryHistory = () => {
  const [history, setHistory] = useState([]);

  // Fetch History from the backend
  useEffect(() => {
    const fetchHistory = async () => {
      const res = await fetch("http://localhost:8000/api/v1/history");
      const data = await res.json();
      setHistory(data.history);
    };
    fetchHistory();
  }, []);

  return (
    <div className="bg-white p-4 mt-6 rounded shadow-md max-w-2xl mx-auto">
      <h2 className="text-xl font-semibold mb-4">Previous Questions</h2>
      {history.length === 0 ? (
        <p>No history available yet.</p>
      ) : (
        <ul className="space-y-4">
          {history.map((entry, idx) => (
            <li key={idx} className="border-b pb-3">
              <p className="font-bold text-blue-700 mb-3">{entry.question}</p>
              <p className="text-sm text-gray-500">{formatResponse(entry.response)}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default QueryHistory;
