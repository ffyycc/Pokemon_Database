# Quasar App (my_411_project)

A Quasar Framework app

## How to begin

可以先在`prototype`文件夹中查看我们需要完成的工作。

我们只会用到 `/components`, `/layouts`, `/router`, `/pages` 文件夹，其中
- `/components`存放了单读的vue component，
- `/pages`存放了由不同components组成的页面，
- `/router`存放了页面所对应的path，i.e ‘www.xxx.com/hub’，‘www.dce.com/mypokemon’等，
- `/layout`存放了页面的框架，页面和layout的关系就像门之于门框
我们需要做的事情是：
1. 在`/components`文件夹中写单独的vue-component
2. 将vue-component拼成页面，存放至 `/pages` 文件夹
3. 在`/router`中将页面与对应的 path 和 layout 连接上
4. 大功告成

可以以`router`文件夹的`routes.ts`作为切入点，了解quasar和vue是如何工作的。

## Install the dependencies
```bash
yarn
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)
```bash
quasar dev
```

### Lint the files
```bash
yarn run lint
```

### Build the app for production
```bash
quasar build
```

### Customize the configuration
See [Configuring quasar.conf.js](https://v1.quasar.dev/quasar-cli/quasar-conf-js).