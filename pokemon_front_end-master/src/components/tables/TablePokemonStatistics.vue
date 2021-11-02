<template>
  <q-table
    grid
    title="Pokemon Statistics for HP"
    :columns="columns"
    :data="pokemonStatistics"
  />
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';

@Component
export default class TablePokemonStatistics extends Vue {
  /* eslint-disable @typescript-eslint/no-unsafe-assignment */
  columns = [
    {
      name: 'Pokemon ID', label: 'Pokemon ID', field: 'pokemon_ID', sortable: true, required: true,
    },
    {
      name: 'Training Count', label: 'Training Count', field: 'training_count', sortable: true, required: true,
    },
  ];

  pokemonStatistics = [];

  created() {
    this.$axios.get('public_info/statistics')
      .then((response) => {
        this.pokemonStatistics = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }
}
</script>
