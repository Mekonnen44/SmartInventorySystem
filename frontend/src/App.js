import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get('/api/products/')
      .then(response => setProducts(response.data))
      .catch(error => console.error('Error fetching products:', error));
  }, []);

  return (
    <div className="App">
      <h1>Product Dashboard</h1>
      <ul>
        {products.map(product => (
          <li key={product.id}>{product.name} - {product.quantity}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;