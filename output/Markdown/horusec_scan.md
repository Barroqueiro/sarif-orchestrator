# Vulnerability Report

This report was automaticly generated based on the vulnerabilities specification of a [SARIF](https://sarifweb.azurewebsites.net) file.

## Tool information

> Name: HorusecEngine


> Information Uri: [https://docs.horusec.io/docs/cli/analysis-tools/overview/](https://docs.horusec.io/docs/cli/analysis-tools/overview/)


> Version: 2.8.0



---

## Vulnerabilities

---

(1/1) * Possible vulnerability detected: Potential Hard-coded credential
The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.

### Locations
#### **Physical Location**
- app/app.py


- Line 25

```
app.config['SECRET_KEY_HMAC'] = 'secret'
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-LEAKS-25
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: Potential Hard-coded credential
	The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: Potential Hard-coded credential
	The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: Potential Hard-coded credential
The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.

### Locations
#### **Physical Location**
- app/app.py


- Line 26

```
app.config['SECRET_KEY_HMAC_2'] = 'am0r3C0mpl3xK3y'
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-LEAKS-25
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: Potential Hard-coded credential
	The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: Potential Hard-coded credential
	The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: Potential Hard-coded credential
The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.

### Locations
#### **Physical Location**
- app/app.py


- Line 27

```
app.config['SECRET_KEY_HMAC_3'] = 'ak0r3C0mpl3xK3y'
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-LEAKS-25
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: Potential Hard-coded credential
	The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: Potential Hard-coded credential
	The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: Potential Hard-coded credential
The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.

### Locations
#### **Physical Location**
- app/app.py


- Line 185

```
MAC'], algorithm='HS256')
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-LEAKS-25
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: Potential Hard-coded credential
	The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: Potential Hard-coded credential
	The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: Hard-coded password
The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.

### Locations
#### **Physical Location**
- app/app.py


- Line 64

```
user.password = 'admin123'
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-LEAKS-26
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: Hard-coded password
	The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: Hard-coded password
	The software contains hard-coded credentials, such as a password or cryptographic key, which it uses for its own inbound authentication, outbound communication to external components, or encryption of internal data. For more information checkout the CWE-798 (https://cwe.mitre.org/data/definitions/798.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: No use eval
The eval function is extremely dangerous. Because if any user input is not handled correctly and passed to it, it will be possible to execute code remotely in the context of your application (RCE - Remote Code Executuion). For more information checkout the CWE-94 (https://cwe.mitre.org/data/definitions/94.html) advisory.

### Locations
#### **Physical Location**
- app/static/loader.js


- Line 24

```
eval(b);return{}};
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-JAVASCRIPT-2
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use eval
	The eval function is extremely dangerous. Because if any user input is not handled correctly and passed to it, it will be possible to execute code remotely in the context of your application (RCE - Remote Code Executuion). For more information checkout the CWE-94 (https://cwe.mitre.org/data/definitions/94.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use eval
	The eval function is extremely dangerous. Because if any user input is not handled correctly and passed to it, it will be possible to execute code remotely in the context of your application (RCE - Remote Code Executuion). For more information checkout the CWE-94 (https://cwe.mitre.org/data/definitions/94.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: No use eval
The eval function is extremely dangerous. Because if any user input is not handled correctly and passed to it, it will be possible to execute code remotely in the context of your application (RCE - Remote Code Executuion). For more information checkout the CWE-94 (https://cwe.mitre.org/data/definitions/94.html) advisory.

### Locations
#### **Physical Location**
- app/static/loader.js


- Line 26

```
eval(g+a+f);if(K.global.$gwtExport&&K.global.$gwtExport.$jscomp&&!K.global.$gwtExport.$jscomp.transp
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-JAVASCRIPT-2
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use eval
	The eval function is extremely dangerous. Because if any user input is not handled correctly and passed to it, it will be possible to execute code remotely in the context of your application (RCE - Remote Code Executuion). For more information checkout the CWE-94 (https://cwe.mitre.org/data/definitions/94.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use eval
	The eval function is extremely dangerous. Because if any user input is not handled correctly and passed to it, it will be possible to execute code remotely in the context of your application (RCE - Remote Code Executuion). For more information checkout the CWE-94 (https://cwe.mitre.org/data/definitions/94.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: No use eval
The eval function is extremely dangerous. Because if any user input is not handled correctly and passed to it, it will be possible to execute code remotely in the context of your application (RCE - Remote Code Executuion). For more information checkout the CWE-94 (https://cwe.mitre.org/data/definitions/94.html) advisory.

### Locations
#### **Physical Location**
- app/static/loader.js


- Line 33

```
eval("var _evalTest_ = 1;"),"undefined"!=typeof K.global._evalTest_){try{delete K.global._evalTest_}
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-JAVASCRIPT-2
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use eval
	The eval function is extremely dangerous. Because if any user input is not handled correctly and passed to it, it will be possible to execute code remotely in the context of your application (RCE - Remote Code Executuion). For more information checkout the CWE-94 (https://cwe.mitre.org/data/definitions/94.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use eval
	The eval function is extremely dangerous. Because if any user input is not handled correctly and passed to it, it will be possible to execute code remotely in the context of your application (RCE - Remote Code Executuion). For more information checkout the CWE-94 (https://cwe.mitre.org/data/definitions/94.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: No use eval
The eval function is extremely dangerous. Because if any user input is not handled correctly and passed to it, it will be possible to execute code remotely in the context of your application (RCE - Remote Code Executuion). For more information checkout the CWE-94 (https://cwe.mitre.org/data/definitions/94.html) advisory.

### Locations
#### **Physical Location**
- app/static/loader.js


- Line 41

```
eval(b)}catch(h){return!1}}var d={es3:!1},e=!1,f=K.global.navigator&&K.global.navigator.userAgent?K.
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-JAVASCRIPT-2
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use eval
	The eval function is extremely dangerous. Because if any user input is not handled correctly and passed to it, it will be possible to execute code remotely in the context of your application (RCE - Remote Code Executuion). For more information checkout the CWE-94 (https://cwe.mitre.org/data/definitions/94.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use eval
	The eval function is extremely dangerous. Because if any user input is not handled correctly and passed to it, it will be possible to execute code remotely in the context of your application (RCE - Remote Code Executuion). For more information checkout the CWE-94 (https://cwe.mitre.org/data/definitions/94.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: Origins should be verified during cross-origin communications
Browsers allow message exchanges between Window objects of different origins. Because any window can send / receive messages from other window it is important to verify the sender&#39;s / receiver&#39;s identity: When sending message with postMessage method, the identity&#39;s receiver should be defined (the wildcard keyword (*) should not be used).
When receiving message with message event, the sender&#39;s identity should be verified using the origin and possibly source properties. For more information checkout the OWASP A2:2017 (https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication) and (https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) advisory.

### Locations
#### **Physical Location**
- app/static/loader.js


- Line 120

```
.postMessage(d,e)}}});if("undefined"!==typeof b&&!K.g.userAgent.v.xc()){var c=new b,d={},e=d;c.port1
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-JAVASCRIPT-11
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: Origins should be verified during cross-origin communications
	Browsers allow message exchanges between Window objects of different origins. Because any window can send / receive messages from other window it is important to verify the sender&#39;s / receiver&#39;s identity: When sending message with postMessage method, the identity&#39;s receiver should be defined (the wildcard keyword (*) should not be used).
	When receiving message with message event, the sender&#39;s identity should be verified using the origin and possibly source properties. For more information checkout the OWASP A2:2017 (https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication) and (https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: Origins should be verified during cross-origin communications
	Browsers allow message exchanges between Window objects of different origins. Because any window can send / receive messages from other window it is important to verify the sender&#39;s / receiver&#39;s identity: When sending message with postMessage method, the identity&#39;s receiver should be defined (the wildcard keyword (*) should not be used).
	When receiving message with message event, the sender&#39;s identity should be verified using the origin and possibly source properties. For more information checkout the OWASP A2:2017 (https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication) and (https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: Origins should be verified during cross-origin communications
Browsers allow message exchanges between Window objects of different origins. Because any window can send / receive messages from other window it is important to verify the sender&#39;s / receiver&#39;s identity: When sending message with postMessage method, the identity&#39;s receiver should be defined (the wildcard keyword (*) should not be used).
When receiving message with message event, the sender&#39;s identity should be verified using the origin and possibly source properties. For more information checkout the OWASP A2:2017 (https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication) and (https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) advisory.

### Locations
#### **Physical Location**
- app/static/loader.js


- Line 120

```
.addEventListener("message",b,!1);this.port1={};this.port2={postMessage:function(){c.postMessage(d,e
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-JAVASCRIPT-11
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: Origins should be verified during cross-origin communications
	Browsers allow message exchanges between Window objects of different origins. Because any window can send / receive messages from other window it is important to verify the sender&#39;s / receiver&#39;s identity: When sending message with postMessage method, the identity&#39;s receiver should be defined (the wildcard keyword (*) should not be used).
	When receiving message with message event, the sender&#39;s identity should be verified using the origin and possibly source properties. For more information checkout the OWASP A2:2017 (https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication) and (https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: Origins should be verified during cross-origin communications
	Browsers allow message exchanges between Window objects of different origins. Because any window can send / receive messages from other window it is important to verify the sender&#39;s / receiver&#39;s identity: When sending message with postMessage method, the identity&#39;s receiver should be defined (the wildcard keyword (*) should not be used).
	When receiving message with message event, the sender&#39;s identity should be verified using the origin and possibly source properties. For more information checkout the OWASP A2:2017 (https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication) and (https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: No use weak random number generator
When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.

### Locations
#### **Physical Location**
- app/static/loader.js


- Line 30

```
Math.random()>>>0);K.Fl=0;K.$q=K.ng;K.Os=K.Xk;K.cj=function(b){var c=K.aa(b);if(c==y||c==r){if(b.clo
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-JAVASCRIPT-6
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use weak random number generator
	When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use weak random number generator
	When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: No use weak random number generator
When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.

### Locations
#### **Physical Location**
- app/static/loader.js


- Line 56

```
Math.random()).toString(36)+Math.abs(Math.floor(2147483648*Math.random())^K.now()).toString(36)};
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-JAVASCRIPT-6
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use weak random number generator
	When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use weak random number generator
	When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: No use weak random number generator
When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.

### Locations
#### **Physical Location**
- app/static/loader.js


- Line 56

```
Math.random())^K.now()).toString(36)};
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-JAVASCRIPT-6
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use weak random number generator
	When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use weak random number generator
	When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: No use weak random number generator
When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.

### Locations
#### **Physical Location**
- app/static/loader.js


- Line 58

```
Math.random()|0;K.f.rq=function(){return"goog_"+K.f.Jl++};K.f.Nt=function(b){var c=Number(b);return
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-JAVASCRIPT-6
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use weak random number generator
	When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use weak random number generator
	When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: No use weak random number generator
When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.

### Locations
#### **Physical Location**
- app/static/loader.js


- Line 119

```
Math.random(),e="file:"==c.location.protocol?"*":c.location.protocol+"//"+c.location.host;b=K.bind(f
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-JAVASCRIPT-6
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use weak random number generator
	When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use weak random number generator
	When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: No use weak random number generator
When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.

### Locations
#### **Physical Location**
- app/static/loader.js


- Line 155

```
Math.random()*b)};K.s.Wt=function(b,c){return b+Math.random()*(c-b)};K.s.Yp=function(b,c,d){return M
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-JAVASCRIPT-6
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use weak random number generator
	When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use weak random number generator
	When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.
    </details>





---

(1/1) * Possible vulnerability detected: No use weak random number generator
When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.

### Locations
#### **Physical Location**
- app/static/loader.js


- Line 155

```
Math.random()*(c-b)};K.s.Yp=function(b,c,d){return Math.min(Math.max(b,c),d)};K.s.Yg=function(b,c){b
```






### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    HS-JAVASCRIPT-6
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://docs.horusec.io/docs/cli/analysis-tools/overview/">https://docs.horusec.io/docs/cli/analysis-tools/overview/</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use weak random number generator
	When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    (1/1) * Possible vulnerability detected: No use weak random number generator
	When software generates predictable values in a context requiring unpredictability, it may be possible for an attacker to guess the next value that will be generated, and use this guess to impersonate another user or access sensitive information. As the Math.random() function relies on a weak pseudorandom number generator, this function should not be used for security-critical applications or for protecting sensitive data. In such context, a cryptographically strong pseudorandom number generator (CSPRNG) should be used instead. For more information checkout the CWE-338 (https://cwe.mitre.org/data/definitions/338.html) advisory.
    </details>





---

