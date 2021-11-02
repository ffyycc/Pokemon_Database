<template>
  <q-table
    flat
    title="Pokemon"
    :columns="pokemonColumns"
    :data="pokemons"
    :loading="loading"
  >
    <template v-slot:top-right>
      <div class="row q-gutter-sm">

        <!-- Search Card -->
        <q-card bordered flat class="col">
          <q-item>

            <q-item-section avatar class="text-grey">
              Pokemon ID
            </q-item-section>

            <q-item-section>

              <!-- Search Input -->
              <q-input
                v-model="searchID"
                use-input
                dense
                type="number"
                @blur="searchPokemon"
              >

                <template v-slot:append>
                  <!-- Search button -->
                  <q-btn
                    flat
                    icon="search"
                    @click="searchPokemon"
                  />
                </template>

              </q-input>
            </q-item-section>

          </q-item>
        </q-card>
      </div>
    </template>

    <template v-slot:body-cell-action="props">
      <q-td :props="props" class="q-gutter-xs">
        <q-btn
          label="Adopt"
          color="secondary"
          @click="adoptPokemon(props.row)"/>
      </q-td>
    </template>

    <template v-slot:body-cell-id="props">
      <q-td :props="props" class="q-gutter-xs">
        {{ props.row.pokemon_id }}
      </q-td>
    </template>

    <template v-slot:body-cell-types="props">
      <q-td :props="props" class="q-gutter-xs">
        <q-badge
          v-for="type in props.row.types"
          :key="type"
          :label="type"/>
      </q-td>
    </template>

  </q-table>
</template>

<script lang="ts">
import { UserStateInterface } from 'src/store/userStore/state';
import { Vue, Component } from 'vue-property-decorator';
import { State } from 'vuex-class';

@Component
export default class TablePokemon extends Vue {
  /* eslint-disable @typescript-eslint/no-unsafe-return */
  /* eslint-disable @typescript-eslint/no-unsafe-member-access */
  /* eslint-disable @typescript-eslint/no-floating-promises */
  /* eslint-disable @typescript-eslint/no-unsafe-assignment */
  /* eslint-disable @typescript-eslint/no-unsafe-call */
  /* eslint-disable @typescript-eslint/adjacent-overload-signatures */
  /* eslint-disable no-void */
  /* eslint-disable no-unused-vars */
  @State('user') userStore!: UserStateInterface;

  searchID = 0;

  pokemonColumns = [
    {
      name: 'action', label: 'Action', required: false,
    },
    {
      name: 'id', label: 'ID', field: 'pokemon_id', required: true,
    },
    {
      name: 'hp', label: 'HP', field: 'hp', required: true,
    },
    {
      name: 'attack', label: 'Attack', field: 'attack', required: true,
    },
    {
      name: 'defense', label: 'Defense', field: 'defense', required: true,
    },
    {
      name: 'specialAttack', label: 'Special Attack', field: 'specialAttack', required: true,
    },
    {
      name: 'specialDefense', label: 'Special Defense', field: 'specialDefense', required: true,
    },
    {
      name: 'speed', label: 'Speed', field: 'speed', required: true,
    },
    {
      name: 'height', label: 'Height', field: 'height', required: true,
    },
    {
      name: 'weight', label: 'Weight', field: 'weight', required: true,
    },
    {
      name: 'gender', label: 'Gender', field: 'gender', required: true,
    },
    {
      name: 'generation', label: 'Generation', field: 'generation', required: true,
    },
    {
      name: 'legendary', label: 'Legendary', field: 'legendary', required: true,
    },
    {
      name: 'types', label: 'Types', field: 'types', required: true,
    },
  ];

  pokemons = [];

  pokemonTypes = [];

  loading = false;

  created() {
    this.getPokemon();
    this.getTypes();
  }

  getTypes() {
    this.$axios.get('/types/all')
      .then((response) => {
        const a = [];
        response.data.forEach((e) => {
          a.push(e.id);
        });
        this.pokemonTypes = a;
      })
      .catch((error) => console.log(error));
  }

  getPokemon() {
    this.loading = true;
    this.$q.notify({
      color: 'primary',
      message: 'counting pokemon...',
    });

    this.$axios.get('/pokemon/all')
      .then((response) => {
        console.log(response);
        this.pokemons = response.data;
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
      })
      .finally(() => {
        this.loading = false;
      });
  }

  adoptPokemon(row) {
    this.loading = true;
    this.$q.notify({
      color: 'primary',
      message: 'Adopt pokemon...',
    });

    /* eslint-disable camelcase */
    /* eslint-disable consistent-return */
    /* eslint-disable @typescript-eslint/restrict-template-expressions */
    const {
      pokemon_id,
      hp,
      attack,
      defense,
      specialAttack,
      specialDefense,
      speed,
      weight,
      height,
      types,
    } = row;

    this.$axios.post('/pokemon/adopt', {
      userId: this.userStore.userId,
      pokemon_id,
      hp,
      attack,
      defense,
      specialAttack,
      specialDefense,
      speed,
      weight,
      height,
      types,
    })
      .then((response) => {
        this.$q.notify({
          color: 'primary',
          message: 'Hello my friend!',
        });
      })
      .catch((error) => {
        console.log(error);
      })
      .finally(() => {
        this.loading = false;
      });
  }

  getRandomTypes() {
    const r = Math.floor(Math.random() * this.pokemonTypes.length);
    const type1 = this.pokemonTypes[r];
    const type2 = this.pokemonTypes[r - 1 < 0 ? this.pokemonTypes.length - 1 : r - 1];
    return [type1, type2];
  }

  searchPokemon() {
    if (this.searchID === '') {
      return this.getPokemon();
    }

    this.$q.notify({
      color: 'primary',
      message: `fetching pokemon with id at least ${this.searchID}`,
    });

    this.$axios.post('/pokemon/search', {
      pokemon_id: this.searchID,
    })
      .then((response) => {
        console.log(response);
        this.pokemons = response.data;
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

  createPokemon() {
    this.loading = true;
    this.$q.notify({
      color: 'primary',
      message: 'Breeding pokemon...',
    });

    const types = this.getRandomTypes();
    this.$axios.post('/pokemon/create', {
      hp: 99,
      attack: 99,
      defense: 99,
      specialAttack: 99,
      specialDefense: 99,
      speed: 99,
      types,
    })
      .then((response) => {
        this.$q.notify({
          color: 'primary',
          message: `${response.data.message}! Say hello to the new pokemon!`,
        });
        this.getPokemon();
      })
      .catch((error) => {
        console.log(error);
      })
      .finally(() => {
        this.loading = false;
      });
  }

  updatePokemon(row) {
    this.loading = true;
    this.$q.notify({
      color: 'primary',
      message: 'updating pokemon...',
    });

    this.$axios.post('/pokemon/update', {
      pokemon_id: row.pokemon_id,
      hp: row.hp,
      attack: row.attack,
      defense: row.defense,
      specialAttack: row.specialAttack,
      specialDefense: row.specialDefense,
      speed: row.speed,
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
        this.loading = false;
      });
  }

  deletePokemon(id) {
    this.$q.notify({
      color: 'primary',
      message: `deleting pokemon with id ${id}`,
    });

    this.$axios.post('/pokemon/delete', {
      pokemon_id: id,
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
        this.getPokemon();
      });
  }
}
</script>
