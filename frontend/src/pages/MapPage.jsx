import { useEffect, useState } from 'react'
import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet'
import { useNavigate } from 'react-router-dom'
import { districts } from '../data/districts'

const provinceColor = {
  Kigali: '#a855f7',
  Southern: '#16a34a',
  Western: '#3b82f6',
  Northern: '#eab308',
  Eastern: '#f97316',
}

function MapPage() {
  const [geoData, setGeoData] = useState(null)
  const navigate = useNavigate()

  useEffect(() => {
    fetch('/rwanda-districts.geojson')
      .then((res) => res.json())
      .then((data) => setGeoData(data))
      .catch((err) => console.error('Failed to load GeoJSON:', err))
  }, [])

  const findDistrict = (name) =>
    districts.find((d) => d.name.toLowerCase() === name.toLowerCase())

  const styleFeature = (feature) => {
    const district = findDistrict(feature.properties.shapeName)
    const color = district ? provinceColor[district.province] : '#9ca3af'
    return {
      fillColor: color,
      weight: 1.5,
      opacity: 1,
      color: '#ffffff',
      fillOpacity: 0.65,
    }
  }

  const onEachFeature = (feature, layer) => {
    const district = findDistrict(feature.properties.shapeName)

    const tooltipContent = district
      ? '<div style="font-family: sans-serif; padding: 4px;">' +
        '<strong style="color: #14532d; font-size: 14px;">' + district.name + '</strong><br/>' +
        '<span style="color: #666; font-size: 11px;">' + district.province + ' Province</span><br/>' +
        '<span style="font-size: 12px;">' + district.agriPercent.toFixed(1) + '% agricultural</span><br/>' +
        '<span style="font-size: 12px;">' + district.seasonalCrops.toFixed(1) + 'k ha seasonal crops</span>' +
        '</div>'
      : '<strong>' + feature.properties.shapeName + '</strong>'

    layer.bindTooltip(tooltipContent, { sticky: true })

    layer.on({
      mouseover: (e) => {
        e.target.setStyle({ weight: 3, color: '#14532d', fillOpacity: 0.9 })
        e.target.bringToFront()
      },
      mouseout: (e) => {
        e.target.setStyle({ weight: 1.5, color: '#ffffff', fillOpacity: 0.65 })
      },
      click: () => {
        navigate('/districts/' + feature.properties.shapeName)
      },
    })
  }

  return (
    <main className="max-w-6xl mx-auto px-6 py-12">
      <div className="mb-6">
        <h1 className="text-4xl font-bold text-farm-dark mb-2">Interactive Map</h1>
        <p className="text-gray-600">Click a district to see its agricultural profile</p>
      </div>

      <div className="bg-white rounded-lg shadow-lg overflow-hidden relative" style={{ height: '600px' }}>
        {geoData ? (
          <MapContainer
            center={[-1.94, 29.87]}
            zoom={8}
            style={{ height: '100%', width: '100%' }}
            scrollWheelZoom={true}
          >
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <GeoJSON data={geoData} style={styleFeature} onEachFeature={onEachFeature} />
          </MapContainer>
        ) : (
          <div className="h-full flex items-center justify-center text-gray-500">Loading map...</div>
        )}

        <div className="absolute bottom-4 right-4 bg-white p-3 rounded-lg shadow-lg z-[1000] text-xs">
          <div className="font-bold text-farm-dark mb-2">Province</div>
          {Object.entries(provinceColor).map(([province, color]) => (
            <div key={province} className="flex items-center gap-2 mb-1">
              <span
                style={{
                  backgroundColor: color,
                  width: '12px',
                  height: '12px',
                  display: 'inline-block',
                  borderRadius: '2px',
                }}
              />
              <span>{province}</span>
            </div>
          ))}
        </div>
      </div>

      <p className="text-xs text-gray-500 text-center mt-4">
        Boundaries: geoBoundaries · Data: NISR SAS 2026
      </p>
    </main>
  )
}

export default MapPage
