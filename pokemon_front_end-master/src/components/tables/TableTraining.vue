<template>
  <q-table
    flat
    title="Training"
    :columns="trainingColumns"
    :data="trainings"
    :loading="loading"
  >
    <template v-slot:top-right>

      <div class="row q-gutter-sm">
        <q-card bordered flat class="col" v-if="!updatable">
          <q-item>
            <q-item-section avatar class="text-grey">
              Training ID
            </q-item-section>
            <q-item-section>
              <q-input
                v-model="searchID"
                use-input
                dense
                type="number"
                @blur="searchTraining"
              >
                <template v-slot:append>
                  <q-btn
                    flat
                    icon="search"
                    @click="searchTraining"
                  />
                </template>
              </q-input>
            </q-item-section>
          </q-item>
        </q-card>
      </div>

    </template>

    <template v-slot:body-cell-action="props">
      <q-td key="action" :props="props">
        <q-btn
          flat dense round v-if="updatable"
          icon="close"
          @click="deleteTraining(props.row.training_id)"/>
      </q-td>
    </template>

    <template v-slot:body-cell-share_info="props">
      <q-td key="share_info" :props="props">
        <q-toggle
          v-if="updatable"
          :value="getShareInfo(props.row.share_info)"
          @input="toggleShareInfo(props.row)"/>
      </q-td>
    </template>

    <template v-slot:body-cell-hp_T="props">
      <q-td key="hp_T" :props="props">
        {{ props.row.hp_T }}
        <q-popup-edit v-if="updatable"
          v-model.number="props.row.hp_T"
          @save="updateTraining(props.row)">
          <q-input type="number" v-model.number="props.row.hp_T" dense autofocus />
        </q-popup-edit>
      </q-td>
    </template>

    <template v-slot:body-cell-attack_T="props">
      <q-td key="attack_T" :props="props">
        {{ props.row.attack_T }}
        <q-popup-edit v-if="updatable"
          v-model.number="props.row.attack_T"
          @save="updateTraining(props.row)">
          <q-input type="number" v-model.number="props.row.attack_T" dense autofocus />
        </q-popup-edit>
      </q-td>
    </template>

    <template v-slot:body-cell-defense_T="props">
      <q-td key="defense_T" :props="props">
        {{ props.row.defense_T }}
        <q-popup-edit v-if="updatable"
          v-model.number="props.row.defense_T"
          @save="updateTraining(props.row)">
          <q-input type="number" v-model.number="props.row.defense_T" dense autofocus />
        </q-popup-edit>
      </q-td>
    </template>

    <template v-slot:body-cell-specialAttack_T="props">
      <q-td key="specialAttack_T" :props="props">
        {{ props.row.specialAttack_T }}
        <q-popup-edit v-if="updatable"
          v-model.number="props.row.specialAttack_T"
          @save="updateTraining(props.row)">
          <q-input type="number" v-model.number="props.row.specialAttack_T" dense autofocus />
        </q-popup-edit>
      </q-td>
    </template>

    <template v-slot:body-cell-specialDefense_T="props">
      <q-td key="specialDefense_T" :props="props">
        {{ props.row.specialDefense_T }}
        <q-popup-edit v-if="updatable"
          v-model.number="props.row.specialDefense_T"
          @save="updateTraining(props.row)">
          <q-input type="number" v-model.number="props.row.specialDefense_T" dense autofocus />
        </q-popup-edit>
      </q-td>
    </template>

    <template v-slot:body-cell-speed_T="props">
      <q-td key="speed_T" :props="props">
        {{ props.row.speed_T }}
        <q-popup-edit v-if="updatable"
          v-model.number="props.row.speed_T"
          @save="updateTraining(props.row)">
          <q-input type="number" v-model.number="props.row.speed_T" dense autofocus />
        </q-popup-edit>
      </q-td>
    </template>

    <template v-slot:body-cell-weight_T="props">
      <q-td key="weight_T" :props="props">
        {{ props.row.weight_T }}
        <q-popup-edit v-if="updatable"
          v-model.number="props.row.weight_T"
          @save="updateTraining(props.row)">
          <q-input type="number" v-model.number="props.row.weight_T" dense autofocus />
        </q-popup-edit>
      </q-td>
    </template>

    <template v-slot:body-cell-height_T="props">
      <q-td key="height_T" :props="props">
        {{ props.row.height_T }}
        <q-popup-edit v-if="updatable"
          v-model.number="props.row.height_T"
          @save="updateTraining(props.row)">
          <q-input type="number" v-model.number="props.row.height_T" dense autofocus />
        </q-popup-edit>
      </q-td>
    </template>

  </q-table>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator';

@Component
export default class TableTraining extends Vue {
/* eslint-disable @typescript-eslint/no-unsafe-return */
/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-floating-promises */
/* eslint-disable @typescript-eslint/no-unsafe-assignment */
/* eslint-disable class-methods-use-this */
/* eslint-disable consistent-return */
/* eslint-disable no-unused-vars */
/* eslint-disable camelcase */
/* eslint-disable @typescript-eslint/restrict-template-expressions */
  @Prop({ default: '-1' }) trainerId!: string;

  @Prop({ default: false }) updatable!: boolean;

  searchID = 0

