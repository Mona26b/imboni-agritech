// National-level statistics from NISR Seasonal Agricultural Survey 2026 Season B

export const overview = {
  totalLand: 2376298,          // hectares
  agriculturalLand: 1413813,   // hectares
  agriculturalPercent: 59.5,
  seasonalCropsLand: 1022374,  // hectares
  permanentCropsLand: 525525,  // hectares
  permanentPasture: 83419,     // hectares
}

export const surveyInfo = {
  districts: 30,
  segments: 1200,
  largeScaleFarmers: 505,
  dataCollectionStart: 'April 19, 2026',
  dataCollectionEnd: 'June 28, 2026',
  period: 'March 2026 – June 2026',
}

export const farmingPractices = {
  improvedSeeds: { overall: 20.9, ssf: 19.4, lsf: 65 },
  organicFertilizer: { overall: 81.3, ssf: 81.7, lsf: 71.3 },
  inorganicFertilizer: { overall: 57.5, ssf: 56.7, lsf: 80.2 },
  pesticides: { overall: 39.1, ssf: 37.7, lsf: 80 },
  irrigation: { overall: 13.1 },
  agroforestry: { overall: 58 },
  mechanization: { overall: 1.8 },
}

export const topCrops = [
  { name: 'Bean', area: 333735, unit: 'ha' },
  { name: 'Banana', area: 250772, unit: 'ha' },
  { name: 'Cassava', area: 192305, unit: 'ha' },
  { name: 'Sorghum', area: 103139, unit: 'ha' },
  { name: 'Maize', area: 94823, unit: 'ha' },
  { name: 'Cooking banana', area: 97498, unit: 'ha' },
  { name: 'Sweet potato', area: 84775, unit: 'ha' },
  { name: 'Irish potato', area: 48424, unit: 'ha' },
]
