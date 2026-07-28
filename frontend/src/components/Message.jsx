function Message({ role, text }) {
  const isUser = role === "user";

  return (
    <div
      style={{
        display: "flex",
        justifyContent: isUser ? "flex-end" : "flex-start",
        marginBottom: "12px",
      }}
    >
      <div
        style={{
          background: isUser ? "#2563eb" : "#e5e7eb",
          color: isUser ? "#fff" : "#000",
          padding: "12px",
          borderRadius: "10px",
          maxWidth: "70%",
        }}
      >
        {text}
      </div>
    </div>
  );
}

export default Message;