import { useState } from "react";

function ChatInput({ onSend }) {
  const [question, setQuestion] = useState("");

  const send = () => {
    if (!question.trim()) return;

    onSend(question);
    setQuestion("");
  };

  return (
    <div
      style={{
        display: "flex",
        marginTop: "15px",
        gap: "10px",
      }}
    >
      <input
        style={{
          flex: 1,
          padding: "12px",
        }}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            send();
          }
        }}
        placeholder="Ask a question..."
      />

      <button onClick={send}>
        Send
      </button>
    </div>
  );
}

export default ChatInput;