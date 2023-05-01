<template>

    <div class="list-group px" v-for="order in orders">
        <OrderDishesItem :order="order"/>
    </div>

</template>

<script lang="js">
import useOrderStore from '@/stores/orders.js';
import OrderDishesItem from './OrderDishesItem.vue';
import { mapActions, mapState } from 'pinia';

export default {
    name: "OrderDishesList",

    components: {
        OrderDishesItem
    },

    data() {
        return {
            orders: []
        }
    },

    methods: {
        ...mapActions(useOrderStore, ['reqGetAllOrders'])
    },

    async created() {
        this.orders = await this.reqGetAllOrders();
    }
}
</script>