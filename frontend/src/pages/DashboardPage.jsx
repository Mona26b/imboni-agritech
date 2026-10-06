import { overview, surveyInfo, farmingPractices, topCrops } from '../data/nationalStats'

function formatNumber(n) {
  return n.toLocaleString('en-US')
}

function StatCard({ label, value, sub, icon }) {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
      <div className="text-3xl mb-2">{icon}</div>
      <div className="text-3xl font-bold text-farm-green mb-1">{value}</div>
      <div className="text-sm font-semibold text-farm-dark">{label}</div>
      {sub && <div className="text-xs text-gray-500 mt-1">{sub}</div>}
    </div>
  )
}

function PracticeBar({ label, value, ssf, lsf }) {
  return (
    <div className="mb-4">
      <div className="flex justify-between mb-1">
        <span className="font-semibold text-farm-dark">{label}</span>
        <span className="text-farm-green font-bold">{value}%</span>
      </div>
      <div className="w-full bg-gray-200 rounded-full h-2 mb-1">
        <div
          className="bg-farm-green h-2 rounded-full transition-all"
          style={{ width: `${value}%` }}
        />
      </div>
      {(ssf !== undefined || lsf !== undefined) && (
        <div className="flex justify-between text-xs text-gray-500">
          <span>Small-scale: {ssf}%</span>
          <span>Large-scale: {lsf}%</span>
        </div>
      )}
    </div>
  )
}

function DashboardPage() {
  return (
    <main className="max-w-6xl mx-auto px-6 py-12">
      <div className="mb-10">
        <h1 className="text-4xl font-bold text-farm-dark mb-2">📊 National Dashboard</h1>
        <p className="text-gray-600">
          Season B 2026 · Data collected {surveyInfo.dataCollectionStart} – {surveyInfo.dataCollectionEnd}
        </p>
      </div>

      <section className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-12">
        <StatCard icon="🗺️" value={surveyInfo.districts} label="Districts covered" />
        <StatCard icon="📍" value={formatNumber(surveyInfo.segments)} label="Sampled segments" />
        <StatCard icon="👨‍🌾" value={surveyInfo.largeScaleFarmers} label="Large-scale farmers" />
        <StatCard icon="📅" value="Season B" label="2026 agricultural season" />
      </section>

      <section className="mb-12">
        <h2 className="text-2xl font-bold text-farm-dark mb-4">🌍 Land Use</h2>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <StatCard
            icon="🌱"
            value={`${(overview.totalLand / 1000000).toFixed(3)}M ha`}
            label="Total land area"
          />
          <StatCard
            icon="🌾"
            value={`${(overview.agriculturalLand / 1000000).toFixed(3)}M ha`}
            label="Agricultural land"
            sub={`${overview.agriculturalPercent}% of total`}
          />
          <StatCard
            icon="🌿"
            value={`${(overview.seasonalCropsLand / 1000000).toFixed(3)}M ha`}
            label="Seasonal crops"
          />
          <StatCard
            icon="🌳"
            value={`${(overview.permanentCropsLand / 1000000).toFixed(3)}M ha`}
            label="Permanent crops"
          />
        </div>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl font-bold text-farm-dark mb-4">🚜 Farming Practices</h2>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <PracticeBar
            label="Organic fertilizer"
            value={farmingPractices.organicFertilizer.overall}
            ssf={farmingPractices.organicFertilizer.ssf}
            lsf={farmingPractices.organicFertilizer.lsf}
          />
          <PracticeBar
            label="Inorganic fertilizer"
            value={farmingPractices.inorganicFertilizer.overall}
            ssf={farmingPractices.inorganicFertilizer.ssf}
            lsf={farmingPractices.inorganicFertilizer.lsf}
          />
          <PracticeBar
            label="Improved seeds"
            value={farmingPractices.improvedSeeds.overall}
            ssf={farmingPractices.improvedSeeds.ssf}
            lsf={farmingPractices.improvedSeeds.lsf}
          />
          <PracticeBar
            label="Pesticides"
            value={farmingPractices.pesticides.overall}
            ssf={farmingPractices.pesticides.ssf}
            lsf={farmingPractices.pesticides.lsf}
          />
          <PracticeBar
            label="Agroforestry"
            value={farmingPractices.agroforestry.overall}
          />
          <PracticeBar
            label="Irrigation"
            value={farmingPractices.irrigation.overall}
          />
          <PracticeBar
            label="Mechanization"
            value={farmingPractices.mechanization.overall}
          />
        </div>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl font-bold text-farm-dark mb-4">🌾 Top Crops by Area</h2>
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          <table className="w-full">
            <thead className="bg-farm-dark text-white">
              <tr>
                <th className="text-left p-4">Crop</th>
                <th className="text-right p-4">Area (ha)</th>
              </tr>
            </thead>
            <tbody>
              {topCrops.map((crop) => (
                <tr key={crop.name} className="border-b hover:bg-farm-light">
                  <td className="p-4 font-medium">{crop.name}</td>
                  <td className="p-4 text-right text-farm-green font-bold">
                    {formatNumber(crop.area)}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <div className="text-xs text-gray-500 text-center mt-8">
        Source: NISR, Seasonal Agricultural Survey 2026 Season B
      </div>
    </main>
  )
}

export default DashboardPage
