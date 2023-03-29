Vue.component('alert', {
  data: function () {
    return {
      count: 0,
    }
  },
  props: ['show', 'msg', 'type'],
  template: '<div :class="\'text-center alert mt-4 \'+type" v-if="show">{{msg}}</div>'
})

const app = new Vue({
  delimiters: ["{:", ":}"],
  data() {
    return {
      content:'',
      results:[],
    }
  },
  methods: {
    queryAi: function () {
      let self = this;
      if(this.content.trim() == ''){
        return;
      }
      const form = new FormData();
      form.append('content', self.content);
      axios.post("/ask", form).then(resp => {
        console.log("ask ai resp", resp.data);
        let data = resp.data;
        console.log('data', data);



        console.log(data.choices[0].message.content);
        self.results.push(data);

        setTimeout(function(){
          let ele = document.getElementsByTagName('html')[0];
          ele.scrollTop = ele.scrollHeight;  // 把元素滚动到的位置设置为元素的高度
        }, 200);
      });
    }, 
  },
  computed: {
  },
  created() {
  },
  mounted: function(){
  }

}).$mount('#container');