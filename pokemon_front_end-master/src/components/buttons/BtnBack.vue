/* eslint-disable */
<template>
  <q-btn
    flat
    rounded
    color="primary"
    icon="chevron_left"
    label="Back"
    v-bind="$attrs"
    @click="back"/>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';

@Component
export default class ComponentName extends Vue {
  back() {
    this.$router.go(-1);
  }
}
</script>
