import { useParams, Link } from 'react-router-dom'
import { districts, provinceColors } from '../data/districts'

function DistrictDetailPage() {
  const { districtName } = useParams()
  const district = districts.find((d) => d.name === districtName)

  if (!district) {
    return (
      <main className="max-w-6xl mx-auto px-6 py-16 text-center">
        <h1 className="text-3xl font-bold text-farm-dark mb-4">District not found</h1>
        <Link to="/districts" className="text-farm-green hover:underline">
          ← Back to all districts
        </Link>
      </main>
    )
  }

  const stats = [
    { label: 'Total land area', value: `${district.totalLand.toFixed(2)}k ha` },
    { label: 'Agricultural land', value: `${district.agriLand.toFixed(2)}k ha` },
    { label: '% agricultural', value: `${district.agriPercent.toFixed(1)}%` },
    { label: 'Seasonal crops', value: `${district.seasonalCrops.toFixed(2)}k ha` },
    { label: 'Permanent crops', value: `${district.permanentCrops.toFixed(2)}k ha` },
    { label: 'Erosion control', value: `${district.erosionControl.toFixed(1)}%` },
    { label: 'Agroforestry', value: `${district.agroforestry.toFixed(1)}%` },
    { label: 'Organic fertilizer', value: `${district.organicFert.toFixed(1)}%` },
    { label: 'Inorganic fertilizer', value: `${district.inorganicFert.toFixed(1)}%` },
  ]

  return (
    <main className="max-w-6xl mx-auto px-6 py-12">
      <Link to="/districts" className="text-farm-green hover:underline mb-4 inline-block">
        ← Back to all districts
      </Link>

      <div className="mb-8">
        <div className="flex items-center gap-4 mb-2">
          <h1 className="text-4xl font-bold text-farm-dark">{district.name}</h1>
          <span className={`text-sm px-3 py-1 rounded-full font-semibold ${provinceColors[district.province]}`}>
            {district.province} Province
          </span>
        </div>
        <p className="text-gray-600">
          Agricultural profile · Season B 2026
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {stats.map((s) => (
          <div key={s.label} className="bg-white p-6 rounded-lg shadow-md border-l-4 border-farm-green">
            <div className="text-2xl font-bold text-farm-green mb-1">{s.value}</div>
            <div className="text-sm text-farm-dark font-medium">{s.label}</div>
          </div>
        ))}
      </div>

      <div className="mt-12 bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-bold text-farm-dark mb-3">About this data</h2>
        <p className="text-gray-600 text-sm">
          Data comes from the NISR Seasonal Agricultural Survey (SAS) 2026 Season B,
          collected between April 19 and June 28, 2026. Percentages reflect the share
          of farmers or agricultural land in the district using each practice.
        </p>
      </div>
    </main>
  )
}

export default DistrictDetailPage
