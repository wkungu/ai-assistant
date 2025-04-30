'use client';

import { useState } from "react";
import QueryForm from "@/app/components/QueryForm";
import ResponseDisplay from "@/app/components/ResponseDisplay";
import QueryHistory from "@/app/components/QueryHistory";

const Home = () => {
  const [response, setResponse] = useState("")
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState(false);
  const [error, setError] = useState("");

  // Handle submitting the questions to the API
  const handleQuerySubmit = async (question) => {
    setLoading(true);
    setError("");
    try {
      const res = await fetch("http://localhost:8000/api/v1/query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      });

      if (!res.ok) throw new Error("Failed to fetch response");

      const data = await res.json();
      setResponse(data.response);
    } catch (err) {
      setError("Something went wrong! Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1 className="text-2xl md:text-3xl font-bold text-center mt-6 mb-4">
      Ask Your Business Questions
      </h1>
      <div className="flex justify-center w-full mx-auto">
      <button
        type="button"
        onClick={() => setHistory(!history)}
        className="mt-4 w-1/5 mx-auto bg-orange-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-lg transition"
      >
        {history? 'Hide ': 'View '} History
      </button>
      </div>
      {!history && (
        <>
        <QueryForm onSubmit={handleQuerySubmit} />
        {loading && <p className="mt-6 text-blue-600 text-center">💼 Fetching advice...</p>}
        {error && <p className="mt-4 text-red-600 text-center">{error}</p>}
        {response && !loading && <ResponseDisplay response={response} />}
        </>
      )}
      {history && <QueryHistory />}
    </div>
  );
};

export default Home;
