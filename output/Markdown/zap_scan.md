# Vulnerability Report

This report was automaticly generated based on the vulnerabilities specification of a [SARIF](https://sarifweb.azurewebsites.net) file.

## Tool information

> Name: OWASP ZAP


> Information Uri: [https://www.zaproxy.org/](https://www.zaproxy.org/)


> Version: 2.12.0

> Semantic version: 2.12.0


---

## Vulnerabilities

---

Based on the successful response status code cloud metadata may have been returned in the response. Check the response data to see if any cloud metadata has been returned.
The meta data returned can include information that would allow an attacker to completely compromise the system.

### Locations
#### **Physical Location**
- http://localhost:5000/latest/meta-data/


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    90034
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Cloud Metadata Potentially Exposed
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Cloud Metadata Attack attempts to abuse a misconfigured NGINX server in order to access the instance metadata maintained by cloud service providers such as AWS, GCP and Azure.
	All of these providers provide metadata via an internal unroutable IP address &#39;169.254.169.254&#39; - this can be exposed by incorrectly configured NGINX servers and accessed by using this IP address in the Host header field.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

The response does not include either Content-Security-Policy with &#39;frame-ancestors&#39; directive or X-Frame-Options to protect against &#39;ClickJacking&#39; attacks.

### Locations
#### **Physical Location**
- http://localhost:5000


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10020
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Missing Anti-clickjacking Header
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The response does not include either Content-Security-Policy with &#39;frame-ancestors&#39; directive or X-Frame-Options to protect against &#39;ClickJacking&#39; attacks.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

The response does not include either Content-Security-Policy with &#39;frame-ancestors&#39; directive or X-Frame-Options to protect against &#39;ClickJacking&#39; attacks.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10020
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Missing Anti-clickjacking Header
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The response does not include either Content-Security-Policy with &#39;frame-ancestors&#39; directive or X-Frame-Options to protect against &#39;ClickJacking&#39; attacks.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

The response does not include either Content-Security-Policy with &#39;frame-ancestors&#39; directive or X-Frame-Options to protect against &#39;ClickJacking&#39; attacks.

### Locations
#### **Physical Location**
- http://localhost:5000/robots.txt


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10020
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Missing Anti-clickjacking Header
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The response does not include either Content-Security-Policy with &#39;frame-ancestors&#39; directive or X-Frame-Options to protect against &#39;ClickJacking&#39; attacks.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

The response does not include either Content-Security-Policy with &#39;frame-ancestors&#39; directive or X-Frame-Options to protect against &#39;ClickJacking&#39; attacks.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10020
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Missing Anti-clickjacking Header
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The response does not include either Content-Security-Policy with &#39;frame-ancestors&#39; directive or X-Frame-Options to protect against &#39;ClickJacking&#39; attacks.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

The response does not include either Content-Security-Policy with &#39;frame-ancestors&#39; directive or X-Frame-Options to protect against &#39;ClickJacking&#39; attacks.

### Locations
#### **Physical Location**
- http://localhost:5000/sitemap.xml


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10020
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Missing Anti-clickjacking Header
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The response does not include either Content-Security-Policy with &#39;frame-ancestors&#39; directive or X-Frame-Options to protect against &#39;ClickJacking&#39; attacks.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

### Locations
#### **Physical Location**
- http://localhost:5000


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10038
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Content Security Policy (CSP) Header Not Set
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10038
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Content Security Policy (CSP) Header Not Set
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

### Locations
#### **Physical Location**
- http://localhost:5000/robots.txt


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10038
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Content Security Policy (CSP) Header Not Set
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10038
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Content Security Policy (CSP) Header Not Set
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

### Locations
#### **Physical Location**
- http://localhost:5000/sitemap.xml


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10038
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Content Security Policy (CSP) Header Not Set
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token] was found in the following HTML form: [Form 1: &#34;email&#34; &#34;password&#34; ].

### Locations
#### **Physical Location**
- http://localhost:5000


- Line 1

```
<form
        method="post"
        action="/login">
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10202
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Absence of Anti-CSRF Tokens
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No Anti-CSRF tokens were found in a HTML submission form.
	A cross-site request forgery is an attack that involves forcing a victim to send an HTTP request to a target destination without their knowledge or intent in order to perform an action as the victim. The underlying cause is application functionality using predictable URL/form actions in a repeatable way. The nature of the attack is that CSRF exploits the trust that a web site has for a user. By contrast, cross-site scripting (XSS) exploits the trust that a user has for a web site. Like XSS, CSRF attacks are not necessarily cross-site, but they can be. Cross-site request forgery is also known as CSRF, XSRF, one-click attack, session riding, confused deputy, and sea surf.
	
	CSRF attacks are effective in a number of situations, including:
	    * The victim has an active session on the target site.
	    * The victim is authenticated via HTTP auth on the target site.
	    * The victim is on the same local network as the target site.
	
	CSRF has primarily been used to perform an action against a target site using the victim&#39;s privileges, but recent techniques have been discovered to disclose information by gaining access to the response. The risk of information disclosure is dramatically increased when the target site is vulnerable to XSS, because XSS can be used as a platform for CSRF, allowing the attack to operate within the bounds of the same-origin policy.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token] was found in the following HTML form: [Form 1: &#34;email&#34; &#34;password&#34; ].

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1

```
<form
        method="post"
        action="/login">
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10202
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Absence of Anti-CSRF Tokens
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No Anti-CSRF tokens were found in a HTML submission form.
	A cross-site request forgery is an attack that involves forcing a victim to send an HTTP request to a target destination without their knowledge or intent in order to perform an action as the victim. The underlying cause is application functionality using predictable URL/form actions in a repeatable way. The nature of the attack is that CSRF exploits the trust that a web site has for a user. By contrast, cross-site scripting (XSS) exploits the trust that a user has for a web site. Like XSS, CSRF attacks are not necessarily cross-site, but they can be. Cross-site request forgery is also known as CSRF, XSRF, one-click attack, session riding, confused deputy, and sea surf.
	
	CSRF attacks are effective in a number of situations, including:
	    * The victim has an active session on the target site.
	    * The victim is authenticated via HTTP auth on the target site.
	    * The victim is on the same local network as the target site.
	
	CSRF has primarily been used to perform an action against a target site using the victim&#39;s privileges, but recent techniques have been discovered to disclose information by gaining access to the response. The risk of information disclosure is dramatically increased when the target site is vulnerable to XSS, because XSS can be used as a platform for CSRF, allowing the attack to operate within the bounds of the same-origin policy.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token] was found in the following HTML form: [Form 1: &#34;email&#34; &#34;password&#34; &#34;registration_code&#34; ].

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1

```
<form
        method="post"
        action="/signup">
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10202
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Absence of Anti-CSRF Tokens
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No Anti-CSRF tokens were found in a HTML submission form.
	A cross-site request forgery is an attack that involves forcing a victim to send an HTTP request to a target destination without their knowledge or intent in order to perform an action as the victim. The underlying cause is application functionality using predictable URL/form actions in a repeatable way. The nature of the attack is that CSRF exploits the trust that a web site has for a user. By contrast, cross-site scripting (XSS) exploits the trust that a user has for a web site. Like XSS, CSRF attacks are not necessarily cross-site, but they can be. Cross-site request forgery is also known as CSRF, XSRF, one-click attack, session riding, confused deputy, and sea surf.
	
	CSRF attacks are effective in a number of situations, including:
	    * The victim has an active session on the target site.
	    * The victim is authenticated via HTTP auth on the target site.
	    * The victim is on the same local network as the target site.
	
	CSRF has primarily been used to perform an action against a target site using the victim&#39;s privileges, but recent techniques have been discovered to disclose information by gaining access to the response. The risk of information disclosure is dramatically increased when the target site is vulnerable to XSS, because XSS can be used as a platform for CSRF, allowing the attack to operate within the bounds of the same-origin policy.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

A sensitive file was identified as accessible or available. This may leak administrative, configuration, or credential information which can be leveraged by a malicious individual to further attack the system or conduct social engineering efforts.

### Locations
#### **Physical Location**
- http://localhost:5000/._darcs


- Line 1

```
HTTP/1.1 200 OK
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    40035
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Hidden File Found
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A sensitive file was identified as accessible or available. This may leak administrative, configuration, or credential information which can be leveraged by a malicious individual to further attack the system or conduct social engineering efforts.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

A sensitive file was identified as accessible or available. This may leak administrative, configuration, or credential information which can be leveraged by a malicious individual to further attack the system or conduct social engineering efforts.

### Locations
#### **Physical Location**
- http://localhost:5000/.bzr


- Line 1

```
HTTP/1.1 200 OK
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    40035
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Hidden File Found
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A sensitive file was identified as accessible or available. This may leak administrative, configuration, or credential information which can be leveraged by a malicious individual to further attack the system or conduct social engineering efforts.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

A sensitive file was identified as accessible or available. This may leak administrative, configuration, or credential information which can be leveraged by a malicious individual to further attack the system or conduct social engineering efforts.

### Locations
#### **Physical Location**
- http://localhost:5000/.hg


- Line 1

```
HTTP/1.1 200 OK
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    40035
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Hidden File Found
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A sensitive file was identified as accessible or available. This may leak administrative, configuration, or credential information which can be leveraged by a malicious individual to further attack the system or conduct social engineering efforts.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

A sensitive file was identified as accessible or available. This may leak administrative, configuration, or credential information which can be leveraged by a malicious individual to further attack the system or conduct social engineering efforts.

### Locations
#### **Physical Location**
- http://localhost:5000/BitKeeper


- Line 1

```
HTTP/1.1 200 OK
```






### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    40035
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Hidden File Found
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A sensitive file was identified as accessible or available. This may leak administrative, configuration, or credential information which can be leveraged by a malicious individual to further attack the system or conduct social engineering efforts.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

The following pattern was used: \bSELECT\b and was detected in the element starting with: &#34;!function(t,e){&#34;object&#34;==typeof exports&amp;&amp;&#34;undefined&#34;!=typeof module?module.exports=e(require(&#34;@popperjs/core&#34;)):&#34;function&#34;==type&#34;, see evidence field for the suspicious comment/snippet.

### Locations
#### **Physical Location**
- http://localhost:5000/bootstrap/static/js/bootstrap.min.js


- Line 6

```
select
```






### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10027
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Information Disclosure - Suspicious Comments
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The response appears to contain suspicious comments which may help an attacker. Note: Matches made within script blocks or files are against the entire content not only comments.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/home


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/home


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/home


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/home


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/home


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/home


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/home


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/home


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/home


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/home


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/home


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/home


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10104
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    User Agent Fuzzer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

The origin domain used for comparison was: 
localhost
preferences=gASVEwAAAAAAAAB9lIwEbW9kZZSMBWxpZ2h0lHMu


### Locations
#### **Physical Location**
- http://localhost:5000


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    90033
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Loosely Scoped Cookie
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Cookies can be scoped by domain or path. This check is only concerned with domain scope.The domain scope applied to a cookie determines which domains can access it. For example, a cookie can be scoped strictly to a subdomain e.g. www.nottrusted.com, or loosely scoped to a parent domain e.g. nottrusted.com. In the latter case, any subdomain of nottrusted.com can access the cookie. Loosely scoped cookies are common in mega-applications like google.com and live.com. Cookies set from a subdomain like app.foo.bar are transmitted only to that domain by the browser. However, cookies scoped to a parent-level domain may be transmitted to the parent, or any subdomain of the parent.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

The origin domain used for comparison was: 
localhost
preferences=gASVEwAAAAAAAAB9lIwEbW9kZZSMBWxpZ2h0lHMu


### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    90033
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Loosely Scoped Cookie
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Cookies can be scoped by domain or path. This check is only concerned with domain scope.The domain scope applied to a cookie determines which domains can access it. For example, a cookie can be scoped strictly to a subdomain e.g. www.nottrusted.com, or loosely scoped to a parent domain e.g. nottrusted.com. In the latter case, any subdomain of nottrusted.com can access the cookie. Loosely scoped cookies are common in mega-applications like google.com and live.com. Cookies set from a subdomain like app.foo.bar are transmitted only to that domain by the browser. However, cookies scoped to a parent-level domain may be transmitted to the parent, or any subdomain of the parent.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

The origin domain used for comparison was: 
localhost
session=.eJyFjrEKwzAMRH9F1Wz6AV47de8WhyKwXAtcp5XSZjD592jpXDi443hwN_BeGlllwzgNhNUNWXVRDDgS8pOkJYwwJbxVMSjCLYMH5fdHlPM54Rwg4YvMtkXzX3h3hd_URtqlP3zs2r_UJMPFMe6rULOTk3Pwh8pWMRaveD8AqA077w.Y9PSIg.hPcWBA5LSdhS_zc5p50fORuwNyw


### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    90033
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Loosely Scoped Cookie
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Cookies can be scoped by domain or path. This check is only concerned with domain scope.The domain scope applied to a cookie determines which domains can access it. For example, a cookie can be scoped strictly to a subdomain e.g. www.nottrusted.com, or loosely scoped to a parent domain e.g. nottrusted.com. In the latter case, any subdomain of nottrusted.com can access the cookie. Loosely scoped cookies are common in mega-applications like google.com and live.com. Cookies set from a subdomain like app.foo.bar are transmitted only to that domain by the browser. However, cookies scoped to a parent-level domain may be transmitted to the parent, or any subdomain of the parent.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

The origin domain used for comparison was: 
localhost
session=.eJyFjrEKwzAMRH9F1Wz6AV47de8WhyKwXAtcp5XSZjD592jpXDi443hwN_BeGlllwzgNhNUNWXVRDDgS8pOkJYwwJbxVMSjCLYMH5fdHlPM54Rwg4YvMtkXzX3h3hd_URtqlP3zs2r_UJMPFMe6rULOTk3Pwh8pWMRaveD8AqA077w.Y9PSKg.q1hAkzDDm_GeKFRcpHwMzXZNS8M


### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    90033
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Loosely Scoped Cookie
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Cookies can be scoped by domain or path. This check is only concerned with domain scope.The domain scope applied to a cookie determines which domains can access it. For example, a cookie can be scoped strictly to a subdomain e.g. www.nottrusted.com, or loosely scoped to a parent domain e.g. nottrusted.com. In the latter case, any subdomain of nottrusted.com can access the cookie. Loosely scoped cookies are common in mega-applications like google.com and live.com. Cookies set from a subdomain like app.foo.bar are transmitted only to that domain by the browser. However, cookies scoped to a parent-level domain may be transmitted to the parent, or any subdomain of the parent.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

The origin domain used for comparison was: 
localhost
session=eyJfZmxhc2hlcyI6W3siIHQiOlsid2FybmluZyIsIkludmFsaWQgQ3JlZGVudGlhbHMhIl19XSwiX2ZyZXNoIjpmYWxzZX0.Y9PSEQ.miZIrD0ypMRmv2svWvMJBHokkrg


### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    90033
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Loosely Scoped Cookie
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Cookies can be scoped by domain or path. This check is only concerned with domain scope.The domain scope applied to a cookie determines which domains can access it. For example, a cookie can be scoped strictly to a subdomain e.g. www.nottrusted.com, or loosely scoped to a parent domain e.g. nottrusted.com. In the latter case, any subdomain of nottrusted.com can access the cookie. Loosely scoped cookies are common in mega-applications like google.com and live.com. Cookies set from a subdomain like app.foo.bar are transmitted only to that domain by the browser. However, cookies scoped to a parent-level domain may be transmitted to the parent, or any subdomain of the parent.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

The origin domain used for comparison was: 
localhost
session=eyJfZnJlc2giOmZhbHNlfQ.Y9PSIg.EBXyljVr86h4brJhCWIOphrz3qU


### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    90033
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Loosely Scoped Cookie
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Cookies can be scoped by domain or path. This check is only concerned with domain scope.The domain scope applied to a cookie determines which domains can access it. For example, a cookie can be scoped strictly to a subdomain e.g. www.nottrusted.com, or loosely scoped to a parent domain e.g. nottrusted.com. In the latter case, any subdomain of nottrusted.com can access the cookie. Loosely scoped cookies are common in mega-applications like google.com and live.com. Cookies set from a subdomain like app.foo.bar are transmitted only to that domain by the browser. However, cookies scoped to a parent-level domain may be transmitted to the parent, or any subdomain of the parent.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

The origin domain used for comparison was: 
localhost
session=eyJfZnJlc2giOmZhbHNlfQ.Y9PSKg.KdwN2MJjn_qQSJGz3bMBwT-qC9M


### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    90033
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Loosely Scoped Cookie
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Cookies can be scoped by domain or path. This check is only concerned with domain scope.The domain scope applied to a cookie determines which domains can access it. For example, a cookie can be scoped strictly to a subdomain e.g. www.nottrusted.com, or loosely scoped to a parent domain e.g. nottrusted.com. In the latter case, any subdomain of nottrusted.com can access the cookie. Loosely scoped cookies are common in mega-applications like google.com and live.com. Cookies set from a subdomain like app.foo.bar are transmitted only to that domain by the browser. However, cookies scoped to a parent-level domain may be transmitted to the parent, or any subdomain of the parent.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

The origin domain used for comparison was: 
localhost
session=.eJyFjTEKwkAQRa8y_jp4gLRW9nbZIAM7MQPrRmeiKZbcPdNYCx_eLx68hvtU2Gdx9EMDrQGI2WLo0BLkyVoSehoSbrM6TSolUxyT90dN8jlh7Cjhxe7bYvmvvMe6X2pjq1ofEbvWLxfNdAlN6qpc_BTmuB9OETbD.Y9PSIQ.-MopVY3qkM34CMwWEw7tOEG6C3Y


### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    90033
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Loosely Scoped Cookie
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Cookies can be scoped by domain or path. This check is only concerned with domain scope.The domain scope applied to a cookie determines which domains can access it. For example, a cookie can be scoped strictly to a subdomain e.g. www.nottrusted.com, or loosely scoped to a parent domain e.g. nottrusted.com. In the latter case, any subdomain of nottrusted.com can access the cookie. Loosely scoped cookies are common in mega-applications like google.com and live.com. Cookies set from a subdomain like app.foo.bar are transmitted only to that domain by the browser. However, cookies scoped to a parent-level domain may be transmitted to the parent, or any subdomain of the parent.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

The origin domain used for comparison was: 
localhost
session=.eJyFjTEKwkAQRa8y_jp4gLRW9nbZIAM7MQPrRmeiKZbcPdNYCx_eLx68hvtU2Gdx9EMDrQGI2WLo0BLkyVoSehoSbrM6TSolUxyT90dN8jlh7Cjhxe7bYvmvvMe6X2pjq1ofEbvWLxfNdAlN6qpc_BTmuB9OETbD.Y9PSKg.gS3-pLfapDv_BF1UoKyq_zm8SJ8


### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    90033
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Loosely Scoped Cookie
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Cookies can be scoped by domain or path. This check is only concerned with domain scope.The domain scope applied to a cookie determines which domains can access it. For example, a cookie can be scoped strictly to a subdomain e.g. www.nottrusted.com, or loosely scoped to a parent domain e.g. nottrusted.com. In the latter case, any subdomain of nottrusted.com can access the cookie. Loosely scoped cookies are common in mega-applications like google.com and live.com. Cookies set from a subdomain like app.foo.bar are transmitted only to that domain by the browser. However, cookies scoped to a parent-level domain may be transmitted to the parent, or any subdomain of the parent.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

The origin domain used for comparison was: 
localhost
session=eyJfZmxhc2hlcyI6W3siIHQiOlsid2FybmluZyIsIkludmFsaWQgQ3JlZGVudGlhbHMhIl19XX0.Y9PSEQ.ZZ9TdKmI3HGkddAzwI5CprrSRlQ


### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    90033
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Loosely Scoped Cookie
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Cookies can be scoped by domain or path. This check is only concerned with domain scope.The domain scope applied to a cookie determines which domains can access it. For example, a cookie can be scoped strictly to a subdomain e.g. www.nottrusted.com, or loosely scoped to a parent domain e.g. nottrusted.com. In the latter case, any subdomain of nottrusted.com can access the cookie. Loosely scoped cookies are common in mega-applications like google.com and live.com. Cookies set from a subdomain like app.foo.bar are transmitted only to that domain by the browser. However, cookies scoped to a parent-level domain may be transmitted to the parent, or any subdomain of the parent.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

The origin domain used for comparison was: 
localhost
session=.eJwNxkEKgDAMBdGrhL8Wd248gJewIrFGLVQLSVwV725h4E3FemS2SwzjXEHegKgWRYcaoHImc2VP5Vlj2SVgpDlgSpJ3ul9z2oTYKQu3HyherBxd1CiX5-wDlq-1fD-SxSSg.Y9PSEQ.ZGT4qfZ7OlxMOxKGH7uqCT9C70U


### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- None


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    90033
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Loosely Scoped Cookie
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Cookies can be scoped by domain or path. This check is only concerned with domain scope.The domain scope applied to a cookie determines which domains can access it. For example, a cookie can be scoped strictly to a subdomain e.g. www.nottrusted.com, or loosely scoped to a parent domain e.g. nottrusted.com. In the latter case, any subdomain of nottrusted.com can access the cookie. Loosely scoped cookies are common in mega-applications like google.com and live.com. Cookies set from a subdomain like app.foo.bar are transmitted only to that domain by the browser. However, cookies scoped to a parent-level domain may be transmitted to the parent, or any subdomain of the parent.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    low
    </details>






---

A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.

### Locations
#### **Physical Location**
- http://localhost:5000


- Line 1

```
Set-Cookie: preferences
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10010
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Cookie No HttpOnly Flag
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1

```
Set-Cookie: preferences
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10010
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Cookie No HttpOnly Flag
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At &#34;High&#34; threshold this scan rule will not alert on client or server error responses.

### Locations
#### **Physical Location**
- http://localhost:5000


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10021
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    X-Content-Type-Options Header Missing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Anti-MIME-Sniffing header X-Content-Type-Options was not set to &#39;nosniff&#39;. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At &#34;High&#34; threshold this scan rule will not alert on client or server error responses.

### Locations
#### **Physical Location**
- http://localhost:5000/bootstrap/static/css/bootstrap.min.css


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10021
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    X-Content-Type-Options Header Missing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Anti-MIME-Sniffing header X-Content-Type-Options was not set to &#39;nosniff&#39;. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At &#34;High&#34; threshold this scan rule will not alert on client or server error responses.

### Locations
#### **Physical Location**
- http://localhost:5000/bootstrap/static/js/bootstrap.min.js


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10021
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    X-Content-Type-Options Header Missing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Anti-MIME-Sniffing header X-Content-Type-Options was not set to &#39;nosniff&#39;. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At &#34;High&#34; threshold this scan rule will not alert on client or server error responses.

### Locations
#### **Physical Location**
- http://localhost:5000/bootstrap/static/umd/popper.min.js


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10021
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    X-Content-Type-Options Header Missing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Anti-MIME-Sniffing header X-Content-Type-Options was not set to &#39;nosniff&#39;. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At &#34;High&#34; threshold this scan rule will not alert on client or server error responses.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10021
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    X-Content-Type-Options Header Missing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Anti-MIME-Sniffing header X-Content-Type-Options was not set to &#39;nosniff&#39;. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At &#34;High&#34; threshold this scan rule will not alert on client or server error responses.

### Locations
#### **Physical Location**
- http://localhost:5000/robots.txt


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10021
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    X-Content-Type-Options Header Missing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Anti-MIME-Sniffing header X-Content-Type-Options was not set to &#39;nosniff&#39;. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At &#34;High&#34; threshold this scan rule will not alert on client or server error responses.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10021
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    X-Content-Type-Options Header Missing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Anti-MIME-Sniffing header X-Content-Type-Options was not set to &#39;nosniff&#39;. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At &#34;High&#34; threshold this scan rule will not alert on client or server error responses.

### Locations
#### **Physical Location**
- http://localhost:5000/sitemap.xml


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10021
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    X-Content-Type-Options Header Missing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Anti-MIME-Sniffing header X-Content-Type-Options was not set to &#39;nosniff&#39;. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At &#34;High&#34; threshold this scan rule will not alert on client or server error responses.

### Locations
#### **Physical Location**
- http://localhost:5000/static/favicon.ico


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10021
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    X-Content-Type-Options Header Missing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Anti-MIME-Sniffing header X-Content-Type-Options was not set to &#39;nosniff&#39;. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At &#34;High&#34; threshold this scan rule will not alert on client or server error responses.

### Locations
#### **Physical Location**
- http://localhost:5000/static/icon.png


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10021
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    X-Content-Type-Options Header Missing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Anti-MIME-Sniffing header X-Content-Type-Options was not set to &#39;nosniff&#39;. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

### Locations
#### **Physical Location**
- http://localhost:5000


- Line 1

```
nginx/1.14.2
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10036
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Server Leaks Version Information via &#34;Server&#34; HTTP Response Header Field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1

```
nginx/1.14.2
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10036
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Server Leaks Version Information via &#34;Server&#34; HTTP Response Header Field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

### Locations
#### **Physical Location**
- http://localhost:5000/bootstrap/static/css/bootstrap.min.css


- Line 1

```
nginx/1.14.2
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10036
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Server Leaks Version Information via &#34;Server&#34; HTTP Response Header Field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

### Locations
#### **Physical Location**
- http://localhost:5000/bootstrap/static/js/bootstrap.min.js


- Line 1

```
nginx/1.14.2
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10036
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Server Leaks Version Information via &#34;Server&#34; HTTP Response Header Field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

### Locations
#### **Physical Location**
- http://localhost:5000/bootstrap/static/umd/popper.min.js


- Line 1

```
nginx/1.14.2
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10036
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Server Leaks Version Information via &#34;Server&#34; HTTP Response Header Field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

### Locations
#### **Physical Location**
- http://localhost:5000/home


- Line 1

```
nginx/1.14.2
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10036
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Server Leaks Version Information via &#34;Server&#34; HTTP Response Header Field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1

```
nginx/1.14.2
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10036
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Server Leaks Version Information via &#34;Server&#34; HTTP Response Header Field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

### Locations
#### **Physical Location**
- http://localhost:5000/robots.txt


- Line 1

```
nginx/1.14.2
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10036
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Server Leaks Version Information via &#34;Server&#34; HTTP Response Header Field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1

```
nginx/1.14.2
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10036
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Server Leaks Version Information via &#34;Server&#34; HTTP Response Header Field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

### Locations
#### **Physical Location**
- http://localhost:5000/sitemap.xml


- Line 1

```
nginx/1.14.2
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10036
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Server Leaks Version Information via &#34;Server&#34; HTTP Response Header Field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

### Locations
#### **Physical Location**
- http://localhost:5000/static/favicon.ico


- Line 1

```
nginx/1.14.2
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10036
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Server Leaks Version Information via &#34;Server&#34; HTTP Response Header Field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

### Locations
#### **Physical Location**
- http://localhost:5000/static/icon.png


- Line 1

```
nginx/1.14.2
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10036
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Server Leaks Version Information via &#34;Server&#34; HTTP Response Header Field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1

```
nginx/1.14.2
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10036
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Server Leaks Version Information via &#34;Server&#34; HTTP Response Header Field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1

```
nginx/1.14.2
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10036
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Server Leaks Version Information via &#34;Server&#34; HTTP Response Header Field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The web/application server is leaking version information via the &#34;Server&#34; HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    high
    </details>






---

A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a &#39;cross-site&#39; request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.

### Locations
#### **Physical Location**
- http://localhost:5000


- Line 1

```
Set-Cookie: preferences
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10054
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Cookie without SameSite Attribute
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a &#39;cross-site&#39; request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a &#39;cross-site&#39; request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1

```
Set-Cookie: preferences
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10054
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Cookie without SameSite Attribute
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a &#39;cross-site&#39; request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a &#39;cross-site&#39; request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.

### Locations
#### **Physical Location**
- http://localhost:5000/


- Line 1

```
Set-Cookie: session
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10054
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Cookie without SameSite Attribute
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a &#39;cross-site&#39; request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a &#39;cross-site&#39; request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1

```
Set-Cookie: session
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10054
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Cookie without SameSite Attribute
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a &#39;cross-site&#39; request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a &#39;cross-site&#39; request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.

### Locations
#### **Physical Location**
- http://localhost:5000/login


- Line 1

```
Set-Cookie: session
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10054
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Cookie without SameSite Attribute
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a &#39;cross-site&#39; request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a &#39;cross-site&#39; request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.

### Locations
#### **Physical Location**
- http://localhost:5000/signup


- Line 1

```
Set-Cookie: session
```






### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    10054
  </details>



+ <details>
    <summary>Short Description</summary>
    <br>
    Cookie without SameSite Attribute
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a &#39;cross-site&#39; request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.
    </details>




+ <details>
    <summary>Confidence</summary>
    <br>
    medium
    </details>






---

