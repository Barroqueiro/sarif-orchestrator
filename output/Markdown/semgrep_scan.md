# Vulnerability Report

This report was automaticly generated based on the vulnerabilities specification of a [SARIF](https://sarifweb.azurewebsites.net) file.

## Tool information

> Name: semgrep





> Semantic version: 1.5.0


---

## Vulnerabilities

---

User controlled data in methods like `innerHTML`, `outerHTML` or `document.write` is an anti-pattern that can lead to XSS vulnerabilities

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/static/loader.js


- Line 153

```
K.b.l.kc=function(b,c,d){var e={},f;for(f in b)e[f]=b[f];for(f in c)e[f]=c[f];for(f in d){var g=f.toLowerCase();if(g in b)throw Error('Cannot override "'+g+'" attribute, got "'+f+'" with value "'+d[f]+'"');g in c&&delete e[g];e[f]=d[f]}return e};K.b.l.Tm=K.b.l.pa("<!DOCTYPE html>",K.h.i.O.sa);K.b.l.EMPTY=K.b.l.pa("",K.h.i.O.sa);K.b.l.ze=K.b.l.pa("<br>",K.h.i.O.sa);K.a.S={};K.a.S.Ln={bm:"afterbegin",cm:"afterend",rm:"beforebegin",sm:"beforeend"};K.a.S.ur=function(b,c,d){b.insertAdjacentHTML(c,K.b.l.u(d))};K.a.S.wi={MATH:!0,SCRIPT:!0,STYLE:!0,SVG:!0,TEMPLATE:!0};K.a.S.oh=function(b,c){if(K.m.oa&&K.a.S.wi[b.tagName.toUpperCase()])throw Error("goog.dom.safe.setInnerHtml cannot be used to set content of "+b.tagName+".");b.innerHTML=K.b.l.u(c)};K.a.S.tt=function(b,c){b.outerHTML=K.b.l.u(c)};K.a.S.wt=function(b,c){b.style.cssText=K.b.F.u(c)};K.a.S.yq=function(b,c){b.write(K.b.l.u(c))};
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    javascript.browser.security.insecure-document-method.insecure-document-method
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/javascript.browser.security.insecure-document-method.insecure-document-method">https://semgrep.dev/r/javascript.browser.security.insecure-document-method.insecure-document-method</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    User controlled data in methods like `innerHTML`, `outerHTML` or `document.write` is an anti-pattern that can lead to XSS vulnerabilities
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    User controlled data in methods like `innerHTML`, `outerHTML` or `document.write` is an anti-pattern that can lead to XSS vulnerabilities
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

User controlled data in methods like `innerHTML`, `outerHTML` or `document.write` is an anti-pattern that can lead to XSS vulnerabilities

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/static/loader.js


- Line 153

```
K.b.l.kc=function(b,c,d){var e={},f;for(f in b)e[f]=b[f];for(f in c)e[f]=c[f];for(f in d){var g=f.toLowerCase();if(g in b)throw Error('Cannot override "'+g+'" attribute, got "'+f+'" with value "'+d[f]+'"');g in c&&delete e[g];e[f]=d[f]}return e};K.b.l.Tm=K.b.l.pa("<!DOCTYPE html>",K.h.i.O.sa);K.b.l.EMPTY=K.b.l.pa("",K.h.i.O.sa);K.b.l.ze=K.b.l.pa("<br>",K.h.i.O.sa);K.a.S={};K.a.S.Ln={bm:"afterbegin",cm:"afterend",rm:"beforebegin",sm:"beforeend"};K.a.S.ur=function(b,c,d){b.insertAdjacentHTML(c,K.b.l.u(d))};K.a.S.wi={MATH:!0,SCRIPT:!0,STYLE:!0,SVG:!0,TEMPLATE:!0};K.a.S.oh=function(b,c){if(K.m.oa&&K.a.S.wi[b.tagName.toUpperCase()])throw Error("goog.dom.safe.setInnerHtml cannot be used to set content of "+b.tagName+".");b.innerHTML=K.b.l.u(c)};K.a.S.tt=function(b,c){b.outerHTML=K.b.l.u(c)};K.a.S.wt=function(b,c){b.style.cssText=K.b.F.u(c)};K.a.S.yq=function(b,c){b.write(K.b.l.u(c))};
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    javascript.browser.security.insecure-document-method.insecure-document-method
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/javascript.browser.security.insecure-document-method.insecure-document-method">https://semgrep.dev/r/javascript.browser.security.insecure-document-method.insecure-document-method</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    User controlled data in methods like `innerHTML`, `outerHTML` or `document.write` is an anti-pattern that can lead to XSS vulnerabilities
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    User controlled data in methods like `innerHTML`, `outerHTML` or `document.write` is an anti-pattern that can lead to XSS vulnerabilities
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using the Django object-relational mappers (ORM) instead of raw SQL queries.

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
    python.django.security.injection.tainted-sql-string.tainted-sql-string
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.django.security.injection.tainted-sql-string.tainted-sql-string">https://semgrep.dev/r/python.django.security.injection.tainted-sql-string.tainted-sql-string</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using the Django object-relational mappers (ORM) instead of raw SQL queries.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using the Django object-relational mappers (ORM) instead of raw SQL queries.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using an object-relational mapper (ORM) such as SQLAlchemy which will protect your queries.

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
    python.flask.security.injection.tainted-sql-string.tainted-sql-string
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.flask.security.injection.tainted-sql-string.tainted-sql-string">https://semgrep.dev/r/python.flask.security.injection.tainted-sql-string.tainted-sql-string</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using an object-relational mapper (ORM) such as SQLAlchemy which will protect your queries.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using an object-relational mapper (ORM) such as SQLAlchemy which will protect your queries.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

By not specifying a USER, a program in the container may run as &#39;root&#39;. This is a security hazard. If an attacker can control a process running as root, they may have control over the container. Ensure that the last USER in a Dockerfile is a USER other than &#39;root&#39;.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/Dockerfile


- Line 13

```
ENTRYPOINT ["python"]
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    dockerfile.security.missing-user.missing-user
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/dockerfile.security.missing-user.missing-user">https://semgrep.dev/r/dockerfile.security.missing-user.missing-user</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    By not specifying a USER, a program in the container may run as &#39;root&#39;. This is a security hazard. If an attacker can control a process running as root, they may have control over the container. Ensure that the last USER in a Dockerfile is a USER other than &#39;root&#39;.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    By not specifying a USER, a program in the container may run as &#39;root&#39;. This is a security hazard. If an attacker can control a process running as root, they may have control over the container. Ensure that the last USER in a Dockerfile is a USER other than &#39;root&#39;.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

By not specifying a USER, a program in the container may run as &#39;root&#39;. This is a security hazard. If an attacker can control a process running as root, they may have control over the container. Ensure that the last USER in a Dockerfile is a USER other than &#39;root&#39;.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/Dockerfile


- Line 15

```
CMD ["app.py"]
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    dockerfile.security.missing-user.missing-user
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/dockerfile.security.missing-user.missing-user">https://semgrep.dev/r/dockerfile.security.missing-user.missing-user</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    By not specifying a USER, a program in the container may run as &#39;root&#39;. This is a security hazard. If an attacker can control a process running as root, they may have control over the container. Ensure that the last USER in a Dockerfile is a USER other than &#39;root&#39;.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    By not specifying a USER, a program in the container may run as &#39;root&#39;. This is a security hazard. If an attacker can control a process running as root, they may have control over the container. Ensure that the last USER in a Dockerfile is a USER other than &#39;root&#39;.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Hardcoded JWT secret or private key is used. This is a Insufficiently Protected Credentials weakness: https://cwe.mitre.org/data/definitions/522.html Consider using an appropriate security mechanism to protect the credentials (e.g. keeping secrets in environment variables)

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
    python.jwt.security.jwt-hardcode.jwt-python-hardcoded-secret
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.jwt.security.jwt-hardcode.jwt-python-hardcoded-secret">https://semgrep.dev/r/python.jwt.security.jwt-hardcode.jwt-python-hardcoded-secret</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Hardcoded JWT secret or private key is used. This is a Insufficiently Protected Credentials weakness: https://cwe.mitre.org/data/definitions/522.html Consider using an appropriate security mechanism to protect the credentials (e.g. keeping secrets in environment variables)
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Hardcoded JWT secret or private key is used. This is a Insufficiently Protected Credentials weakness: https://cwe.mitre.org/data/definitions/522.html Consider using an appropriate security mechanism to protect the credentials (e.g. keeping secrets in environment variables)
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected JWT token decoded with &#39;verify=False&#39;. This bypasses any integrity checks for the token which means the token could be tampered with by malicious actors. Ensure that the JWT token is verified.

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
    python.jwt.security.unverified-jwt-decode.unverified-jwt-decode
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.jwt.security.unverified-jwt-decode.unverified-jwt-decode">https://semgrep.dev/r/python.jwt.security.unverified-jwt-decode.unverified-jwt-decode</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected JWT token decoded with &#39;verify=False&#39;. This bypasses any integrity checks for the token which means the token could be tampered with by malicious actors. Ensure that the JWT token is verified.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected JWT token decoded with &#39;verify=False&#39;. This bypasses any integrity checks for the token which means the token could be tampered with by malicious actors. Ensure that the JWT token is verified.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected the use of an insecure deserialization library in a Flask route. These libraries are prone to code execution vulnerabilities. Ensure user data does not enter this function. To fix this, try to avoid serializing whole objects. Consider instead using a serializer such as JSON.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 330

```
ydata = yaml.load(y)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.flask.security.insecure-deserialization.insecure-deserialization
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.flask.security.insecure-deserialization.insecure-deserialization">https://semgrep.dev/r/python.flask.security.insecure-deserialization.insecure-deserialization</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected the use of an insecure deserialization library in a Flask route. These libraries are prone to code execution vulnerabilities. Ensure user data does not enter this function. To fix this, try to avoid serializing whole objects. Consider instead using a serializer such as JSON.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected the use of an insecure deserialization library in a Flask route. These libraries are prone to code execution vulnerabilities. Ensure user data does not enter this function. To fix this, try to avoid serializing whole objects. Consider instead using a serializer such as JSON.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Avoiding SQL string concatenation: untrusted input concatenated with raw SQL query can result in SQL Injection. In order to execute raw query safely, prepared statement should be used. SQLAlchemy provides TextualSQL to easily used prepared statement with named parameters. For complex SQL composition, use SQL Expression Language or Schema Definition Language. In most cases, SQLAlchemy ORM will be a better option.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 262

```
str_query = "SELECT first_name, last_name, username FROM customer WHERE username = '%s';" % search_term
                    # mycust = Customer.query.filter_by(username = search_term).first()
                    # return jsonify({'Customer': mycust.username, 'First Name': mycust.first_name}),200

                    search_query = db.engine.execute(str_query)
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.sqlalchemy.security.sqlalchemy-execute-raw-query.sqlalchemy-execute-raw-query
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.sqlalchemy.security.sqlalchemy-execute-raw-query.sqlalchemy-execute-raw-query">https://semgrep.dev/r/python.sqlalchemy.security.sqlalchemy-execute-raw-query.sqlalchemy-execute-raw-query</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Avoiding SQL string concatenation: untrusted input concatenated with raw SQL query can result in SQL Injection. In order to execute raw query safely, prepared statement should be used. SQLAlchemy provides TextualSQL to easily used prepared statement with named parameters. For complex SQL composition, use SQL Expression Language or Schema Definition Language. In most cases, SQLAlchemy ORM will be a better option.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Avoiding SQL string concatenation: untrusted input concatenated with raw SQL query can result in SQL Injection. In order to execute raw query safely, prepared statement should be used. SQLAlchemy provides TextualSQL to easily used prepared statement with named parameters. For complex SQL composition, use SQL Expression Language or Schema Definition Language. In most cases, SQLAlchemy ORM will be a better option.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 104

```
template = '''<html>
    <head>
    <title>Error</title>
    </head>
    <body>
    <h1>Oops that page doesn't exist!!</h1>
    <h3>%s</h3>
    </body>
    </html>
    ''' % request.url

    return render_template_string(template, dir = dir, help = help, locals = locals),404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.flask.security.dangerous-template-string.dangerous-template-string
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.flask.security.dangerous-template-string.dangerous-template-string">https://semgrep.dev/r/python.flask.security.dangerous-template-string.dangerous-template-string</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 272

```
template = '''<html>
                        <head>
                        <title>Error</title>
                        </head>
                        <body>
                        <h1>Oops Error Occurred</h1>
                        <h3>%s</h3>
                        </body>
                        </html>
                        ''' % str(e)
                    return render_template_string(template, dir=dir, help=help, locals=locals), 404
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.flask.security.dangerous-template-string.dangerous-template-string
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.flask.security.dangerous-template-string.dangerous-template-string">https://semgrep.dev/r/python.flask.security.dangerous-template-string.dangerous-template-string</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected the use of eval(). eval() can be dangerous if used to evaluate dynamic content. If this content can be input from outside the program, this may be a code injection vulnerability. Ensure evaluated content is not definable by external sources.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/static/loader.js


- Line 24

```
K.Tl=function(b){return"(function(){"+b+"\n;})();\n"};K.fs=function(b){var c=K.na;try{K.na={Wd:void 0,ld:!1};if(K.za(b))var d=b.call(void 0,{});else if(K.L(b))K.Ml()&&(b=K.Tl(b)),d=K.Ck.call(void 0,b);else throw Error("Invalid module definition");var e=K.na.Wd;if(!K.L(e)||!e)throw Error('Invalid module name "'+e+'"');K.na.ld?K.tf(e,d):K.vi&&Object.seal&&typeof d==y&&null!=d&&Object.seal(d);K.Fk[e]=d}finally{K.na=c}};K.Ck=function(b){eval(b);return{}};
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    javascript.browser.security.eval-detected.eval-detected
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/javascript.browser.security.eval-detected.eval-detected">https://semgrep.dev/r/javascript.browser.security.eval-detected.eval-detected</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected the use of eval(). eval() can be dangerous if used to evaluate dynamic content. If this content can be input from outside the program, this may be a code injection vulnerability. Ensure evaluated content is not definable by external sources.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected the use of eval(). eval() can be dangerous if used to evaluate dynamic content. If this content can be input from outside the program, this may be a code injection vulnerability. Ensure evaluated content is not definable by external sources.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected the use of eval(). eval() can be dangerous if used to evaluate dynamic content. If this content can be input from outside the program, this may be a code injection vulnerability. Ensure evaluated content is not definable by external sources.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/static/loader.js


- Line 26

```
K.Rt=function(b,c){var d=K.global.$jscomp;d||(K.global.$jscomp=d={});var e=d.je;if(!e){var f=K.La+K.Bi,g=K.zk(f);if(g){eval(g+a+f);if(K.global.$gwtExport&&K.global.$gwtExport.$jscomp&&!K.global.$gwtExport.$jscomp.transpile)throw Error('The transpiler did not properly export the "transpile" method. $gwtExport: '+JSON.stringify(K.global.$gwtExport));K.global.$jscomp.je=K.global.$gwtExport.$jscomp.transpile;d=K.global.$jscomp;e=d.je}}if(!e){var h=" requires transpilation but no transpiler was found.";
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    javascript.browser.security.eval-detected.eval-detected
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/javascript.browser.security.eval-detected.eval-detected">https://semgrep.dev/r/javascript.browser.security.eval-detected.eval-detected</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected the use of eval(). eval() can be dangerous if used to evaluate dynamic content. If this content can be input from outside the program, this may be a code injection vulnerability. Ensure evaluated content is not definable by external sources.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected the use of eval(). eval() can be dangerous if used to evaluate dynamic content. If this content can be input from outside the program, this may be a code injection vulnerability. Ensure evaluated content is not definable by external sources.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected the use of eval(). eval() can be dangerous if used to evaluate dynamic content. If this content can be input from outside the program, this may be a code injection vulnerability. Ensure evaluated content is not definable by external sources.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/static/loader.js


- Line 41

```
K.gj=function(){function b(b,c){e?d[b]=!0:c()?d[b]=!1:e=d[b]=!0}function c(b){try{return!!eval(b)}catch(h){return!1}}var d={es3:!1},e=!1,f=K.global.navigator&&K.global.navigator.userAgent?K.global.navigator.userAgent:"";b("es5",function(){return c("[1,].length==1")});b("es6",function(){var b=f.match(/Edge\/(\d+)(\.\d)*/i);return b&&15>Number(b[1])?!1:c('(()=>{"use strict";class X{constructor(){if(new.target!=String)throw 1;this.x=42}}let q=Reflect.construct(X,[],String);if(q.x!=42||!(q instanceof String))throw 1;for(const a of[2,3]){if(a==2)continue;function f(z={a}){let a=0;return z.a}{function f(){return 0;}}return f()==3}})()')});
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    javascript.browser.security.eval-detected.eval-detected
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/javascript.browser.security.eval-detected.eval-detected">https://semgrep.dev/r/javascript.browser.security.eval-detected.eval-detected</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected the use of eval(). eval() can be dangerous if used to evaluate dynamic content. If this content can be input from outside the program, this may be a code injection vulnerability. Ensure evaluated content is not definable by external sources.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected the use of eval(). eval() can be dangerous if used to evaluate dynamic content. If this content can be input from outside the program, this may be a code injection vulnerability. Ensure evaluated content is not definable by external sources.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected a template variable used in an anchor tag with the &#39;href&#39; attribute. This allows a malicious actor to input the &#39;javascript:&#39; URI and is subject to cross- site scripting (XSS) attacks. If using a relative URL, start with a literal forward slash and concatenate the URL, like this: href=&#39;/{{link}}&#39;. You may also consider setting the Content Security Policy (CSP) header.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/templates/index.html


- Line 12

```
<li><a href = "{{ url[0] }}">{{ url[0] }}</a> - {{ url[1] }} - Allowed Methods: {{ url[2] }}</li>
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    javascript.express.security.audit.xss.mustache.var-in-href.var-in-href
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/javascript.express.security.audit.xss.mustache.var-in-href.var-in-href">https://semgrep.dev/r/javascript.express.security.audit.xss.mustache.var-in-href.var-in-href</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected a template variable used in an anchor tag with the &#39;href&#39; attribute. This allows a malicious actor to input the &#39;javascript:&#39; URI and is subject to cross- site scripting (XSS) attacks. If using a relative URL, start with a literal forward slash and concatenate the URL, like this: href=&#39;/{{link}}&#39;. You may also consider setting the Content Security Policy (CSP) header.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected a template variable used in an anchor tag with the &#39;href&#39; attribute. This allows a malicious actor to input the &#39;javascript:&#39; URI and is subject to cross- site scripting (XSS) attacks. If using a relative URL, start with a literal forward slash and concatenate the URL, like this: href=&#39;/{{link}}&#39;. You may also consider setting the Content Security Policy (CSP) header.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure this is safe, check that the HTML is rendered safely. Otherwise, use templates (`django.shortcuts.render`) which will safely render HTML instead.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 104

```
template = '''<html>
    <head>
    <title>Error</title>
    </head>
    <body>
    <h1>Oops that page doesn't exist!!</h1>
    <h3>%s</h3>
    </body>
    </html>
    ''' % request.url
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.django.security.injection.raw-html-format.raw-html-format
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.django.security.injection.raw-html-format.raw-html-format">https://semgrep.dev/r/python.django.security.injection.raw-html-format.raw-html-format</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure this is safe, check that the HTML is rendered safely. Otherwise, use templates (`django.shortcuts.render`) which will safely render HTML instead.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure this is safe, check that the HTML is rendered safely. Otherwise, use templates (`django.shortcuts.render`) which will safely render HTML instead.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

It looks like MD5 is used as a password hash. MD5 is not considered a secure password hash because it can be cracked by an attacker in a short amount of time. Use a suitable password hashing function such as scrypt. You can use `hashlib.scrypt`.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 142

```
hash_pass = hashlib.md5(password).hexdigest()
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.lang.security.audit.md5-used-as-password.md5-used-as-password
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.lang.security.audit.md5-used-as-password.md5-used-as-password">https://semgrep.dev/r/python.lang.security.audit.md5-used-as-password.md5-used-as-password</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    It looks like MD5 is used as a password hash. MD5 is not considered a secure password hash because it can be cracked by an attacker in a short amount of time. Use a suitable password hashing function such as scrypt. You can use `hashlib.scrypt`.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    It looks like MD5 is used as a password hash. MD5 is not considered a secure password hash because it can be cracked by an attacker in a short amount of time. Use a suitable password hashing function such as scrypt. You can use `hashlib.scrypt`.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Possibility of prototype polluting function detected. By adding or modifying attributes of an object prototype, it is possible to create attributes that exist on every object, or replace critical attributes with malicious ones. This can be problematic if the software depends on existence or non-existence of certain attributes, or uses pre-defined attributes of object prototype (such as hasOwnProperty, toString or valueOf). Possible mitigations might be: freezing the object prototype, using an object without prototypes (via Object.create(null) ), blocking modifications of attributes that resolve to object prototype, using Map instead of object.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/static/loader.js


- Line 3

```
J.Kj=function(b){return"undefined"!=typeof window&&window===b?b:"undefined"!=typeof global&&null!=global?global:b};J.global=J.Kj(this);J.Vk=function(b){if(b){for(var c=J.global,d=["Promise"],e=0;e<d.length-1;e++){var f=d[e];f in c||(c[f]={});c=c[f]}d=d[d.length-1];e=c[d];b=b(e);b!=e&&null!=b&&J.defineProperty(c,d,{configurable:!0,writable:!0,value:b})}};
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    javascript.lang.security.audit.prototype-pollution.prototype-pollution-loop.prototype-pollution-loop
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/javascript.lang.security.audit.prototype-pollution.prototype-pollution-loop.prototype-pollution-loop">https://semgrep.dev/r/javascript.lang.security.audit.prototype-pollution.prototype-pollution-loop.prototype-pollution-loop</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Possibility of prototype polluting function detected. By adding or modifying attributes of an object prototype, it is possible to create attributes that exist on every object, or replace critical attributes with malicious ones. This can be problematic if the software depends on existence or non-existence of certain attributes, or uses pre-defined attributes of object prototype (such as hasOwnProperty, toString or valueOf). Possible mitigations might be: freezing the object prototype, using an object without prototypes (via Object.create(null) ), blocking modifications of attributes that resolve to object prototype, using Map instead of object.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Possibility of prototype polluting function detected. By adding or modifying attributes of an object prototype, it is possible to create attributes that exist on every object, or replace critical attributes with malicious ones. This can be problematic if the software depends on existence or non-existence of certain attributes, or uses pre-defined attributes of object prototype (such as hasOwnProperty, toString or valueOf). Possible mitigations might be: freezing the object prototype, using an object without prototypes (via Object.create(null) ), blocking modifications of attributes that resolve to object prototype, using Map instead of object.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Possibility of prototype polluting function detected. By adding or modifying attributes of an object prototype, it is possible to create attributes that exist on every object, or replace critical attributes with malicious ones. This can be problematic if the software depends on existence or non-existence of certain attributes, or uses pre-defined attributes of object prototype (such as hasOwnProperty, toString or valueOf). Possible mitigations might be: freezing the object prototype, using an object without prototypes (via Object.create(null) ), blocking modifications of attributes that resolve to object prototype, using Map instead of object.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/static/loader.js


- Line 106

```
K.object.Xq=function(b){var c=0,d;for(d in b)c++;return c};K.object.Vq=function(b){for(var c in b)return c};K.object.Wq=function(b){for(var c in b)return b[c]};K.object.contains=function(b,c){return K.object.ej(b,c)};K.object.lr=function(b){var c=[],d=0,e;for(e in b)c[d++]=b[e];return c};K.object.Yf=function(b){var c=[],d=0,e;for(e in b)c[d++]=e;return c};K.object.kr=function(b,c){var d=K.Pb(c),e=d?c:arguments;for(d=d?0:1;d<e.length&&(b=b[e[d]],K.P(b));d++);return b};
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    javascript.lang.security.audit.prototype-pollution.prototype-pollution-loop.prototype-pollution-loop
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/javascript.lang.security.audit.prototype-pollution.prototype-pollution-loop.prototype-pollution-loop">https://semgrep.dev/r/javascript.lang.security.audit.prototype-pollution.prototype-pollution-loop.prototype-pollution-loop</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Possibility of prototype polluting function detected. By adding or modifying attributes of an object prototype, it is possible to create attributes that exist on every object, or replace critical attributes with malicious ones. This can be problematic if the software depends on existence or non-existence of certain attributes, or uses pre-defined attributes of object prototype (such as hasOwnProperty, toString or valueOf). Possible mitigations might be: freezing the object prototype, using an object without prototypes (via Object.create(null) ), blocking modifications of attributes that resolve to object prototype, using Map instead of object.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Possibility of prototype polluting function detected. By adding or modifying attributes of an object prototype, it is possible to create attributes that exist on every object, or replace critical attributes with malicious ones. This can be problematic if the software depends on existence or non-existence of certain attributes, or uses pre-defined attributes of object prototype (such as hasOwnProperty, toString or valueOf). Possible mitigations might be: freezing the object prototype, using an object without prototypes (via Object.create(null) ), blocking modifications of attributes that resolve to object prototype, using Map instead of object.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

RegExp() called with a `c` function argument, this might  allow an attacker to cause a Denial of Service (DoS)  within your application as RegExP which blocks the main thread.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/static/loader.js


- Line 55

```
K.f.Cb=function(b,c,d){var e=b;0<=c&&c<b.length&&0<d&&(e=b.substr(0,c)+b.substr(c+d,b.length-c-d));return e};K.f.remove=function(b,c){return b.replace(c,"")};K.f.Ls=function(b,c){c=new RegExp(K.f.Zd(c),"g");return b.replace(c,"")};K.f.Rs=function(b,c,d){c=new RegExp(K.f.Zd(c),"g");return b.replace(c,d.replace(/\$/g,"$$$$"))};K.f.Zd=function(b){return String(b).replace(/([-()\[\]{}+?*.$\^|,:#<!\\])/g,"\\$1").replace(/\x08/g,"\\x08")};
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    javascript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/javascript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp">https://semgrep.dev/r/javascript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    RegExp() called with a `$ARG` function argument, this might  allow an attacker to cause a Denial of Service (DoS)  within your application as RegExP which blocks the main thread.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    RegExp() called with a `$ARG` function argument, this might  allow an attacker to cause a Denial of Service (DoS)  within your application as RegExP which blocks the main thread.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

RegExp() called with a `c` function argument, this might  allow an attacker to cause a Denial of Service (DoS)  within your application as RegExP which blocks the main thread.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/static/loader.js


- Line 55

```
K.f.Cb=function(b,c,d){var e=b;0<=c&&c<b.length&&0<d&&(e=b.substr(0,c)+b.substr(c+d,b.length-c-d));return e};K.f.remove=function(b,c){return b.replace(c,"")};K.f.Ls=function(b,c){c=new RegExp(K.f.Zd(c),"g");return b.replace(c,"")};K.f.Rs=function(b,c,d){c=new RegExp(K.f.Zd(c),"g");return b.replace(c,d.replace(/\$/g,"$$$$"))};K.f.Zd=function(b){return String(b).replace(/([-()\[\]{}+?*.$\^|,:#<!\\])/g,"\\$1").replace(/\x08/g,"\\x08")};
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    javascript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/javascript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp">https://semgrep.dev/r/javascript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    RegExp() called with a `$ARG` function argument, this might  allow an attacker to cause a Denial of Service (DoS)  within your application as RegExP which blocks the main thread.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    RegExp() called with a `$ARG` function argument, this might  allow an attacker to cause a Denial of Service (DoS)  within your application as RegExP which blocks the main thread.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

RegExp() called with a `c` function argument, this might  allow an attacker to cause a Denial of Service (DoS)  within your application as RegExP which blocks the main thread.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/static/loader.js


- Line 59

```
K.f.Pt=function(b){return String(b).replace(/([A-Z])/g,"-$1").toLowerCase()};K.f.Qt=function(b,c){c=K.L(c)?K.f.Zd(c):"\\s";return b.replace(new RegExp("(^"+(c?"|["+c+"]+":"")+")([a-z])","g"),function(b,c,f){return c+f.toUpperCase()})};K.f.Tp=function(b){return String(b.charAt(0)).toUpperCase()+String(b.substr(1)).toLowerCase()};K.f.parseInt=function(b){isFinite(b)&&(b=String(b));return K.L(b)?/^\s*-?0x/i.test(b)?parseInt(b,16):parseInt(b,10):NaN};
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    javascript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/javascript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp">https://semgrep.dev/r/javascript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    RegExp() called with a `$ARG` function argument, this might  allow an attacker to cause a Denial of Service (DoS)  within your application as RegExP which blocks the main thread.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    RegExp() called with a `$ARG` function argument, this might  allow an attacker to cause a Denial of Service (DoS)  within your application as RegExP which blocks the main thread.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected a template variable used in an anchor tag with the &#39;href&#39; attribute. This allows a malicious actor to input the &#39;javascript:&#39; URI and is subject to cross- site scripting (XSS) attacks. Use the &#39;url&#39; template tag to safely generate a URL. You may also consider setting the Content Security Policy (CSP) header.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/templates/index.html


- Line 12

```
<li><a href = "{{ url[0] }}">{{ url[0] }}</a> - {{ url[1] }} - Allowed Methods: {{ url[2] }}</li>
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.django.security.audit.xss.template-href-var.template-href-var
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.django.security.audit.xss.template-href-var.template-href-var">https://semgrep.dev/r/python.django.security.audit.xss.template-href-var.template-href-var</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected a template variable used in an anchor tag with the &#39;href&#39; attribute. This allows a malicious actor to input the &#39;javascript:&#39; URI and is subject to cross- site scripting (XSS) attacks. Use the &#39;url&#39; template tag to safely generate a URL. You may also consider setting the Content Security Policy (CSP) header.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected a template variable used in an anchor tag with the &#39;href&#39; attribute. This allows a malicious actor to input the &#39;javascript:&#39; URI and is subject to cross- site scripting (XSS) attacks. Use the &#39;url&#39; template tag to safely generate a URL. You may also consider setting the Content Security Policy (CSP) header.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected a template variable used in an anchor tag with the &#39;href&#39; attribute. This allows a malicious actor to input the &#39;javascript:&#39; URI and is subject to cross- site scripting (XSS) attacks. Use &#39;url_for()&#39; to safely generate a URL. You may also consider setting the Content Security Policy (CSP) header.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/templates/index.html


- Line 12

```
<li><a href = "{{ url[0] }}">{{ url[0] }}</a> - {{ url[1] }} - Allowed Methods: {{ url[2] }}</li>
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.flask.security.xss.audit.template-href-var.template-href-var
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.flask.security.xss.audit.template-href-var.template-href-var">https://semgrep.dev/r/python.flask.security.xss.audit.template-href-var.template-href-var</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected a template variable used in an anchor tag with the &#39;href&#39; attribute. This allows a malicious actor to input the &#39;javascript:&#39; URI and is subject to cross- site scripting (XSS) attacks. Use &#39;url_for()&#39; to safely generate a URL. You may also consider setting the Content Security Policy (CSP) header.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected a template variable used in an anchor tag with the &#39;href&#39; attribute. This allows a malicious actor to input the &#39;javascript:&#39; URI and is subject to cross- site scripting (XSS) attacks. Use &#39;url_for()&#39; to safely generate a URL. You may also consider setting the Content Security Policy (CSP) header.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected possible formatted SQL query. Use parameterized queries instead.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 266

```
search_query = db.engine.execute(str_query)
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.lang.security.audit.formatted-sql-query.formatted-sql-query
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.lang.security.audit.formatted-sql-query.formatted-sql-query">https://semgrep.dev/r/python.lang.security.audit.formatted-sql-query.formatted-sql-query</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected possible formatted SQL query. Use parameterized queries instead.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected possible formatted SQL query. Use parameterized queries instead.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 142

```
hash_pass = hashlib.md5(password).hexdigest()
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.lang.security.insecure-hash-algorithms.insecure-hash-algorithm-md5
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.lang.security.insecure-hash-algorithms.insecure-hash-algorithm-md5">https://semgrep.dev/r/python.lang.security.insecure-hash-algorithms.insecure-hash-algorithm-md5</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/code/saes_module.py


- Line 785

```
digest_enc_key = hashlib.md5(enc_key.encode()).hexdigest()
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.lang.security.insecure-hash-algorithms.insecure-hash-algorithm-md5
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.lang.security.insecure-hash-algorithms.insecure-hash-algorithm-md5">https://semgrep.dev/r/python.lang.security.insecure-hash-algorithms.insecure-hash-algorithm-md5</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/code/saes_module.py


- Line 793

```
digest_shuffle_key = hashlib.md5(shuffle_key.encode()).hexdigest()
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.lang.security.insecure-hash-algorithms.insecure-hash-algorithm-md5
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.lang.security.insecure-hash-algorithms.insecure-hash-algorithm-md5">https://semgrep.dev/r/python.lang.security.insecure-hash-algorithms.insecure-hash-algorithm-md5</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure this is safe, check that the HTML is rendered safely. Otherwise, use templates (`flask.render_template`) which will safely render HTML instead.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 104

```
template = '''<html>
    <head>
    <title>Error</title>
    </head>
    <body>
    <h1>Oops that page doesn't exist!!</h1>
    <h3>%s</h3>
    </body>
    </html>
    ''' % request.url
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.flask.security.injection.raw-html-concat.raw-html-format
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.flask.security.injection.raw-html-concat.raw-html-format">https://semgrep.dev/r/python.flask.security.injection.raw-html-concat.raw-html-format</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure this is safe, check that the HTML is rendered safely. Otherwise, use templates (`flask.render_template`) which will safely render HTML instead.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure this is safe, check that the HTML is rendered safely. Otherwise, use templates (`flask.render_template`) which will safely render HTML instead.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 115

```
return render_template_string(template, dir = dir, help = help, locals = locals),404
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.flask.security.audit.render-template-string.render-template-string
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.flask.security.audit.render-template-string.render-template-string">https://semgrep.dev/r/python.flask.security.audit.render-template-string.render-template-string</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 282

```
return render_template_string(template, dir=dir, help=help, locals=locals), 404
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    python.flask.security.audit.render-template-string.render-template-string
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://semgrep.dev/r/python.flask.security.audit.render-template-string.render-template-string">https://semgrep.dev/r/python.flask.security.audit.render-template-string.render-template-string</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>







---

