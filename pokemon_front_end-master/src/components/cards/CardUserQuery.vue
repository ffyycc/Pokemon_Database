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

    <!-- Query Section -->
    <q-card-section>
      <q-list>
        <q-item dense>
          <q-item-section avatar>
            Email
          </q-item-section>
          <q-item-section>
            <q-input dense
              v-model="email"
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
              label="Next"
              @click="queryUser"/>
          </q-item-section>
        </q-item>
      </q-list>
    </q-card-section>
  </q-card>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import { State, Mutation } from 'vuex-class';
import BtnBack from 'src/components/buttons/BtnBack.vue';
import CardUserPortrait from 'src/components/cards/CardUserPortrait.vue';
import { UserStateInterface } from 'src/store/userStore/state';

@Component({
  components: {
    CardUserPortrait,
    BtnBack,
  },
})
export default class CardUserQuery extends Vue {
  /* eslint-disable @typescript-eslint/no-unsafe-return */
  /* eslint-disable @typescript-eslint/no-unsafe-member-access */
  /* eslint-disable @typescript-eslint/no-floating-promises */
  /* eslint-disable @typescript-eslint/no-unsafe-assignment */
  /* eslint-disable @typescript-eslint/no-unsafe-call */
  /* eslint-disable @typescript-eslint/adjacent-overload-signatures */
  /* eslint-disable no-void */
  /* eslint-disable no-unused-vars */
  @State('user') userStore!: UserStateInterface;

  @Mutation('UPDATE_EMAIL', { namespace: 'user' }) updateNickname!;

  get user() {
    return this.userStore;
  }

  get email() {
    return this.user.email;
  }

  set email(newName) {
    this.updateNickname(newName);
  }

  queryUser() {
    if (!this.user.email.trim().length) {
      this.$q.notify({
        color: 'danger',
        message: 'Email cannot be empty',
      });
      return;
    }
    this.$axios.post('/user/exists', {
      email: this.user.email,
    })
      .then((response) => {
        const { user } = this;
        if (response.data.exists) {
          void this.$router.replace({
            path: '/auth/login',
          });
        } else {
          void this.$router.replace('/auth/register');
        }
      })
      .catch((error) => {
        console.log(error);
        this.$q.notify({
          color: 'danger',
          message: error.message,
        });
      });
  }
}
</script>
