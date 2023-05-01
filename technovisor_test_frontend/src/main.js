import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'

import './assets/main.css'

import './scss/styles.scss'
import * as bootstrap from 'bootstrap'


const app = createApp(App)

app.use(createPinia())
app.mount('#app')

export default app