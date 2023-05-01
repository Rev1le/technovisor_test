<template>

    <a class="list-group-item list-group-item-action">
        
        <div class="d-flex justify-content-start">
            <h5 class="mb-1 padding-50">Заказ № {{ order.id }} </h5>
            <small class="text-muted">
                 на {{ toLocalDateFormat(order.date) }}
            </small>
        </div>

        <div v-if="order.dishes.length">
            <p class="mb-1">Для {{ order.worker.name }} заказаны блюда:</p>
            
            <small class="text-muted">  
                <ul class="list-group" v-for="dish in order.dishes">
                    <li class="list-group-item d-flex justify-content-between align-items-center">{{ dish.title }}</li>
                </ul>
            </small>

        </div>
        
        <p v-else class="mb-1">
            Для {{ order.worker.name }} был сделан заказ без блюд
        </p>
    </a>

</template>

<script lang="js">
export default {
    name: 'OrderDishesItem',

    data() {
        return {

        }
    },

    props: {
        order: {
            type: Object,
            required: true
        },
    },

    methods: {
        toLocalDateFormat(date_str) {
            var options = {year: 'numeric', month: 'long', day: 'numeric' };
            var date = new Date(date_str)
            
            return date.toLocaleDateString("ru-RU", options);
        }
    }
}
</script>