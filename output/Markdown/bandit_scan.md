# Vulnerability Report

This report was automaticly generated based on the vulnerabilities specification of a [SARIF](https://sarifweb.azurewebsites.net) file.

## Tool information

> Name: Bandit







---

## Vulnerabilities

---

Use of weak MD4, MD5, or SHA1 hash for security. Consider usedforsecurity=False

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 142

```
hash_pass = hashlib.md5(password).hexdigest()
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    B324
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://bandit.readthedocs.io/en/1.7.4/plugins/b324_hashlib.html">https://bandit.readthedocs.io/en/1.7.4/plugins/b324_hashlib.html</a>
    </details>







---

Use of weak MD4, MD5, or SHA1 hash for security. Consider usedforsecurity=False

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/code/saes_module.py


- Line 785

```
digest_enc_key = hashlib.md5(enc_key.encode()).hexdigest()
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    B324
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://bandit.readthedocs.io/en/1.7.4/plugins/b324_hashlib.html">https://bandit.readthedocs.io/en/1.7.4/plugins/b324_hashlib.html</a>
    </details>







---

Use of weak MD4, MD5, or SHA1 hash for security. Consider usedforsecurity=False

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/code/saes_module.py


- Line 793

```
digest_shuffle_key = hashlib.md5(shuffle_key.encode()).hexdigest()
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    B324
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://bandit.readthedocs.io/en/1.7.4/plugins/b324_hashlib.html">https://bandit.readthedocs.io/en/1.7.4/plugins/b324_hashlib.html</a>
    </details>







---

Possible SQL injection vector through string-based query construction.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 262

```
str_query = "SELECT first_name, last_name, username FROM customer WHERE username = '%s';" % search_term
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    B608
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://bandit.readthedocs.io/en/1.7.4/plugins/b608_hardcoded_sql_expressions.html">https://bandit.readthedocs.io/en/1.7.4/plugins/b608_hardcoded_sql_expressions.html</a>
    </details>







---

Use of unsafe yaml load. Allows instantiation of arbitrary objects. Consider yaml.safe_load().

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 330

```
ydata = yaml.load(y)
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    B506
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://bandit.readthedocs.io/en/1.7.4/plugins/b506_yaml_load.html">https://bandit.readthedocs.io/en/1.7.4/plugins/b506_yaml_load.html</a>
    </details>







---

Possible hardcoded password: &#39;secret&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 25

```
app.config['SECRET_KEY_HMAC'] = 'secret'
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    B105
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://bandit.readthedocs.io/en/1.7.4/plugins/b105_hardcoded_password_string.html">https://bandit.readthedocs.io/en/1.7.4/plugins/b105_hardcoded_password_string.html</a>
    </details>







---

Possible hardcoded password: &#39;am0r3C0mpl3xK3y&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 26

```
app.config['SECRET_KEY_HMAC_2'] = 'am0r3C0mpl3xK3y'
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    B105
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://bandit.readthedocs.io/en/1.7.4/plugins/b105_hardcoded_password_string.html">https://bandit.readthedocs.io/en/1.7.4/plugins/b105_hardcoded_password_string.html</a>
    </details>







---

Possible hardcoded password: &#39;ak0r3C0mpl3xK3y&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 27

```
app.config['SECRET_KEY_HMAC_3'] = 'ak0r3C0mpl3xK3y'
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    B105
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://bandit.readthedocs.io/en/1.7.4/plugins/b105_hardcoded_password_string.html">https://bandit.readthedocs.io/en/1.7.4/plugins/b105_hardcoded_password_string.html</a>
    </details>







---

Possible hardcoded password: &#39;F12Zr47jyX R~X@H!jmM]Lwf/,?KT&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 28

```
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    B105
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://bandit.readthedocs.io/en/1.7.4/plugins/b105_hardcoded_password_string.html">https://bandit.readthedocs.io/en/1.7.4/plugins/b105_hardcoded_password_string.html</a>
    </details>







---

Possible hardcoded password: &#39;admin123&#39;

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 64

```
user.password = 'admin123'
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    B105
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://bandit.readthedocs.io/en/1.7.4/plugins/b105_hardcoded_password_string.html">https://bandit.readthedocs.io/en/1.7.4/plugins/b105_hardcoded_password_string.html</a>
    </details>







---

Standard pseudo-random generators are not suitable for security/cryptographic purposes.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 296

```
rand = random.randint(1, 100)
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    B311
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_calls.html#b311-random">https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_calls.html#b311-random</a>
    </details>







---

Standard pseudo-random generators are not suitable for security/cryptographic purposes.

### Locations
#### **Physical Location**
- Security-Pipeline-Testing/app/app.py


- Line 320

```
rand = random.randint(1,100)
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    B311
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_calls.html#b311-random">https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_calls.html#b311-random</a>
    </details>







---

