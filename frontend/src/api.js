import Vue from 'vue'

// Token related URLs
const OBTAIN = '/auth/obtain/'
const REFRESH = '/auth/refresh/'

// Site URLs
const AUGMENT_VIEW = '/reports/augmentview/'
const AUGMENT_ENTRIES = '/reports/augment_entries/'
const CURRENT_CAPACITY = '/reports/current_capacity/'
const DASHBOARD = '/reports/dashboardview/'
const NODE = '/reports/node/'
const PATH = '/reports/path/'
const LOCATION = '/reports/location/'
const TRAFFIC_INFO = '/reports/traffic_info/'
const WCF_UTIL = '/reports/wcfutils/'
const SSP_UTIL = '/reports/ssputils/'
const CAP_ADDED = '/reports/augmentadded/'
const CAP_COUNT = '/reports/augmentcount/'
const TOTAL_CAP = '/reports/augmentChart/'
const DASHBOARDVIEW_MY = '/reports/dashboardviewfilterMY/'
const DASHBOARDVIEW_PATHINFO = '/reports/dashboardviewPathinfo/'

// Site Settings / Admin
const DEPARTMENT_PERMISSIONS = '/api/admin/functions/bps_admin/'
const USER_PERMISSIONS = '/api/admin/functions/user_admin/'
const SSP_UTIL_FILTER = '/reports/SSPUtilfilter/'
const WCF_UTIL_FILTER = '/reports/WCFUtilfilter/'

export function augmentEntries (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${AUGMENT_ENTRIES}`, { headers: headers })
}

export function augmentview (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${AUGMENT_VIEW}`, { headers: headers })
}

export async function authenticate (userData) {
  return Vue.axios.post(`${OBTAIN}`, userData)
}

export function currentCapacity (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${CURRENT_CAPACITY}`, { headers: headers })
}

export function dashboard (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${DASHBOARD}`, { headers: headers })
}

export function postdashboard (token, id) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${DASHBOARD}${id}/`, { headers: headers })
}


export function wcfUtilization (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${WCF_UTIL}`, { headers: headers })
}

export function wcfFilter (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${WCF_UTIL_FILTER}`, { headers: headers })
}

export function sspUtilization (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${SSP_UTIL}`, { headers: headers })
}

export function sspFilter (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${SSP_UTIL_FILTER}`, { headers: headers })
}

export function capacityAdded (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${CAP_ADDED}`, { headers: headers })
}

export function capacityCount (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${CAP_COUNT}`, { headers: headers })
}

export function totalcapacity (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${TOTAL_CAP}`, { headers: headers })
}

export function dashboardviewmy (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${DASHBOARDVIEW_MY}`, { headers: headers })
}

export function dashboardviewpathinfo (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${DASHBOARDVIEW_PATHINFO}`, { headers: headers })
}

export function location (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${LOCATION}`, { headers: headers })
}

export function node (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${NODE}`, { headers: headers })
}

export function path (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${PATH}`, { headers: headers })
}

export function trafficInfo (token) {
  const headers = {
    Authorization: `jwt ${token}`,
    'Content-Type': 'application/json'
  }
  return Vue.axios.get(`${TRAFFIC_INFO}`, { headers: headers })
}

export async function getDepartmentPermissions () {
  return Vue.axios.get(`${DEPARTMENT_PERMISSIONS}`)
}

export async function getUserPermissions () {
  return Vue.axios.get(`${USER_PERMISSIONS}`)
}

export async function refreshToken (token) {
  return Vue.axios.post(`${REFRESH}`, token)
}

export async function setDepartmentPermissions (permissions) {
  const id = permissions.id
  return Vue.axios.put(`${DEPARTMENT_PERMISSIONS}${id}/`, permissions)
}

export async function setUserPermissions (permissions) {
  const id = permissions.id
  return Vue.axios.put(`${USER_PERMISSIONS}${id}/`, permissions)
}
