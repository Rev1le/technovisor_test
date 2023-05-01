<template>
  <!--Модальное окно на кнопку-->
  <div class="d-flex justify-content-center">
    <button class="create_btn btn btn-primary" @click="switchShowDialog">Создать заказ</button>
  </div>

  <CreateModalWindow v-model:show="showDialog">
    <div class="justify-content-center">
      <FormValid/>
    </div>
  </CreateModalWindow>

  <OrderDishesList />

</template>

<script>
import OrderDishesList from "@/components/OrderDishesList.vue";
import FormValid from "@/components/FormValid.vue";
import CreateModalWindow from "@/components/CreateModalWindow.vue";

export default {
  name: "MainPageView",

  components: {
    CreateModalWindow,
    OrderDishesList,
    FormValid,
  },

  data() {
    return {
      // Контролирует отображение модального окна
      showDialog: true,
    };
  },

  methods: {
    async createOrder() {
      console.log("Создание заказа...");
    },

    switchShowDialog() {
      this.showDialog = !this.showDialog;
    },
  },
};
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
  font-family: "Poppins", sans-serif;
  text-decoration: none;
}
</style>
