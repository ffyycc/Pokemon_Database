<template>
  <q-table
    flat
    title="User"
    :columns="usercolumns"
    :data="users"
    :loading="loading"
  >
    <template v-slot:top-right>
      <div class="row q-gutter-sm">
        <q-btn
          class="col-auto"
          color="secondary"
          label="create user"
          @click="createUser"
        />
        <q-card bordered flat class="col">
          <q-item>
            <q-item-section avatar class="text-grey">
              User ID
            </q-item-section>
            <q-item-section>
              <q-input
                v-model="searchID"
                use-input
                dense
                type="number"
                @blur="searchUser"
              >
                <template v-slot:append>
                  <q-btn
                    flat
                    icon="search"
                    @click="searchUser"
                  />
                </template>
              </q-input>
            </q-item-section>
          </q-item>
        </q-card>
      </div>
    </template>

    <template v-slot:body="props">
      <q-tr :props="props">
        <q-td key="user_id" :props="props">
          {{ props.row.user_id }}
          <q-btn
            flat dense round
            icon="close"
            @click="deleteUser(props.row.user_id)"/>
        </q-td>
        <q-td key="userName" :props="props">
          {{ props.row.userName }}
          <q-popup-edit v-model.number="props.row.userName"
                        buttons
                        @save="updateUser(props.row)"
          >
            <q-input
              v-model.number="props.row.userName"
              type="text"
              dense autofocus counter
            />
          </q-popup-edit>
        </q-td>
        <q-td key="userPassword" :props="props">
          {{ props.row.userPassword }}
          <q-popup-edit v-model.number="props.row.userPassword"
                        buttons
                        @save="updateUser(props.row)"
          >
            <q-input
              v-model.number="props.row.userPassword"
              type="text"
              dense autofocus counter
            />
          </q-popup-edit>
        </q-td>
        <q-td key="userEmail" :props="props">
          {{ props.row.userEmail }}
          <q-popup-edit v-model.number="props.row.userEmail"
                        buttons
                        @save="updateUser(props.row)"
          >
            <q-input
              v-model.number="props.row.userEmail"
              type="text"
              dense autofocus counter
            />
          </q-popup-edit>
        </q-td>
        <q-td key="privacy" :props="props">
          {{ props.row.privacy }}
          <q-popup-edit v-model.number="props.row.privacy"
                        buttons
                        @save="updateUser(props.row)"
          >
            <q-input
              v-model.number="props.row.privacy"
              type="number"
              dense autofocus counter
            />
          </q-popup-edit>
        </q-td>
      </q-tr>
    </template>
  </q-table>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';

@Component
export default class TableUser extends Vue {
/* eslint-disable @typescript-eslint/no-unsafe-return */
/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-floating-promises */
/* eslint-disable @typescript-eslint/no-unsafe-assignment */
/* eslint-disable class-methods-use-this */
/* eslint-disable consistent-return */
/* eslint-disable no-unused-vars */
/* eslint-disable camelcase */
/* eslint-disable @typescript-eslint/restrict-template-expressions */
  searchID = 0

  usercolumns = [
    {
      name: 'user_id', label: 'userID', field: 'user_id', required: true,
    },
    {
      name: 'userName', label: 'userName', field: 'userName', required: true,
    },
    {
      name: 'userPassword', label: 'userPassword', field: 'userPassword', required: true,
    },
    {
      name: 'userEmail', label: 'userEmail', field: 'userEmail', required: true,
    },
    {
      name: 'privacy', label: 'privacy', field: 'privacy', required: true,
    },
  ];

  users = [];

  loading = false;

  created() {
    this.getUser();
  }

  createUser() {
    this.$q.notify({
      color: 'primary',
      message: 'Creating user...',
    });

    this.$axios.post('/user/create', {
    })
      .then((response) => {
        this.$q.notify({
          color: 'primary',
          message: `${response.data.message}!Welcome user!`,
        });
        this.getUser();
      })
      .catch((error) => {
        console.log(error);
      });
  }

  getUser() {
    this.loading = true;
    this.$q.notify({
      color: 'primary',
      message: 'select user...',
    });

    this.$axios.get('/user/front10')
      .then((response) => {
        console.log(response);
        this.users = response.data;
        this.$q.notify({
          color: 'primary',
          message: 'Find top 10 users!',
        });
      })
      .catch((error) => {
        console.log(error);
        this.$q.notify({
          color: 'danger',
          message: error.message,
        });
      })
      .finally(() => {
        this.loading = false;
      });
  }

  searchUser() {
    if (this.searchID === '') {
      return this.getUser();
    }

    this.$q.notify({
      color: 'primary',
      message: `fetching user with id ${this.searchID}`,
    });

    this.$axios.post('/user/search', {
      user_id: this.searchID,
    })
      .then((response) => {
        console.log(response);
        this.users = response.data;
        this.$q.notify({
          color: 'primary',
          message: 'Gotcha!',
        });
        this.searchID = 0;
      })
      .catch((error) => {
        console.log(error);
        this.$q.notify({
          color: 'danger',
          message: error.message,
        });
      });
  }

  updateUser(row) {
    this.$q.notify({
      color: 'primary',
      message: 'updating pokemon...',
    });

    this.$axios.post('/user/update', {
      user_id: row.user_id,
      userName: row.userName,
      userPassword: row.userPassword,
      userEmail: row.userEmail,
      privacy: row.privacy,
    })
      .then((response) => {
        this.$q.notify({
          color: 'primary',
          message: response.data.message,
        });
      })
      .catch((error) => {
        this.$q.notify({
          color: 'danger',
          message: error.message,
        });
      });
  }

  deleteUser(user_id) {
    this.$q.notify({
      color: 'primary',
      message: `deleting user with id ${user_id}`,
    });

    this.$axios.post('/user/delete', {
      user_id,
    })
      .then((response) => {
        this.$q.notify({
          color: 'primary',
          message: response.data.message,
        });
      })
      .catch((error) => {
        this.$q.notify({
          color: 'danger',
          message: error.message,
        });
      })
      .finally(() => {
        this.getUser();
      });
  }
}
</script>
