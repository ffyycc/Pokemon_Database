<template>
  <q-card>
    <!-- Back Button Section -->
    <q-card-actions>
      <btn-back/>
    </q-card-actions>

    <!-- User Portrait Section -->
    <q-card-section>
      <card-user-portrait :user="user"/>
    </q-card-section>

    <!-- Password Section -->
    <q-card-section>
      <q-list>
        <q-item dense>
          <q-item-section avatar>
            Password
          </q-item-section>
          <q-item-section>
            <q-input dense
              v-model="pwd"
              type="password"
            />
          </q-item-section>
        </q-item>
      </q-list>
    </q-card-section>

    <!-- Confirm Register Section -->
    <q-card-section align="right">
      <q-list>
        <q-item>
          <q-item-section>
            <q-btn
              unelevated
              rounded
              class="q-px-md"
              color="primary"
              label="Login"
              @click="tryLogin"/>
          </q-item-section>
        </q-item>
      </q-list>
    </q-card-section>
  </q-card>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import CardUserPortrait from 'src/components/cards/CardUserPortrait.vue';
import BtnBack from 'src/components/buttons/BtnBack.vue';
import { Mutation, State } from 'vuex-class';
import { UserStateInterface } from 'src/store/userStore/state';

const namespace = 'user';

@Component({
  components: {
    CardUserPortrait,
    BtnBack,
  },
})
export default class CardUserLogin extends Vue {
  /* eslint-disable @typescript-eslint/no-unsafe-return */
  /* eslint-disable @typescript-eslint/no-unsafe-member-access */
  /* eslint-disable @typescript-eslint/no-floating-promises */
  /* eslint-disable @typescript-eslint/no-unsafe-assignment */
  @State('user') userStore!: UserStateInterface;

  @Mutation('UPDATE_USER_ID', { namespace }) updateUserId!: () => void;

  @Mutation('UPDATE_EMAIL', { namespace }) updateEmail!: () => void;

  get user() {
    return this.userStore;
  }

  // TODO: add user password data abstraction
  // TODO: add data validation functionality
  pwd = '';

  tryLogin() {
    this.$axios.post('/user/login', {
      email: this.user.email,
      password: this.pwd,
    })
      .then((res) => {
        console.log(res);
        if (res.status === 200) {
          this.updateUserId(res.data.user.user_id);
          this.updateEmail(res.data.user.userEmail);
          console.log(this.user);
          this.$router.push('/');
        } else {
          this.$q.notify({
            color: 'danger',
            message: res.data.message,
          });
        }
      })
      .catch((err) => {
        console.log(err);
        this.$q.notify({
          color: 'danger',
          message: 'Credential Not Match',
        });
      });
  }
}
</script>
