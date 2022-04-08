import store from './store'

export function userHasPermission (permission) {
  let profile = store.state.profile
  if (profile.permissions) {
    return profile.permissions[permission] === true || profile.permissions['SUPERUSER'] === true
  }
  return false
}

export function setSideMenu (menu) {
  store.commit('setSideMenu', menu)
}