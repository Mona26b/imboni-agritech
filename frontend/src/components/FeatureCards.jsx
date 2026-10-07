function FeatureCards() {
  const cards = [
    { title: 'District coverage', desc: 'Agricultural indicators across all Rwanda districts.' },
    { title: 'Crop indicators', desc: 'Area, production, and yield by crop and district.' },
    { title: 'Practice trends', desc: 'Fertilizer, seed, irrigation, and land management patterns.' },
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
