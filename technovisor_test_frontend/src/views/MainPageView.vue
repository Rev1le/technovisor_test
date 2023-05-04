<template>
  <header class="d-flex justify-content-center py-3">
    <ul class="nav nav-pills">
      <li class="nav-item">
        <button
          class="create_btn btn btn-primary"
          aria-current="page"
          @click="switchShowCreateOrder"
        >
          Создать заказ
        </button>
      </li>
      <li class="nav-item">
        <button
          class="create_btn btn btn-primary"
          aria-current="page"
          @click="switchShowReportDeltatime"
        >
          Отчет заказов за промежуток времени
        </button>
      </li>
      <li class="nav-item">
        <button
          class="create_btn btn btn-primary"
          aria-current="page"
          @click="switchShowReportSumDishes"
        >
          Отчет суммирования блюд в заданный день
        </button>
      </li>
    </ul>
  </header>

  <CreateModalWindow v-model:show="showCreateOrder">
    <FormValid />
  </CreateModalWindow>

  <CreateModalWindow v-model:show="showReportDeltatime">
    <ReportDeltatime />
  </CreateModalWindow>

  <CreateModalWindow v-model:show="showReportSumDishes">
    <ReportSumDishes />
  </CreateModalWindow>

  <OrderDishesList />
</template>

<script>
import OrderDishesList from "@/components/OrderDishesList.vue";
import FormValid from "@/components/FormValid.vue";
import CreateModalWindow from "@/components/CreateModalWindow.vue";
import ReportSumDishes from "@/components/ReportSumDishes.vue";
import ReportDeltatime from "../components/ReportDeltatime.vue";

export default {
  name: "MainPageView",

  components: {
    CreateModalWindow,
    OrderDishesList,
    FormValid,
    ReportSumDishes,
    ReportDeltatime,
  },

  data() {
    return {
      // Контролирует отображение модального окна
      showCreateOrder: false,
      showReportDeltatime: false,
      showReportSumDishes: false,
      inputDate: "",
    };
  },

  methods: {
    async createOrder() {
      console.log("Создание заказа...");
    },

    switchShowCreateOrder() {
      this.showCreateOrder = !this.showCreateOrder;
    },

    switchShowReportDeltatime() {
      this.showReportDeltatime = !this.showReportDeltatime;
    },

    switchShowReportSumDishes() {
      this.showReportSumDishes = !this.showReportSumDishes;
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
