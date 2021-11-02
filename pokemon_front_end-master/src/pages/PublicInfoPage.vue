<template>
  <q-page class="row items-center justify-evenly q-gutter-lg bg-grey-2">
    <table-training class="col-12"
      :updatable="false"
    />
  </q-page>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import TableTraining from 'src/components/tables/TableTraining.vue';

@Component({
  components: {
    TableTraining,
  },
})
export default class PageName extends Vue {
}
</script>
