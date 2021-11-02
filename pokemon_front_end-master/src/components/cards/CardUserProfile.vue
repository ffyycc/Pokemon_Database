<template>
  <q-card>
    <!-- Back Button Section -->
    <q-card-actions>
      <btn-back/>
    </q-card-actions>

    <!-- User Portrait Section -->
    <q-card-section>
      <card-user-portrait/>
    </q-card-section>

    <!-- User Profile Section -->
    <q-card-section>
      <q-list>
        <!-- Account Type -->
        <q-item>
          <q-item-section avatar>
            I'm a
          </q-item-section>
          <q-item-section>
            <q-radio
              v-model="accountType"
              val="student"
              label="Student" />
          </q-item-section>
          <q-item-section>
            <q-radio
              v-model="accountType"
              val="teacher"
              label="Teacher" />
          </q-item-section>
        </q-item>

        <!-- First name / Last name -->
        <q-item>
          <q-item-section>
            <q-input dense
              v-model="firstName"
              placeholder="First name"
            />
          </q-item-section>
          <q-item-section>
            <q-input dense
              v-model="lastName"
              placeholder="Last name"
            />
          </q-item-section>
        </q-item>

        <!-- Date of Birth -->
        <q-item>
          <q-item-section avatar>
            Date of Birth
          </q-item-section>
          <q-item-section>
            <q-input
              dense
              v-model="dateOfBirth"
              type="date"
            />
          </q-item-section>
        </q-item>
      </q-list>
    </q-card-section>

    <!-- Confirm Register Section -->
    <q-card-section align="right">
      <q-list>
        <q-item>
          <q-item-section>
            <q-btn
              unelevated
              rounded
              class="q-px-md"
              color="primary"
              label="Register"/>
          </q-item-section>
        </q-item>
      </q-list>
    </q-card-section>
  </q-card>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import CardUserPortrait from 'src/components/cards/CardUserPortrait.vue';
import BtnBack from 'src/components/buttons/BtnBack.vue';

@Component({
  components: {
    CardUserPortrait,
    BtnBack,
  },
})
export default class CardUserProfile extends Vue {
  // TODO: add user password data abstraction
  // TODO: add data validation functionality
  accountType = '';

  firstName = '';

  lastName = '';

  dateOfBirth = '';
}
</script>
