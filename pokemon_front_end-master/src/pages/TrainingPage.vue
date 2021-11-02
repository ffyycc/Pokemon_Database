<template>
  <q-page class="row items-center justify-evenly q-gutter-lg bg-grey-2">
    <table-training
      :trainerId="user.userId"
      :updatable="true"
      class="col-12"/>
  </q-page>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import TableTraining from 'src/components/tables/TableTraining.vue';
import { State } from 'vuex-class';
import { UserStateInterface } from 'src/store/userStore/state';

@Component({
  components: {
    TableTraining,
  },
})
export default class PageIndex extends Vue {
  @State('user') userStore!: UserStateInterface;

  get user() {
    return this.userStore;
  }
}
</script>
