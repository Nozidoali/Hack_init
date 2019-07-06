from flask import Flask, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    else:
        return redirect('login')
        # render_template('index.html')
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('title')
        object = open("user.txt", 'w')
        
        title = request.form.get('title')  # 传入表单对应输入字段的 name 值
        year = request.form.get('year')
        print(title, year)


        object.write(title)
        object.write(" ")
        object.write(year)
        object.write("\n")



        object.close()
        return 'Logged in as %s' % escape(session['username'])
    return render_template('login.html')
    #'''
    #    <form action="" method="post">
    #        <p><input type=text name=username>
    #        <p><input type=submit value=Login>
    #    </form>
    #'''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'