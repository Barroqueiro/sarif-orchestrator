


# Report for semgrep


+ <details>
  <summary>Driver</summary>

  + <details>
    <summary>Name</summary>

    - semgrep   
    </details>
  + <details>
    <summary>Other_value</summary>

    + <details>
      <summary>Other_value_2</summary>

      - :D   
      </details>   
    </details>
  + <details>
    <summary>Rules</summary>
   
    </details>
  + <details>
    <summary>Semanticversion</summary>

    - 1.5.0   
    </details>   
  </details>








## Tool information


## Detected the use of eval(). eval() can be dangerous if used to evaluate dynamic content. If this content can be input from outside the program, this may be a code injection vulnerability. Ensure evaluated content is not definable by external sources.

## Detected the use of eval(). eval() can be dangerous if used to evaluate dynamic content. If this content can be input from outside the program, this may be a code injection vulnerability. Ensure evaluated content is not definable by external sources.

## Detected the use of eval(). eval() can be dangerous if used to evaluate dynamic content. If this content can be input from outside the program, this may be a code injection vulnerability. Ensure evaluated content is not definable by external sources.

## User controlled data in methods like `innerHTML`, `outerHTML` or `document.write` is an anti-pattern that can lead to XSS vulnerabilities

## User controlled data in methods like `innerHTML`, `outerHTML` or `document.write` is an anti-pattern that can lead to XSS vulnerabilities

## Detected a template variable used in an anchor tag with the &#39;href&#39; attribute. This allows a malicious actor to input the &#39;javascript:&#39; URI and is subject to cross- site scripting (XSS) attacks. If using a relative URL, start with a literal forward slash and concatenate the URL, like this: href=&#39;/{{link}}&#39;. You may also consider setting the Content Security Policy (CSP) header.

## Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure this is safe, check that the HTML is rendered safely. Otherwise, use templates (`django.shortcuts.render`) which will safely render HTML instead.

## Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using the Django object-relational mappers (ORM) instead of raw SQL queries.

## Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using an object-relational mapper (ORM) such as SQLAlchemy which will protect your queries.

## It looks like MD5 is used as a password hash. MD5 is not considered a secure password hash because it can be cracked by an attacker in a short amount of time. Use a suitable password hashing function such as scrypt. You can use `hashlib.scrypt`.

## Possibility of prototype polluting function detected. By adding or modifying attributes of an object prototype, it is possible to create attributes that exist on every object, or replace critical attributes with malicious ones. This can be problematic if the software depends on existence or non-existence of certain attributes, or uses pre-defined attributes of object prototype (such as hasOwnProperty, toString or valueOf). Possible mitigations might be: freezing the object prototype, using an object without prototypes (via Object.create(null) ), blocking modifications of attributes that resolve to object prototype, using Map instead of object.

## Possibility of prototype polluting function detected. By adding or modifying attributes of an object prototype, it is possible to create attributes that exist on every object, or replace critical attributes with malicious ones. This can be problematic if the software depends on existence or non-existence of certain attributes, or uses pre-defined attributes of object prototype (such as hasOwnProperty, toString or valueOf). Possible mitigations might be: freezing the object prototype, using an object without prototypes (via Object.create(null) ), blocking modifications of attributes that resolve to object prototype, using Map instead of object.

## By not specifying a USER, a program in the container may run as &#39;root&#39;. This is a security hazard. If an attacker can control a process running as root, they may have control over the container. Ensure that the last USER in a Dockerfile is a USER other than &#39;root&#39;.

## By not specifying a USER, a program in the container may run as &#39;root&#39;. This is a security hazard. If an attacker can control a process running as root, they may have control over the container. Ensure that the last USER in a Dockerfile is a USER other than &#39;root&#39;.

## RegExp() called with a `c` function argument, this might  allow an attacker to cause a Denial of Service (DoS)  within your application as RegExP which blocks the main thread.

## RegExp() called with a `c` function argument, this might  allow an attacker to cause a Denial of Service (DoS)  within your application as RegExP which blocks the main thread.

## RegExp() called with a `c` function argument, this might  allow an attacker to cause a Denial of Service (DoS)  within your application as RegExP which blocks the main thread.

## Detected a template variable used in an anchor tag with the &#39;href&#39; attribute. This allows a malicious actor to input the &#39;javascript:&#39; URI and is subject to cross- site scripting (XSS) attacks. Use the &#39;url&#39; template tag to safely generate a URL. You may also consider setting the Content Security Policy (CSP) header.

## Detected a template variable used in an anchor tag with the &#39;href&#39; attribute. This allows a malicious actor to input the &#39;javascript:&#39; URI and is subject to cross- site scripting (XSS) attacks. Use &#39;url_for()&#39; to safely generate a URL. You may also consider setting the Content Security Policy (CSP) header.

## Detected possible formatted SQL query. Use parameterized queries instead.

## Hardcoded JWT secret or private key is used. This is a Insufficiently Protected Credentials weakness: https://cwe.mitre.org/data/definitions/522.html Consider using an appropriate security mechanism to protect the credentials (e.g. keeping secrets in environment variables)

## Detected JWT token decoded with &#39;verify=False&#39;. This bypasses any integrity checks for the token which means the token could be tampered with by malicious actors. Ensure that the JWT token is verified.

## Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead.

## Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead.

## Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead.

## Detected the use of an insecure deserialization library in a Flask route. These libraries are prone to code execution vulnerabilities. Ensure user data does not enter this function. To fix this, try to avoid serializing whole objects. Consider instead using a serializer such as JSON.

## Avoiding SQL string concatenation: untrusted input concatenated with raw SQL query can result in SQL Injection. In order to execute raw query safely, prepared statement should be used. SQLAlchemy provides TextualSQL to easily used prepared statement with named parameters. For complex SQL composition, use SQL Expression Language or Schema Definition Language. In most cases, SQLAlchemy ORM will be a better option.

## Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure this is safe, check that the HTML is rendered safely. Otherwise, use templates (`flask.render_template`) which will safely render HTML instead.

## Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.

## Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.

## Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.

## Found a template created with string formatting. This is susceptible to server-side template injection and cross-site scripting attacks.

