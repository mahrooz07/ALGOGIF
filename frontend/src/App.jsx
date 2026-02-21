import React, { useState, useRef, useEffect } from 'react';
import './App.css';

function App() {
  const [messages, setMessages] = useState([
    { role: 'agent', text: 'Hi! Select a domain and tell me what you want to visualize.', imageUrl: null }
  ]);
  const [input, setInput] = useState('');
  const [domain, setDomain] = useState('Data Structures');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  // Available learning domains
  const domains = ['Data Structures', 'GraphDB', 'Machine Learning', 'Mathematics'];

  // Auto-scroll to the newest message
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim()) return;

    // 1. Add user's message to chat
    const userMessage = { role: 'user', text: input, imageUrl: null };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    // 2. Call the FastAPI backend
    try {
      const response = await fetch('http://localhost:8000/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ domain: domain, query: input }),
      });

      const data = await response.json();

      // 3. Display the result
      if (data.status === 'success') {
        setMessages((prev) => [
          ...prev,
          { role: 'agent', text: `Here is the visualization for: ${input}`, imageUrl: data.url }
        ]);
      } else {
        throw new Error(data.detail || 'Generation failed');
      }
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { role: 'agent', text: `Error: ${error.message}. Is the backend running?`, imageUrl: null }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header className="header">
        <h1>Visual Learning AI</h1>
        <select 
          value={domain} 
          onChange={(e) => setDomain(e.target.value)}
          className="domain-selector"
        >
          {domains.map((d) => (
            <option key={d} value={d}>{d}</option>
          ))}
        </select>
      </header>

      <div className="chat-window">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.role}`}>
            <div className="bubble">
              <p>{msg.text}</p>
              {/* Render the GIF if it exists */}
              {msg.imageUrl && (
                <img src={msg.imageUrl} alt="Generated Visualization" className="generated-gif" />
              )}
            </div>
          </div>
        ))}
        {loading && (
          <div className="message agent">
            <div className="bubble loading">Writing code & rendering animation... ⏳</div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="input-area">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          placeholder={`Ask about ${domain}...`}
        />
        <button onClick={handleSend} disabled={loading}>Send</button>
      </div>
    </div>
  );
}

export default App;