<template>
<div class="home" id="app">
<el-row>
  <el-col :span="12" :offset="6">
  <el-form ref="form" :model="form" label-width="380px">
    <el-form-item :label="question.question_desc" v-for="(question, index) in questionList">
      <el-radio-group v-model="question.answer">
        <el-radio v-for="option in question.options" :label="option.option_value" label-width="180px">{{ option.option_desc }}</el-radio>
      </el-radio-group>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">提交</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>
  </el-col>
</el-row>
</div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      form: {
        resource: '',
      },
      questionList: [],
    }
  },
  mounted: function () {
    this.showQuestions()
  },
  methods: {
    onSubmit () {
      console.log(this.questionList)
    },
    showQuestions () {
      this.$http.get('http://127.0.0.1:8001/api/show_questions')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.code === 0) {
            this.questionList = res['data'],
            this.answerList = new Array(res['count'])
          } else {
            this.$message.error('查询问题失败')
            console.log(res['msg'])
          }
        })
    }
  }
}
</script>
