import { Link } from 'react-router-dom'

function Hero() {
  return (
    <section className="text-center">
      <h2 className="text-5xl font-bold text-farm-dark mb-6">
        Rwanda agricultural data
      </h2>
      <p className="text-xl text-farm-earth mb-8 max-w-2xl mx-auto">
        Review land use, crop area, fertilizer use, and district-level farming trends from the 2026 Season B survey.
      </p>
      <Link
        to="/dashboard"
        className="inline-block bg-farm-green hover:bg-farm-dark text-white px-8 py-3 rounded-lg text-lg font-semibold transition-colors"
      >
        Open dashboard
      </Link>
    </section>
  )
}

export default Hero
