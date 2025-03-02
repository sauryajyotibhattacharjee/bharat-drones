import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="bg-primary text-white p-4 shadow-md">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-2xl font-bold">Bharat Heavy Drones</h1>
        <div className="space-x-6">
          <Link to="/" className="hover:text-secondary">Home</Link>
          <Link to="/about" className="hover:text-secondary">About</Link>
          <Link to="/team" className="hover:text-secondary">Team</Link>
          <Link to="/products" className="hover:text-secondary">Products</Link>
          <Link to="/achievements" className="hover:text-secondary">Achievements</Link>
          <Link to="/contact" className="hover:text-secondary">Contact</Link>
          <Link to="/signin" className="hover:text-secondary">SignIn</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
