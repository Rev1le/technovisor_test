<template>
  <h1>HIMAN</h1>
  <input id="date" type="date" v-model="selectedValues.date"/>
  <br />
  
  <select v-model="selectedValues.dishes" multiple="multiple">
    <option v-for="dish in dishes">
      {{ dish.fields.title }}
    </option>
  </select>

  <select v-model="selectedValues.worker" class="worker_select">
    <option v-for="worker in workers">
      {{ worker.fields.name }}
    </option>
  </select>

  <button @click="getFormValues">Send</button>
</template>

<script lang="js">
import axios from 'axios';

export default {
    name: "FormValid",
    data() {
        return {
            workers: [],
            dishes: [],
            selectedValues: {
              date: "",
              worker: "",
              dishes: [],
            }
        }
    },
    methods: {
      getFormValues() {
        console.log("выбранные поля:", this.selectedValues);
      }
    },
    async created() {
        const dishes_response = await axios.get("http://127.0.0.1:8000/api/v1/dishes");
        this.dishes = dishes_response.data;

        const workers_response = await axios.get("http://127.0.0.1:8000/api/v1/workers");
        this.workers = workers_response.data;
    },
}
</script>
