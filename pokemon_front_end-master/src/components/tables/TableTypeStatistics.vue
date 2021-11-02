<template>
  <q-table
    grid
    title="Type Statistics"
    :columns="columns"
    :data="typestatistics">

  </q-table>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';

@Component
export default class TableTypeStatistics extends Vue {
  /* eslint-disable @typescript-eslint/no-unsafe-return */
  /* eslint-disable @typescript-eslint/no-unsafe-member-access */
  /* eslint-disable @typescript-eslint/no-floating-promises */
  /* eslint-disable @typescript-eslint/no-unsafe-assignment */
  /* eslint-disable class-methods-use-this */
  /* eslint-disable consistent-return */
  /* eslint-disable no-unused-vars */
  /* eslint-disable camelcase */
  /* eslint-disable @typescript-eslint/restrict-template-expressions */
  columns = [
    { name: 'attacking_id', label: 'Attacking Type', field: 'attacking_id' },
    {
      name: 'sharpness', label: 'Sharpness', field: 'sharpness', sortable: true,
    },
    {
      name: 'fragility', label: 'Fragility', field: 'fragility', sortable: true,
    },
  ];

  typestatistics = [];

  created() {
    this.$axios.get('types/statistics')
      .then((response) => {
        this.typestatistics = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }
}
</script>
