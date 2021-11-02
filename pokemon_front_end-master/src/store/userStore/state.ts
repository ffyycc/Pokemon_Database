export interface UserStateInterface {
  email: string,
  portrait: string,
  userId: number,
}

function state(): UserStateInterface {
  return {
    email: '',
    portrait: 'https://cdn4.iconfinder.com/data/icons/small-n-flat/24/user-alt-512.png',
    userId: -1,
  };
}

export default state;
