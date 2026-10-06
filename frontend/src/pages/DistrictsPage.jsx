import { useState } from 'react'
import { Link } from 'react-router-dom'
import { districts, provinces, provinceColors } from '../data/districts'

function DistrictsPage() {
  const [search, setSearch] = useState('')
  const [provinceFilter, setProvinceFilter] = useState('All')

  const filtered = districts.filter((d) => {
    const matchesSearch = d.name.toLowerCase().includes(search.toLowerCase())
    const matchesProvince = provinceFilter === 'All' || d.province === provinceFilter
    return matchesSearch && matchesProvince
  })

  return (
    <main className="max-w-6xl mx-auto px-6 py-12">
      <div className="mb-8">
        <h1 className="text-4xl font-bold text-farm-dark mb-2">🌾 Districts</h1>
        <p className="text-gray-600">
          Explore agricultural data for all 30 districts of Rwanda
        </p>
      </div>

      {/* Filters */}
      <div className="mb-8 flex flex-col md:flex-row gap-4">
        <input
          type="text"
          placeholder="Search district..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-farm-green"
        />
        <select
          value={provinceFilter}
          onChange={(e) => setProvinceFilter(e.target.value)}
          className="px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-farm-green bg-white"
        >
          <option value="All">All Provinces</option>
          {provinces.map((p) => (
            <option key={p} value={p}>{p}</option>
          ))}
        </select>
      </div>

      {/* Results count */}
      <p className="text-sm text-gray-500 mb-4">
        Showing {filtered.length} of {districts.length} districts
      </p>

      {/* District grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filtered.map((district) => (
          <Link
            key={district.name}
            to={`/districts/${district.name}`}
            className="bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition-all hover:-translate-y-1 border-t-4 border-farm-green"
          >
            <div className="flex items-start justify-between mb-3">
              <h3 className="text-xl font-bold text-farm-dark">{district.name}</h3>
              <span className={`text-xs px-2 py-1 rounded-full font-semibold ${provinceColors[district.province]}`}>
                {district.province}
              </span>
            </div>
            <div className="space-y-2 text-sm">
              <div className="flex justify-between">
                <span className="text-gray-500">Total land:</span>
                <span className="font-semibold">{district.totalLand.toFixed(1)}k ha</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-500">Agricultural:</span>
                <span className="font-semibold text-farm-green">
                  {district.agriPercent.toFixed(1)}%
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-500">Organic fertilizer:</span>
                <span className="font-semibold">{district.organicFert.toFixed(0)}%</span>
              </div>
            </div>
            <div className="mt-4 text-farm-green text-sm font-semibold">
              View details →
            </div>
          </Link>
        ))}
      </div>

      {filtered.length === 0 && (
        <div className="text-center py-16 text-gray-500">
          <p className="text-xl mb-2">🔍 No districts found</p>
          <p className="text-sm">Try a different search term or province filter.</p>
        </div>
      )}
    </main>
  )
}

export default DistrictsPage
