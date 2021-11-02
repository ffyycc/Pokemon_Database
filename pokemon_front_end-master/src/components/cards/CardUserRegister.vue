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
        <q-item dense>
          <q-item-section avatar>
            Confirm Password
          </q-item-section>
          <q-item-section>
            <q-input dense
              v-model="pwdConfirm"
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
              label="Continue"
              @click="tryRegister"/>
          </q-item-section>
        </q-item>
      </q-list>
    </q-card-section>
  </q-card>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import { State, Mutation } from 'vuex-class';
import CardUserPortrait from 'src/components/cards/CardUserPortrait.vue';
import BtnBack from 'src/components/buttons/BtnBack.vue';
import { UserStateInterface } from 'src/store/userStore/state';

const namespace = 'user';

@Component({
  components: {
    CardUserPortrait,
    BtnBack,
  },
})
export default class CardUserRegister extends Vue {
  /* eslint-disable @typescript-eslint/no-unsafe-return */
  /* eslint-disable @typescript-eslint/no-unsafe-member-access */
  /* eslint-disable @typescript-eslint/no-floating-promises */
  /* eslint-disable @typescript-eslint/no-unsafe-assignment */
  /* eslint-disable @typescript-eslint/no-unsafe-call */
  /* eslint-disable @typescript-eslint/adjacent-overload-signatures */
  /* eslint-disable no-void */
  /* eslint-disable no-unused-vars */
  @State('user') userStore!: UserStateInterface;

  @Mutation('UPDATE_USER_ID', { namespace }) updateUserId!: (val: number) => void;

  @Mutation('UPDATE_EMAIL', { namespace }) updateEmail!: (val: number) => void;

  get user() {
    return this.userStore;
  }

  pwd = '';

  pwdConfirm = '';

  created() {
    console.log(this.$route.params);
  }

  tryRegister() {
    // TODO: data connection
    // this.$router.push('/auth/profile');
    this.$axios.post('/user/register', {
      email: this.userStore.email,
      password: this.pwd,
    })
      .then((response) => {
        if (response.status === 200) {
          this.updateUserId(response.data.user.user_id);
          this.$router.push('/');
        } else {
          this.$q.notify({
            color: 'danger',
            message: response.data.message,
          });
        }
      })
      .catch((err) => {
        this.$q.notify({
          color: 'danger',
          message: err.message,
        });
      });
  }
}
</script>
