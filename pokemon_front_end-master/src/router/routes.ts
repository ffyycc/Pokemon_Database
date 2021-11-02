import { RouteConfig } from 'vue-router';

const routes: RouteConfig[] = [
  {
    path: '/auth',
    component: () => import('layouts/GuestLayout.vue'),
    children: [
      {
        path: '/',
        component: () => import('src/pages/auth/Auth.vue'),
        props: true,
        children: [
          { path: '', component: () => import('src/pages/auth/AuthSelectAccount.vue') },
          { path: 'login', component: () => import('src/components/cards/CardUserLogin.vue'), props: true },
          { path: 'query', component: () => import('src/components/cards/CardUserQuery.vue') },
          { path: 'register', component: () => import('src/components/cards/CardUserRegister.vue'), props: true },
        ],
      },
    ],
  },
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'error', component: () => import('pages/Error404.vue') },
    ],
  },
  {
    path: '/statistics',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/TypeStatisticsPage.vue') },
      { path: 'error', component: () => import('pages/Error404.vue') },
    ],
  },
  {
    path: '/publicinfo',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/PublicInfoPage.vue') },
      { path: 'error', component: () => import('pages/Error404.vue') },
    ],
  },
  {
    path: '/training',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/TrainingPage.vue') },
      { path: 'error', component: () => import('pages/Error404.vue') },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue'),
  },
];

export default routes;
