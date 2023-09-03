<template>
  <div>
    <test :appList="friends" />
  </div>
</template>

<script>
import test from "./components/test.vue";

export default {
  name: "App",
  components: {
    test,
  },
  data() {
    return {
      friends: [
        { name: "John", index: 0 },
        { name: "Jane", index: 1 },
        { name: "Kevin", index: 2 },
        { name: "Andrew", index: 3 },
      ],
    };
  },
  methods: {},
};
</script>
