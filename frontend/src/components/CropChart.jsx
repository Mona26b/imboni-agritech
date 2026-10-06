import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'
import { topCrops } from '../data/nationalStats'

function CropChart() {
  const data = topCrops.map((c) => ({
    name: c.name,
    area: c.area / 1000, // thousands of hectares for readability
  }))

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h3 className="text-xl font-bold text-farm-dark mb-4">
        🌾 Top Crops by Area (thousands of hectares)
      </h3>
      <ResponsiveContainer width="100%" height={350}>
        <BarChart data={data} margin={{ top: 10, right: 20, left: 0, bottom: 60 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" />
          <XAxis
            dataKey="name"
            angle={-35}
            textAnchor="end"
            interval={0}
            tick={{ fontSize: 12 }}
            height={80}
          />
          <YAxis tick={{ fontSize: 12 }} />
          <Tooltip
            formatter={(value) => [`${value.toFixed(1)}k ha`, 'Area']}
            contentStyle={{ borderRadius: '8px', border: '1px solid #16a34a' }}
          />
          <Bar dataKey="area" fill="#16a34a" radius={[6, 6, 0, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}

export default CropChart
