function App() {
  return (
    <div className="min-h-screen bg-farm-light">
      <header className="bg-farm-dark text-white p-6 shadow-lg">
        <div className="max-w-6xl mx-auto flex items-center justify-between">
          <h1 className="text-2xl font-bold">🌱 Imboni Agri-tech</h1>
          <nav className="space-x-6 text-sm">
            <a href="#" className="hover:text-farm-sun">Home</a>
            <a href="#" className="hover:text-farm-sun">Dashboard</a>
            <a href="#" className="hover:text-farm-sun">Map</a>
            <a href="#" className="hover:text-farm-sun">Districts</a>
          </nav>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-6 py-16">
        <section className="text-center">
          <h2 className="text-5xl font-bold text-farm-dark mb-6">
            Data-driven agriculture for Rwanda
          </h2>
          <p className="text-xl text-farm-earth mb-8 max-w-2xl mx-auto">
            Explore seasonal crop data, fertilizer usage, and farming practices 
            across all 30 districts — powered by the Seasonal Agricultural Survey 2026.
          </p>
          <button className="bg-farm-green hover:bg-farm-dark text-white px-8 py-3 rounded-lg text-lg font-semibold transition-colors">
            Explore the Data →
          </button>
        </section>

        <section className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-20">
          <div className="bg-white p-6 rounded-lg shadow-md">
            <div className="text-3xl mb-2">🌾</div>
            <h3 className="text-xl font-bold text-farm-dark mb-2">30 Districts</h3>
            <p className="text-gray-600">Complete seasonal crop and land-use data</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-md">
            <div className="text-3xl mb-2">📊</div>
            <h3 className="text-xl font-bold text-farm-dark mb-2">15+ Crops</h3>
            <p className="text-gray-600">Maize, beans, cassava, banana, and more</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-md">
            <div className="text-3xl mb-2">🗺️</div>
            <h3 className="text-xl font-bold text-farm-dark mb-2">Interactive Map</h3>
            <p className="text-gray-600">Visualize data district by district</p>
          </div>
        </section>
      </main>

      <footer className="bg-farm-dark text-white py-6 text-center mt-20">
        <p className="text-sm">
          Data source: NISR, Seasonal Agricultural Survey 2026 Season B
        </p>
      </footer>
    </div>
  )
}

export default App
