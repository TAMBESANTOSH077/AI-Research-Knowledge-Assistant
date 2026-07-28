import { useState } from "react";
import api from "../services/api";

function ChatBox() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!question.trim()) return;

    const userMessage = {
      role: "user",
      text: question,
    };

    setMessages((prev) => [...prev, userMessage]);

    try {
      const response = await api.post("/chat/", {
        question,
      });

      const aiMessage = {
        role: "assistant",
        text: response.data.answer,
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "❌ Unable to connect to backend.",
        },
      ]);
    }

    setQuestion("");
  };

  return (
    <div className="card chat-card">

      <h2>💬 AI Assistant</h2>

      <div className="chat-window">

        {messages.length === 0 ? (
          <div className="empty-chat">
            🤖 Ask me anything about your uploaded PDF.
          </div>
        ) : (
          messages.map((msg, index) => (
            <div
              key={index}
              className={
                msg.role === "user"
                  ? "user-message"
                  : "ai-message"
              }
            >
              {msg.text}
            </div>
          ))
        )}

      </div>

      <div className="chat-input-container">

        <input
          type="text"
          placeholder="Ask a question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") sendMessage();
          }}
        />

        <button className="send-btn" onClick={sendMessage}>
          🚀
        </button>

      </div>

    </div>
  );
}

export default ChatBox;