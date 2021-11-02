import { MutationTree } from 'vuex';
import { UserStateInterface } from './state';

const mutation: MutationTree<UserStateInterface> = {
  UPDATE_EMAIL(state, val: string) {
    state.email = val;
  },
  UPDATE_USER_ID(state, val: number) {
    state.userId = val;
  },
};

export default mutation;
