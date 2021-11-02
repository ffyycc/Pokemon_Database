<template>
  <q-card flat v-bind="$attrs" v-on="$listeners">
    <q-card-section class="column justify-center">
      <div class="row justify-center">
        <q-avatar round size="100px">
          <img :src="portrait">
        </q-avatar>
      </div>
      <p class="col q-mt-md text-center">
        {{ email }}
      </p>
    </q-card-section>
  </q-card>
</template>

<script>
import { Vue, Component, Prop } from 'vue-property-decorator';

@Component()
export default class CardUserPortrait extends Vue {
  @Prop({
    default: {
      userId: 1,
      portrait: 'https://cdn.quasar.dev/img/parallax2.jpg',
      email: 'Adam Sandwitch',
    },
  }) user;

  // TODO: User Portrait Data Abstraction
  get portrait() {
    /* eslint-disable @typescript-eslint/no-unsafe-return */
    /* eslint-disable @typescript-eslint/no-unsafe-member-access */
    return this.user.portrait;
  }

  get email() {
    return this.user.email;
  }
}
</script>
