#!/usr/bin/env python3

from flask import Flask, render_template_string, request
import os 

app = Flask(__name__)
blacklist = ['import','getattr', 'class', 'os','subclasses','mro','eval','if',' subprocess','file','open','popen','builtins','compile','execfile','from_pyfile','config','local','self','item','getitem','getattribute','func_globals', 'init', '{{', '}}', ":", ";", '-', "_", "[", "]", "join"]


@app.route("/")
def home():
    user = request.args.get('user') or None

    template = '''
    <html><head><title>Get The Flag</title><style>body {margin: 90px;}</style></head><body>
    '''
    if user == None:
        template = template + '''
        <h1>Login Form</h1>
        <form>
        <input name="user" style="border: 2px solid #C21010; padding: 10px; border-radius: 10px; margin-bottom: 25px;" value="Username"><br>
        <input type="submit" value="Log In" style="border: 0px; padding: 5px 20px ; color: #C21010;">
        </form>
        '''.format(user)
    else:
        for no in blacklist:
            if no in user:
                user = user.replace(no, ' ').lower()
            else:
                continue
            a =  ['config', 'self']
            return ''.join(['{{% set {}=None%}}'.format(c) for c in a]) + user
        
        template = template + '''
        <h1>Basic {}</h1>
        Blah blah blah<br>
        '''.format(user)

    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=9000)

