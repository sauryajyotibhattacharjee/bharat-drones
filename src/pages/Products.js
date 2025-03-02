const Products = () => {
    const products = [
      "Organ Delivery Drone",
      "Precision Agriculture Drone",
      "Defense FPV Surveillance Drone",
      "Kamikaze Drone",
      "3D Printed Ballistic Missiles",
    ];
  
    return (
      <div className="p-10">
        <h2 className="text-3xl font-bold text-gray-800">Our Products</h2>
        <ul className="mt-4 list-disc list-inside text-gray-600">
          {products.map((product, index) => (
            <li key={index}>{product}</li>
          ))}
        </ul>
      </div>
    );
  };
  
  export default Products;
  