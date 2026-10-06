import { Link } from 'react-router-dom'

function Hero() {
  return (
    <section className="text-center">
      <h2 className="text-5xl font-bold text-farm-dark mb-6">
        Data-driven agriculture for Rwanda
      </h2>
      <p className="text-xl text-farm-earth mb-8 max-w-2xl mx-auto">
        Explore seasonal crop data, fertilizer usage, and farming practices 
        across all 30 districts — powered by the Seasonal Agricultural Survey 2026.
      </p>
      <Link
        to="/dashboard"
        className="inline-block bg-farm-green hover:bg-farm-dark text-white px-8 py-3 rounded-lg text-lg font-semibold transition-colors"
      >
        Explore the Data →
      </Link>
    </section>
  )
}

export default Hero
