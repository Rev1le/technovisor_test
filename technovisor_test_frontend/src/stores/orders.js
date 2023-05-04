import axios from 'axios';
import { defineStore } from 'pinia';

const useOrderStore = defineStore(
    'orders', {

        state: () => ({
            orders: [],
            api_url: "http://127.0.0.1:8000/api/v1"
        }),

        getters: {
            getOrders() {
                return this.orders
            }
        },

        actions: {

            async reqGetAllOrders() {
                console.log("Получение всех заказов...")

                try {
                    const response = await axios.get(this.api_url+"/orders/?format=json");
                    console.log("Полученные заказы: ", response.data);
                    
                    if (response.status === 200) {
                        this.orders = response.data;
                        this.saveToLocalStorage();
                        return this.orders
                    }
                } 

                catch (e) {
                    console.log("Ошибка при запросе всех заказов: ", e);
                }
            },

            async saveToLocalStorage() {
                const localStorage = window.localStorage;
                localStorage.setItem('orders', this.orders);
            },

            async createOrder(data) {
                console.log('Start');
                const response = await axios.post(
                    "http://127.0.0.1:8000/api/v1/create_order/", 
                    data=data
                );

                console.log("Резщультат создания ордера", response);
            }
        }
    }
)

export default useOrderStore
