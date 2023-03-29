
from flask import Flask, render_template, request
import ai_query as ai
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/query')
def query():

    return ai.query("what time?")

@app.route('/query/<content>')
def query_arg(content):

    return ai.query(content)


@app.post('/ask')
def ask():
    content = request.form['content']
    return ai.query(content)


    

# @app.get("/login")
# def login():
#   return render_template('login.html')

# @app.post("/login")
# def login2():
#   print('login form', request.form)
#   username = request.form['username']
#   password = request.form['password']
#   with open('data/accounts.json', 'r+') as file:
#     text = file.read()
#     accounts = json.loads(text)
#     if username in accounts and password == accounts[username]['password']:
#        session['username'] = username
#        return redirect('/home')
#     else:
#        return render_template('login.html', err_msg="User name or password wrong.")

# @app.route("/logout")
# def logout():
#    session.pop('username')
#    return redirect('/home')


# @app.get("/register")
# def register():
#   return render_template('register.html')

# @app.post("/register")
# def register2():
#   username = request.form['username']
#   password = request.form['password']
#   password2 = request.form['confirm_password']
#   print("input", username, password, password2)
#   if username == '' or password == '' or password2 == '':
#      return render_template('register.html', err_msg="Required field can not be empty.")
#   if password != password2:
#      return render_template('register.html', err_msg="Confirm password is not same as password.")
#   with open('data/accounts.json', 'r+') as file:
#     text = file.read()
#     accounts = json.loads(text)
#     if username in accounts:
#        return render_template('register.html', err_msg="Account already exists.")
#     else:
#        accounts[username] = {'username':username, 'password':password}
#        text = json.dumps(accounts, indent=4)
#        file.seek(0)
#        file.write(text)

#   return render_template('register.html', success_msg="Register successfylly.")

# @app.route('/acts')
# @login_required_json
# def acts():
#    acts = appdata.load_activities()
#    return json.dumps({"code":0, "data":acts})

# @app.post('/create')
# @login_required_json
# def create_act():
#   print("form", request.form)
#   act_type = request.form['type']
#   act_name = request.form['name']
#   if act_type != '0' and act_type != '1':
#      return json.dumps({"code":1, "msg":"Error activity type."})
#   acts = appdata.load_activities_json()
#   acts['max'] = acts['max'] + 1
#   acts['datas'].append({'id':acts['max'], 'type':int(act_type), 'name':act_name, 'state':0, 'accounts':[]})
#   appdata.save_activities(acts)

#   return json.dumps({"code":0, "msg":"Create activity successfully."})
     

# @app.post('/join')
# @login_required_json
# def join():
#    id = request.form['id']
#    amount = request.form['amount']
#    act = appdata.get_act(int(id))
#    if(act is None):
#       return json.dumps({"code":1, "msg":"Activity does not exist."})
   
#    username = session['username']
#    print("user", username)
#    updated = False
#    for account in act['accounts']:
#       if account['account'] == username:
#          account['amount'] = int(amount)
#          updated = True
#    if not updated:
#       act['accounts'].append({'account':username, 'amount':int(amount)})


#    appdata.update_act(act)
#    return json.dumps({"code":0, "data":0})


# @app.post('/finish')
# @login_required_json
# def finish():
#    act_id = request.form['id']
#    act = appdata.get_act(int(act_id))
#    if(act is None):
#       return json.dumps({"code":1, "msg":"Activity does not exist."})
   
   
#    act['state'] = 1
#    if act['type'] == 0:
#       total = 0
#       for acc in act['accounts']:
#          total = total + acc['amount']
#       act['result'] = cal_gdp(act)
#    else:
#       max_amount = 0
#       max_acc = ''
#       for acc in act['accounts']:
#          if acc['amount'] > max_amount:
#             max_amount = acc['amount']
#             max_acc = acc['account']
#       act['result'] = max_acc
   

#    appdata.update_act(act)
#    return json.dumps({"code":0, "data":0})


# def cal_gdp(act):
#    machines = []
#    datas = []
#    shares = []
#    for acc in act['accounts']:
#       machine = VirtualMachine(acc['account'])
#       machines.append(machine)
#       datas.append(PrivateScalar(acc['amount'], machine))

#    for i in range(len(machines)):
#       share_sec = datas[i].share(machines)
#       shares.append(share_sec)


#    if len(datas) > 0:
#       sum_sec = sum(shares)
#       re_a = sum_sec.reconstruct(machines[0])
#       return re_a.value
#    else:
#       return 0

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()