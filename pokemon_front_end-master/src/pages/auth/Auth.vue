<template>
  <q-page padding class="fit bg-grey-2">
    <div class="row justify-center absolute-center">
      <router-view/>
    </div>
  </q-page>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';

@Component
export default class PageName extends Vue {
}
</script>
