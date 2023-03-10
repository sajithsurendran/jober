// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    app: {
        head :{
            title : "Jober"
        }
    },
    modules: [
        '@nuxtjs/tailwindcss',
        '@element-plus/nuxt',
        '@nuxt/image-edge',
        'nuxt-icon',
      ],
    css: ['vuetify/lib/styles/main.sass'],
    build: {
        transpile: ['vuetify'],
      },
    vite: {
        define: {
          'process.env.DEBUG': false,
        },
    },
    image: {
      dir:'assets/'
    }
})
