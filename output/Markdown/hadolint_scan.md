# Vulnerability Report

This report was automaticly generated based on the vulnerabilities specification of a [SARIF](https://sarifweb.azurewebsites.net) file.

## Tool information

> Name: Hadolint

> Full name: Haskell Dockerfile Linter


> Information Uri: [https://github.com/hadolint/hadolint](https://github.com/hadolint/hadolint)

> Version: 2.12.0



---

## Vulnerabilities

Pin versions in pip. Instead of `pip install &lt;package&gt;` use `pip install &lt;package&gt;==&lt;version&gt;` or `pip install --requirement &lt;requirements file&gt;`

### Locations
#### **Physical Location**
- /input/Security-Pipeline-Testing/Dockerfile


- Line 9







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    DL3013
  </details>








---

Avoid use of cache directory with pip. Use `pip install --no-cache-dir &lt;package&gt;`

### Locations
#### **Physical Location**
- /input/Security-Pipeline-Testing/Dockerfile


- Line 9







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    DL3042
  </details>








---

