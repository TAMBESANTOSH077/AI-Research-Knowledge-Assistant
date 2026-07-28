function Sidebar() {
  const menuItems = [
    { icon: "📄", name: "Upload" },
    { icon: "💬", name: "Chat" },
    { icon: "📝", name: "Summary" },
    { icon: "🔍", name: "Search" },
    { icon: "📊", name: "Analytics" },
    { icon: "📑", name: "Compare" },
  ];

  return (
    <aside className="sidebar">
      <h2 className="sidebar-title">Dashboard</h2>

      <div className="sidebar-menu">
        {menuItems.map((item) => (
          <button key={item.name} className="sidebar-item">
            <span className="sidebar-icon">{item.icon}</span>
            <span>{item.name}</span>
          </button>
        ))}
      </div>
    </aside>
  );
}

export default Sidebar;