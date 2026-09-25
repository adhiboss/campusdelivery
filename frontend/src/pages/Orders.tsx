import React, { useState, useEffect } from 'react';

const Orders: React.FC = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    // Fetch orders API call here
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4 text-[#8B1E2F]">My Orders</h1>
      <div className="bg-white p-4 shadow rounded">
        {orders.length === 0 ? (
          <p>No orders found.</p>
        ) : (
          <ul>
            {orders.map((order: any) => (
              <li key={order.id}>{order.tracking_id} - {order.status}</li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
};

export default Orders;
