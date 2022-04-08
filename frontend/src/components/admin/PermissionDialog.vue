<template>
  <v-dialog v-model="dialog" max-width="1280px">
    <template v-slot:activator="{ on }">
      <v-icon
        small
        v-on="on"
      >
        visibility
      </v-icon>
    </template>
    <v-card v-if="dialog === true">
      <v-card-title>
        <span class="headline">{{ formTitle }}:</span>
      </v-card-title>
      <v-card-text>
        <v-form ref="form">
          <v-container v-if="permissions">
            <span class="title">{{ whoAmIEditing }}:</span>
            <v-row>
              <template v-for="(group, index) in editedItem.settings">
                <v-col cols="12" sm="6" md="4" lg="2" :key="index">
                  <v-checkbox v-model="group.value" :label="group.name" />
                </v-col>
              </template>
            </v-row>
          </v-container>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <div class="flex-grow-1"></div>
        <v-btn color="blue darken-1" text @click="cancel">Cancel</v-btn>
        <v-btn
          color="blue darken-1"
          text
          @click="save"
        >
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { setDepartmentPermissions, setUserPermissions } from '@/api'

export default {
  props: {
    id: undefined,
    groups: undefined,
    permissions: undefined,
    type: undefined
  },
  data () {
    return {
      dialog: false,
      editedItem: {}
    }
  },
  computed: {
    formTitle () {
      if (this.type) {
        return this.type[0].toUpperCase() + this.type.slice(1) + ' Permission Editor'
      }
      return 'Invalid Dialog'
    },
    whoAmIEditing () {
      return this.editedItem[this.type]
    }
  },
  components: {

  },
  methods: {
    cancel () {
      this.dialog = false
    },
    async save () {
      try {
        if (this.type === 'department') {
          await setDepartmentPermissions(this.editedItem)
        } else {
          await setUserPermissions(this.editedItem)
        }
        this.$emit('save')
        this.dialog = false
      } catch (error) {
        console.error(error)
        window.alert('There was an error saving the permissions...')
      }
    },
    setItem () {
      if (this.id) {
        let item = this.permissions.find(obj => {
          return obj.id === this.id
        })
        this.editedItem = JSON.parse(JSON.stringify(item))
      } else {
        this.editedItem = {}
      }
    }
  },
  watch: {
    dialog () {
      this.setItem()
    }
  }
}
</script>
