<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-2">
        <div v-for="(item, index) in appList" :key="index">
          <div class="rounded m-2 p-2 shadow-sm" @click="indexSet(item.name)">
            <p class="fw-bold m-0 name row">{{ item.name }}</p>
            <p
              class="cardInfo m-0 cardInfo row"
              style="font-size: 0.8rem"
              v-if="check[index].status == true"
            >
              {{
                this.msgs.list[index].msg[this.msgs.list[index].msg.length - 1]
                  .msg
              }}
            </p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="chat-content hide p-0">
          <div class="line fw-bold m-3" style="font: Arial">
            {{ this.msgs.list[this.chatIndex].name }}
          </div>
          <hr />
          <!-- 채팅 띄우기 -->
          <div v-for="(item, i) in this.msgs.list[this.chatIndex].msg">
            <div class="line">
              <span
                v-if="item.tag == 'user'"
                class="chat-box mine me-2 rounded"
                type="button"
                @click="alertIt"
                >{{ item.msg }}</span
              >
            </div>
            <div class="line">
              <span
                v-if="item.tag == 'computer'"
                class="chat-box bot ms-2 rounded"
                type="button"
                @click="alertIt"
              >
                {{ item.msg }}
              </span>
            </div>
          </div>
          <!-- 채팅입력창 -->
          <div
            class="container-fluid pe-0"
            style="position: fixed; bottom: 0; width: 84"
          >
            <div class="row my-2">
              <div class="col-9">
                <input
                  class="form-control input"
                  placeholder="Message for here"
                  v-on:keyup.enter="sendMsg()"
                  v-model="newChat"
                  ref="cursor"
                />
              </div>
              <div class="col-1 pe-5">
                <button
                  class="btn btn-secondary"
                  style="width: 100% !important"
                  @click="sendMsg()"
                >
                  ▶️
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "Function",
  components: {},
  props: {
    appList: {
      type: Array,
      default: "default type",
    },
  },
  data() {
    return {
      check: [
        { name: "John", status: false },
        { name: "Jane", status: false },
        { name: "Kevin", status: false },
        { name: "Andrew", status: false },
      ],
      last: "",
      // 친구창 데이터
      chatIndex: 0,
      // 채팅창 데이터
      newChat: "",
      msgs: {
        list: [
          { name: "John", msg: [] },
          { name: "Jane", msg: [] },
          { name: "Kevin", msg: [] },
          { name: "Andrew", msg: [] },
        ],
      },
    };
  },
  methods: {
    indexSet(name) {
      console.log(name);
      if (name == "John") {
        this.chatIndex = 0;
      } else if (name == "Jane") {
        this.chatIndex = 1;
      } else if (name == "Kevin") {
        this.chatIndex = 2;
      } else if (name == "Andrew") {
        this.chatIndex = 3;
      }
      console.log(this.chatIndex);
    },
    sendMsg() {
      this.msgs.list[this.chatIndex].msg.push({
        tag: "user",
        msg: this.newChat,
      });
      axios
        .post("http://127.0.0.1:5000/", {
          msg: this.newChat,
          name: this.chatIndex,
        })
        .then((res) => {
          this.msgs.list[this.chatIndex].msg.push({
            tag: "computer",
            msg: res.data,
          });
          console.log(this.msgs);
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {});
      this.newChat = "";
      this.$refs.cursor.focus();
      this.check[this.chatIndex].status = true;
    },
  },
};
</script>
<style>
.cardInfo {
  font-size: 14px;
}
.avatar {
  width: 50px;
  height: 50px;
  object-fit: fill;
  padding: 0 !important;
  margin-left: 16px;
  border-radius: 100%;
}
.name {
  font-size: 18.5px;
}
.line {
  margin-top: 10px;
  display: flex;
}
.mine {
  color: #262630;
  background-color: #ffec42;
  margin-left: auto;
}
.chat-content {
  background-color: #9bbad8;
  height: 94vh;
  overflow-y: scroll;
}
.hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.hide::-webkit-scrollbar {
  display: none;
}
.chat-box {
  max-width: 200px;
  padding: 5px;
}
.bot {
  background-color: #fdfefe;
  color: #0b0b0b;
}
</style>
