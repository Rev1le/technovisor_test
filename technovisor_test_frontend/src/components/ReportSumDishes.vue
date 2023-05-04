<template>
  <input class="form-control" id="date" type="date" v-model="inputDate" />

  <button @click="getReportSumDishes" class="btn btn-primary" type="submit">
    Send
  </button>
</template>

<script>
import axios from "axios";

export default {
  name: "ReportSumDishes",

  data() {
    return {
      inputDate: "",
    };
  },

  methods: {
    async getReportSumDishes() {
      console.log("Получаем сумму блюд в дне");
      const response = await axios.get(
        `http://127.0.0.1:8000/api/v1/orders_on_day_xlsx?date=${this.inputDate}`,
        { responseType: "arraybuffer" }
      );

      if (response.data == "None") {
        alert("Блюд в данный день не было заказано");
        return;
      }

      console.log(response.data);

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");

      link.href = url;
      link.setAttribute("download", "report_dishes_on_date.xlsx");

      document.body.appendChild(link);
      link.click();
    },
  },
};
</script>
