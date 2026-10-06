import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import Footer from './components/Footer'
import LandingPage from './pages/LandingPage'
import DashboardPage from './pages/DashboardPage'
import MapPage from './pages/MapPage'
import DistrictsPage from './pages/DistrictsPage'
import DistrictDetailPage from './pages/DistrictDetailPage'

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-farm-light flex flex-col">
        <Header />
        <div className="flex-1">
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/dashboard" element={<DashboardPage />} />
            <Route path="/map" element={<MapPage />} />
            <Route path="/districts" element={<DistrictsPage />} />
            <Route path="/districts/:districtName" element={<DistrictDetailPage />} />
          </Routes>
        </div>
        <Footer />
      </div>
    </BrowserRouter>
  )
}

export default App
