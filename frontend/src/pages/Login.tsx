import React from 'react';

const Login: React.FC = () => {
  return (
    <div className="flex h-screen items-center justify-center bg-gray-50">
      <div className="p-8 bg-white shadow rounded-md w-full max-w-sm">
        <h1 className="text-2xl font-bold mb-6 text-center text-[#8B1E2F]">CDH Login</h1>
        <form>
          <div className="mb-4">
            <label className="block text-sm font-medium mb-1">Email</label>
            <input type="email" className="w-full border p-2 rounded" />
          </div>
          <div className="mb-4">
            <label className="block text-sm font-medium mb-1">Password</label>
            <input type="password" className="w-full border p-2 rounded" />
          </div>
          <button className="w-full bg-[#8B1E2F] text-white p-2 rounded hover:bg-red-800 transition">
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
