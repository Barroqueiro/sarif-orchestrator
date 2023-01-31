# Vulnerability Report

This report was automaticly generated based on the vulnerabilities specification of a [SARIF](https://sarifweb.azurewebsites.net) file.

## Tool information

> Name: flake8


> Information Uri: [https://flake8.pycqa.org/](https://flake8.pycqa.org/)


> Version: 4.0.1



---

## Vulnerabilities

line too long (110 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 1

```
from flask import session, Flask, jsonify, request, Response, render_template, render_template_string, url_for
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

line too long (82 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 4

```
from jwt.exceptions import DecodeError, MissingRequiredClaimError, InvalidKeyError
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

expected 2 blank lines, found 1

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 34

```
class User(db.Model):
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E302
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 35

```
id = db.Column(db.Integer, primary_key = True)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 35

```
id = db.Column(db.Integer, primary_key = True)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 36

```
username = db.Column(db.String(80), unique = True)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 36

```
username = db.Column(db.String(80), unique = True)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 37

```
password = db.Column(db.String(80), unique = True)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 37

```
password = db.Column(db.String(80), unique = True)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

too many blank lines (2)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 40

```
def __repr__(self):
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E303
  </details>








---

expected 2 blank lines, found 1

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 43

```
class Customer(db.Model):
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E302
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 44

```
id = db.Column(db.Integer, primary_key = True)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 44

```
id = db.Column(db.Integer, primary_key = True)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 48

```
ccn = db.Column(db.String(80), nullable = True)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 48

```
ccn = db.Column(db.String(80), nullable = True)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

too many blank lines (2)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 53

```
def __repr__(self):
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E303
  </details>








---

expected 2 blank lines, found 1

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 56

```
@app.before_first_request
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E302
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 68

```
for i in range(0,5):
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 73

```
cust.email = fake.simple_profile(sex = None)['mail']
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 73

```
cust.email = fake.simple_profile(sex = None)['mail']
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 74

```
cust.username = fake.simple_profile(sex = None)['username']
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 74

```
cust.username = fake.simple_profile(sex = None)['username']
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 82

```
exp_date = datetime.datetime.utcnow() + datetime.timedelta(minutes = 240)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 82

```
exp_date = datetime.datetime.utcnow() + datetime.timedelta(minutes = 240)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

expected 2 blank lines, found 1

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 85

```
def verify_jwt(token):
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E302
  </details>








---

line too long (129 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 87

```
decoded = jwt.decode(token, app.config['SECRET_KEY_HMAC'], verify=True, issuer = 'we45', leeway=10, algorithms=['HS256'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 87

```
decoded = jwt.decode(token, app.config['SECRET_KEY_HMAC'], verify=True, issuer = 'we45', leeway=10, algorithms=['HS256'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 87

```
decoded = jwt.decode(token, app.config['SECRET_KEY_HMAC'], verify=True, issuer = 'we45', leeway=10, algorithms=['HS256'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

expected 2 blank lines, found 1

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 97

```
def insecure_verify(token):
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E302
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 98

```
decoded = jwt.decode(token, verify = False)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 98

```
decoded = jwt.decode(token, verify = False)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

expected 2 blank lines, found 1

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 102

```
@app.errorhandler(404)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E302
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 115

```
return render_template_string(template, dir = dir, help = help, locals = locals),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 115

```
return render_template_string(template, dir = dir, help = help, locals = locals),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 115

```
return render_template_string(template, dir = dir, help = help, locals = locals),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 115

```
return render_template_string(template, dir = dir, help = help, locals = locals),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 115

```
return render_template_string(template, dir = dir, help = help, locals = locals),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 115

```
return render_template_string(template, dir = dir, help = help, locals = locals),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

line too long (88 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 115

```
return render_template_string(template, dir = dir, help = help, locals = locals),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 115

```
return render_template_string(template, dir = dir, help = help, locals = locals),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

expected 2 blank lines, found 1

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 117

```
def has_no_empty_params(rule):
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E302
  </details>








---

expected 2 blank lines, found 1

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 122

```
@app.route('/', methods = ['GET'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E302
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 122

```
@app.route('/', methods = ['GET'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 122

```
@app.route('/', methods = ['GET'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

line too long (91 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 127

```
if ("GET" in rule.methods or "POST" in rule.methods) and has_no_empty_params(rule):
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

test for membership should be &#39;not in&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 128

```
if not 'static' in rule.endpoint:
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E713
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 132

```
return render_template('index.html', urls = links)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 132

```
return render_template('index.html', urls = links)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 135

```
@app.route('/register/user', methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 135

```
@app.route('/register/user', methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 147

```
return jsonify({'Created': user_created}),200
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 149

```
return jsonify({'Error': str(e.message)}),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

expected 2 blank lines, found 1

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 151

```
@app.route('/register/customer', methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E302
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 151

```
@app.route('/register/customer', methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 151

```
@app.route('/register/customer', methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

line too long (82 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 162

```
cust = Customer(first_name, last_name, email, username, password, ccn)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 166

```
return jsonify({'Created': user_created}),200
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 168

```
return jsonify({'Error': str(e.message)}),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 171

```
@app.route('/login', methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 171

```
@app.route('/login', methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

line too long (120 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 174

```
'''
    You will need to authenticate to this URI first. You will need to pass a JSON body with a username and password key.
    If you enter a valid username and password, a JWT token is returned in the HTTP Response in the Authorization header.
    This token can be used for subsequent requests.
    '''
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

line too long (121 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 175

```
'''
    You will need to authenticate to this URI first. You will need to pass a JSON body with a username and password key.
    If you enter a valid username and password, a JWT token is returned in the HTTP Response in the Authorization header.
    This token can be used for subsequent requests.
    '''
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 183

```
auth_user = User.query.filter_by(username = username, password = password).first()
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 183

```
auth_user = User.query.filter_by(username = username, password = password).first()
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 183

```
auth_user = User.query.filter_by(username = username, password = password).first()
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 183

```
auth_user = User.query.filter_by(username = username, password = password).first()
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

line too long (90 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 183

```
auth_user = User.query.filter_by(username = username, password = password).first()
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

line too long (213 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 185

```
auth_token = jwt.encode({'user': username, 'exp': get_exp_date(), 'nbf': datetime.datetime.utcnow(), 'iss': 'we45', 'iat': datetime.datetime.utcnow()}, app.config['SECRET_KEY_HMAC'], algorithm='HS256')
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

line too long (82 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 186

```
resp = Response(json.dumps({'Authenticated': True, "User": username}))
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

block comment should start with &#39;# &#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 187

```
#resp.set_cookie('SESSIONID', auth_token)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E265
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 193

```
return jsonify({'Error': 'No User here...'}),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

do not use bare &#39;except&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 194

```
except:
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E722
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 195

```
return jsonify({'Error': 'Unable to recognize Input'}),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

expected 2 blank lines, found 1

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 197

```
@app.route('/fetch/customer', methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E302
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 197

```
@app.route('/fetch/customer', methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 197

```
@app.route('/fetch/customer', methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 201

```
return jsonify({'Error': 'Not Authenticated!'}),403
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 204

```
return jsonify({'Error': 'Invalid Token'}),403
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

line too long (99 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 210

```
customer_dict = {'id': customer_record.id, 'firstname': customer_record.first_name,
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

line too long (103 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 211

```
'lastname': customer_record.last_name, 'email': customer_record.email,
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

line too long (100 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 212

```
'cc_num': customer_record.ccn, 'username': customer_record.username
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

closing bracket does not match visual indentation

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 213

```
}
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E124
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 215

```
return jsonify(customer_dict),200
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 217

```
return jsonify({'Error': 'No Customer Found'}),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 219

```
return jsonify({'Error': 'Invalid Request'}),400
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 222

```
@app.route('/get/<cust_id>', methods = ['GET'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 222

```
@app.route('/get/<cust_id>', methods = ['GET'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

line too long (103 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 234

```
customer_dict = {'id': customer_record.id, 'firstname': customer_record.first_name,
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

continuation line under-indented for visual indent

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 235

```
'lastname': customer_record.last_name, 'email': customer_record.email,
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E128
  </details>








---

line too long (103 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 235

```
'lastname': customer_record.last_name, 'email': customer_record.email,
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

continuation line under-indented for visual indent

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 236

```
'cc_num': customer_record.ccn, 'username': customer_record.username
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E128
  </details>








---

line too long (100 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 236

```
'cc_num': customer_record.ccn, 'username': customer_record.username
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

closing bracket does not match visual indentation

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 237

```
}
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E124
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 238

```
return jsonify(customer_dict),200
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 240

```
return jsonify({'Error': 'No Customer Found'}),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 242

```
return jsonify({'Error': 'Invalid Request'}),400
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

too many blank lines (4)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 247

```
@app.route('/search', methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E303
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 247

```
@app.route('/search', methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 247

```
@app.route('/search', methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 251

```
return jsonify({'Error': 'Not Authenticated!'}),403
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 254

```
return jsonify({'Error': 'Invalid Token'}),403
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

line too long (123 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 262

```
str_query = "SELECT first_name, last_name, username FROM customer WHERE username = '%s';" % search_term
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

line too long (87 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 263

```
# mycust = Customer.query.filter_by(username = search_term).first()
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

line too long (104 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 264

```
# return jsonify({'Customer': mycust.username, 'First Name': mycust.first_name}),200
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 270

```
return jsonify(results),200
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

line too long (99 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 282

```
return render_template_string(template, dir=dir, help=help, locals=locals), 404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

whitespace before &#39;(&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 306

```
print (para.text)  # '\n\n'.join([para.text for paragraph in document.paragraphs])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E211
  </details>








---

line too long (94 &gt; 79 characters)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 306

```
print (para.text)  # '\n\n'.join([para.text for paragraph in document.paragraphs])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E501
  </details>








---

expected 2 blank lines, found 1

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 311

```
@app.route("/yaml")
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E302
  </details>








---

expected 2 blank lines, found 1

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 316

```
@app.route("/yaml_hammer", methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E302
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 316

```
@app.route("/yaml_hammer", methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 316

```
@app.route("/yaml_hammer", methods = ['POST'])
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

missing whitespace after &#39;,&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 320

```
rand = random.randint(1,100)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E231
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 332

```
return render_template('view.html', name = json.dumps(ydata))
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

unexpected spaces around keyword / parameter equals

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 332

```
return render_template('view.html', name = json.dumps(ydata))
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E251
  </details>








---

too many blank lines (3)

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 336

```
if __name__ == "__main__":
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    E303
  </details>








---

&#39;flask.session&#39; imported but unused

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 1

```
from flask import session, Flask, jsonify, request, Response, render_template, render_template_string, url_for
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    F401
  </details>








---

&#39;jwt.exceptions.InvalidKeyError&#39; imported but unused

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 4

```
from jwt.exceptions import DecodeError, MissingRequiredClaimError, InvalidKeyError
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    F401
  </details>








---

redefinition of unused &#39;os&#39; from line 8

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 17

```
import os
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    F811
  </details>








---

