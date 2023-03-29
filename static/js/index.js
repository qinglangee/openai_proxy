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
      responses:[],
      loading: false,
    }
  },
  methods: {
    queryAi: function () {
      let self = this;
      if(this.content.trim() == ''){
        return;
      }
      self.loading = true;
      const form = new FormData();
      form.append('content', self.content);
      axios.post("/ask", form).then(resp => {
        console.log("ask ai resp", resp.data);
        let data = resp.data;
        console.log('data', data);


        self.loading = false;
        console.log(self.getQueryAnswer(data));
        self.results.push(self.content);
        self.results.push(self.getQueryAnswer(data));
        self.responses.push(data);

        setTimeout(function(){
          let ele = document.getElementsByTagName('html')[0];
          ele.scrollTop = ele.scrollHeight;  // 把元素滚动到的位置设置为元素的高度
        }, 200);
      });
    }, 
    getQueryAnswer: function(responseData){
      let r = responseData;
      if(r.choices != null && r.choices.length > 0 && r.choices[0].message != null ){
        return r.choices[0].message.content;
      }else{
        return "Can not get answer content."
      }
    }
  },
  computed: {
  },
  created() {
  },
  mounted: function(){
  }

}).$mount('#container');