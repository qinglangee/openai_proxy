# openai_proxy
可以代理请求 chatGPT api, 放在国外服务器不会被封， 可惜 api 额度用完了。  


# gpt 提示技巧

## 四个原则 
### 1. 写清晰的指令。 
清晰不是简短，太短了容易描述不清楚。  
tactic 1: 用分隔符，分隔指令的不同部分。 
tactic 2: 要求结构化输出。 可以要求它输出 html , json 之类的格式便于利用。 
tactic 3: 检查是否满足条件，可以跟它明说，如果条件不满足你直接说不满足，不要胡说。 
tactic 4: Few-shot prompting. 给它一些完成任务的例子。 

### 2. Give the model time to think
tactic 1: 给任务分成几个步骤。 让它按步骤进行。  
tactic 2: Instruct the model to work out its own solution before rushing to a conclusion. 指示模型在匆忙做出结论之前思考解决方案。  
  prompt: 判断一个解决方案是否正确。 首先， 你自己解决一下这个问题，然后跟要判断的比较一下， 在你自己解决问题前不要做出判断 。 