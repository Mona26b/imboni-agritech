import { Link } from 'react-router-dom'

function Header() {
  return (
    <header className="bg-farm-dark text-white p-6 shadow-lg">
      <div className="max-w-6xl mx-auto flex items-center justify-between">
        <Link to="/" className="text-2xl font-bold">Imboni Agri-tech</Link>
        <nav className="space-x-6 text-sm">
          <Link to="/" className="hover:text-farm-sun">Home</Link>
          <Link to="/dashboard" className="hover:text-farm-sun">Dashboard</Link>
          <Link to="/map" className="hover:text-farm-sun">Map</Link>
          <Link to="/districts" className="hover:text-farm-sun">Districts</Link>
        </nav>
      </div>
    </header>
  )
}

export default Header
