<template>
    <!--Модальное окно на кнопку-->
    <button class="create_btn" @click="createOrder">Создать заказ</button>

    <OrderDishesList/>
    
    <FormValid/>
</template>


<script>
import OrderDishesList from '@/components/OrderDishesList.vue';
import FormValid from '@/components/FormValid.vue';

export default {
    name: "MainPageView",

    components: {
        OrderDishesList,
        FormValid
    },

    data() {
        return {

        }
    },

    methods: {
        async createOrder() {
            console.log("Создание заказа...")
        }
    }
}
</script>

<style scoped>
.create_btn {
  font-size: 16px;
  font-weight: 400;
  display: inline-block;
  padding: 10px 28px;
  border-radius: 4px;
  transition: 0.5s;
  color: #f8f9fa;
  background: #0ea2bd;
  font-family: 'Poppins', sans-serif;
  text-decoration: none;
}
</style>