<template>
  <h1>Создание заказа:</h1>
  <div id="DateInput">
    Выбор даты:
    <input 
      class="form-control" 
      id="date" 
      type="date" 
      v-model="selectedValues.date" />
  </div>

  <br />

  <div>
    Выбор работника:
    <select  
      v-model="selectedValues.worker" 
      class="worker_select form-control form-select form-select-sm mb-3">
      
      <option v-for="worker in workers">
        {{ worker.fields.name }}
      </option>

    </select>
  </div>

  <div>
    Выбор блюд:
    <select 
      v-model="selectedValues.dishes" 
      multiple="multiple"
      class="dishes_select form-control form-select form-select-sm mb-3">
      
      <option v-for="dish in dishes">
        {{ dish.fields.title }}
      </option>
      
    </select>
  </div>

  <button @click="getFormValues" class="btn btn-primary" type="submit">Send</button>
</template>

<script lang="js">
import axios from 'axios';
import useOrderStore from '@/stores/orders.js';
import { mapActions } from 'pinia';

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
      ...mapActions(useOrderStore, ['createOrder']),
      
      async getFormValues() {
        console.log("выбранные поля:", this.selectedValues);
        
        const inputData = this.selectedValues;
        //await this.createOrder(inputData);
        console.log('Finish');
      },
    },
    async created() {
        const dishes_response = await axios.get("http://127.0.0.1:8080/api/v1/dishes");
        this.dishes = dishes_response.data;

        const workers_response = await axios.get("http://127.0.0.1:8080/api/v1/workers");
        this.workers = workers_response.data;
    },
}
</script>