  trainingColumns = [
    {
      name: 'training_id', label: 'training_id', field: 'training_id', required: true,
    },
    {
      name: 'pokemon_id', label: 'pokemon_id', field: 'pokemon_id', required: true,
    },
    {
      name: 'hp_T', label: 'hp_T', field: 'hp_T', required: true,
    },
    {
      name: 'attack_T', label: 'attack_T', field: 'attack_T', required: true,
    },
    {
      name: 'defense_T', label: 'defense_T', field: 'defense_T', required: true,
    },
    {
      name: 'specialAttack_T', label: 'specialAttack_T', field: 'specialAttack_T', required: true,
    },
    {
      name: 'specialDefense_T', label: 'specialDefense_T', field: 'specialDefense_T', required: true,
    },
    {
      name: 'speed_T', label: 'speed_T', field: 'speed_T', required: true,
    },
    {
      name: 'height_T', label: 'Height_T', field: 'height_T', required: true,
    },
    {
      name: 'weight_T', label: 'Weight_T', field: 'weight_T', required: true,
    },

  ];

  trainings = [];

  loading = false;

  created() {
    if (this.trainerId !== '-1') {
      this.trainingColumns.unshift(
        {
          name: 'action', label: 'Action', field: '', required: false,
        },
        {
          name: 'share_info', label: 'Public?', field: 'share_info', required: false,
        },
      );
    }
    this.getTraining();
  }

  getTraining() {
    this.loading = true;
    this.$q.notify({
      color: 'primary',
      message: 'Where are my Pokemons?',
    });

    const url = this.trainerId === '-1'
      ? '/training/all'
      : `/training/user/${this.trainerId}`;

    this.$axios.get(url)
      .then((response) => {
        console.log('Get pokemon: ', response);
        this.trainings = response.data;
        this.$q.notify({
          color: 'primary',
          message: 'Here they are!',
        });
      })
      .catch((error) => {
        console.log(error);
        this.$q.notify({
          color: 'danger',
          message: error.message,
        });
      })
      .finally(() => {
        this.loading = false;
      });
  }

  getShareInfo(s) {
    return !!s;
  }

  toggleShareInfo(row) {
    row.share_info = !row.share_info;
    const data = {
      training_id: row.training_id,
      user_id: this.trainerId,
      share_info: row.share_info ? 1 : 0,
    };
    console.log(data);
    this.$axios.post('/public_info/update', data)
      .then((response) => {
        this.$q.notify({
          color: 'primary',
          message: response.data.message,
        });
      })
      .catch((error) => {
        this.$q.notify({
          color: 'danger',
          message: error.message,
        });
      })
      .finally(() => {
        this.getTraining();
      });
  }

  searchTraining() {
    if (this.searchID === '') {
      return this.getTraining();
    }

    this.$q.notify({
      color: 'primary',
      message: `fetching 10 trainees with training_id at least ${this.searchID}`,
    });

    this.$axios.post('/training/search', {
      training_id: this.searchID,
    })
      .then((response) => {
        console.log(response);
        this.trainings = response.data;
        this.$q.notify({
          color: 'primary',
          message: 'Gotcha!',
        });
      })
      .catch((error) => {
        console.log(error);
        this.$q.notify({
          color: 'danger',
          message: error.message,
        });
      });
  }

  createTraining() {
    this.$q.notify({
      color: 'primary',
      message: 'Breeding training pokemons...',
    });

    this.$axios.post('/training/create', {
      hp_T: 100,
      attack_T: 100,
      defense_T: 100,
      specialAttack_T: 100,
      specialDefense_T: 100,
      speed_T: 100,
      height_T: 100,
      weight_T: 100,
    })
      .then((response) => {
        this.$q.notify({
          color: 'primary',
          message: `${response.data.message}! Say hello to the new training pokemon!`,
        });
        this.getTraining();
      })
      .catch((error) => {
        console.log(error);
      });
  }

  updateTraining(row) {
    this.$q.notify({
      color: 'primary',
      message: 'updating trainee pokemon...',
    });

    this.$axios.post('/training/update', {
      user_id: this.trainerId,
      pokemon_id: row.pokemon_id,
      training_id: row.training_id,
      hp_T: row.hp_T,
      attack_T: row.attack_T,
      defense_T: row.defense_T,
      specialAttack_T: row.specialAttack_T,
      specialDefense_T: row.specialDefense_T,
      speed_T: row.speed_T,
      height_T: row.height_T,
      weight_T: row.weight_T,
    })
      .then((response) => {
        this.$q.notify({
          color: 'primary',
          message: response.data.message,
        });
      })
      .catch((error) => {
        this.$q.notify({
          color: 'danger',
          message: error.message,
        });
      })
      .finally((res) => {
        this.getTraining();
      });
  }

  deleteTraining(training_id) {
    this.$q.notify({
      color: 'primary',
      message: `deleting trainee with id ${training_id}`,
    });

    this.$axios.post('/training/delete', {
      training_id,
      user_id: this.trainerId,
    })
      .then((response) => {
        this.$q.notify({
          color: 'primary',
          message: response.data.message,
        });
      })
      .catch((error) => {
        this.$q.notify({
          color: 'danger',
          message: error.message,
        });
      })
      .finally(() => {
        this.getTraining();
      });
  }
}
</script>
