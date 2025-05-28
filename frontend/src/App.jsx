import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [token, setToken] = useState('');
  const [summary, setSummary] = useState([]);

  const handleRegister = async () => {
    const email = prompt('Email:');
    const password = prompt('Password:');
    await axios.post('/api/register', { email, password });
    alert('Registered!');
  };

  const handleLogin = async () => {
    const email = prompt('Email:');
    const password = prompt('Password:');
    const res = await axios.post('/api/login', { email, password });
    setToken(res.data.access_token);
    alert('Logged in!');
  };

  const handleClockIn = async () => {
    await axios.post('/api/clock-in', null, { params: { token } });
    alert('Clock-in recorded!');
  };

  const handleClockOut = async () => {
    await axios.post('/api/clock-out', null, { params: { token } });
    alert('Clock-out recorded!');
  };

  const fetchSummary = async () => {
    const res = await axios.get('/api/summary', { params: { token } });
    setSummary(res.data);
  };

  const downloadCSV = () => {
    window.open(`/api/export/csv?token=${token}`, '_blank');
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">WorkTime Tracker</h1>
      <button onClick={handleRegister} className="bg-blue-500 text-white px-4 py-2 m-1">Register</button>
      <button onClick={handleLogin} className="bg-green-500 text-white px-4 py-2 m-1">Login</button>
      <button onClick={handleClockIn} className="bg-yellow-500 text-white px-4 py-2 m-1">Clock In</button>
      <button onClick={handleClockOut} className="bg-red-500 text-white px-4 py-2 m-1">Clock Out</button>
      <button onClick={fetchSummary} className="bg-purple-500 text-white px-4 py-2 m-1">View Summary</button>
      <button onClick={downloadCSV} className="bg-gray-700 text-white px-4 py-2 m-1">Download CSV</button>
      <ul className="mt-4">
        {summary.map((item, index) => (
          <li key={index} className="border p-2 my-1">
            {item.date}: {item.hours ? item.hours.toFixed(2) : 'In progress'} hrs
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;