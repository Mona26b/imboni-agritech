import { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import { farmingPractices } from '../data/nationalStats'

const COLORS = ['#16a34a', '#3b82f6', '#eab308', '#f97316', '#a855f7', '#06b6d4', '#6b7280']

function PracticesChart() {
  const data = [
    { name: 'Organic fertilizer', value: farmingPractices.organicFertilizer.overall },
    { name: 'Inorganic fertilizer', value: farmingPractices.inorganicFertilizer.overall },
    { name: 'Agroforestry', value: farmingPractices.agroforestry.overall },
    { name: 'Pesticides', value: farmingPractices.pesticides.overall },
    { name: 'Improved seeds', value: farmingPractices.improvedSeeds.overall },
    { name: 'Irrigation', value: farmingPractices.irrigation.overall },
    { name: 'Mechanization', value: farmingPractices.mechanization.overall },
  ]

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h3 className="text-xl font-bold text-farm-dark mb-4">
        🚜 Farming Practices Adoption (%)
      </h3>
      <ResponsiveContainer width="100%" height={350}>
        <PieChart>
          <Pie
            data={data}
            cx="50%"
            cy="50%"
            innerRadius={60}
            outerRadius={110}
            paddingAngle={2}
            dataKey="value"
            label={({ name, value }) => `${name}: ${value}%`}
            labelLine={false}
          >
            {data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip formatter={(value) => `${value}%`} />
        </PieChart>
      </ResponsiveContainer>
    </div>
  )
}

export default PracticesChart
