/** eslint-disable */
<template>
  <q-table
    title="Advanced Query"
    :columns="columns"
    :data="advancedQuery"
  />
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';

@Component
export default class TableAdvancedQuery extends Vue {
  columns = [
    { name: 'training_ID', label: 'training_ID', field: 'training_ID' },
    {
      name: 'hp_T', label: 'hp_T', field: 'hp_T', sortable: true,
    },
    {
      name: 'attack_T', label: 'attack_T', field: 'attack_T', sortable: true,
    },
    {
      name: 'specialAttack_T', label: 'specialAttack_T', field: 'specialAttack_T', sortable: true,
    },
    {
      name: 'attack', label: 'attack', field: 'attack', sortable: true,
    },
    {
      name: 'specialAttack', label: 'specialAttack', field: 'specialAttack', sortable: true,
    },
    {
      name: 'defense_T', label: 'defense_T', field: 'defense_T', sortable: true,
    },
    {
      name: 'specialDefense_T', label: 'specialDefense_T', field: 'specialDefense_T', sortable: true,
    },
    {
      name: 'defense', label: 'defense', field: 'defense', sortable: true,
    },
    {
      name: 'specialDefense', label: 'specialDefense', field: 'specialDefense', sortable: true,
    },

  ];

  advancedQuery = [];
  /* eslint-disable @typescript-eslint/no-unsafe-return */
  /* eslint-disable @typescript-eslint/no-unsafe-member-access */
  /* eslint-disable @typescript-eslint/no-floating-promises */
  /* eslint-disable @typescript-eslint/no-unsafe-assignment */
  /* eslint-disable @typescript-eslint/no-unsafe-call */
  /* eslint-disable @typescript-eslint/adjacent-overload-signatures */
  /* eslint-disable no-void */
  /* eslint-disable no-unused-vars */

  created() {
    this.$axios.get('/advanced_query')
      .then((response) => {
        this.advancedQuery = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }
}
</script>
