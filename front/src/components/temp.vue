<template>
  <div>
    <div class="chat-content hide p-0">
      <div class="line">
        <button
          @click="$emit('close-modal')"
          class="btn btn-outline-secondary ms-2 me-3"
        >
          ←
        </button>
        <div class="line fw-bold" style="font: Arial">
          {{ this.msgs.list[this.chatIndex]["name"] }}
        </div>
      </div>
      <!-- 채팅내역 -->
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
</template>

<script>
import axios from "axios";

export default {
  props: ["chatIndex"],
  data() {
    return {
      newChat: "",
      msgs: {
        list: [
          {
            name: "John",
            msg: [],
          },
          {
            name: "Jane",
            msg: [],
          },
          {
            name: "Kevin",
            msg: [],
          },
          {
            name: "Andrew",
            msg: [],
          },
        ],
      },
    };
  },
  methods: {
    alertIt() {
      alert("hello");
    },
    getLastMsg(l) {
      return l[l.length - 1].msg;
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
          console.log(res.data);
          this.msgs.list[this.chatIndex].msg.push({
            tag: "computer",
            msg: res.data["GPTanswer"],
          });
          console.log(this.msgs);
          this.$emit("final", res.data["lastMSG"], res.data["name"]);
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {});
      this.newChat = "";
      this.$refs.cursor.focus();
    },
  },
};
</script>
<style>
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
