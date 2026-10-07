// All 30 districts of Rwanda with key agricultural statistics
// Source: NISR, Seasonal Agricultural Survey 2026 Season B

export const districts = [
  // KIGALI CITY
  { name: 'Nyarugenge', province: 'Kigali', totalLand: 13.09, agriLand: 7.85, agriPercent: 59.97, seasonalCrops: 4.57, permanentCrops: 3.31, organicFert: 64.66, inorganicFert: 34.59, erosionControl: 80.45, agroforestry: 57.07 },
  { name: 'Gasabo', province: 'Kigali', totalLand: 42.71, agriLand: 20.64, agriPercent: 48.33, seasonalCrops: 15.98, permanentCrops: 9.89, organicFert: 77.63, inorganicFert: 42.43, erosionControl: 89.80, agroforestry: 54.27 },
  { name: 'Kicukiro', province: 'Kigali', totalLand: 16.56, agriLand: 5.47, agriPercent: 33.03, seasonalCrops: 3.39, permanentCrops: 2.30, organicFert: 47.83, inorganicFert: 20.29, erosionControl: 73.91, agroforestry: 46.94 },

  // SOUTHERN PROVINCE
  { name: 'Nyanza', province: 'Southern', totalLand: 67.04, agriLand: 47.30, agriPercent: 70.55, seasonalCrops: 40.91, permanentCrops: 15.03, organicFert: 87.41, inorganicFert: 40.65, erosionControl: 97.12, agroforestry: 57.37 },
  { name: 'Gisagara', province: 'Southern', totalLand: 67.48, agriLand: 46.05, agriPercent: 68.24, seasonalCrops: 39.21, permanentCrops: 15.27, organicFert: 80.00, inorganicFert: 39.60, erosionControl: 94.80, agroforestry: 53.17 },
  { name: 'Nyaruguru', province: 'Southern', totalLand: 101.05, agriLand: 35.87, agriPercent: 35.50, seasonalCrops: 26.42, permanentCrops: 10.40, organicFert: 97.97, inorganicFert: 83.72, erosionControl: 99.71, agroforestry: 44.79 },
  { name: 'Huye', province: 'Southern', totalLand: 58.06, agriLand: 37.03, agriPercent: 63.78, seasonalCrops: 32.24, permanentCrops: 13.78, organicFert: 90.09, inorganicFert: 36.49, erosionControl: 93.47, agroforestry: 46.45 },
  { name: 'Nyamagabe', province: 'Southern', totalLand: 109.07, agriLand: 49.45, agriPercent: 45.34, seasonalCrops: 35.06, permanentCrops: 14.87, organicFert: 96.60, inorganicFert: 70.29, erosionControl: 97.28, agroforestry: 43.33 },
  { name: 'Ruhango', province: 'Southern', totalLand: 62.58, agriLand: 46.18, agriPercent: 73.79, seasonalCrops: 34.27, permanentCrops: 15.61, organicFert: 85.18, inorganicFert: 28.52, erosionControl: 95.31, agroforestry: 48.77 },
  { name: 'Muhanga', province: 'Southern', totalLand: 64.09, agriLand: 44.02, agriPercent: 68.68, seasonalCrops: 29.13, permanentCrops: 18.39, organicFert: 91.47, inorganicFert: 39.40, erosionControl: 96.77, agroforestry: 59.36 },
  { name: 'Kamonyi', province: 'Southern', totalLand: 65.75, agriLand: 48.99, agriPercent: 74.51, seasonalCrops: 36.33, permanentCrops: 19.48, organicFert: 87.22, inorganicFert: 35.90, erosionControl: 95.49, agroforestry: 52.06 },

  // WESTERN PROVINCE
  { name: 'Karongi', province: 'Western', totalLand: 78.81, agriLand: 44.62, agriPercent: 56.62, seasonalCrops: 29.02, permanentCrops: 20.71, organicFert: 95.02, inorganicFert: 64.48, erosionControl: 96.38, agroforestry: 50.18 },
  { name: 'Rutsiro', province: 'Western', totalLand: 66.06, agriLand: 35.94, agriPercent: 54.40, seasonalCrops: 21.23, permanentCrops: 14.59, organicFert: 96.88, inorganicFert: 64.58, erosionControl: 98.44, agroforestry: 51.91 },
  { name: 'Rubavu', province: 'Western', totalLand: 33.88, agriLand: 24.31, agriPercent: 71.76, seasonalCrops: 20.84, permanentCrops: 4.82, organicFert: 66.32, inorganicFert: 70.79, erosionControl: 94.21, agroforestry: 54.14 },
  { name: 'Nyabihu', province: 'Western', totalLand: 54.03, agriLand: 30.82, agriPercent: 57.04, seasonalCrops: 23.75, permanentCrops: 3.96, organicFert: 96.73, inorganicFert: 89.70, erosionControl: 98.49, agroforestry: 70.38 },
  { name: 'Ngororero', province: 'Western', totalLand: 66.66, agriLand: 43.83, agriPercent: 65.75, seasonalCrops: 29.00, permanentCrops: 15.31, organicFert: 97.53, inorganicFert: 81.07, erosionControl: 98.77, agroforestry: 60.22 },
  { name: 'Rusizi', province: 'Western', totalLand: 91.63, agriLand: 39.19, agriPercent: 42.77, seasonalCrops: 30.45, permanentCrops: 14.75, organicFert: 75.70, inorganicFert: 66.53, erosionControl: 92.23, agroforestry: 63.29 },
  { name: 'Nyamasheke', province: 'Western', totalLand: 94.77, agriLand: 37.14, agriPercent: 39.19, seasonalCrops: 27.92, permanentCrops: 17.80, organicFert: 90.32, inorganicFert: 70.75, erosionControl: 98.71, agroforestry: 62.79 },

  // NORTHERN PROVINCE
  { name: 'Rulindo', province: 'Northern', totalLand: 56.62, agriLand: 34.47, agriPercent: 60.88, seasonalCrops: 21.67, permanentCrops: 14.55, organicFert: 95.61, inorganicFert: 68.03, erosionControl: 96.55, agroforestry: 54.68 },
  { name: 'Gakenke', province: 'Northern', totalLand: 70.03, agriLand: 46.43, agriPercent: 66.29, seasonalCrops: 32.26, permanentCrops: 16.40, organicFert: 98.54, inorganicFert: 82.95, erosionControl: 99.17, agroforestry: 51.63 },
  { name: 'Musanze', province: 'Northern', totalLand: 50.92, agriLand: 30.47, agriPercent: 59.83, seasonalCrops: 22.73, permanentCrops: 4.60, organicFert: 87.86, inorganicFert: 74.76, erosionControl: 94.76, agroforestry: 50.38 },
  { name: 'Burera', province: 'Northern', totalLand: 58.42, agriLand: 37.73, agriPercent: 64.59, seasonalCrops: 29.20, permanentCrops: 4.79, organicFert: 85.74, inorganicFert: 63.10, erosionControl: 99.16, agroforestry: 56.18 },
  { name: 'Gicumbi', province: 'Northern', totalLand: 82.47, agriLand: 54.17, agriPercent: 65.69, seasonalCrops: 41.32, permanentCrops: 15.87, organicFert: 97.37, inorganicFert: 60.98, erosionControl: 98.87, agroforestry: 54.43 },

  // EASTERN PROVINCE
  { name: 'Rwamagana', province: 'Eastern', totalLand: 65.14, agriLand: 43.46, agriPercent: 66.71, seasonalCrops: 32.29, permanentCrops: 17.31, organicFert: 74.65, inorganicFert: 49.70, erosionControl: 90.62, agroforestry: 71.23 },
  { name: 'Nyagatare', province: 'Eastern', totalLand: 191.48, agriLand: 147.10, agriPercent: 76.82, seasonalCrops: 84.66, permanentCrops: 70.00, organicFert: 59.48, inorganicFert: 74.88, erosionControl: 80.89, agroforestry: 67.99 },
  { name: 'Gatsibo', province: 'Eastern', totalLand: 153.27, agriLand: 78.40, agriPercent: 51.15, seasonalCrops: 57.42, permanentCrops: 36.38, organicFert: 82.68, inorganicFert: 67.60, erosionControl: 96.37, agroforestry: 67.43 },
  { name: 'Kayonza', province: 'Eastern', totalLand: 179.99, agriLand: 89.34, agriPercent: 49.64, seasonalCrops: 58.81, permanentCrops: 40.94, organicFert: 72.62, inorganicFert: 58.94, erosionControl: 88.97, agroforestry: 58.60 },
  { name: 'Kirehe', province: 'Eastern', totalLand: 114.15, agriLand: 77.18, agriPercent: 67.61, seasonalCrops: 59.65, permanentCrops: 31.25, organicFert: 50.07, inorganicFert: 43.31, erosionControl: 82.90, agroforestry: 68.74 },
  { name: 'Ngoma', province: 'Eastern', totalLand: 80.26, agriLand: 56.45, agriPercent: 70.33, seasonalCrops: 44.12, permanentCrops: 25.92, organicFert: 48.53, inorganicFert: 28.68, erosionControl: 80.00, agroforestry: 61.29 },
  { name: 'Bugesera', province: 'Eastern', totalLand: 120.19, agriLand: 73.90, agriPercent: 61.49, seasonalCrops: 58.55, permanentCrops: 17.22, organicFert: 76.20, inorganicFert: 59.22, erosionControl: 81.28, agroforestry: 69.93 },
]

export const provinces = ['Kigali', 'Southern', 'Western', 'Northern', 'Eastern']

export function normalizeDistrictName(value) {
  return String(value ?? '')
    .trim()
    .toLowerCase()
}

export function slugifyDistrictName(value) {
  return normalizeDistrictName(value)
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
}

export function getDistrictByName(value) {
  const normalized = normalizeDistrictName(value)

  if (!normalized) {
    return undefined
  }

  return districts.find((district) => {
    const districtName = normalizeDistrictName(district.name)
    const districtSlug = slugifyDistrictName(district.name)
    return districtName === normalized || districtSlug === normalized
  })
}

export const provinceColors = {
  'Kigali': 'bg-purple-100 text-purple-800',
  'Southern': 'bg-green-100 text-green-800',
  'Western': 'bg-blue-100 text-blue-800',
  'Northern': 'bg-yellow-100 text-yellow-800',
  'Eastern': 'bg-orange-100 text-orange-800',
}
