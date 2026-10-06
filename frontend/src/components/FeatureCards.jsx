function FeatureCards() {
  const cards = [
    { title: '30 Districts', desc: 'Complete seasonal crop and land-use data' },
    { title: '15+ Crops', desc: 'Maize, beans, cassava, banana, and more' },
    { title: 'Interactive Map', desc: 'Visualize data district by district' },
  ]

  return (
    <section className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-20">
      {cards.map((c) => (
        <div key={c.title} className="bg-white p-6 rounded-lg shadow-md border-t-4 border-farm-green">
          <h3 className="text-xl font-bold text-farm-dark mb-2">{c.title}</h3>
          <p className="text-gray-600">{c.desc}</p>
        </div>
      ))}
    </section>
  )
}

export default FeatureCards
