import React from 'react';

interface MainLayoutProps {
  children: React.ReactNode;
}

const MainLayout: React.FC<MainLayoutProps> = ({ children }) => {
  return (
    <div className="min-h-screen bg-gray-100 flex">
      {/* Sidebar Placeholder */}
      <aside className="w-64 bg-[#8B1E2F] text-white p-6">
        <h2 className="text-xl font-bold mb-8">CDH</h2>
        <nav className="flex flex-col gap-4">
          <a href="/" className="hover:text-red-200">Dashboard</a>
          <a href="/orders" className="hover:text-red-200">Orders</a>
          <a href="/profile" className="hover:text-red-200">Profile</a>
        </nav>
      </aside>

      <div className="flex-1 flex flex-col">
        {/* Header Placeholder */}
        <header className="bg-white shadow p-4 flex justify-between items-center">
          <h2 className="text-lg font-semibold">Campus Delivery Hub</h2>
          <div>Profile | Logout</div>
        </header>

        {/* Page Content */}
        <main className="flex-1 p-6">
          {children}
        </main>
      </div>
    </div>
  );
};

export default MainLayout;
