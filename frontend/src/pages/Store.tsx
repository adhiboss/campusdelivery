import React, { useState, useEffect } from 'react';

const Store: React.FC = () => {
  const [products] = useState<any[]>([
    { id: 1, name: 'University Hoodie', price: 40 }
  ]);

  useEffect(() => {
    // Fetch store products API call here
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4 text-[#8B1E2F]">University Store</h1>
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        {products.length === 0 ? (
          <p>Store is empty.</p>
        ) : (
          products.map((item: any) => (
            <div key={item.id} className="bg-white p-4 shadow rounded">
              <h2 className="font-semibold">{item.name}</h2>
              <p>${item.price}</p>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default Store;
