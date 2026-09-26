import React from 'react';
import { Outlet, Link } from 'react-router-dom';

const MainLayout: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100 flex">
      {/* Sidebar Placeholder */}
      <aside className="w-64 bg-[#8B1E2F] text-white p-6">
        <h2 className="text-xl font-bold mb-8">CDH</h2>
        <nav className="flex flex-col gap-4">
          <Link to="/" className="hover:text-red-200">Dashboard</Link>
          <Link to="/orders" className="hover:text-red-200">Orders</Link>
          <Link to="/marketplace" className="hover:text-red-200">Marketplace</Link>
          <Link to="/store" className="hover:text-red-200">Store</Link>
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
          <Outlet />
        </main>
      </div>
    </div>
  );
};

export default MainLayout;
