<template>
  <div id="fcard" class="rounded m-2 p-2 shadow-sm" @click="openSend">
    <p class="fw-bold m-0 name row">{{ name }}</p>
    <p class="cardInfo m-0 cardInfo row" v-if="place == 0">{{ LSmsg }}</p>
  </div>
</template>
<script>
export default {
  name: "MyFriend",
  components: {},
  data() {
    return {
      index: 0,
    };
  },
  props: {
    name: String,
    msg: Array,
    LSmsg: String,
    place: Number,
  },
  methods: {
    openSend() {
      this.$emit("send");
      console.log(this.name);
      if (this.name == "John") {
        this.index = 0;
      } else if (this.name == "Jane") {
        this.index = 1;
      } else if (this.name == "Kevin") {
        this.index = 2;
      } else {
        this.index = 3;
      }
      console.log(this.index);
      this.$emit("open", this.index);
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
</style>
