import Message from "./Message";

function ChatWindow({ messages }) {
  return (
    <div
      style={{
        height: "350px",
        overflowY: "auto",
        border: "1px solid #ddd",
        borderRadius: "8px",
        padding: "15px",
        marginBottom: "15px",
      }}
    >
      {messages.length === 0 ? (
        <p>Start chatting with your AI assistant.</p>
      ) : (
        messages.map((msg, index) => (
          <Message
            key={index}
            role={msg.role}
            text={msg.text}
          />
        ))
      )}
    </div>
  );
}

export default ChatWindow;