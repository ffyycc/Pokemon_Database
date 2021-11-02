<template>
  <q-table
    grid
    title="Select Good Pokemon"
    :columns="columns"
    :data="highstat"
  />
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';

@Component
export default class TableHighData extends Vue {
  /* eslint-disable @typescript-eslint/no-unsafe-return */
  /* eslint-disable @typescript-eslint/no-unsafe-member-access */
  /* eslint-disable @typescript-eslint/no-floating-promises */
  /* eslint-disable @typescript-eslint/no-unsafe-assignment */
  /* eslint-disable @typescript-eslint/no-unsafe-call */
  /* eslint-disable @typescript-eslint/adjacent-overload-signatures */
  /* eslint-disable no-void */
  /* eslint-disable no-unused-vars */

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
      name: 'defense_T', label: 'defense_T', field: 'defense_T', sortable: true,
    },
    {
      name: 'specialDefense_T', label: 'specialDefense_T', field: 'specialDefense_T', sortable: true,
    },
    {
      name: 'speed', label: 'speed', field: 'speed', sortable: true,
    },
    {
      name: 'legendary', label: 'legendary', field: 'legendary', sortable: true,
    },

  ];

  highstat = [];

  created() {
    this.$axios.get('pokemon/highattr')
      .then((response) => {
        this.highstat = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }
}
</script>
