<template>
  <q-page class="row items-center justify-evenly q-gutter-lg bg-grey-2">
    <table-type-statistics class="col-12"/>
    <table-pokemon-statistics class="col-12"/>
    <table-high-data class="col-12"/>
    <table-advanced-query class="col-12"/>
  </q-page>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import TableTypeStatistics from 'src/components/tables/TableTypeStatistics.vue';
import TablePokemonStatistics from 'src/components/tables/TablePokemonStatistics.vue';
import TableHighData from 'src/components/tables/TableHighData.vue';
import TableAdvancedQuery from 'src/components/tables/TableAdvancedQuery.vue';

@Component({
  components: {
    TableTypeStatistics,
    TablePokemonStatistics,
    TableHighData,
    TableAdvancedQuery,
  },
})
export default class PageIndex extends Vue {
}
</script>
