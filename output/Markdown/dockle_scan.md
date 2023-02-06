# Vulnerability Report

This report was automaticly generated based on the vulnerabilities specification of a [SARIF](https://sarifweb.azurewebsites.net) file.

## Tool information

> Name: Dockle


> Information Uri: [https://github.com/goodwithtech/dockle](https://github.com/goodwithtech/dockle)





---

## Vulnerabilities

---

Suspicious filename found : usr/local/lib/python2.7/dist-packages/easy_thumbnails/tests/settings.py (You can suppress it with &#34;-af settings.py&#34;), Suspicious filename found : usr/local/lib/python2.7/dist-packages/userena/runtests/settings.py (You can suppress it with &#34;-af settings.py&#34;), Suspicious filename found : usr/local/lib/python2.7/dist-packages/userena/settings.py (You can suppress it with &#34;-af settings.py&#34;), Suspicious filename found : usr/local/lib/python2.7/dist-packages/rest_framework_nested/runtests/settings.py (You can suppress it with &#34;-af settings.py&#34;), Suspicious filename found : usr/local/lib/python2.7/dist-packages/django_js_reverse/tests/settings.py (You can suppress it with &#34;-af settings.py&#34;), Suspicious filename found : usr/local/lib/python2.7/dist-packages/constance/settings.py (You can suppress it with &#34;-af settings.py&#34;), Suspicious filename found : usr/local/lib/python2.7/dist-packages/cssutils/settings.py (You can suppress it with &#34;-af settings.py&#34;), Suspicious filename found : usr/local/lib/python2.7/dist-packages/grappelli/settings.py (You can suppress it with &#34;-af settings.py&#34;), Suspicious filename found : usr/local/lib/python2.7/dist-packages/django_premailer/tests/settings.py (You can suppress it with &#34;-af settings.py&#34;), Suspicious filename found : usr/local/lib/python2.7/dist-packages/django_countries/tests/settings.py (You can suppress it with &#34;-af settings.py&#34;), Suspicious filename found : usr/local/lib/python2.7/dist-packages/pymongo/settings.py (You can suppress it with &#34;-af settings.py&#34;), Suspicious filename found : usr/local/lib/python2.7/dist-packages/newsletter/settings.py (You can suppress it with &#34;-af settings.py&#34;), Suspicious filename found : usr/local/lib/python2.7/dist-packages/rest_framework/settings.py (You can suppress it with &#34;-af settings.py&#34;), Suspicious filename found : usr/local/lib/python2.7/dist-packages/django_extensions/settings.py (You can suppress it with &#34;-af settings.py&#34;), Suspicious filename found : usr/local/lib/python2.7/dist-packages/guardian/conf/settings.py (You can suppress it with &#34;-af settings.py&#34;)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/easy_thumbnails/tests/settings.py




#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/userena/runtests/settings.py




#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/userena/settings.py




#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/rest_framework_nested/runtests/settings.py




#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/django_js_reverse/tests/settings.py




#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/constance/settings.py




#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/cssutils/settings.py




#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/grappelli/settings.py




#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/django_premailer/tests/settings.py




#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/django_countries/tests/settings.py




#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/pymongo/settings.py




#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/newsletter/settings.py




#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/rest_framework/settings.py




#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/django_extensions/settings.py




#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/guardian/conf/settings.py







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CIS-DI-0010
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://github.com/goodwithtech/dockle/blob/master/CHECKPOINT.md#CIS-DI-0010">https://github.com/goodwithtech/dockle/blob/master/CHECKPOINT.md#CIS-DI-0010</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Do not store credential in environment variables/files
    </details>






---

Use &#39;rm -rf /var/lib/apt/lists&#39; after &#39;apt-get install|update&#39; : RUN /bin/sh -c curl -sL https://deb.nodesource.com/setup_12.x | bash -     &amp;&amp; apt-get install -y nodejs # buildkit, Use &#39;rm -rf /var/lib/apt/lists&#39; after &#39;apt-get install|update&#39; : RUN /bin/sh -c apt update  &amp;&amp; apt -y -q install build-essential libssl-dev libffi-dev python3-dev cargo                           libjpeg-dev libpq-dev postgresql-client curl git python-pip                           vim libcurl4-openssl-dev uwsgi uwsgi-plugin-python                           python-dev libxml2-dev libxslt1-dev libyaml-dev # buildkit

### Locations
#### **Physical Location**
- metadata




#### **Physical Location**
- metadata







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    DKL-DI-0005
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://github.com/goodwithtech/dockle/blob/master/CHECKPOINT.md#DKL-DI-0005">https://github.com/goodwithtech/dockle/blob/master/CHECKPOINT.md#DKL-DI-0005</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Clear apt-get caches
    </details>






---

Last user should not be root

### Locations
#### **Physical Location**
- metadata







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CIS-DI-0001
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://github.com/goodwithtech/dockle/blob/master/CHECKPOINT.md#CIS-DI-0001">https://github.com/goodwithtech/dockle/blob/master/CHECKPOINT.md#CIS-DI-0001</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Create a user for the container
    </details>






---

export DOCKER_CONTENT_TRUST=1 before docker pull/build

### Locations
#### **Physical Location**
- ENVIRONMENT variable on HOST OS







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CIS-DI-0005
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://github.com/goodwithtech/dockle/blob/master/CHECKPOINT.md#CIS-DI-0005">https://github.com/goodwithtech/dockle/blob/master/CHECKPOINT.md#CIS-DI-0005</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Enable Content trust for Docker
    </details>






---

not found HEALTHCHECK statement

### Locations
#### **Physical Location**
- metadata







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CIS-DI-0006
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://github.com/goodwithtech/dockle/blob/master/CHECKPOINT.md#CIS-DI-0006">https://github.com/goodwithtech/dockle/blob/master/CHECKPOINT.md#CIS-DI-0006</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Add HEALTHCHECK instruction to the container image
    </details>






---

