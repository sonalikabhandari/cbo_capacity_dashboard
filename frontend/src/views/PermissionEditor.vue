<template>
  <v-container fluid>
    <v-row>
      <v-col class="ml-0 mt-0 pa-1" cols="12">
        <v-card ml-5 mt-5 class="elevation-10">
          <v-card-title>
            <span class="subtitle-2">Edit {{ type }} permissions...</span>
            <v-col cols="3">
              <v-text-field
                append-icon="search"
                :label="typeFilterLabel"
                v-model="search"
              ></v-text-field>
            </v-col>
            <v-col cols="2">
              <v-select
                :items="groups"
                multiple
                label="Filter by Group Role"
                v-model="filterGroup"
              >
                <template v-slot:selection="{ item, index }">
                  <v-chip v-if="index === 0" small>
                    <span>{{ item }}</span>
                  </v-chip>
                  <span v-if="index === 1" class="grey--text caption">
                    {{ displayLength(filterGroup.length - 1) }}
                  </span>
                </template>
              </v-select>
            </v-col>
          </v-card-title>
          <v-data-table
            :headers="headers"
            :items="tableData"
            item-key="id"
            class="elevation-10"
            :items-per-page="10"
          >
            <template
              v-slot:item.action="{ item }"
            >
              <permission-dialog
                :id="item.id"
                :type="type"
                :groups="groups"
                :permissions="permissions"
                @save="loadData"
              ></permission-dialog>
            </template>

          </v-data-table>

        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { getDepartmentPermissions, getUserPermissions } from '@/api'
import PermissionDialog from '@/components/admin/PermissionDialog'

export default {
  name: 'PermissionEditor',
  props: {
    type: undefined
  },
  components: {
    PermissionDialog
  },
  data () {
    return {
      groups: [],
      permissions: [],
      search: undefined,
      filterGroup: undefined
    }
  },
  computed: {
    formatType () {
      return this.type[0].toUpperCase() + this.type.slice(1)
    },
    headers () {
      let headers = [
        {
          text: 'Update',
          align: 'start',
          value: 'action',
          width: '1'
        },
        {
          text: this.formatType,
          align: 'end',
          value: this.type,
          filter: value => {
            if (!this.search) return true
            if (this.search.length === 0) return true
            return value.toLowerCase().includes(this.search.toLowerCase())
          }
        }
      ]

      this.groups.forEach((group, index, arr) => {
        headers.push({
          text: group,
          align: 'end',
          value: group
        })
      })

      return headers
    },
    tableData () {
      let data = []
      this.permissions.forEach((permission, index, arr) => {
        let obj = { id: permission.id }
        obj[this.type] = permission[this.type]
        let settings = permission.settings
        settings.forEach((group, index, arr) => {
          obj[group.name] = group.value ? 'Yes' : 'No'
        })
        // I have my group filter here due to it being dynamic to the groups
        // in the system.  We will return any matches and all if no filter is set
        // might be a better way to accomplish this under headers, idk???
        if (!this.filterGroup || this.filterGroup.length === 0) {
          data.push(obj)
        } else {
          this.filterGroup.some((group, index, arr) => {
            if (obj[group] === 'Yes') {
              data.push(obj)
              return true
            }
          })
        }
      })
      return data
    },
    typeFilterLabel () {
      return `Filter by ${this.type}`
    }
  },
  methods: {
    async loadData () {
      if (this.type === 'department') {
        let response = await getDepartmentPermissions()
        let data = response.data
        this.groups = data.groups
        this.permissions = data.permissions
      } else if (this.type === 'user') {
        let response = await getUserPermissions()
        let data = response.data
        this.groups = data.groups
        this.permissions = data.permissions
      } else {
        this.groups = undefined
        this.permissions = undefined
      }
    },
    displayLength (len) {
      let end = 'other'
      if (len > 1) end = end + 's'
      return `(+${len} ${end})`
    }
  },
  beforeMount () {
    this.loadData()
  },
  watch: {
    type () {
      this.loadData()
    }
  }
}

</script>

<style scoped>
.table {
  background-color: #fff;
  color: #363636;
  border-collapse: collapse;
  border-spacing: 0;
}

.is-fullwidth {
  width: 100%;
}
</style>
