<template>
  <q-page class="row items-center justify-evenly q-gutter-lg bg-grey-2">
    <table-pokemon class="col-12"/>
  </q-page>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import TablePokemon from 'src/components/tables/TablePokemon.vue';

@Component({
  components: {
    TablePokemon,
  },
})
export default class PageIndex extends Vue {
}
</script>
