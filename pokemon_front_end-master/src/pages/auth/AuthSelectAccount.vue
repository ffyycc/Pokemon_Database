<template>
  <div class="row q-gutter-lg">
    <q-btn
      class="bg-white q-pa-none"
      no-caps
      v-for="account in accounts"
      :key="account.user_id"
      @click="jumpToLogin(account)"
    >
      <card-user-portrait
        :user="account"
        class="cursor-pointer bg-transparent"
      />
    </q-btn>
    <q-btn no-caps class="bg-white q-pa-none" @click="jumpToQuery">
      <card-user-portrait
        :user="addUserAccount"
        class="cursor-pointer bg-transparent"
        />
    </q-btn>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import CardUserPortrait from 'src/components/cards/CardUserPortrait.vue';

@Component({
  components: {
    CardUserPortrait,
  },
})
export default class SelectAccount extends Vue {
/* eslint-disable @typescript-eslint/no-unsafe-return */
/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-floating-promises */
/* eslint-disable @typescript-eslint/no-unsafe-assignment */
/* eslint-disable @typescript-eslint/no-unsafe-call */
/* eslint-disable @typescript-eslint/adjacent-overload-signatures */
  addUserAccount = {
    user_id: -1,
    portrait: 'https://www.freepnglogos.com/pics/plus-icon',
    email: 'Add Account',
  };

  accounts = [];

  jumpToLogin() {
    // TODO: should pass user info to login page
    this.$router.push('/auth/login');
  }

  jumpToQuery() {
    // console.log("Should jump to Query Page");
    this.$router.push('/auth/query');
  }
}
</script>
