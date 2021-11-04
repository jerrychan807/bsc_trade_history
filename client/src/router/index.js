import Vue from 'vue'
import VueRouter from 'vue-router'
import History from "../components/History";
import HistoryDemo from "../components/HistoryDemo";

Vue.use(VueRouter)

const routes = [
    {
        path: '/history',
        name: 'History',
        component: History,
        meta: {
            title: 'BscTradeHistory'
        }
    },
    {
        path: '/historydemo',
        name: 'HistoryDemo',
        component: HistoryDemo
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
