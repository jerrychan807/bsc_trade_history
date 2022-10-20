<template>
  <div class="container bg-dark">
    <div class="row">
      <div class="col-sm-10">
        <!--        <h1><img src="/assets/logo.png" alt="logo"></h1>-->
        <title>BscTradeHistory</title>
        <h1>
          <b-card bg-variant="dark" text-variant="white" title="BscTradeHistory">
            <b-card-text>
              Make your BSC transaction simple.
            </b-card-text>
          </b-card>
        </h1>
        <hr>
        <b-form inline @submit="onSubmit" @reset="onReset" class="w-100">
          <!--          <label class="sr-only" for="inline-form-input-name">Address</label>-->
          <b-input
              id="inline-form-input-name"
              class="mb-2 mr-sm-2 mb-sm-0"
              placeholder="Address"
              type="text"
              v-model="addressForm.address"
          ></b-input>
          <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
        <br><br>
        <table class="table table-hover text-white">
          <thead>
          <tr>
            <th scope="col">时间</th>
            <th scope="col">项目</th>
            <th scope="col">动作</th>
            <th scope="col">Token记录</th>
            <th scope="col">Gas费用</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(r, index) in history" :key="index">
            <td>{{ r.date }}</td>
            <td v-if="r.project_name === 'Unknown'">
              <img :src="r.logo_url" style="width: 28px; height: 28px;">{{ r.contract_address | ellipsis }}
            </td>
            <td v-else>
              <img :src="r.logo_url" style="width: 28px; height: 28px;">{{ r.project_name }}
            </td>
            <td>{{ r.func_name }}</td>
            <td>
              <b-list-group v-for="item in r.token_transfered_list" :key="item.date">
                <b-list-group-item v-if="item.side === 'add'" variant="dark">
                  <img :src="item.image_url" style="width: 20px; height: 20px;">
                  +{{ item.amount }} {{ item.token_symbol }}
                </b-list-group-item>
                <b-list-group-item v-if="item.side === 'reduce'" variant="dark">
                  <img :src="item.image_url" style="width: 20px; height: 20px;">
                  -{{ item.amount }} {{ item.token_symbol }}
                </b-list-group-item>
              </b-list-group>
            </td>
            <td>{{ r.cost_bnb }}BNB(${{ r.cost_usd }})</td>
          </tr>
          </tbody>
        </table>
        <b-button-group>
          <b-button @click="prevPage">上一页</b-button>
          <b-button variant="success">页数:{{ currentPage }}</b-button>
          <b-button @click="nextPage">下一页</b-button>
        </b-button-group>
      </div>
    </div>

  </div>
</template>

<style>
html,
body {
  margin: 0;
  padding: 0;
  background-color: #343a40;
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      history: [],
      currentPage: 1,
      offset: 10,
      items: [],
      addressForm: {
        address: '',
        page: 1,
        offset: 10,
      },

      message: '',
      showMessage: false,
    };
  },
  filters: {
    ellipsis(value) {
      if (!value) return '';
      if (value.length > 8) {
        return value.slice(0, 8) + '...'
      }
      return value
    }
  },
  components: {
    // alert: Alert,
  },
  methods: {
    getResources() {
      const path = 'http://199.255.96.224:5001/historyDemo';
      axios.post(path)
          .then((res) => {
            this.history = res.data.result;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
    },
    nextPage() {
      this.currentPage = this.currentPage + 1
      // alert(JSON.stringify(this.currentPage))
      const payload = {
        address: this.addressForm.address,
        page: this.currentPage,
        offset: this.offset,
      };
      this.submitAddr(payload);
    },
    prevPage() {
      this.currentPage = this.currentPage - 1
      const payload = {
        address: this.addressForm.address,
        page: this.currentPage,
        offset: this.offset,
      };
      this.submitAddr(payload);
    },
    submitAddr(payload) {
      const path = 'http://199.255.96.224:5001/history';
      axios.post(path, payload, {timeout: 20000})
          .then((res) => {
            this.history = res.data.result;
            // alert(JSON.stringify(this.history))
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error);
          });
    },
    initForm() {
      this.addressForm.address = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      // alert(JSON.stringify(this.addressForm))
      // this.$refs.addResModal.hide();
      const payload = {
        address: this.addressForm.address,
        page: this.addressForm.page,
        offset: this.addressForm.offset,
      };
      this.submitAddr(payload);
      // this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addResModal.hide();
      this.initForm();
    },
  },
  created() {
    // this.getResources();
  },
};
</script>