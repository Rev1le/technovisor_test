<template>
  <!-- <input class="form-control" id="date" type="date" v-model="inputDate" />

  <button @click="getReportDeltatime" class="btn btn-primary" type="submit">
    Send
  </button> -->
</template>

<script>
import axios from "axios";
export default {
  name: "ReportDeltatime",

  data() {
    return {
      inputDate: "",
    };
  },

  methods: {
    async getReportDeltatime() {
      console.log("Получаем таблицу блюд");
      const response = await axios.get("http://127.0.0.1:8000/api/v1/xlsx/", {
        responseType: "arraybuffer",
      });

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");

      link.href = url;
      link.setAttribute("download", "report_orders_on_timedelta.xlsx");

      document.body.appendChild(link);
      link.click();
    },
  },

  async created() {
    await this.getReportDeltatime();
  },
};
</script>
