import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import data from '../assets/scientists.json';
import '../components/styles/ScientistDetail.css';

function ScientistDetail() {
  const { id } = useParams();
  const scientist = data.find(s => s.id === id);

  const [answer, setAnswer] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  if (!scientist) return <div>Scientist not found</div>;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    const payload = {
      user_id: 1,
      scientist_id: id,
      answer: parseFloat(answer)
    };

    try {
      const res = await fetch('http://cdl-backend-dzho.onrender.com/api/submit_answer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      if (!res.ok) {
        throw new Error(`Server error: ${res.status}`);
      }

      const data = await res.json();
      setResult(data.message || 'Unexpected response');
    } catch (error) {
      console.error(error);
      setResult('Error: Could not reach the server.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="detail-container">
      <img src={`/images/${scientist.image}`} alt={scientist.name} className="detail-image" />
      <h2>{scientist.name}</h2>
      <h4>{scientist.period}</h4>
      <p>{scientist.description}</p>

      <div className="challenge-box">
        <h3>Challenge Problem:</h3>
        <p>{scientist.question || "What is the orbital period of a planet 1 AU from a Sun-like star (in years)?"}</p>

        <form onSubmit={handleSubmit}>
          <input
            type="number"
            step="any"
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            placeholder="Enter your answer..."
          />
          <button type="submit" disabled={loading}>Submit Answer</button>
        </form>

        {loading && <p>Submitting...</p>}
        {result && <p className="result-message">{result}</p>}
      </div>
    </div>
  );
}

export default ScientistDetail;
