import React, { useState, useEffect } from 'react';

const Marketplace: React.FC = () => {
  const [listings, setListings] = useState([]);

  useEffect(() => {
    // Fetch marketplace listings API call here
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4 text-[#8B1E2F]">Student Marketplace</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {listings.length === 0 ? (
          <p>No active listings.</p>
        ) : (
          listings.map((item: any) => (
            <div key={item.id} className="bg-white p-4 shadow rounded">
              <h2 className="font-semibold">{item.title}</h2>
              <p>${item.price}</p>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default Marketplace;
