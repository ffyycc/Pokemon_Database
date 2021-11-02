<template>
  <q-layout view="lHh Lpr lFf">
    <!-- header 对应了页面最顶端的蓝色条 -->
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          Quasar App
        </q-toolbar-title>

        <q-tabs v-model="tab" shrink stretch>
          <q-route-tab to="/" name="pokeindex" label="Pokemon Index" />
          <q-route-tab to="/training" name="training" label="My Hub" />
          <q-route-tab to="/publicinfo" name="publicinfo" label="Pokemon Hub" />
          <q-route-tab to="/statistics" name="Statistics" label="Statistics" />
        </q-tabs>
      </q-toolbar>
    </q-header>

    <!-- page-container 中会放入不同的页面 -->
    <q-page-container>
      <!-- 在不同的path下 router-view 会显示不同的 component -->
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import EssentialLink from 'components/EssentialLink.vue';
import { UserStateInterface } from 'src/store/userStore/state';
import { Vue, Component } from 'vue-property-decorator';
import { State } from 'vuex-class';

@Component({
  components: { EssentialLink },
})
export default class MainLayout extends Vue {
  @State('user') userStore!: UserStateInterface;

  leftDrawerOpen = false;

  tab = 'pokeindex';

  /* eslint-disable @typescript-eslint/no-unsafe-return */
  /* eslint-disable @typescript-eslint/no-unsafe-member-access */
  /* eslint-disable @typescript-eslint/no-floating-promises */
  /* eslint-disable @typescript-eslint/no-unsafe-assignment */
  /* eslint-disable @typescript-eslint/no-unsafe-call */
  /* eslint-disable @typescript-eslint/adjacent-overload-signatures */
  /* eslint-disable no-void */
  created() {
    if (!this.userStore.email.length) {
      void this.$router.push('/auth');
    }
  }
}
</script>
