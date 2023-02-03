# Vulnerability Report

This report was automaticly generated based on the vulnerabilities specification of a [SARIF](https://sarifweb.azurewebsites.net) file.

## Tool information

> Name: Trivy

> Full name: Trivy Vulnerability Scanner

> Information Uri: [https://github.com/aquasecurity/trivy](https://github.com/aquasecurity/trivy)


> Version: 0.34.0



---

## Vulnerabilities

---

Package: libksba8
Installed Version: 1.3.5-2
Vulnerability CVE-2022-3515
Severity: HIGH
Fixed Version: 1.3.5-2ubuntu0.18.04.1
Link: [CVE-2022-3515](https://avd.aquasec.com/nvd/cve-2022-3515)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3515
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3515">https://avd.aquasec.com/nvd/cve-2022-3515</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libksba: integer overflow may lead to remote code execution
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in the Libksba library due to an integer overflow within the CRL parser. The vulnerability can be exploited remotely for code execution on the target system by passing specially crafted data to the application, for example, a malicious S/MIME attachment.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    8.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3515
	Severity: HIGH
	Package: libksba8
	Fixed Version: 1.3.5-2ubuntu0.18.04.1
	Link: [CVE-2022-3515](https://avd.aquasec.com/nvd/cve-2022-3515)
	A vulnerability was found in the Libksba library due to an integer overflow within the CRL parser. The vulnerability can be exploited remotely for code execution on the target system by passing specially crafted data to the application, for example, a malicious S/MIME attachment.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-42703
Severity: HIGH
Fixed Version: 4.15.0-200.211
Link: [CVE-2022-42703](https://avd.aquasec.com/nvd/cve-2022-42703)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42703
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42703">https://avd.aquasec.com/nvd/cve-2022-42703</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: use-after-free related to leaf anon_vma double reuse
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    mm/rmap.c in the Linux kernel before 5.19.7 has a use-after-free related to leaf anon_vma double reuse.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    8.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42703
	Severity: HIGH
	Package: linux-libc-dev
	Fixed Version: 4.15.0-200.211
	Link: [CVE-2022-42703](https://avd.aquasec.com/nvd/cve-2022-42703)
	mm/rmap.c in the Linux kernel before 5.19.7 has a use-after-free related to leaf anon_vma double reuse.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-43945
Severity: HIGH
Fixed Version: 
Link: [CVE-2022-43945](https://avd.aquasec.com/nvd/cve-2022-43945)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-43945
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-43945">https://avd.aquasec.com/nvd/cve-2022-43945</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: nfsd buffer overflow by RPC message over TCP with garbage data
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Linux kernel NFSD implementation prior to versions 5.19.17 and 6.0.2 are vulnerable to buffer overflow. NFSD tracks the number of pages held by each NFSD thread by combining the receive and send buffers of a remote procedure call (RPC) into a single array of pages. A client can force the send buffer to shrink by sending an RPC message over TCP with garbage data added at the end of the message. The RPC message with garbage data is still correctly formed according to the specification and is passed forward to handlers. Vulnerable code in NFSD is not expecting the oversized request and writes beyond the allocated buffer space. CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    8.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-43945
	Severity: HIGH
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-43945](https://avd.aquasec.com/nvd/cve-2022-43945)
	The Linux kernel NFSD implementation prior to versions 5.19.17 and 6.0.2 are vulnerable to buffer overflow. NFSD tracks the number of pages held by each NFSD thread by combining the receive and send buffers of a remote procedure call (RPC) into a single array of pages. A client can force the send buffer to shrink by sending an RPC message over TCP with garbage data added at the end of the message. The RPC message with garbage data is still correctly formed according to the specification and is passed forward to handlers. Vulnerable code in NFSD is not expecting the oversized request and writes beyond the allocated buffer space. CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-25287
Severity: CRITICAL
Fixed Version: 8.2.0
Link: [CVE-2021-25287](https://avd.aquasec.com/nvd/cve-2021-25287)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-25287
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-25287">https://avd.aquasec.com/nvd/cve-2021-25287</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Out-of-bounds read in J2K image reader
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Pillow before 8.2.0. There is an out-of-bounds read in J2kDecode, in j2ku_graya_la.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    9.1
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-25287
	Severity: CRITICAL
	Package: Pillow
	Fixed Version: 8.2.0
	Link: [CVE-2021-25287](https://avd.aquasec.com/nvd/cve-2021-25287)
	An issue was discovered in Pillow before 8.2.0. There is an out-of-bounds read in J2kDecode, in j2ku_graya_la.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-25288
Severity: CRITICAL
Fixed Version: 8.2.0
Link: [CVE-2021-25288](https://avd.aquasec.com/nvd/cve-2021-25288)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-25288
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-25288">https://avd.aquasec.com/nvd/cve-2021-25288</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Out-of-bounds read in J2K image reader
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Pillow before 8.2.0. There is an out-of-bounds read in J2kDecode, in j2ku_gray_i.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    9.1
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-25288
	Severity: CRITICAL
	Package: Pillow
	Fixed Version: 8.2.0
	Link: [CVE-2021-25288](https://avd.aquasec.com/nvd/cve-2021-25288)
	An issue was discovered in Pillow before 8.2.0. There is an out-of-bounds read in J2kDecode, in j2ku_gray_i.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-25289
Severity: CRITICAL
Fixed Version: 8.1.1
Link: [CVE-2021-25289](https://avd.aquasec.com/nvd/cve-2021-25289)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-25289
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-25289">https://avd.aquasec.com/nvd/cve-2021-25289</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: insufficent fix for CVE-2020-35654 due to incorrect error checking in TiffDecode.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Pillow before 8.1.1. TiffDecode has a heap-based buffer overflow when decoding crafted YCbCr files because of certain interpretation conflicts with LibTIFF in RGBA mode. NOTE: this issue exists because of an incomplete fix for CVE-2020-35654.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    9.8
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-25289
	Severity: CRITICAL
	Package: Pillow
	Fixed Version: 8.1.1
	Link: [CVE-2021-25289](https://avd.aquasec.com/nvd/cve-2021-25289)
	An issue was discovered in Pillow before 8.1.1. TiffDecode has a heap-based buffer overflow when decoding crafted YCbCr files because of certain interpretation conflicts with LibTIFF in RGBA mode. NOTE: this issue exists because of an incomplete fix for CVE-2020-35654.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-34552
Severity: CRITICAL
Fixed Version: 8.3.0
Link: [CVE-2021-34552](https://avd.aquasec.com/nvd/cve-2021-34552)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-34552
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-34552">https://avd.aquasec.com/nvd/cve-2021-34552</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Buffer overflow in image convert function
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Pillow through 8.2.0 and PIL (aka Python Imaging Library) through 1.1.7 allow an attacker to pass controlled parameters directly into a convert function to trigger a buffer overflow in Convert.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    9.8
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-34552
	Severity: CRITICAL
	Package: Pillow
	Fixed Version: 8.3.0
	Link: [CVE-2021-34552](https://avd.aquasec.com/nvd/cve-2021-34552)
	Pillow through 8.2.0 and PIL (aka Python Imaging Library) through 1.1.7 allow an attacker to pass controlled parameters directly into a convert function to trigger a buffer overflow in Convert.c.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2022-22817
Severity: CRITICAL
Fixed Version: 9.0.0
Link: [CVE-2022-22817](https://avd.aquasec.com/nvd/cve-2022-22817)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-22817
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-22817">https://avd.aquasec.com/nvd/cve-2022-22817</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: PIL.ImageMath.eval allows evaluation of arbitrary expressions
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    PIL.ImageMath.eval in Pillow before 9.0.0 allows evaluation of arbitrary expressions, such as ones that use the Python exec method. A lambda expression could also be used,
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    9.8
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-22817
	Severity: CRITICAL
	Package: Pillow
	Fixed Version: 9.0.0
	Link: [CVE-2022-22817](https://avd.aquasec.com/nvd/cve-2022-22817)
	PIL.ImageMath.eval in Pillow before 9.0.0 allows evaluation of arbitrary expressions, such as ones that use the Python exec method. A lambda expression could also be used,
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2022-24303
Severity: CRITICAL
Fixed Version: 9.0.1
Link: [CVE-2022-24303](https://avd.aquasec.com/nvd/cve-2022-24303)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-24303
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-24303">https://avd.aquasec.com/nvd/cve-2022-24303</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: temporary directory with a space character allows removal of unrelated file after im.show() and related actions
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Pillow before 9.0.1 allows attackers to delete files because spaces in temporary pathnames are mishandled.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    9.1
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-24303
	Severity: CRITICAL
	Package: Pillow
	Fixed Version: 9.0.1
	Link: [CVE-2022-24303](https://avd.aquasec.com/nvd/cve-2022-24303)
	Pillow before 9.0.1 allows attackers to delete files because spaces in temporary pathnames are mishandled.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2020-10379
Severity: HIGH
Fixed Version: 7.1.0
Link: [CVE-2020-10379](https://avd.aquasec.com/nvd/cve-2020-10379)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-10379
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-10379">https://avd.aquasec.com/nvd/cve-2020-10379</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: two buffer overflows in libImaging/TiffDecode.c due to small buffers allocated in ImagingLibTiffDecode()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In Pillow before 7.1.0, there are two Buffer Overflows in libImaging/TiffDecode.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.8
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-10379
	Severity: HIGH
	Package: Pillow
	Fixed Version: 7.1.0
	Link: [CVE-2020-10379](https://avd.aquasec.com/nvd/cve-2020-10379)
	In Pillow before 7.1.0, there are two Buffer Overflows in libImaging/TiffDecode.c.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2020-11538
Severity: HIGH
Fixed Version: 7.1.0
Link: [CVE-2020-11538](https://avd.aquasec.com/nvd/cve-2020-11538)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-11538
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-11538">https://avd.aquasec.com/nvd/cve-2020-11538</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: out-of-bounds reads/writes in the parsing of SGI image files in expandrow/expandrow2
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In libImaging/SgiRleDecode.c in Pillow through 7.0.0, a number of out-of-bounds reads exist in the parsing of SGI image files, a different issue than CVE-2020-5311.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    8.1
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-11538
	Severity: HIGH
	Package: Pillow
	Fixed Version: 7.1.0
	Link: [CVE-2020-11538](https://avd.aquasec.com/nvd/cve-2020-11538)
	In libImaging/SgiRleDecode.c in Pillow through 7.0.0, a number of out-of-bounds reads exist in the parsing of SGI image files, a different issue than CVE-2020-5311.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2020-35653
Severity: HIGH
Fixed Version: 8.1.0
Link: [CVE-2020-35653](https://avd.aquasec.com/nvd/cve-2020-35653)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-35653
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-35653">https://avd.aquasec.com/nvd/cve-2020-35653</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Buffer over-read in PCX image reader
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In Pillow before 8.1.0, PcxDecode has a buffer over-read when decoding a crafted PCX file because the user-supplied stride value is trusted for buffer calculations.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.1
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-35653
	Severity: HIGH
	Package: Pillow
	Fixed Version: 8.1.0
	Link: [CVE-2020-35653](https://avd.aquasec.com/nvd/cve-2020-35653)
	In Pillow before 8.1.0, PcxDecode has a buffer over-read when decoding a crafted PCX file because the user-supplied stride value is trusted for buffer calculations.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2020-35654
Severity: HIGH
Fixed Version: 8.1.0
Link: [CVE-2020-35654](https://avd.aquasec.com/nvd/cve-2020-35654)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-35654
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-35654">https://avd.aquasec.com/nvd/cve-2020-35654</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: decoding crafted YCbCr files could result in heap-based buffer overflow
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In Pillow before 8.1.0, TiffDecode has a heap-based buffer overflow when decoding crafted YCbCr files because of certain interpretation conflicts with LibTIFF in RGBA mode.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    8.8
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-35654
	Severity: HIGH
	Package: Pillow
	Fixed Version: 8.1.0
	Link: [CVE-2020-35654](https://avd.aquasec.com/nvd/cve-2020-35654)
	In Pillow before 8.1.0, TiffDecode has a heap-based buffer overflow when decoding crafted YCbCr files because of certain interpretation conflicts with LibTIFF in RGBA mode.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-23437
Severity: HIGH
Fixed Version: 8.3.2
Link: [CVE-2021-23437](https://avd.aquasec.com/nvd/cve-2021-23437)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-23437
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-23437">https://avd.aquasec.com/nvd/cve-2021-23437</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: possible ReDoS via the getrgb function
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The package pillow 5.2.0 and before 8.3.2 are vulnerable to Regular Expression Denial of Service (ReDoS) via the getrgb function.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-23437
	Severity: HIGH
	Package: Pillow
	Fixed Version: 8.3.2
	Link: [CVE-2021-23437](https://avd.aquasec.com/nvd/cve-2021-23437)
	The package pillow 5.2.0 and before 8.3.2 are vulnerable to Regular Expression Denial of Service (ReDoS) via the getrgb function.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-25290
Severity: HIGH
Fixed Version: 8.1.1
Link: [CVE-2021-25290](https://avd.aquasec.com/nvd/cve-2021-25290)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-25290
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-25290">https://avd.aquasec.com/nvd/cve-2021-25290</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Negative-offset memcpy in TIFF image reader
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Pillow before 8.1.1. In TiffDecode.c, there is a negative-offset memcpy with an invalid size.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-25290
	Severity: HIGH
	Package: Pillow
	Fixed Version: 8.1.1
	Link: [CVE-2021-25290](https://avd.aquasec.com/nvd/cve-2021-25290)
	An issue was discovered in Pillow before 8.1.1. In TiffDecode.c, there is a negative-offset memcpy with an invalid size.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-25291
Severity: HIGH
Fixed Version: 8.1.1
Link: [CVE-2021-25291](https://avd.aquasec.com/nvd/cve-2021-25291)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-25291
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-25291">https://avd.aquasec.com/nvd/cve-2021-25291</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: out-of-bounds read in TiffReadRGBATile in TiffDecode.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Pillow before 8.1.1. In TiffDecode.c, there is an out-of-bounds read in TiffreadRGBATile via invalid tile boundaries.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-25291
	Severity: HIGH
	Package: Pillow
	Fixed Version: 8.1.1
	Link: [CVE-2021-25291](https://avd.aquasec.com/nvd/cve-2021-25291)
	An issue was discovered in Pillow before 8.1.1. In TiffDecode.c, there is an out-of-bounds read in TiffreadRGBATile via invalid tile boundaries.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-25293
Severity: HIGH
Fixed Version: 8.1.1
Link: [CVE-2021-25293](https://avd.aquasec.com/nvd/cve-2021-25293)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-25293
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-25293">https://avd.aquasec.com/nvd/cve-2021-25293</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Out-of-bounds read in SGI RLE image reader
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Pillow before 8.1.1. There is an out-of-bounds read in SGIRleDecode.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-25293
	Severity: HIGH
	Package: Pillow
	Fixed Version: 8.1.1
	Link: [CVE-2021-25293](https://avd.aquasec.com/nvd/cve-2021-25293)
	An issue was discovered in Pillow before 8.1.1. There is an out-of-bounds read in SGIRleDecode.c.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-27921
Severity: HIGH
Fixed Version: 8.1.1
Link: [CVE-2021-27921](https://avd.aquasec.com/nvd/cve-2021-27921)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-27921
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-27921">https://avd.aquasec.com/nvd/cve-2021-27921</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Excessive memory allocation in BLP image reader
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Pillow before 8.1.1 allows attackers to cause a denial of service (memory consumption) because the reported size of a contained image is not properly checked for a BLP container, and thus an attempted memory allocation can be very large.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-27921
	Severity: HIGH
	Package: Pillow
	Fixed Version: 8.1.1
	Link: [CVE-2021-27921](https://avd.aquasec.com/nvd/cve-2021-27921)
	Pillow before 8.1.1 allows attackers to cause a denial of service (memory consumption) because the reported size of a contained image is not properly checked for a BLP container, and thus an attempted memory allocation can be very large.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-27922
Severity: HIGH
Fixed Version: 8.1.1
Link: [CVE-2021-27922](https://avd.aquasec.com/nvd/cve-2021-27922)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-27922
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-27922">https://avd.aquasec.com/nvd/cve-2021-27922</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Excessive memory allocation in ICNS image reader
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Pillow before 8.1.1 allows attackers to cause a denial of service (memory consumption) because the reported size of a contained image is not properly checked for an ICNS container, and thus an attempted memory allocation can be very large.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-27922
	Severity: HIGH
	Package: Pillow
	Fixed Version: 8.1.1
	Link: [CVE-2021-27922](https://avd.aquasec.com/nvd/cve-2021-27922)
	Pillow before 8.1.1 allows attackers to cause a denial of service (memory consumption) because the reported size of a contained image is not properly checked for an ICNS container, and thus an attempted memory allocation can be very large.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-27923
Severity: HIGH
Fixed Version: 8.1.1
Link: [CVE-2021-27923](https://avd.aquasec.com/nvd/cve-2021-27923)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-27923
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-27923">https://avd.aquasec.com/nvd/cve-2021-27923</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Excessive memory allocation in ICO image reader
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Pillow before 8.1.1 allows attackers to cause a denial of service (memory consumption) because the reported size of a contained image is not properly checked for an ICO container, and thus an attempted memory allocation can be very large.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-27923
	Severity: HIGH
	Package: Pillow
	Fixed Version: 8.1.1
	Link: [CVE-2021-27923](https://avd.aquasec.com/nvd/cve-2021-27923)
	Pillow before 8.1.1 allows attackers to cause a denial of service (memory consumption) because the reported size of a contained image is not properly checked for an ICO container, and thus an attempted memory allocation can be very large.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-28676
Severity: HIGH
Fixed Version: 8.2.0
Link: [CVE-2021-28676](https://avd.aquasec.com/nvd/cve-2021-28676)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-28676
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-28676">https://avd.aquasec.com/nvd/cve-2021-28676</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Infinite loop in FLI image reader
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Pillow before 8.2.0. For FLI data, FliDecode did not properly check that the block advance was non-zero, potentially leading to an infinite loop on load.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-28676
	Severity: HIGH
	Package: Pillow
	Fixed Version: 8.2.0
	Link: [CVE-2021-28676](https://avd.aquasec.com/nvd/cve-2021-28676)
	An issue was discovered in Pillow before 8.2.0. For FLI data, FliDecode did not properly check that the block advance was non-zero, potentially leading to an infinite loop on load.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-28677
Severity: HIGH
Fixed Version: 8.2.0
Link: [CVE-2021-28677](https://avd.aquasec.com/nvd/cve-2021-28677)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-28677
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-28677">https://avd.aquasec.com/nvd/cve-2021-28677</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Excessive CPU use in EPS image reader
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Pillow before 8.2.0. For EPS data, the readline implementation used in EPSImageFile has to deal with any combination of \r and \n as line endings. It used an accidentally quadratic method of accumulating lines while looking for a line ending. A malicious EPS file could use this to perform a DoS of Pillow in the open phase, before an image was accepted for opening.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-28677
	Severity: HIGH
	Package: Pillow
	Fixed Version: 8.2.0
	Link: [CVE-2021-28677](https://avd.aquasec.com/nvd/cve-2021-28677)
	An issue was discovered in Pillow before 8.2.0. For EPS data, the readline implementation used in EPSImageFile has to deal with any combination of \r and \n as line endings. It used an accidentally quadratic method of accumulating lines while looking for a line ending. A malicious EPS file could use this to perform a DoS of Pillow in the open phase, before an image was accepted for opening.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2022-45198
Severity: HIGH
Fixed Version: 9.2.0
Link: [CVE-2022-45198](https://avd.aquasec.com/nvd/cve-2022-45198)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-45198
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-45198">https://avd.aquasec.com/nvd/cve-2022-45198</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Pillow before 9.2.0 performs Improper Handling of Highly Compressed GI ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Pillow before 9.2.0 performs Improper Handling of Highly Compressed GIF Data (Data Amplification).
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-45198
	Severity: HIGH
	Package: Pillow
	Fixed Version: 9.2.0
	Link: [CVE-2022-45198](https://avd.aquasec.com/nvd/cve-2022-45198)
	Pillow before 9.2.0 performs Improper Handling of Highly Compressed GIF Data (Data Amplification).
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2022-45199
Severity: HIGH
Fixed Version: 9.3.0
Link: [CVE-2022-45199](https://avd.aquasec.com/nvd/cve-2022-45199)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-45199
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-45199">https://avd.aquasec.com/nvd/cve-2022-45199</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Pillow before 9.3.0 allows denial of service via SAMPLESPERPIXEL. ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Pillow before 9.3.0 allows denial of service via SAMPLESPERPIXEL.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-45199
	Severity: HIGH
	Package: Pillow
	Fixed Version: 9.3.0
	Link: [CVE-2022-45199](https://avd.aquasec.com/nvd/cve-2022-45199)
	Pillow before 9.3.0 allows denial of service via SAMPLESPERPIXEL.
    </details>



---

Package: celery
Installed Version: 3.1.26.post2
Vulnerability CVE-2021-23727
Severity: HIGH
Fixed Version: 5.2.2
Link: [CVE-2021-23727](https://avd.aquasec.com/nvd/cve-2021-23727)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/celery-3.1.26.post2.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-23727
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-23727">https://avd.aquasec.com/nvd/cve-2021-23727</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    celery: stored command injection vulnerability may allow privileges escalation
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    This affects the package celery before 5.2.2. It by default trusts the messages and metadata stored in backends (result stores). When reading task metadata from the backend, the data is deserialized. Given that an attacker can gain access to, or somehow manipulate the metadata within a celery backend, they could trigger a stored command injection vulnerability and potentially gain further access to the system.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-23727
	Severity: HIGH
	Package: celery
	Fixed Version: 5.2.2
	Link: [CVE-2021-23727](https://avd.aquasec.com/nvd/cve-2021-23727)
	This affects the package celery before 5.2.2. It by default trusts the messages and metadata stored in backends (result stores). When reading task metadata from the backend, the data is deserialized. Given that an attacker can gain access to, or somehow manipulate the metadata within a celery backend, they could trigger a stored command injection vulnerability and potentially gain further access to the system.
    </details>



---

Package: lxml
Installed Version: 4.7.1
Vulnerability CVE-2022-2309
Severity: HIGH
Fixed Version: 4.9.1
Link: [CVE-2022-2309](https://avd.aquasec.com/nvd/cve-2022-2309)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/lxml-4.7.1.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2309
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2309">https://avd.aquasec.com/nvd/cve-2022-2309</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    lxml: NULL Pointer Dereference in lxml
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    NULL Pointer Dereference allows attackers to cause a denial of service (or application crash). This only applies when lxml is used together with libxml2 2.9.10 through 2.9.14. libxml2 2.9.9 and earlier are not affected. It allows triggering crashes through forged input data, given a vulnerable code sequence in the application. The vulnerability is caused by the iterwalk function (also used by the canonicalize function). Such code shouldn&amp;#39;t be in wide-spread use, given that parsing + iterwalk would usually be replaced with the more efficient iterparse function. However, an XML converter that serialises to C14N would also be vulnerable, for example, and there are legitimate use cases for this code sequence. If untrusted input is received (also remotely) and processed via iterwalk function, a crash can be triggered.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2309
	Severity: HIGH
	Package: lxml
	Fixed Version: 4.9.1
	Link: [CVE-2022-2309](https://avd.aquasec.com/nvd/cve-2022-2309)
	NULL Pointer Dereference allows attackers to cause a denial of service (or application crash). This only applies when lxml is used together with libxml2 2.9.10 through 2.9.14. libxml2 2.9.9 and earlier are not affected. It allows triggering crashes through forged input data, given a vulnerable code sequence in the application. The vulnerability is caused by the iterwalk function (also used by the canonicalize function). Such code shouldn&#39;t be in wide-spread use, given that parsing + iterwalk would usually be replaced with the more efficient iterparse function. However, an XML converter that serialises to C14N would also be vulnerable, for example, and there are legitimate use cases for this code sequence. If untrusted input is received (also remotely) and processed via iterwalk function, a crash can be triggered.
    </details>



---

Package: pysaml2
Installed Version: 4.9.0
Vulnerability CVE-2020-5390
Severity: HIGH
Fixed Version: 5.0.0
Link: [CVE-2020-5390](https://avd.aquasec.com/nvd/cve-2020-5390)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/pysaml2-4.9.0.dist-info/METADATA


- Line 1







### Level

- Error


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-5390
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-5390">https://avd.aquasec.com/nvd/cve-2020-5390</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pysaml2: does not check that the signature in a SAML document is enveloped
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    PySAML2 before 5.0.0 does not check that the signature in a SAML document is enveloped and thus signature wrapping is effective, i.e., it is affected by XML Signature Wrapping (XSW). The signature information and the node/object that is signed can be in different places and thus the signature verification will succeed, but the wrong data will be used. This specifically affects the verification of assertion that have been signed.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-5390
	Severity: HIGH
	Package: pysaml2
	Fixed Version: 5.0.0
	Link: [CVE-2020-5390](https://avd.aquasec.com/nvd/cve-2020-5390)
	PySAML2 before 5.0.0 does not check that the signature in a SAML document is enveloped and thus signature wrapping is effective, i.e., it is affected by XML Signature Wrapping (XSW). The signature information and the node/object that is signed can be in different places and thus the signature verification will succeed, but the wrong data will be used. This specifically affects the verification of assertion that have been signed.
    </details>



---

Package: binutils
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2022-38533
Severity: MEDIUM
Fixed Version: 2.30-21ubuntu1~18.04.8
Link: [CVE-2022-38533](https://avd.aquasec.com/nvd/cve-2022-38533)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-38533
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-38533">https://avd.aquasec.com/nvd/cve-2022-38533</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: heap-based buffer overflow in bfd_getl32() when called by strip_main() in objcopy.c via a crafted file
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In GNU Binutils before 2.40, there is a heap-buffer-overflow in the error function bfd_getl32 when called from the strip_main function in strip-new via a crafted file.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-38533
	Severity: MEDIUM
	Package: libbinutils
	Fixed Version: 2.30-21ubuntu1~18.04.8
	Link: [CVE-2022-38533](https://avd.aquasec.com/nvd/cve-2022-38533)
	In GNU Binutils before 2.40, there is a heap-buffer-overflow in the error function bfd_getl32 when called from the strip_main function in strip-new via a crafted file.
    </details>



---

Package: binutils-common
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2022-38533
Severity: MEDIUM
Fixed Version: 2.30-21ubuntu1~18.04.8
Link: [CVE-2022-38533](https://avd.aquasec.com/nvd/cve-2022-38533)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-38533
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-38533">https://avd.aquasec.com/nvd/cve-2022-38533</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: heap-based buffer overflow in bfd_getl32() when called by strip_main() in objcopy.c via a crafted file
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In GNU Binutils before 2.40, there is a heap-buffer-overflow in the error function bfd_getl32 when called from the strip_main function in strip-new via a crafted file.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-38533
	Severity: MEDIUM
	Package: libbinutils
	Fixed Version: 2.30-21ubuntu1~18.04.8
	Link: [CVE-2022-38533](https://avd.aquasec.com/nvd/cve-2022-38533)
	In GNU Binutils before 2.40, there is a heap-buffer-overflow in the error function bfd_getl32 when called from the strip_main function in strip-new via a crafted file.
    </details>



---

Package: binutils-x86-64-linux-gnu
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2022-38533
Severity: MEDIUM
Fixed Version: 2.30-21ubuntu1~18.04.8
Link: [CVE-2022-38533](https://avd.aquasec.com/nvd/cve-2022-38533)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-38533
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-38533">https://avd.aquasec.com/nvd/cve-2022-38533</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: heap-based buffer overflow in bfd_getl32() when called by strip_main() in objcopy.c via a crafted file
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In GNU Binutils before 2.40, there is a heap-buffer-overflow in the error function bfd_getl32 when called from the strip_main function in strip-new via a crafted file.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-38533
	Severity: MEDIUM
	Package: libbinutils
	Fixed Version: 2.30-21ubuntu1~18.04.8
	Link: [CVE-2022-38533](https://avd.aquasec.com/nvd/cve-2022-38533)
	In GNU Binutils before 2.40, there is a heap-buffer-overflow in the error function bfd_getl32 when called from the strip_main function in strip-new via a crafted file.
    </details>



---

Package: ca-certificates
Installed Version: 20211016~18.04.1
Vulnerability CVE-2022-23491
Severity: MEDIUM
Fixed Version: 20211016ubuntu0.18.04.1
Link: [CVE-2022-23491](https://avd.aquasec.com/nvd/cve-2022-23491)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-23491
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-23491">https://avd.aquasec.com/nvd/cve-2022-23491</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Certifi removing TrustCor root certificate
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Certifi is a curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. Certifi 2022.12.07 removes root certificates from &amp;#34;TrustCor&amp;#34; from the root store. These are in the process of being removed from Mozilla&amp;#39;s trust store. TrustCor&amp;#39;s root certificates are being removed pursuant to an investigation prompted by media reporting that TrustCor&amp;#39;s ownership also operated a business that produced spyware. Conclusions of Mozilla&amp;#39;s investigation can be found in the linked google group discussion.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    6.8
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-23491
	Severity: MEDIUM
	Package: certifi
	Fixed Version: 2022.12.07
	Link: [CVE-2022-23491](https://avd.aquasec.com/nvd/cve-2022-23491)
	Certifi is a curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. Certifi 2022.12.07 removes root certificates from &#34;TrustCor&#34; from the root store. These are in the process of being removed from Mozilla&#39;s trust store. TrustCor&#39;s root certificates are being removed pursuant to an investigation prompted by media reporting that TrustCor&#39;s ownership also operated a business that produced spyware. Conclusions of Mozilla&#39;s investigation can be found in the linked google group discussion.
    </details>



---

Package: cpp-7
Installed Version: 7.5.0-3ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: curl
Installed Version: 7.58.0-2ubuntu3.20
Vulnerability CVE-2022-32221
Severity: MEDIUM
Fixed Version: 7.58.0-2ubuntu3.21
Link: [CVE-2022-32221](https://avd.aquasec.com/nvd/cve-2022-32221)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-32221
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-32221">https://avd.aquasec.com/nvd/cve-2022-32221</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    curl: POST following PUT confusion
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    When doing HTTP(S) transfers, libcurl might erroneously use the read callback (`CURLOPT_READFUNCTION`) to ask for data to send, even when the `CURLOPT_POSTFIELDS` option has been set, if the same handle previously was used to issue a `PUT` request which used that callback. This flaw may surprise the application and cause it to misbehave and either send off the wrong data or use memory after free or similar in the subsequent `POST` request. The problem exists in the logic for a reused handle when it is changed from a PUT to a POST.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-32221
	Severity: MEDIUM
	Package: libcurl4-openssl-dev
	Fixed Version: 7.58.0-2ubuntu3.21
	Link: [CVE-2022-32221](https://avd.aquasec.com/nvd/cve-2022-32221)
	When doing HTTP(S) transfers, libcurl might erroneously use the read callback (`CURLOPT_READFUNCTION`) to ask for data to send, even when the `CURLOPT_POSTFIELDS` option has been set, if the same handle previously was used to issue a `PUT` request which used that callback. This flaw may surprise the application and cause it to misbehave and either send off the wrong data or use memory after free or similar in the subsequent `POST` request. The problem exists in the logic for a reused handle when it is changed from a PUT to a POST.
    </details>



---

Package: dbus
Installed Version: 1.12.2-1ubuntu1.3
Vulnerability CVE-2022-42010
Severity: MEDIUM
Fixed Version: 1.12.2-1ubuntu1.4
Link: [CVE-2022-42010](https://avd.aquasec.com/nvd/cve-2022-42010)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42010
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42010">https://avd.aquasec.com/nvd/cve-2022-42010</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    dbus: dbus-daemon crashes when receiving message with incorrectly nested parentheses and curly brackets
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in D-Bus before 1.12.24, 1.13.x and 1.14.x before 1.14.4, and 1.15.x before 1.15.2. An authenticated attacker can cause dbus-daemon and other programs that use libdbus to crash when receiving a message with certain invalid type signatures.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42010
	Severity: MEDIUM
	Package: libdbus-1-3
	Fixed Version: 1.12.2-1ubuntu1.4
	Link: [CVE-2022-42010](https://avd.aquasec.com/nvd/cve-2022-42010)
	An issue was discovered in D-Bus before 1.12.24, 1.13.x and 1.14.x before 1.14.4, and 1.15.x before 1.15.2. An authenticated attacker can cause dbus-daemon and other programs that use libdbus to crash when receiving a message with certain invalid type signatures.
    </details>



---

Package: dbus
Installed Version: 1.12.2-1ubuntu1.3
Vulnerability CVE-2022-42011
Severity: MEDIUM
Fixed Version: 1.12.2-1ubuntu1.4
Link: [CVE-2022-42011](https://avd.aquasec.com/nvd/cve-2022-42011)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42011
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42011">https://avd.aquasec.com/nvd/cve-2022-42011</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    dbus: dbus-daemon can be crashed by messages with array length inconsistent with element type
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in D-Bus before 1.12.24, 1.13.x and 1.14.x before 1.14.4, and 1.15.x before 1.15.2. An authenticated attacker can cause dbus-daemon and other programs that use libdbus to crash when receiving a message where an array length is inconsistent with the size of the element type.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42011
	Severity: MEDIUM
	Package: libdbus-1-3
	Fixed Version: 1.12.2-1ubuntu1.4
	Link: [CVE-2022-42011](https://avd.aquasec.com/nvd/cve-2022-42011)
	An issue was discovered in D-Bus before 1.12.24, 1.13.x and 1.14.x before 1.14.4, and 1.15.x before 1.15.2. An authenticated attacker can cause dbus-daemon and other programs that use libdbus to crash when receiving a message where an array length is inconsistent with the size of the element type.
    </details>



---

Package: dbus
Installed Version: 1.12.2-1ubuntu1.3
Vulnerability CVE-2022-42012
Severity: MEDIUM
Fixed Version: 1.12.2-1ubuntu1.4
Link: [CVE-2022-42012](https://avd.aquasec.com/nvd/cve-2022-42012)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42012
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42012">https://avd.aquasec.com/nvd/cve-2022-42012</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    dbus: `_dbus_marshal_byteswap` doesn&amp;#39;t process fds in messages with &amp;#34;foreign&amp;#34; endianness correctly
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in D-Bus before 1.12.24, 1.13.x and 1.14.x before 1.14.4, and 1.15.x before 1.15.2. An authenticated attacker can cause dbus-daemon and other programs that use libdbus to crash by sending a message with attached file descriptors in an unexpected format.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42012
	Severity: MEDIUM
	Package: libdbus-1-3
	Fixed Version: 1.12.2-1ubuntu1.4
	Link: [CVE-2022-42012](https://avd.aquasec.com/nvd/cve-2022-42012)
	An issue was discovered in D-Bus before 1.12.24, 1.13.x and 1.14.x before 1.14.4, and 1.15.x before 1.15.2. An authenticated attacker can cause dbus-daemon and other programs that use libdbus to crash by sending a message with attached file descriptors in an unexpected format.
    </details>



---

Package: gcc-7
Installed Version: 7.5.0-3ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: gcc-7-base
Installed Version: 7.5.0-3ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: gcc-8-base
Installed Version: 8.4.0-1ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: git
Installed Version: 1:2.17.1-1ubuntu0.12
Vulnerability CVE-2022-39253
Severity: MEDIUM
Fixed Version: 1:2.17.1-1ubuntu0.13
Link: [CVE-2022-39253](https://avd.aquasec.com/nvd/cve-2022-39253)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-39253
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-39253">https://avd.aquasec.com/nvd/cve-2022-39253</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    git: exposure of sensitive information to a malicious actor
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Git is an open source, scalable, distributed revision control system. Versions prior to 2.30.6, 2.31.5, 2.32.4, 2.33.5, 2.34.5, 2.35.5, 2.36.3, and 2.37.4 are subject to exposure of sensitive information to a malicious actor. When performing a local clone (where the source and target of the clone are on the same volume), Git copies the contents of the source&amp;#39;s `$GIT_DIR/objects` directory into the destination by either creating hardlinks to the source contents, or copying them (if hardlinks are disabled via `--no-hardlinks`). A malicious actor could convince a victim to clone a repository with a symbolic link pointing at sensitive information on the victim&amp;#39;s machine. This can be done either by having the victim clone a malicious repository on the same machine, or having them clone a malicious repository embedded as a bare repository via a submodule from any source, provided they clone with the `--recurse-submodules` option. Git does not create symbolic links in the `$GIT_DIR/objects` directory. The problem has been patched in the versions published on 2022-10-18, and backported to v2.30.x. Potential workarounds: Avoid cloning untrusted repositories using the `--local` optimization when on a shared machine, either by passing the `--no-local` option to `git clone` or cloning from a URL that uses the `file://` scheme. Alternatively, avoid cloning repositories from untrusted sources with `--recurse-submodules` or run `git config --global protocol.file.allow user`.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-39253
	Severity: MEDIUM
	Package: git-man
	Fixed Version: 1:2.17.1-1ubuntu0.13
	Link: [CVE-2022-39253](https://avd.aquasec.com/nvd/cve-2022-39253)
	Git is an open source, scalable, distributed revision control system. Versions prior to 2.30.6, 2.31.5, 2.32.4, 2.33.5, 2.34.5, 2.35.5, 2.36.3, and 2.37.4 are subject to exposure of sensitive information to a malicious actor. When performing a local clone (where the source and target of the clone are on the same volume), Git copies the contents of the source&#39;s `$GIT_DIR/objects` directory into the destination by either creating hardlinks to the source contents, or copying them (if hardlinks are disabled via `--no-hardlinks`). A malicious actor could convince a victim to clone a repository with a symbolic link pointing at sensitive information on the victim&#39;s machine. This can be done either by having the victim clone a malicious repository on the same machine, or having them clone a malicious repository embedded as a bare repository via a submodule from any source, provided they clone with the `--recurse-submodules` option. Git does not create symbolic links in the `$GIT_DIR/objects` directory. The problem has been patched in the versions published on 2022-10-18, and backported to v2.30.x. Potential workarounds: Avoid cloning untrusted repositories using the `--local` optimization when on a shared machine, either by passing the `--no-local` option to `git clone` or cloning from a URL that uses the `file://` scheme. Alternatively, avoid cloning repositories from untrusted sources with `--recurse-submodules` or run `git config --global protocol.file.allow user`.
    </details>



---

Package: git
Installed Version: 1:2.17.1-1ubuntu0.12
Vulnerability CVE-2022-39260
Severity: MEDIUM
Fixed Version: 1:2.17.1-1ubuntu0.13
Link: [CVE-2022-39260](https://avd.aquasec.com/nvd/cve-2022-39260)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-39260
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-39260">https://avd.aquasec.com/nvd/cve-2022-39260</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    git: git shell function that splits command arguments can lead to arbitrary heap writes.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Git is an open source, scalable, distributed revision control system. `git shell` is a restricted login shell that can be used to implement Git&amp;#39;s push/pull functionality via SSH. In versions prior to 2.30.6, 2.31.5, 2.32.4, 2.33.5, 2.34.5, 2.35.5, 2.36.3, and 2.37.4, the function that splits the command arguments into an array improperly uses an `int` to represent the number of entries in the array, allowing a malicious actor to intentionally overflow the return value, leading to arbitrary heap writes. Because the resulting array is then passed to `execv()`, it is possible to leverage this attack to gain remote code execution on a victim machine. Note that a victim must first allow access to `git shell` as a login shell in order to be vulnerable to this attack. This problem is patched in versions 2.30.6, 2.31.5, 2.32.4, 2.33.5, 2.34.5, 2.35.5, 2.36.3, and 2.37.4 and users are advised to upgrade to the latest version. Disabling `git shell` access via remote logins is a viable short-term workaround.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-39260
	Severity: MEDIUM
	Package: git-man
	Fixed Version: 1:2.17.1-1ubuntu0.13
	Link: [CVE-2022-39260](https://avd.aquasec.com/nvd/cve-2022-39260)
	Git is an open source, scalable, distributed revision control system. `git shell` is a restricted login shell that can be used to implement Git&#39;s push/pull functionality via SSH. In versions prior to 2.30.6, 2.31.5, 2.32.4, 2.33.5, 2.34.5, 2.35.5, 2.36.3, and 2.37.4, the function that splits the command arguments into an array improperly uses an `int` to represent the number of entries in the array, allowing a malicious actor to intentionally overflow the return value, leading to arbitrary heap writes. Because the resulting array is then passed to `execv()`, it is possible to leverage this attack to gain remote code execution on a victim machine. Note that a victim must first allow access to `git shell` as a login shell in order to be vulnerable to this attack. This problem is patched in versions 2.30.6, 2.31.5, 2.32.4, 2.33.5, 2.34.5, 2.35.5, 2.36.3, and 2.37.4 and users are advised to upgrade to the latest version. Disabling `git shell` access via remote logins is a viable short-term workaround.
    </details>



---

Package: git-man
Installed Version: 1:2.17.1-1ubuntu0.12
Vulnerability CVE-2022-39253
Severity: MEDIUM
Fixed Version: 1:2.17.1-1ubuntu0.13
Link: [CVE-2022-39253](https://avd.aquasec.com/nvd/cve-2022-39253)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-39253
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-39253">https://avd.aquasec.com/nvd/cve-2022-39253</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    git: exposure of sensitive information to a malicious actor
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Git is an open source, scalable, distributed revision control system. Versions prior to 2.30.6, 2.31.5, 2.32.4, 2.33.5, 2.34.5, 2.35.5, 2.36.3, and 2.37.4 are subject to exposure of sensitive information to a malicious actor. When performing a local clone (where the source and target of the clone are on the same volume), Git copies the contents of the source&amp;#39;s `$GIT_DIR/objects` directory into the destination by either creating hardlinks to the source contents, or copying them (if hardlinks are disabled via `--no-hardlinks`). A malicious actor could convince a victim to clone a repository with a symbolic link pointing at sensitive information on the victim&amp;#39;s machine. This can be done either by having the victim clone a malicious repository on the same machine, or having them clone a malicious repository embedded as a bare repository via a submodule from any source, provided they clone with the `--recurse-submodules` option. Git does not create symbolic links in the `$GIT_DIR/objects` directory. The problem has been patched in the versions published on 2022-10-18, and backported to v2.30.x. Potential workarounds: Avoid cloning untrusted repositories using the `--local` optimization when on a shared machine, either by passing the `--no-local` option to `git clone` or cloning from a URL that uses the `file://` scheme. Alternatively, avoid cloning repositories from untrusted sources with `--recurse-submodules` or run `git config --global protocol.file.allow user`.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-39253
	Severity: MEDIUM
	Package: git-man
	Fixed Version: 1:2.17.1-1ubuntu0.13
	Link: [CVE-2022-39253](https://avd.aquasec.com/nvd/cve-2022-39253)
	Git is an open source, scalable, distributed revision control system. Versions prior to 2.30.6, 2.31.5, 2.32.4, 2.33.5, 2.34.5, 2.35.5, 2.36.3, and 2.37.4 are subject to exposure of sensitive information to a malicious actor. When performing a local clone (where the source and target of the clone are on the same volume), Git copies the contents of the source&#39;s `$GIT_DIR/objects` directory into the destination by either creating hardlinks to the source contents, or copying them (if hardlinks are disabled via `--no-hardlinks`). A malicious actor could convince a victim to clone a repository with a symbolic link pointing at sensitive information on the victim&#39;s machine. This can be done either by having the victim clone a malicious repository on the same machine, or having them clone a malicious repository embedded as a bare repository via a submodule from any source, provided they clone with the `--recurse-submodules` option. Git does not create symbolic links in the `$GIT_DIR/objects` directory. The problem has been patched in the versions published on 2022-10-18, and backported to v2.30.x. Potential workarounds: Avoid cloning untrusted repositories using the `--local` optimization when on a shared machine, either by passing the `--no-local` option to `git clone` or cloning from a URL that uses the `file://` scheme. Alternatively, avoid cloning repositories from untrusted sources with `--recurse-submodules` or run `git config --global protocol.file.allow user`.
    </details>



---

Package: git-man
Installed Version: 1:2.17.1-1ubuntu0.12
Vulnerability CVE-2022-39260
Severity: MEDIUM
Fixed Version: 1:2.17.1-1ubuntu0.13
Link: [CVE-2022-39260](https://avd.aquasec.com/nvd/cve-2022-39260)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-39260
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-39260">https://avd.aquasec.com/nvd/cve-2022-39260</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    git: git shell function that splits command arguments can lead to arbitrary heap writes.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Git is an open source, scalable, distributed revision control system. `git shell` is a restricted login shell that can be used to implement Git&amp;#39;s push/pull functionality via SSH. In versions prior to 2.30.6, 2.31.5, 2.32.4, 2.33.5, 2.34.5, 2.35.5, 2.36.3, and 2.37.4, the function that splits the command arguments into an array improperly uses an `int` to represent the number of entries in the array, allowing a malicious actor to intentionally overflow the return value, leading to arbitrary heap writes. Because the resulting array is then passed to `execv()`, it is possible to leverage this attack to gain remote code execution on a victim machine. Note that a victim must first allow access to `git shell` as a login shell in order to be vulnerable to this attack. This problem is patched in versions 2.30.6, 2.31.5, 2.32.4, 2.33.5, 2.34.5, 2.35.5, 2.36.3, and 2.37.4 and users are advised to upgrade to the latest version. Disabling `git shell` access via remote logins is a viable short-term workaround.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-39260
	Severity: MEDIUM
	Package: git-man
	Fixed Version: 1:2.17.1-1ubuntu0.13
	Link: [CVE-2022-39260](https://avd.aquasec.com/nvd/cve-2022-39260)
	Git is an open source, scalable, distributed revision control system. `git shell` is a restricted login shell that can be used to implement Git&#39;s push/pull functionality via SSH. In versions prior to 2.30.6, 2.31.5, 2.32.4, 2.33.5, 2.34.5, 2.35.5, 2.36.3, and 2.37.4, the function that splits the command arguments into an array improperly uses an `int` to represent the number of entries in the array, allowing a malicious actor to intentionally overflow the return value, leading to arbitrary heap writes. Because the resulting array is then passed to `execv()`, it is possible to leverage this attack to gain remote code execution on a victim machine. Note that a victim must first allow access to `git shell` as a login shell in order to be vulnerable to this attack. This problem is patched in versions 2.30.6, 2.31.5, 2.32.4, 2.33.5, 2.34.5, 2.35.5, 2.36.3, and 2.37.4 and users are advised to upgrade to the latest version. Disabling `git shell` access via remote logins is a viable short-term workaround.
    </details>



---

Package: krb5-locales
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2018-20217
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2018-20217](https://avd.aquasec.com/nvd/cve-2018-20217)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-20217
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-20217">https://avd.aquasec.com/nvd/cve-2018-20217</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: Reachable assertion in the KDC using S4U2Self requests
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A Reachable Assertion issue was discovered in the KDC in MIT Kerberos 5 (aka krb5) before 1.17. If an attacker can obtain a krbtgt ticket using an older encryption type (single-DES, triple-DES, or RC4), the attacker can crash the KDC by making an S4U2Self request.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-20217
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2018-20217](https://avd.aquasec.com/nvd/cve-2018-20217)
	A Reachable Assertion issue was discovered in the KDC in MIT Kerberos 5 (aka krb5) before 1.17. If an attacker can obtain a krbtgt ticket using an older encryption type (single-DES, triple-DES, or RC4), the attacker can crash the KDC by making an S4U2Self request.
    </details>



---

Package: krb5-locales
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2021-36222
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-36222](https://avd.aquasec.com/nvd/cve-2021-36222)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-36222
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-36222">https://avd.aquasec.com/nvd/cve-2021-36222</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: Sending a request containing PA-ENCRYPTED-CHALLENGE padata element without using FAST could result in NULL dereference in KDC which leads to DoS
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ec_verify in kdc/kdc_preauth_ec.c in the Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.4 and 1.19.x before 1.19.2 allows remote attackers to cause a NULL pointer dereference and daemon crash. This occurs because a return value is not properly managed in a certain situation.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-36222
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2021-36222](https://avd.aquasec.com/nvd/cve-2021-36222)
	ec_verify in kdc/kdc_preauth_ec.c in the Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.4 and 1.19.x before 1.19.2 allows remote attackers to cause a NULL pointer dereference and daemon crash. This occurs because a return value is not properly managed in a certain situation.
    </details>



---

Package: krb5-locales
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2021-37750
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-37750](https://avd.aquasec.com/nvd/cve-2021-37750)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-37750
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-37750">https://avd.aquasec.com/nvd/cve-2021-37750</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: NULL pointer dereference in process_tgs_req() in kdc/do_tgs_req.c via a FAST inner body that lacks server field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.5 and 1.19.x before 1.19.3 has a NULL pointer dereference in kdc/do_tgs_req.c via a FAST inner body that lacks a server field.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-37750
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2021-37750](https://avd.aquasec.com/nvd/cve-2021-37750)
	The Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.5 and 1.19.x before 1.19.3 has a NULL pointer dereference in kdc/do_tgs_req.c via a FAST inner body that lacks a server field.
    </details>



---

Package: libapparmor1
Installed Version: 2.12-4ubuntu5.1
Vulnerability CVE-2016-1585
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2016-1585](https://avd.aquasec.com/nvd/cve-2016-1585)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2016-1585
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2016-1585">https://avd.aquasec.com/nvd/cve-2016-1585</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    In all versions of AppArmor mount rules are accidentally widened when  ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In all versions of AppArmor mount rules are accidentally widened when compiled.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2016-1585
	Severity: MEDIUM
	Package: libapparmor1
	Fixed Version: 
	Link: [CVE-2016-1585](https://avd.aquasec.com/nvd/cve-2016-1585)
	In all versions of AppArmor mount rules are accidentally widened when compiled.
    </details>



---

Package: libasan4
Installed Version: 7.5.0-3ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libasn1-8-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2018-16860
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-16860
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-16860">https://avd.aquasec.com/nvd/cve-2018-16860</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: S4U2Self with unkeyed checksum
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in samba&amp;#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-16860
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)
	A flaw was found in samba&#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>



---

Package: libasn1-8-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-44758
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-44758
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-44758">https://avd.aquasec.com/nvd/cve-2021-44758</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Denial of service. [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-44758
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)
	Denial of service. [spnego: send_reject when no mech selected]
    </details>



---

Package: libasn1-8-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3116
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3116
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3116">https://avd.aquasec.com/nvd/cve-2022-3116</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3116
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)
	A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>



---

Package: libasn1-8-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3437
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3437
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3437">https://avd.aquasec.com/nvd/cve-2022-3437</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: heap buffer overflow in GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3437
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)
	A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>



---

Package: libasn1-8-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-41916
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.2
Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-41916
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-41916">https://avd.aquasec.com/nvd/cve-2022-41916</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Version ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&amp;#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&amp;#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-41916
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.2
	Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)
	Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>



---

Package: libasn1-8-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-42898
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42898
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42898">https://avd.aquasec.com/nvd/cve-2022-42898</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: integer overflow vulnerabilities in PAC parsing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42898
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)
	A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>



---

Package: libasn1-8-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-44640
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-44640
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-44640">https://avd.aquasec.com/nvd/cve-2022-44640</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-44640
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)
	[Invalid free in ASN.1 codec]
    </details>



---

Package: libatomic1
Installed Version: 8.4.0-1ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libbinutils
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2022-38533
Severity: MEDIUM
Fixed Version: 2.30-21ubuntu1~18.04.8
Link: [CVE-2022-38533](https://avd.aquasec.com/nvd/cve-2022-38533)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-38533
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-38533">https://avd.aquasec.com/nvd/cve-2022-38533</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: heap-based buffer overflow in bfd_getl32() when called by strip_main() in objcopy.c via a crafted file
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In GNU Binutils before 2.40, there is a heap-buffer-overflow in the error function bfd_getl32 when called from the strip_main function in strip-new via a crafted file.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-38533
	Severity: MEDIUM
	Package: libbinutils
	Fixed Version: 2.30-21ubuntu1~18.04.8
	Link: [CVE-2022-38533](https://avd.aquasec.com/nvd/cve-2022-38533)
	In GNU Binutils before 2.40, there is a heap-buffer-overflow in the error function bfd_getl32 when called from the strip_main function in strip-new via a crafted file.
    </details>



---

Package: libcc1-0
Installed Version: 8.4.0-1ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libcilkrts5
Installed Version: 7.5.0-3ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libcurl3-gnutls
Installed Version: 7.58.0-2ubuntu3.20
Vulnerability CVE-2022-32221
Severity: MEDIUM
Fixed Version: 7.58.0-2ubuntu3.21
Link: [CVE-2022-32221](https://avd.aquasec.com/nvd/cve-2022-32221)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-32221
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-32221">https://avd.aquasec.com/nvd/cve-2022-32221</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    curl: POST following PUT confusion
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    When doing HTTP(S) transfers, libcurl might erroneously use the read callback (`CURLOPT_READFUNCTION`) to ask for data to send, even when the `CURLOPT_POSTFIELDS` option has been set, if the same handle previously was used to issue a `PUT` request which used that callback. This flaw may surprise the application and cause it to misbehave and either send off the wrong data or use memory after free or similar in the subsequent `POST` request. The problem exists in the logic for a reused handle when it is changed from a PUT to a POST.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-32221
	Severity: MEDIUM
	Package: libcurl4-openssl-dev
	Fixed Version: 7.58.0-2ubuntu3.21
	Link: [CVE-2022-32221](https://avd.aquasec.com/nvd/cve-2022-32221)
	When doing HTTP(S) transfers, libcurl might erroneously use the read callback (`CURLOPT_READFUNCTION`) to ask for data to send, even when the `CURLOPT_POSTFIELDS` option has been set, if the same handle previously was used to issue a `PUT` request which used that callback. This flaw may surprise the application and cause it to misbehave and either send off the wrong data or use memory after free or similar in the subsequent `POST` request. The problem exists in the logic for a reused handle when it is changed from a PUT to a POST.
    </details>



---

Package: libcurl4
Installed Version: 7.58.0-2ubuntu3.20
Vulnerability CVE-2022-32221
Severity: MEDIUM
Fixed Version: 7.58.0-2ubuntu3.21
Link: [CVE-2022-32221](https://avd.aquasec.com/nvd/cve-2022-32221)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-32221
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-32221">https://avd.aquasec.com/nvd/cve-2022-32221</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    curl: POST following PUT confusion
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    When doing HTTP(S) transfers, libcurl might erroneously use the read callback (`CURLOPT_READFUNCTION`) to ask for data to send, even when the `CURLOPT_POSTFIELDS` option has been set, if the same handle previously was used to issue a `PUT` request which used that callback. This flaw may surprise the application and cause it to misbehave and either send off the wrong data or use memory after free or similar in the subsequent `POST` request. The problem exists in the logic for a reused handle when it is changed from a PUT to a POST.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-32221
	Severity: MEDIUM
	Package: libcurl4-openssl-dev
	Fixed Version: 7.58.0-2ubuntu3.21
	Link: [CVE-2022-32221](https://avd.aquasec.com/nvd/cve-2022-32221)
	When doing HTTP(S) transfers, libcurl might erroneously use the read callback (`CURLOPT_READFUNCTION`) to ask for data to send, even when the `CURLOPT_POSTFIELDS` option has been set, if the same handle previously was used to issue a `PUT` request which used that callback. This flaw may surprise the application and cause it to misbehave and either send off the wrong data or use memory after free or similar in the subsequent `POST` request. The problem exists in the logic for a reused handle when it is changed from a PUT to a POST.
    </details>



---

Package: libcurl4-openssl-dev
Installed Version: 7.58.0-2ubuntu3.20
Vulnerability CVE-2022-32221
Severity: MEDIUM
Fixed Version: 7.58.0-2ubuntu3.21
Link: [CVE-2022-32221](https://avd.aquasec.com/nvd/cve-2022-32221)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-32221
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-32221">https://avd.aquasec.com/nvd/cve-2022-32221</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    curl: POST following PUT confusion
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    When doing HTTP(S) transfers, libcurl might erroneously use the read callback (`CURLOPT_READFUNCTION`) to ask for data to send, even when the `CURLOPT_POSTFIELDS` option has been set, if the same handle previously was used to issue a `PUT` request which used that callback. This flaw may surprise the application and cause it to misbehave and either send off the wrong data or use memory after free or similar in the subsequent `POST` request. The problem exists in the logic for a reused handle when it is changed from a PUT to a POST.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-32221
	Severity: MEDIUM
	Package: libcurl4-openssl-dev
	Fixed Version: 7.58.0-2ubuntu3.21
	Link: [CVE-2022-32221](https://avd.aquasec.com/nvd/cve-2022-32221)
	When doing HTTP(S) transfers, libcurl might erroneously use the read callback (`CURLOPT_READFUNCTION`) to ask for data to send, even when the `CURLOPT_POSTFIELDS` option has been set, if the same handle previously was used to issue a `PUT` request which used that callback. This flaw may surprise the application and cause it to misbehave and either send off the wrong data or use memory after free or similar in the subsequent `POST` request. The problem exists in the logic for a reused handle when it is changed from a PUT to a POST.
    </details>



---

Package: libdbus-1-3
Installed Version: 1.12.2-1ubuntu1.3
Vulnerability CVE-2022-42010
Severity: MEDIUM
Fixed Version: 1.12.2-1ubuntu1.4
Link: [CVE-2022-42010](https://avd.aquasec.com/nvd/cve-2022-42010)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42010
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42010">https://avd.aquasec.com/nvd/cve-2022-42010</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    dbus: dbus-daemon crashes when receiving message with incorrectly nested parentheses and curly brackets
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in D-Bus before 1.12.24, 1.13.x and 1.14.x before 1.14.4, and 1.15.x before 1.15.2. An authenticated attacker can cause dbus-daemon and other programs that use libdbus to crash when receiving a message with certain invalid type signatures.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42010
	Severity: MEDIUM
	Package: libdbus-1-3
	Fixed Version: 1.12.2-1ubuntu1.4
	Link: [CVE-2022-42010](https://avd.aquasec.com/nvd/cve-2022-42010)
	An issue was discovered in D-Bus before 1.12.24, 1.13.x and 1.14.x before 1.14.4, and 1.15.x before 1.15.2. An authenticated attacker can cause dbus-daemon and other programs that use libdbus to crash when receiving a message with certain invalid type signatures.
    </details>



---

Package: libdbus-1-3
Installed Version: 1.12.2-1ubuntu1.3
Vulnerability CVE-2022-42011
Severity: MEDIUM
Fixed Version: 1.12.2-1ubuntu1.4
Link: [CVE-2022-42011](https://avd.aquasec.com/nvd/cve-2022-42011)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42011
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42011">https://avd.aquasec.com/nvd/cve-2022-42011</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    dbus: dbus-daemon can be crashed by messages with array length inconsistent with element type
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in D-Bus before 1.12.24, 1.13.x and 1.14.x before 1.14.4, and 1.15.x before 1.15.2. An authenticated attacker can cause dbus-daemon and other programs that use libdbus to crash when receiving a message where an array length is inconsistent with the size of the element type.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42011
	Severity: MEDIUM
	Package: libdbus-1-3
	Fixed Version: 1.12.2-1ubuntu1.4
	Link: [CVE-2022-42011](https://avd.aquasec.com/nvd/cve-2022-42011)
	An issue was discovered in D-Bus before 1.12.24, 1.13.x and 1.14.x before 1.14.4, and 1.15.x before 1.15.2. An authenticated attacker can cause dbus-daemon and other programs that use libdbus to crash when receiving a message where an array length is inconsistent with the size of the element type.
    </details>



---

Package: libdbus-1-3
Installed Version: 1.12.2-1ubuntu1.3
Vulnerability CVE-2022-42012
Severity: MEDIUM
Fixed Version: 1.12.2-1ubuntu1.4
Link: [CVE-2022-42012](https://avd.aquasec.com/nvd/cve-2022-42012)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42012
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42012">https://avd.aquasec.com/nvd/cve-2022-42012</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    dbus: `_dbus_marshal_byteswap` doesn&amp;#39;t process fds in messages with &amp;#34;foreign&amp;#34; endianness correctly
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in D-Bus before 1.12.24, 1.13.x and 1.14.x before 1.14.4, and 1.15.x before 1.15.2. An authenticated attacker can cause dbus-daemon and other programs that use libdbus to crash by sending a message with attached file descriptors in an unexpected format.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42012
	Severity: MEDIUM
	Package: libdbus-1-3
	Fixed Version: 1.12.2-1ubuntu1.4
	Link: [CVE-2022-42012](https://avd.aquasec.com/nvd/cve-2022-42012)
	An issue was discovered in D-Bus before 1.12.24, 1.13.x and 1.14.x before 1.14.4, and 1.15.x before 1.15.2. An authenticated attacker can cause dbus-daemon and other programs that use libdbus to crash by sending a message with attached file descriptors in an unexpected format.
    </details>



---

Package: libexpat1
Installed Version: 2.2.5-3ubuntu0.7
Vulnerability CVE-2022-40674
Severity: MEDIUM
Fixed Version: 2.2.5-3ubuntu0.8
Link: [CVE-2022-40674](https://avd.aquasec.com/nvd/cve-2022-40674)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-40674
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-40674">https://avd.aquasec.com/nvd/cve-2022-40674</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    expat: a use-after-free in the doContent function in xmlparse.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    libexpat before 2.4.9 has a use-after-free in the doContent function in xmlparse.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-40674
	Severity: MEDIUM
	Package: libexpat1-dev
	Fixed Version: 2.2.5-3ubuntu0.8
	Link: [CVE-2022-40674](https://avd.aquasec.com/nvd/cve-2022-40674)
	libexpat before 2.4.9 has a use-after-free in the doContent function in xmlparse.c.
    </details>



---

Package: libexpat1
Installed Version: 2.2.5-3ubuntu0.7
Vulnerability CVE-2022-43680
Severity: MEDIUM
Fixed Version: 2.2.5-3ubuntu0.8
Link: [CVE-2022-43680](https://avd.aquasec.com/nvd/cve-2022-43680)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-43680
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-43680">https://avd.aquasec.com/nvd/cve-2022-43680</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    expat: use-after free caused by overeager destruction of a shared DTD in XML_ExternalEntityParserCreate
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In libexpat through 2.4.9, there is a use-after free caused by overeager destruction of a shared DTD in XML_ExternalEntityParserCreate in out-of-memory situations.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-43680
	Severity: MEDIUM
	Package: libexpat1-dev
	Fixed Version: 2.2.5-3ubuntu0.8
	Link: [CVE-2022-43680](https://avd.aquasec.com/nvd/cve-2022-43680)
	In libexpat through 2.4.9, there is a use-after free caused by overeager destruction of a shared DTD in XML_ExternalEntityParserCreate in out-of-memory situations.
    </details>



---

Package: libexpat1-dev
Installed Version: 2.2.5-3ubuntu0.7
Vulnerability CVE-2022-40674
Severity: MEDIUM
Fixed Version: 2.2.5-3ubuntu0.8
Link: [CVE-2022-40674](https://avd.aquasec.com/nvd/cve-2022-40674)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-40674
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-40674">https://avd.aquasec.com/nvd/cve-2022-40674</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    expat: a use-after-free in the doContent function in xmlparse.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    libexpat before 2.4.9 has a use-after-free in the doContent function in xmlparse.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-40674
	Severity: MEDIUM
	Package: libexpat1-dev
	Fixed Version: 2.2.5-3ubuntu0.8
	Link: [CVE-2022-40674](https://avd.aquasec.com/nvd/cve-2022-40674)
	libexpat before 2.4.9 has a use-after-free in the doContent function in xmlparse.c.
    </details>



---

Package: libexpat1-dev
Installed Version: 2.2.5-3ubuntu0.7
Vulnerability CVE-2022-43680
Severity: MEDIUM
Fixed Version: 2.2.5-3ubuntu0.8
Link: [CVE-2022-43680](https://avd.aquasec.com/nvd/cve-2022-43680)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-43680
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-43680">https://avd.aquasec.com/nvd/cve-2022-43680</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    expat: use-after free caused by overeager destruction of a shared DTD in XML_ExternalEntityParserCreate
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In libexpat through 2.4.9, there is a use-after free caused by overeager destruction of a shared DTD in XML_ExternalEntityParserCreate in out-of-memory situations.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-43680
	Severity: MEDIUM
	Package: libexpat1-dev
	Fixed Version: 2.2.5-3ubuntu0.8
	Link: [CVE-2022-43680](https://avd.aquasec.com/nvd/cve-2022-43680)
	In libexpat through 2.4.9, there is a use-after free caused by overeager destruction of a shared DTD in XML_ExternalEntityParserCreate in out-of-memory situations.
    </details>



---

Package: libgcc-7-dev
Installed Version: 7.5.0-3ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libgcc1
Installed Version: 8.4.0-1ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libgomp1
Installed Version: 8.4.0-1ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libgssapi-krb5-2
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2018-20217
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2018-20217](https://avd.aquasec.com/nvd/cve-2018-20217)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-20217
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-20217">https://avd.aquasec.com/nvd/cve-2018-20217</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: Reachable assertion in the KDC using S4U2Self requests
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A Reachable Assertion issue was discovered in the KDC in MIT Kerberos 5 (aka krb5) before 1.17. If an attacker can obtain a krbtgt ticket using an older encryption type (single-DES, triple-DES, or RC4), the attacker can crash the KDC by making an S4U2Self request.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-20217
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2018-20217](https://avd.aquasec.com/nvd/cve-2018-20217)
	A Reachable Assertion issue was discovered in the KDC in MIT Kerberos 5 (aka krb5) before 1.17. If an attacker can obtain a krbtgt ticket using an older encryption type (single-DES, triple-DES, or RC4), the attacker can crash the KDC by making an S4U2Self request.
    </details>



---

Package: libgssapi-krb5-2
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2021-36222
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-36222](https://avd.aquasec.com/nvd/cve-2021-36222)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-36222
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-36222">https://avd.aquasec.com/nvd/cve-2021-36222</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: Sending a request containing PA-ENCRYPTED-CHALLENGE padata element without using FAST could result in NULL dereference in KDC which leads to DoS
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ec_verify in kdc/kdc_preauth_ec.c in the Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.4 and 1.19.x before 1.19.2 allows remote attackers to cause a NULL pointer dereference and daemon crash. This occurs because a return value is not properly managed in a certain situation.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-36222
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2021-36222](https://avd.aquasec.com/nvd/cve-2021-36222)
	ec_verify in kdc/kdc_preauth_ec.c in the Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.4 and 1.19.x before 1.19.2 allows remote attackers to cause a NULL pointer dereference and daemon crash. This occurs because a return value is not properly managed in a certain situation.
    </details>



---

Package: libgssapi-krb5-2
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2021-37750
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-37750](https://avd.aquasec.com/nvd/cve-2021-37750)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-37750
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-37750">https://avd.aquasec.com/nvd/cve-2021-37750</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: NULL pointer dereference in process_tgs_req() in kdc/do_tgs_req.c via a FAST inner body that lacks server field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.5 and 1.19.x before 1.19.3 has a NULL pointer dereference in kdc/do_tgs_req.c via a FAST inner body that lacks a server field.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-37750
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2021-37750](https://avd.aquasec.com/nvd/cve-2021-37750)
	The Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.5 and 1.19.x before 1.19.3 has a NULL pointer dereference in kdc/do_tgs_req.c via a FAST inner body that lacks a server field.
    </details>



---

Package: libgssapi3-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2018-16860
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-16860
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-16860">https://avd.aquasec.com/nvd/cve-2018-16860</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: S4U2Self with unkeyed checksum
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in samba&amp;#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-16860
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)
	A flaw was found in samba&#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>



---

Package: libgssapi3-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-44758
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-44758
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-44758">https://avd.aquasec.com/nvd/cve-2021-44758</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Denial of service. [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-44758
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)
	Denial of service. [spnego: send_reject when no mech selected]
    </details>



---

Package: libgssapi3-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3116
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3116
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3116">https://avd.aquasec.com/nvd/cve-2022-3116</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3116
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)
	A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>



---

Package: libgssapi3-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3437
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3437
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3437">https://avd.aquasec.com/nvd/cve-2022-3437</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: heap buffer overflow in GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3437
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)
	A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>



---

Package: libgssapi3-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-41916
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.2
Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-41916
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-41916">https://avd.aquasec.com/nvd/cve-2022-41916</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Version ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&amp;#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&amp;#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-41916
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.2
	Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)
	Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>



---

Package: libgssapi3-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-42898
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42898
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42898">https://avd.aquasec.com/nvd/cve-2022-42898</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: integer overflow vulnerabilities in PAC parsing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42898
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)
	A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>



---

Package: libgssapi3-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-44640
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-44640
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-44640">https://avd.aquasec.com/nvd/cve-2022-44640</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-44640
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)
	[Invalid free in ASN.1 codec]
    </details>



---

Package: libhcrypto4-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2018-16860
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-16860
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-16860">https://avd.aquasec.com/nvd/cve-2018-16860</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: S4U2Self with unkeyed checksum
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in samba&amp;#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-16860
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)
	A flaw was found in samba&#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>



---

Package: libhcrypto4-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-44758
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-44758
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-44758">https://avd.aquasec.com/nvd/cve-2021-44758</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Denial of service. [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-44758
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)
	Denial of service. [spnego: send_reject when no mech selected]
    </details>



---

Package: libhcrypto4-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3116
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3116
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3116">https://avd.aquasec.com/nvd/cve-2022-3116</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3116
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)
	A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>



---

Package: libhcrypto4-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3437
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3437
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3437">https://avd.aquasec.com/nvd/cve-2022-3437</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: heap buffer overflow in GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3437
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)
	A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>



---

Package: libhcrypto4-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-41916
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.2
Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-41916
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-41916">https://avd.aquasec.com/nvd/cve-2022-41916</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Version ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&amp;#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&amp;#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-41916
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.2
	Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)
	Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>



---

Package: libhcrypto4-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-42898
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42898
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42898">https://avd.aquasec.com/nvd/cve-2022-42898</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: integer overflow vulnerabilities in PAC parsing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42898
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)
	A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>



---

Package: libhcrypto4-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-44640
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-44640
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-44640">https://avd.aquasec.com/nvd/cve-2022-44640</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-44640
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)
	[Invalid free in ASN.1 codec]
    </details>



---

Package: libheimbase1-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2018-16860
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-16860
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-16860">https://avd.aquasec.com/nvd/cve-2018-16860</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: S4U2Self with unkeyed checksum
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in samba&amp;#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-16860
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)
	A flaw was found in samba&#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>



---

Package: libheimbase1-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-44758
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-44758
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-44758">https://avd.aquasec.com/nvd/cve-2021-44758</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Denial of service. [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-44758
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)
	Denial of service. [spnego: send_reject when no mech selected]
    </details>



---

Package: libheimbase1-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3116
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3116
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3116">https://avd.aquasec.com/nvd/cve-2022-3116</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3116
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)
	A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>



---

Package: libheimbase1-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3437
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3437
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3437">https://avd.aquasec.com/nvd/cve-2022-3437</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: heap buffer overflow in GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3437
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)
	A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>



---

Package: libheimbase1-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-41916
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.2
Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-41916
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-41916">https://avd.aquasec.com/nvd/cve-2022-41916</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Version ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&amp;#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&amp;#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-41916
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.2
	Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)
	Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>



---

Package: libheimbase1-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-42898
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42898
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42898">https://avd.aquasec.com/nvd/cve-2022-42898</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: integer overflow vulnerabilities in PAC parsing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42898
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)
	A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>



---

Package: libheimbase1-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-44640
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-44640
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-44640">https://avd.aquasec.com/nvd/cve-2022-44640</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-44640
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)
	[Invalid free in ASN.1 codec]
    </details>



---

Package: libheimntlm0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2018-16860
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-16860
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-16860">https://avd.aquasec.com/nvd/cve-2018-16860</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: S4U2Self with unkeyed checksum
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in samba&amp;#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-16860
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)
	A flaw was found in samba&#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>



---

Package: libheimntlm0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-44758
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-44758
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-44758">https://avd.aquasec.com/nvd/cve-2021-44758</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Denial of service. [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-44758
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)
	Denial of service. [spnego: send_reject when no mech selected]
    </details>



---

Package: libheimntlm0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3116
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3116
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3116">https://avd.aquasec.com/nvd/cve-2022-3116</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3116
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)
	A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>



---

Package: libheimntlm0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3437
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3437
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3437">https://avd.aquasec.com/nvd/cve-2022-3437</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: heap buffer overflow in GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3437
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)
	A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>



---

Package: libheimntlm0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-41916
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.2
Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-41916
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-41916">https://avd.aquasec.com/nvd/cve-2022-41916</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Version ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&amp;#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&amp;#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-41916
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.2
	Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)
	Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>



---

Package: libheimntlm0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-42898
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42898
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42898">https://avd.aquasec.com/nvd/cve-2022-42898</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: integer overflow vulnerabilities in PAC parsing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42898
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)
	A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>



---

Package: libheimntlm0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-44640
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-44640
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-44640">https://avd.aquasec.com/nvd/cve-2022-44640</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-44640
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)
	[Invalid free in ASN.1 codec]
    </details>



---

Package: libhx509-5-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2018-16860
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-16860
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-16860">https://avd.aquasec.com/nvd/cve-2018-16860</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: S4U2Self with unkeyed checksum
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in samba&amp;#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-16860
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)
	A flaw was found in samba&#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>



---

Package: libhx509-5-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-44758
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-44758
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-44758">https://avd.aquasec.com/nvd/cve-2021-44758</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Denial of service. [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-44758
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)
	Denial of service. [spnego: send_reject when no mech selected]
    </details>



---

Package: libhx509-5-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3116
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3116
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3116">https://avd.aquasec.com/nvd/cve-2022-3116</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3116
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)
	A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>



---

Package: libhx509-5-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3437
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3437
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3437">https://avd.aquasec.com/nvd/cve-2022-3437</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: heap buffer overflow in GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3437
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)
	A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>



---

Package: libhx509-5-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-41916
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.2
Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-41916
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-41916">https://avd.aquasec.com/nvd/cve-2022-41916</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Version ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&amp;#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&amp;#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-41916
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.2
	Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)
	Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>



---

Package: libhx509-5-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-42898
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42898
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42898">https://avd.aquasec.com/nvd/cve-2022-42898</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: integer overflow vulnerabilities in PAC parsing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42898
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)
	A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>



---

Package: libhx509-5-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-44640
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-44640
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-44640">https://avd.aquasec.com/nvd/cve-2022-44640</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-44640
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)
	[Invalid free in ASN.1 codec]
    </details>



---

Package: libitm1
Installed Version: 8.4.0-1ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libjpeg-turbo8
Installed Version: 1.5.2-0ubuntu5.18.04.4
Vulnerability CVE-2020-35538
Severity: MEDIUM
Fixed Version: 1.5.2-0ubuntu5.18.04.6
Link: [CVE-2020-35538](https://avd.aquasec.com/nvd/cve-2020-35538)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-35538
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-35538">https://avd.aquasec.com/nvd/cve-2020-35538</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libjpeg-turbo: Null pointer dereference in jcopy_sample_rows() function
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A crafted input file could cause a null pointer dereference in jcopy_sample_rows() when processed by libjpeg-turbo.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-35538
	Severity: MEDIUM
	Package: libjpeg-turbo8-dev
	Fixed Version: 1.5.2-0ubuntu5.18.04.6
	Link: [CVE-2020-35538](https://avd.aquasec.com/nvd/cve-2020-35538)
	A crafted input file could cause a null pointer dereference in jcopy_sample_rows() when processed by libjpeg-turbo.
    </details>



---

Package: libjpeg-turbo8-dev
Installed Version: 1.5.2-0ubuntu5.18.04.4
Vulnerability CVE-2020-35538
Severity: MEDIUM
Fixed Version: 1.5.2-0ubuntu5.18.04.6
Link: [CVE-2020-35538](https://avd.aquasec.com/nvd/cve-2020-35538)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-35538
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-35538">https://avd.aquasec.com/nvd/cve-2020-35538</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libjpeg-turbo: Null pointer dereference in jcopy_sample_rows() function
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A crafted input file could cause a null pointer dereference in jcopy_sample_rows() when processed by libjpeg-turbo.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-35538
	Severity: MEDIUM
	Package: libjpeg-turbo8-dev
	Fixed Version: 1.5.2-0ubuntu5.18.04.6
	Link: [CVE-2020-35538](https://avd.aquasec.com/nvd/cve-2020-35538)
	A crafted input file could cause a null pointer dereference in jcopy_sample_rows() when processed by libjpeg-turbo.
    </details>



---

Package: libk5crypto3
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2018-20217
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2018-20217](https://avd.aquasec.com/nvd/cve-2018-20217)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-20217
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-20217">https://avd.aquasec.com/nvd/cve-2018-20217</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: Reachable assertion in the KDC using S4U2Self requests
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A Reachable Assertion issue was discovered in the KDC in MIT Kerberos 5 (aka krb5) before 1.17. If an attacker can obtain a krbtgt ticket using an older encryption type (single-DES, triple-DES, or RC4), the attacker can crash the KDC by making an S4U2Self request.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-20217
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2018-20217](https://avd.aquasec.com/nvd/cve-2018-20217)
	A Reachable Assertion issue was discovered in the KDC in MIT Kerberos 5 (aka krb5) before 1.17. If an attacker can obtain a krbtgt ticket using an older encryption type (single-DES, triple-DES, or RC4), the attacker can crash the KDC by making an S4U2Self request.
    </details>



---

Package: libk5crypto3
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2021-36222
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-36222](https://avd.aquasec.com/nvd/cve-2021-36222)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-36222
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-36222">https://avd.aquasec.com/nvd/cve-2021-36222</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: Sending a request containing PA-ENCRYPTED-CHALLENGE padata element without using FAST could result in NULL dereference in KDC which leads to DoS
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ec_verify in kdc/kdc_preauth_ec.c in the Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.4 and 1.19.x before 1.19.2 allows remote attackers to cause a NULL pointer dereference and daemon crash. This occurs because a return value is not properly managed in a certain situation.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-36222
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2021-36222](https://avd.aquasec.com/nvd/cve-2021-36222)
	ec_verify in kdc/kdc_preauth_ec.c in the Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.4 and 1.19.x before 1.19.2 allows remote attackers to cause a NULL pointer dereference and daemon crash. This occurs because a return value is not properly managed in a certain situation.
    </details>



---

Package: libk5crypto3
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2021-37750
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-37750](https://avd.aquasec.com/nvd/cve-2021-37750)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-37750
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-37750">https://avd.aquasec.com/nvd/cve-2021-37750</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: NULL pointer dereference in process_tgs_req() in kdc/do_tgs_req.c via a FAST inner body that lacks server field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.5 and 1.19.x before 1.19.3 has a NULL pointer dereference in kdc/do_tgs_req.c via a FAST inner body that lacks a server field.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-37750
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2021-37750](https://avd.aquasec.com/nvd/cve-2021-37750)
	The Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.5 and 1.19.x before 1.19.3 has a NULL pointer dereference in kdc/do_tgs_req.c via a FAST inner body that lacks a server field.
    </details>



---

Package: libkrb5-26-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2018-16860
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-16860
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-16860">https://avd.aquasec.com/nvd/cve-2018-16860</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: S4U2Self with unkeyed checksum
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in samba&amp;#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-16860
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)
	A flaw was found in samba&#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>



---

Package: libkrb5-26-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-44758
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-44758
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-44758">https://avd.aquasec.com/nvd/cve-2021-44758</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Denial of service. [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-44758
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)
	Denial of service. [spnego: send_reject when no mech selected]
    </details>



---

Package: libkrb5-26-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3116
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3116
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3116">https://avd.aquasec.com/nvd/cve-2022-3116</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3116
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)
	A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>



---

Package: libkrb5-26-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3437
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3437
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3437">https://avd.aquasec.com/nvd/cve-2022-3437</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: heap buffer overflow in GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3437
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)
	A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>



---

Package: libkrb5-26-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-41916
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.2
Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-41916
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-41916">https://avd.aquasec.com/nvd/cve-2022-41916</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Version ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&amp;#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&amp;#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-41916
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.2
	Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)
	Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>



---

Package: libkrb5-26-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-42898
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42898
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42898">https://avd.aquasec.com/nvd/cve-2022-42898</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: integer overflow vulnerabilities in PAC parsing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42898
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)
	A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>



---

Package: libkrb5-26-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-44640
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-44640
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-44640">https://avd.aquasec.com/nvd/cve-2022-44640</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-44640
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)
	[Invalid free in ASN.1 codec]
    </details>



---

Package: libkrb5-3
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2018-20217
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2018-20217](https://avd.aquasec.com/nvd/cve-2018-20217)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-20217
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-20217">https://avd.aquasec.com/nvd/cve-2018-20217</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: Reachable assertion in the KDC using S4U2Self requests
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A Reachable Assertion issue was discovered in the KDC in MIT Kerberos 5 (aka krb5) before 1.17. If an attacker can obtain a krbtgt ticket using an older encryption type (single-DES, triple-DES, or RC4), the attacker can crash the KDC by making an S4U2Self request.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-20217
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2018-20217](https://avd.aquasec.com/nvd/cve-2018-20217)
	A Reachable Assertion issue was discovered in the KDC in MIT Kerberos 5 (aka krb5) before 1.17. If an attacker can obtain a krbtgt ticket using an older encryption type (single-DES, triple-DES, or RC4), the attacker can crash the KDC by making an S4U2Self request.
    </details>



---

Package: libkrb5-3
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2021-36222
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-36222](https://avd.aquasec.com/nvd/cve-2021-36222)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-36222
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-36222">https://avd.aquasec.com/nvd/cve-2021-36222</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: Sending a request containing PA-ENCRYPTED-CHALLENGE padata element without using FAST could result in NULL dereference in KDC which leads to DoS
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ec_verify in kdc/kdc_preauth_ec.c in the Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.4 and 1.19.x before 1.19.2 allows remote attackers to cause a NULL pointer dereference and daemon crash. This occurs because a return value is not properly managed in a certain situation.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-36222
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2021-36222](https://avd.aquasec.com/nvd/cve-2021-36222)
	ec_verify in kdc/kdc_preauth_ec.c in the Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.4 and 1.19.x before 1.19.2 allows remote attackers to cause a NULL pointer dereference and daemon crash. This occurs because a return value is not properly managed in a certain situation.
    </details>



---

Package: libkrb5-3
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2021-37750
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-37750](https://avd.aquasec.com/nvd/cve-2021-37750)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-37750
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-37750">https://avd.aquasec.com/nvd/cve-2021-37750</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: NULL pointer dereference in process_tgs_req() in kdc/do_tgs_req.c via a FAST inner body that lacks server field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.5 and 1.19.x before 1.19.3 has a NULL pointer dereference in kdc/do_tgs_req.c via a FAST inner body that lacks a server field.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-37750
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2021-37750](https://avd.aquasec.com/nvd/cve-2021-37750)
	The Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.5 and 1.19.x before 1.19.3 has a NULL pointer dereference in kdc/do_tgs_req.c via a FAST inner body that lacks a server field.
    </details>



---

Package: libkrb5support0
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2018-20217
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2018-20217](https://avd.aquasec.com/nvd/cve-2018-20217)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-20217
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-20217">https://avd.aquasec.com/nvd/cve-2018-20217</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: Reachable assertion in the KDC using S4U2Self requests
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A Reachable Assertion issue was discovered in the KDC in MIT Kerberos 5 (aka krb5) before 1.17. If an attacker can obtain a krbtgt ticket using an older encryption type (single-DES, triple-DES, or RC4), the attacker can crash the KDC by making an S4U2Self request.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-20217
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2018-20217](https://avd.aquasec.com/nvd/cve-2018-20217)
	A Reachable Assertion issue was discovered in the KDC in MIT Kerberos 5 (aka krb5) before 1.17. If an attacker can obtain a krbtgt ticket using an older encryption type (single-DES, triple-DES, or RC4), the attacker can crash the KDC by making an S4U2Self request.
    </details>



---

Package: libkrb5support0
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2021-36222
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-36222](https://avd.aquasec.com/nvd/cve-2021-36222)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-36222
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-36222">https://avd.aquasec.com/nvd/cve-2021-36222</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: Sending a request containing PA-ENCRYPTED-CHALLENGE padata element without using FAST could result in NULL dereference in KDC which leads to DoS
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ec_verify in kdc/kdc_preauth_ec.c in the Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.4 and 1.19.x before 1.19.2 allows remote attackers to cause a NULL pointer dereference and daemon crash. This occurs because a return value is not properly managed in a certain situation.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-36222
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2021-36222](https://avd.aquasec.com/nvd/cve-2021-36222)
	ec_verify in kdc/kdc_preauth_ec.c in the Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.4 and 1.19.x before 1.19.2 allows remote attackers to cause a NULL pointer dereference and daemon crash. This occurs because a return value is not properly managed in a certain situation.
    </details>



---

Package: libkrb5support0
Installed Version: 1.16-2ubuntu0.2
Vulnerability CVE-2021-37750
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-37750](https://avd.aquasec.com/nvd/cve-2021-37750)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-37750
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-37750">https://avd.aquasec.com/nvd/cve-2021-37750</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: NULL pointer dereference in process_tgs_req() in kdc/do_tgs_req.c via a FAST inner body that lacks server field
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.5 and 1.19.x before 1.19.3 has a NULL pointer dereference in kdc/do_tgs_req.c via a FAST inner body that lacks a server field.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-37750
	Severity: MEDIUM
	Package: libkrb5support0
	Fixed Version: 
	Link: [CVE-2021-37750](https://avd.aquasec.com/nvd/cve-2021-37750)
	The Key Distribution Center (KDC) in MIT Kerberos 5 (aka krb5) before 1.18.5 and 1.19.x before 1.19.3 has a NULL pointer dereference in kdc/do_tgs_req.c via a FAST inner body that lacks a server field.
    </details>



---

Package: liblsan0
Installed Version: 8.4.0-1ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libmpx2
Installed Version: 8.4.0-1ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libnghttp2-14
Installed Version: 1.30.0-1ubuntu1
Vulnerability CVE-2019-9511
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2019-9511](https://avd.aquasec.com/nvd/cve-2019-9511)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-9511
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-9511">https://avd.aquasec.com/nvd/cve-2019-9511</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    HTTP/2: large amount of data requests leads to denial of service
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Some HTTP/2 implementations are vulnerable to window size manipulation and stream prioritization manipulation, potentially leading to a denial of service. The attacker requests a large amount of data from a specified resource over multiple streams. They manipulate window size and stream priority to force the server to queue the data in 1-byte chunks. Depending on how efficiently this data is queued, this can consume excess CPU, memory, or both.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-9511
	Severity: MEDIUM
	Package: libnghttp2-14
	Fixed Version: 
	Link: [CVE-2019-9511](https://avd.aquasec.com/nvd/cve-2019-9511)
	Some HTTP/2 implementations are vulnerable to window size manipulation and stream prioritization manipulation, potentially leading to a denial of service. The attacker requests a large amount of data from a specified resource over multiple streams. They manipulate window size and stream priority to force the server to queue the data in 1-byte chunks. Depending on how efficiently this data is queued, this can consume excess CPU, memory, or both.
    </details>



---

Package: libnghttp2-14
Installed Version: 1.30.0-1ubuntu1
Vulnerability CVE-2019-9513
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2019-9513](https://avd.aquasec.com/nvd/cve-2019-9513)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-9513
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-9513">https://avd.aquasec.com/nvd/cve-2019-9513</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    HTTP/2: flood using PRIORITY frames results in excessive resource consumption
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Some HTTP/2 implementations are vulnerable to resource loops, potentially leading to a denial of service. The attacker creates multiple request streams and continually shuffles the priority of the streams in a way that causes substantial churn to the priority tree. This can consume excess CPU.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-9513
	Severity: MEDIUM
	Package: libnghttp2-14
	Fixed Version: 
	Link: [CVE-2019-9513](https://avd.aquasec.com/nvd/cve-2019-9513)
	Some HTTP/2 implementations are vulnerable to resource loops, potentially leading to a denial of service. The attacker creates multiple request streams and continually shuffles the priority of the streams in a way that causes substantial churn to the priority tree. This can consume excess CPU.
    </details>



---

Package: libperl5.26
Installed Version: 5.26.1-6ubuntu0.5
Vulnerability CVE-2020-16156
Severity: MEDIUM
Fixed Version: 5.26.1-6ubuntu0.6
Link: [CVE-2020-16156](https://avd.aquasec.com/nvd/cve-2020-16156)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-16156
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-16156">https://avd.aquasec.com/nvd/cve-2020-16156</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    perl-CPAN: Bypass of verification of signatures in CHECKSUMS files
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    CPAN 2.28 allows Signature Verification Bypass.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-16156
	Severity: MEDIUM
	Package: perl-modules-5.26
	Fixed Version: 5.26.1-6ubuntu0.6
	Link: [CVE-2020-16156](https://avd.aquasec.com/nvd/cve-2020-16156)
	CPAN 2.28 allows Signature Verification Bypass.
    </details>



---

Package: libpython2.7
Installed Version: 2.7.17-1~18.04ubuntu1.8
Vulnerability CVE-2022-45061
Severity: MEDIUM
Fixed Version: 2.7.17-1~18.04ubuntu1.10
Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-45061
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-45061">https://avd.aquasec.com/nvd/cve-2022-45061</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Python: CPU denial of service via inefficient IDNA decoder
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-45061
	Severity: MEDIUM
	Package: python3.6-minimal
	Fixed Version: 3.6.9-1~18.04ubuntu1.9
	Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)
	An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>



---

Package: libpython2.7-dev
Installed Version: 2.7.17-1~18.04ubuntu1.8
Vulnerability CVE-2022-45061
Severity: MEDIUM
Fixed Version: 2.7.17-1~18.04ubuntu1.10
Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-45061
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-45061">https://avd.aquasec.com/nvd/cve-2022-45061</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Python: CPU denial of service via inefficient IDNA decoder
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-45061
	Severity: MEDIUM
	Package: python3.6-minimal
	Fixed Version: 3.6.9-1~18.04ubuntu1.9
	Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)
	An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>



---

Package: libpython2.7-minimal
Installed Version: 2.7.17-1~18.04ubuntu1.8
Vulnerability CVE-2022-45061
Severity: MEDIUM
Fixed Version: 2.7.17-1~18.04ubuntu1.10
Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-45061
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-45061">https://avd.aquasec.com/nvd/cve-2022-45061</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Python: CPU denial of service via inefficient IDNA decoder
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-45061
	Severity: MEDIUM
	Package: python3.6-minimal
	Fixed Version: 3.6.9-1~18.04ubuntu1.9
	Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)
	An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>



---

Package: libpython2.7-stdlib
Installed Version: 2.7.17-1~18.04ubuntu1.8
Vulnerability CVE-2022-45061
Severity: MEDIUM
Fixed Version: 2.7.17-1~18.04ubuntu1.10
Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-45061
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-45061">https://avd.aquasec.com/nvd/cve-2022-45061</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Python: CPU denial of service via inefficient IDNA decoder
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-45061
	Severity: MEDIUM
	Package: python3.6-minimal
	Fixed Version: 3.6.9-1~18.04ubuntu1.9
	Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)
	An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>



---

Package: libpython3.6
Installed Version: 3.6.9-1~18.04ubuntu1.8
Vulnerability CVE-2022-45061
Severity: MEDIUM
Fixed Version: 3.6.9-1~18.04ubuntu1.9
Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-45061
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-45061">https://avd.aquasec.com/nvd/cve-2022-45061</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Python: CPU denial of service via inefficient IDNA decoder
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-45061
	Severity: MEDIUM
	Package: python3.6-minimal
	Fixed Version: 3.6.9-1~18.04ubuntu1.9
	Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)
	An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>



---

Package: libpython3.6-minimal
Installed Version: 3.6.9-1~18.04ubuntu1.8
Vulnerability CVE-2022-45061
Severity: MEDIUM
Fixed Version: 3.6.9-1~18.04ubuntu1.9
Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-45061
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-45061">https://avd.aquasec.com/nvd/cve-2022-45061</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Python: CPU denial of service via inefficient IDNA decoder
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-45061
	Severity: MEDIUM
	Package: python3.6-minimal
	Fixed Version: 3.6.9-1~18.04ubuntu1.9
	Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)
	An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>



---

Package: libpython3.6-stdlib
Installed Version: 3.6.9-1~18.04ubuntu1.8
Vulnerability CVE-2022-45061
Severity: MEDIUM
Fixed Version: 3.6.9-1~18.04ubuntu1.9
Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-45061
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-45061">https://avd.aquasec.com/nvd/cve-2022-45061</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Python: CPU denial of service via inefficient IDNA decoder
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-45061
	Severity: MEDIUM
	Package: python3.6-minimal
	Fixed Version: 3.6.9-1~18.04ubuntu1.9
	Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)
	An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>



---

Package: libquadmath0
Installed Version: 8.4.0-1ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libroken18-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2018-16860
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-16860
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-16860">https://avd.aquasec.com/nvd/cve-2018-16860</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: S4U2Self with unkeyed checksum
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in samba&amp;#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-16860
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)
	A flaw was found in samba&#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>



---

Package: libroken18-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-44758
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-44758
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-44758">https://avd.aquasec.com/nvd/cve-2021-44758</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Denial of service. [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-44758
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)
	Denial of service. [spnego: send_reject when no mech selected]
    </details>



---

Package: libroken18-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3116
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3116
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3116">https://avd.aquasec.com/nvd/cve-2022-3116</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3116
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)
	A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>



---

Package: libroken18-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3437
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3437
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3437">https://avd.aquasec.com/nvd/cve-2022-3437</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: heap buffer overflow in GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3437
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)
	A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>



---

Package: libroken18-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-41916
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.2
Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-41916
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-41916">https://avd.aquasec.com/nvd/cve-2022-41916</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Version ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&amp;#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&amp;#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-41916
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.2
	Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)
	Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>



---

Package: libroken18-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-42898
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42898
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42898">https://avd.aquasec.com/nvd/cve-2022-42898</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: integer overflow vulnerabilities in PAC parsing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42898
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)
	A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>



---

Package: libroken18-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-44640
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-44640
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-44640">https://avd.aquasec.com/nvd/cve-2022-44640</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-44640
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)
	[Invalid free in ASN.1 codec]
    </details>



---

Package: libsqlite3-0
Installed Version: 3.22.0-1ubuntu0.6
Vulnerability CVE-2022-35737
Severity: MEDIUM
Fixed Version: 3.22.0-1ubuntu0.7
Link: [CVE-2022-35737](https://avd.aquasec.com/nvd/cve-2022-35737)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-35737
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-35737">https://avd.aquasec.com/nvd/cve-2022-35737</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    sqlite: an array-bounds overflow if billions of bytes are used in a string argument to a C API
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    SQLite 1.0.12 through 3.39.x before 3.39.2 sometimes allows an array-bounds overflow if billions of bytes are used in a string argument to a C API.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-35737
	Severity: MEDIUM
	Package: libsqlite3-0
	Fixed Version: 3.22.0-1ubuntu0.7
	Link: [CVE-2022-35737](https://avd.aquasec.com/nvd/cve-2022-35737)
	SQLite 1.0.12 through 3.39.x before 3.39.2 sometimes allows an array-bounds overflow if billions of bytes are used in a string argument to a C API.
    </details>



---

Package: libstdc++-7-dev
Installed Version: 7.5.0-3ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libstdc++6
Installed Version: 8.4.0-1ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libsystemd0
Installed Version: 237-3ubuntu10.53
Vulnerability CVE-2022-2526
Severity: MEDIUM
Fixed Version: 237-3ubuntu10.56
Link: [CVE-2022-2526](https://avd.aquasec.com/nvd/cve-2022-2526)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2526
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2526">https://avd.aquasec.com/nvd/cve-2022-2526</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    systemd-resolved: use-after-free when dealing with DnsStream in resolved-dns-stream.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A use-after-free vulnerability was found in systemd. This issue occurs due to the on_stream_io() function and dns_stream_complete() function in &amp;#39;resolved-dns-stream.c&amp;#39; not incrementing the reference counting for the DnsStream object. Therefore, other functions and callbacks called can dereference the DNSStream object, causing the use-after-free when the reference is still used later.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2526
	Severity: MEDIUM
	Package: libudev1
	Fixed Version: 237-3ubuntu10.56
	Link: [CVE-2022-2526](https://avd.aquasec.com/nvd/cve-2022-2526)
	A use-after-free vulnerability was found in systemd. This issue occurs due to the on_stream_io() function and dns_stream_complete() function in &#39;resolved-dns-stream.c&#39; not incrementing the reference counting for the DnsStream object. Therefore, other functions and callbacks called can dereference the DNSStream object, causing the use-after-free when the reference is still used later.
    </details>



---

Package: libsystemd0
Installed Version: 237-3ubuntu10.53
Vulnerability CVE-2022-3821
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-3821](https://avd.aquasec.com/nvd/cve-2022-3821)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3821
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3821">https://avd.aquasec.com/nvd/cve-2022-3821</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    systemd: buffer overrun in format_timespan() function
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An off-by-one Error issue was discovered in Systemd in format_timespan() function of time-util.c. An attacker could supply specific values for time and accuracy that leads to buffer overrun in format_timespan(), leading to a Denial of Service.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3821
	Severity: MEDIUM
	Package: libudev1
	Fixed Version: 
	Link: [CVE-2022-3821](https://avd.aquasec.com/nvd/cve-2022-3821)
	An off-by-one Error issue was discovered in Systemd in format_timespan() function of time-util.c. An attacker could supply specific values for time and accuracy that leads to buffer overrun in format_timespan(), leading to a Denial of Service.
    </details>



---

Package: libtsan0
Installed Version: 8.4.0-1ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libubsan0
Installed Version: 7.5.0-3ubuntu1~18.04
Vulnerability CVE-2020-13844
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-13844
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-13844">https://avd.aquasec.com/nvd/cve-2020-13844</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ARM straight-line speculation vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &amp;#34;straight-line speculation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-13844
	Severity: MEDIUM
	Package: libubsan0
	Fixed Version: 
	Link: [CVE-2020-13844](https://avd.aquasec.com/nvd/cve-2020-13844)
	Arm Armv8-A core implementations utilizing speculative execution past unconditional changes in control flow may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis, aka &#34;straight-line speculation.&#34;
    </details>



---

Package: libudev1
Installed Version: 237-3ubuntu10.53
Vulnerability CVE-2022-2526
Severity: MEDIUM
Fixed Version: 237-3ubuntu10.56
Link: [CVE-2022-2526](https://avd.aquasec.com/nvd/cve-2022-2526)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2526
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2526">https://avd.aquasec.com/nvd/cve-2022-2526</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    systemd-resolved: use-after-free when dealing with DnsStream in resolved-dns-stream.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A use-after-free vulnerability was found in systemd. This issue occurs due to the on_stream_io() function and dns_stream_complete() function in &amp;#39;resolved-dns-stream.c&amp;#39; not incrementing the reference counting for the DnsStream object. Therefore, other functions and callbacks called can dereference the DNSStream object, causing the use-after-free when the reference is still used later.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2526
	Severity: MEDIUM
	Package: libudev1
	Fixed Version: 237-3ubuntu10.56
	Link: [CVE-2022-2526](https://avd.aquasec.com/nvd/cve-2022-2526)
	A use-after-free vulnerability was found in systemd. This issue occurs due to the on_stream_io() function and dns_stream_complete() function in &#39;resolved-dns-stream.c&#39; not incrementing the reference counting for the DnsStream object. Therefore, other functions and callbacks called can dereference the DNSStream object, causing the use-after-free when the reference is still used later.
    </details>



---

Package: libudev1
Installed Version: 237-3ubuntu10.53
Vulnerability CVE-2022-3821
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-3821](https://avd.aquasec.com/nvd/cve-2022-3821)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3821
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3821">https://avd.aquasec.com/nvd/cve-2022-3821</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    systemd: buffer overrun in format_timespan() function
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An off-by-one Error issue was discovered in Systemd in format_timespan() function of time-util.c. An attacker could supply specific values for time and accuracy that leads to buffer overrun in format_timespan(), leading to a Denial of Service.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3821
	Severity: MEDIUM
	Package: libudev1
	Fixed Version: 
	Link: [CVE-2022-3821](https://avd.aquasec.com/nvd/cve-2022-3821)
	An off-by-one Error issue was discovered in Systemd in format_timespan() function of time-util.c. An attacker could supply specific values for time and accuracy that leads to buffer overrun in format_timespan(), leading to a Denial of Service.
    </details>



---

Package: libwind0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2018-16860
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-16860
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-16860">https://avd.aquasec.com/nvd/cve-2018-16860</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: S4U2Self with unkeyed checksum
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in samba&amp;#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-16860
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2018-16860](https://avd.aquasec.com/nvd/cve-2018-16860)
	A flaw was found in samba&#39;s Heimdal KDC implementation, versions 4.8.x up to, excluding 4.8.12, 4.9.x up to, excluding 4.9.8 and 4.10.x up to, excluding 4.10.3, when used in AD DC mode. A man in the middle attacker could use this flaw to intercept the request to the KDC and replace the user name (principal) in the request with any desired user name (principal) that exists in the KDC effectively obtaining a ticket for that principal.
    </details>



---

Package: libwind0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-44758
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-44758
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-44758">https://avd.aquasec.com/nvd/cve-2021-44758</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Denial of service. [spnego: send_reject when no mech selected]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-44758
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2021-44758](https://avd.aquasec.com/nvd/cve-2021-44758)
	Denial of service. [spnego: send_reject when no mech selected]
    </details>



---

Package: libwind0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3116
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3116
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3116">https://avd.aquasec.com/nvd/cve-2022-3116</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3116
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2022-3116](https://avd.aquasec.com/nvd/cve-2022-3116)
	A flawed logical condition in lib/gssapi/spnego/accept_sec_context.c allows a malicious actor to remotely trigger a NULL pointer dereference using a crafted negTokenInit token.
    </details>



---

Package: libwind0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-3437
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3437
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3437">https://avd.aquasec.com/nvd/cve-2022-3437</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: heap buffer overflow in GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3437
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-3437](https://avd.aquasec.com/nvd/cve-2022-3437)
	A heap-based buffer overflow vulnerability was found in Samba within the GSSAPI unwrap_des() and unwrap_des3() routines of Heimdal. The DES and Triple-DES decryption routines in the Heimdal GSSAPI library allow a length-limited write buffer overflow on malloc() allocated memory when presented with a maliciously small packet. This flaw allows a remote user to send specially crafted malicious data to the application, possibly resulting in a denial of service (DoS) attack.
    </details>



---

Package: libwind0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-41916
Severity: MEDIUM
Fixed Version: 7.5.0+dfsg-1ubuntu0.2
Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-41916
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-41916">https://avd.aquasec.com/nvd/cve-2022-41916</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Version ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&amp;#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&amp;#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-41916
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.2
	Link: [CVE-2022-41916](https://avd.aquasec.com/nvd/cve-2022-41916)
	Heimdal is an implementation of ASN.1/DER, PKIX, and Kerberos. Versions prior to 7.7.1 are vulnerable to a denial of service vulnerability in Heimdal&#39;s PKI certificate validation library, affecting the KDC (via PKINIT) and kinit (via PKINIT), as well as any third-party applications using Heimdal&#39;s libhx509. Users should upgrade to Heimdal 7.7.1 or 7.8. There are no known workarounds for this issue.
    </details>



---

Package: libwind0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-42898
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-42898
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-42898">https://avd.aquasec.com/nvd/cve-2022-42898</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    krb5: integer overflow vulnerabilities in PAC parsing
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-42898
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-42898](https://avd.aquasec.com/nvd/cve-2022-42898)
	A vulnerability was found in MIT krb5. This flaw allows an authenticated attacker to cause a KDC or kadmind process to crash by reading beyond the bounds of allocated memory, creating a denial of service. A privileged attacker may similarly be able to cause a Kerberos or GSS application service to crash.
    </details>



---

Package: libwind0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2022-44640
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-44640
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-44640">https://avd.aquasec.com/nvd/cve-2022-44640</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    [Invalid free in ASN.1 codec]
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-44640
	Severity: MEDIUM
	Package: libwind0-heimdal
	Fixed Version: 
	Link: [CVE-2022-44640](https://avd.aquasec.com/nvd/cve-2022-44640)
	[Invalid free in ASN.1 codec]
    </details>



---

Package: libxml2
Installed Version: 2.9.4+dfsg1-6.1ubuntu1.7
Vulnerability CVE-2022-40303
Severity: MEDIUM
Fixed Version: 2.9.4+dfsg1-6.1ubuntu1.8
Link: [CVE-2022-40303](https://avd.aquasec.com/nvd/cve-2022-40303)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-40303
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-40303">https://avd.aquasec.com/nvd/cve-2022-40303</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libxml2: integer overflows with XML_PARSE_HUGE
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in libxml2 before 2.10.3. When parsing a multi-gigabyte XML document with the XML_PARSE_HUGE parser option enabled, several integer counters can overflow. This results in an attempt to access an array at a negative 2GB offset, typically leading to a segmentation fault.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-40303
	Severity: MEDIUM
	Package: libxml2-dev
	Fixed Version: 2.9.4+dfsg1-6.1ubuntu1.8
	Link: [CVE-2022-40303](https://avd.aquasec.com/nvd/cve-2022-40303)
	An issue was discovered in libxml2 before 2.10.3. When parsing a multi-gigabyte XML document with the XML_PARSE_HUGE parser option enabled, several integer counters can overflow. This results in an attempt to access an array at a negative 2GB offset, typically leading to a segmentation fault.
    </details>



---

Package: libxml2
Installed Version: 2.9.4+dfsg1-6.1ubuntu1.7
Vulnerability CVE-2022-40304
Severity: MEDIUM
Fixed Version: 2.9.4+dfsg1-6.1ubuntu1.8
Link: [CVE-2022-40304](https://avd.aquasec.com/nvd/cve-2022-40304)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-40304
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-40304">https://avd.aquasec.com/nvd/cve-2022-40304</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libxml2: dict corruption caused by entity reference cycles
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in libxml2 before 2.10.3. Certain invalid XML entity definitions can corrupt a hash table key, potentially leading to subsequent logic errors. In one case, a double-free can be provoked.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-40304
	Severity: MEDIUM
	Package: libxml2-dev
	Fixed Version: 2.9.4+dfsg1-6.1ubuntu1.8
	Link: [CVE-2022-40304](https://avd.aquasec.com/nvd/cve-2022-40304)
	An issue was discovered in libxml2 before 2.10.3. Certain invalid XML entity definitions can corrupt a hash table key, potentially leading to subsequent logic errors. In one case, a double-free can be provoked.
    </details>



---

Package: libxml2-dev
Installed Version: 2.9.4+dfsg1-6.1ubuntu1.7
Vulnerability CVE-2022-40303
Severity: MEDIUM
Fixed Version: 2.9.4+dfsg1-6.1ubuntu1.8
Link: [CVE-2022-40303](https://avd.aquasec.com/nvd/cve-2022-40303)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-40303
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-40303">https://avd.aquasec.com/nvd/cve-2022-40303</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libxml2: integer overflows with XML_PARSE_HUGE
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in libxml2 before 2.10.3. When parsing a multi-gigabyte XML document with the XML_PARSE_HUGE parser option enabled, several integer counters can overflow. This results in an attempt to access an array at a negative 2GB offset, typically leading to a segmentation fault.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-40303
	Severity: MEDIUM
	Package: libxml2-dev
	Fixed Version: 2.9.4+dfsg1-6.1ubuntu1.8
	Link: [CVE-2022-40303](https://avd.aquasec.com/nvd/cve-2022-40303)
	An issue was discovered in libxml2 before 2.10.3. When parsing a multi-gigabyte XML document with the XML_PARSE_HUGE parser option enabled, several integer counters can overflow. This results in an attempt to access an array at a negative 2GB offset, typically leading to a segmentation fault.
    </details>



---

Package: libxml2-dev
Installed Version: 2.9.4+dfsg1-6.1ubuntu1.7
Vulnerability CVE-2022-40304
Severity: MEDIUM
Fixed Version: 2.9.4+dfsg1-6.1ubuntu1.8
Link: [CVE-2022-40304](https://avd.aquasec.com/nvd/cve-2022-40304)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-40304
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-40304">https://avd.aquasec.com/nvd/cve-2022-40304</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libxml2: dict corruption caused by entity reference cycles
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in libxml2 before 2.10.3. Certain invalid XML entity definitions can corrupt a hash table key, potentially leading to subsequent logic errors. In one case, a double-free can be provoked.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-40304
	Severity: MEDIUM
	Package: libxml2-dev
	Fixed Version: 2.9.4+dfsg1-6.1ubuntu1.8
	Link: [CVE-2022-40304](https://avd.aquasec.com/nvd/cve-2022-40304)
	An issue was discovered in libxml2 before 2.10.3. Certain invalid XML entity definitions can corrupt a hash table key, potentially leading to subsequent logic errors. In one case, a double-free can be provoked.
    </details>



---

Package: libzmq5
Installed Version: 4.2.5-1ubuntu0.2
Vulnerability CVE-2020-15166
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-15166](https://avd.aquasec.com/nvd/cve-2020-15166)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-15166
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-15166">https://avd.aquasec.com/nvd/cve-2020-15166</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    zeromq: unauthenticated clients causing denial-of-service
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In ZeroMQ before version 4.3.3, there is a denial-of-service vulnerability. Users with TCP transport public endpoints, even with CURVE/ZAP enabled, are impacted. If a raw TCP socket is opened and connected to an endpoint that is fully configured with CURVE/ZAP, legitimate clients will not be able to exchange any message. Handshakes complete successfully, and messages are delivered to the library, but the server application never receives them. This is patched in version 4.3.3.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-15166
	Severity: MEDIUM
	Package: libzmq5
	Fixed Version: 
	Link: [CVE-2020-15166](https://avd.aquasec.com/nvd/cve-2020-15166)
	In ZeroMQ before version 4.3.3, there is a denial-of-service vulnerability. Users with TCP transport public endpoints, even with CURVE/ZAP enabled, are impacted. If a raw TCP socket is opened and connected to an endpoint that is fully configured with CURVE/ZAP, legitimate clients will not be able to exchange any message. Handshakes complete successfully, and messages are delivered to the library, but the server application never receives them. This is patched in version 4.3.3.
    </details>



---

Package: libzmq5
Installed Version: 4.2.5-1ubuntu0.2
Vulnerability CVE-2021-20235
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-20235](https://avd.aquasec.com/nvd/cve-2021-20235)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-20235
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-20235">https://avd.aquasec.com/nvd/cve-2021-20235</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    zeromq: Heap overflow when receiving malformed ZMTP v1 packets
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    There&amp;#39;s a flaw in the zeromq server in versions before 4.3.3 in src/decoder_allocators.hpp. The decoder static allocator could have its sized changed, but the buffer would remain the same as it is a static buffer. A remote, unauthenticated attacker who sends a crafted request to the zeromq server could trigger a buffer overflow WRITE of arbitrary data if CURVE/ZAP authentication is not enabled. The greatest impact of this flaw is to application availability, data integrity, and confidentiality.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-20235
	Severity: MEDIUM
	Package: libzmq5
	Fixed Version: 
	Link: [CVE-2021-20235](https://avd.aquasec.com/nvd/cve-2021-20235)
	There&#39;s a flaw in the zeromq server in versions before 4.3.3 in src/decoder_allocators.hpp. The decoder static allocator could have its sized changed, but the buffer would remain the same as it is a static buffer. A remote, unauthenticated attacker who sends a crafted request to the zeromq server could trigger a buffer overflow WRITE of arbitrary data if CURVE/ZAP authentication is not enabled. The greatest impact of this flaw is to application availability, data integrity, and confidentiality.
    </details>



---

Package: libzmq5
Installed Version: 4.2.5-1ubuntu0.2
Vulnerability CVE-2021-20236
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-20236](https://avd.aquasec.com/nvd/cve-2021-20236)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-20236
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-20236">https://avd.aquasec.com/nvd/cve-2021-20236</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    zeromq: Stack overflow on server running PUB/XPUB socket
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in the ZeroMQ server in versions before 4.3.3. This flaw allows a malicious client to cause a stack buffer overflow on the server by sending crafted topic subscription requests and then unsubscribing. The highest threat from this vulnerability is to confidentiality, integrity, as well as system availability.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-20236
	Severity: MEDIUM
	Package: libzmq5
	Fixed Version: 
	Link: [CVE-2021-20236](https://avd.aquasec.com/nvd/cve-2021-20236)
	A flaw was found in the ZeroMQ server in versions before 4.3.3. This flaw allows a malicious client to cause a stack buffer overflow on the server by sending crafted topic subscription requests and then unsubscribing. The highest threat from this vulnerability is to confidentiality, integrity, as well as system availability.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2013-7445
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2013-7445](https://avd.aquasec.com/nvd/cve-2013-7445)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2013-7445
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2013-7445">https://avd.aquasec.com/nvd/cve-2013-7445</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: memory exhaustion via crafted Graphics Execution Manager (GEM) objects
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Direct Rendering Manager (DRM) subsystem in the Linux kernel through 4.x mishandles requests for Graphics Execution Manager (GEM) objects, which allows context-dependent attackers to cause a denial of service (memory consumption) via an application that processes graphics data, as demonstrated by JavaScript code that creates many CANVAS elements for rendering by Chrome or Firefox.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2013-7445
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2013-7445](https://avd.aquasec.com/nvd/cve-2013-7445)
	The Direct Rendering Manager (DRM) subsystem in the Linux kernel through 4.x mishandles requests for Graphics Execution Manager (GEM) objects, which allows context-dependent attackers to cause a denial of service (memory consumption) via an application that processes graphics data, as demonstrated by JavaScript code that creates many CANVAS elements for rendering by Chrome or Firefox.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2015-8553
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2015-8553](https://avd.aquasec.com/nvd/cve-2015-8553)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2015-8553
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2015-8553">https://avd.aquasec.com/nvd/cve-2015-8553</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    CVE-2015-2150 CVE-2015-8553 xen: non-maskable interrupts triggerable by guests (xsa120)
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Xen allows guest OS users to obtain sensitive information from uninitialized locations in host OS kernel memory by not enabling memory and I/O decoding control bits.  NOTE: this vulnerability exists because of an incomplete fix for CVE-2015-0777.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2015-8553
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2015-8553](https://avd.aquasec.com/nvd/cve-2015-8553)
	Xen allows guest OS users to obtain sensitive information from uninitialized locations in host OS kernel memory by not enabling memory and I/O decoding control bits.  NOTE: this vulnerability exists because of an incomplete fix for CVE-2015-0777.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2016-8660
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2016-8660](https://avd.aquasec.com/nvd/cve-2016-8660)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2016-8660
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2016-8660">https://avd.aquasec.com/nvd/cve-2016-8660</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: xfs: local DoS due to a page lock order bug in the XFS seek hole/data implementation
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The XFS subsystem in the Linux kernel through 4.8.2 allows local users to cause a denial of service (fdatasync failure and system hang) by using the vfs syscall group in the trinity program, related to a &amp;#34;page lock order bug in the XFS seek hole/data implementation.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2016-8660
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2016-8660](https://avd.aquasec.com/nvd/cve-2016-8660)
	The XFS subsystem in the Linux kernel through 4.8.2 allows local users to cause a denial of service (fdatasync failure and system hang) by using the vfs syscall group in the trinity program, related to a &#34;page lock order bug in the XFS seek hole/data implementation.&#34;
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2018-17977
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2018-17977](https://avd.aquasec.com/nvd/cve-2018-17977)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-17977
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-17977">https://avd.aquasec.com/nvd/cve-2018-17977</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: Mishandled interactions among XFRM Netlink messages, IPPROTO_AH packets, and IPPROTO_IP packets resulting in a denial of service
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Linux kernel 4.14.67 mishandles certain interaction among XFRM Netlink messages, IPPROTO_AH packets, and IPPROTO_IP packets, which allows local users to cause a denial of service (memory consumption and system hang) by leveraging root access to execute crafted applications, as demonstrated on CentOS 7.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-17977
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2018-17977](https://avd.aquasec.com/nvd/cve-2018-17977)
	The Linux kernel 4.14.67 mishandles certain interaction among XFRM Netlink messages, IPPROTO_AH packets, and IPPROTO_IP packets, which allows local users to cause a denial of service (memory consumption and system hang) by leveraging root access to execute crafted applications, as demonstrated on CentOS 7.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2020-12362
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-12362](https://avd.aquasec.com/nvd/cve-2020-12362)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-12362
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-12362">https://avd.aquasec.com/nvd/cve-2020-12362</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: Integer overflow in Intel(R) Graphics Drivers
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Integer overflow in the firmware for some Intel(R) Graphics Drivers for Windows * before version 26.20.100.7212 and before Linux kernel version 5.5 may allow a privileged user to potentially enable an escalation of privilege via local access.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-12362
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2020-12362](https://avd.aquasec.com/nvd/cve-2020-12362)
	Integer overflow in the firmware for some Intel(R) Graphics Drivers for Windows * before version 26.20.100.7212 and before Linux kernel version 5.5 may allow a privileged user to potentially enable an escalation of privilege via local access.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2020-26141
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-26141](https://avd.aquasec.com/nvd/cve-2020-26141)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-26141
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-26141">https://avd.aquasec.com/nvd/cve-2020-26141</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: not verifying TKIP MIC of fragmented frames
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in the ALFA Windows 10 driver 6.1316.1209 for AWUS036H. The Wi-Fi implementation does not verify the Message Integrity Check (authenticity) of fragmented TKIP frames. An adversary can abuse this to inject and possibly decrypt packets in WPA or WPA2 networks that support the TKIP data-confidentiality protocol.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-26141
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2020-26141](https://avd.aquasec.com/nvd/cve-2020-26141)
	An issue was discovered in the ALFA Windows 10 driver 6.1316.1209 for AWUS036H. The Wi-Fi implementation does not verify the Message Integrity Check (authenticity) of fragmented TKIP frames. An adversary can abuse this to inject and possibly decrypt packets in WPA or WPA2 networks that support the TKIP data-confidentiality protocol.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2020-26145
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-26145](https://avd.aquasec.com/nvd/cve-2020-26145)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-26145
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-26145">https://avd.aquasec.com/nvd/cve-2020-26145</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: accepting plaintext broadcast fragments as full frames
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered on Samsung Galaxy S3 i9305 4.4.4 devices. The WEP, WPA, WPA2, and WPA3 implementations accept second (or subsequent) broadcast fragments even when sent in plaintext and process them as full unfragmented frames. An adversary can abuse this to inject arbitrary network packets independent of the network configuration.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-26145
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2020-26145](https://avd.aquasec.com/nvd/cve-2020-26145)
	An issue was discovered on Samsung Galaxy S3 i9305 4.4.4 devices. The WEP, WPA, WPA2, and WPA3 implementations accept second (or subsequent) broadcast fragments even when sent in plaintext and process them as full unfragmented frames. An adversary can abuse this to inject arbitrary network packets independent of the network configuration.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2020-26541
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-26541](https://avd.aquasec.com/nvd/cve-2020-26541)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-26541
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-26541">https://avd.aquasec.com/nvd/cve-2020-26541</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: security bypass in certs/blacklist.c and certs/system_keyring.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Linux kernel through 5.8.13 does not properly enforce the Secure Boot Forbidden Signature Database (aka dbx) protection mechanism. This affects certs/blacklist.c and certs/system_keyring.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-26541
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2020-26541](https://avd.aquasec.com/nvd/cve-2020-26541)
	The Linux kernel through 5.8.13 does not properly enforce the Secure Boot Forbidden Signature Database (aka dbx) protection mechanism. This affects certs/blacklist.c and certs/system_keyring.c.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2020-27835
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-27835](https://avd.aquasec.com/nvd/cve-2020-27835)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-27835
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-27835">https://avd.aquasec.com/nvd/cve-2020-27835</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: child process is able to access parent mm through hfi dev file handle
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A use after free in the Linux kernel infiniband hfi1 driver in versions prior to 5.10-rc6 was found in the way user calls Ioctl after open dev file and fork. A local user could use this flaw to crash the system.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-27835
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2020-27835](https://avd.aquasec.com/nvd/cve-2020-27835)
	A use after free in the Linux kernel infiniband hfi1 driver in versions prior to 5.10-rc6 was found in the way user calls Ioctl after open dev file and fork. A local user could use this flaw to crash the system.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2020-36310
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2020-36310](https://avd.aquasec.com/nvd/cve-2020-36310)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-36310
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-36310">https://avd.aquasec.com/nvd/cve-2020-36310</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: infinite loop in set_memory_region_test in arch/x86/kvm/svm/svm.c for certain nested page faults
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in the Linux kernel before 5.8. arch/x86/kvm/svm/svm.c allows a set_memory_region_test infinite loop for certain nested page faults, aka CID-e72436bc3a52.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-36310
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2020-36310](https://avd.aquasec.com/nvd/cve-2020-36310)
	An issue was discovered in the Linux kernel before 5.8. arch/x86/kvm/svm/svm.c allows a set_memory_region_test infinite loop for certain nested page faults, aka CID-e72436bc3a52.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-20320
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-20320](https://avd.aquasec.com/nvd/cve-2021-20320)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-20320
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-20320">https://avd.aquasec.com/nvd/cve-2021-20320</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: s390 eBPF JIT miscompilation issues fixes
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in s390 eBPF JIT in bpf_jit_insn in arch/s390/net/bpf_jit_comp.c in the Linux kernel. In this flaw, a local attacker with special user privilege can circumvent the verifier and may lead to a confidentiality problem.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-20320
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-20320](https://avd.aquasec.com/nvd/cve-2021-20320)
	A flaw was found in s390 eBPF JIT in bpf_jit_insn in arch/s390/net/bpf_jit_comp.c in the Linux kernel. In this flaw, a local attacker with special user privilege can circumvent the verifier and may lead to a confidentiality problem.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-33061
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-33061](https://avd.aquasec.com/nvd/cve-2021-33061)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-33061
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-33061">https://avd.aquasec.com/nvd/cve-2021-33061</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: insufficient control flow management for the Intel(R) 82599 Ethernet Controllers and Adapters may lead to DoS
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Insufficient control flow management for the Intel(R) 82599 Ethernet Controllers and Adapters may allow an authenticated user to potentially enable denial of service via local access.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-33061
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-33061](https://avd.aquasec.com/nvd/cve-2021-33061)
	Insufficient control flow management for the Intel(R) 82599 Ethernet Controllers and Adapters may allow an authenticated user to potentially enable denial of service via local access.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-33624
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-33624](https://avd.aquasec.com/nvd/cve-2021-33624)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-33624
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-33624">https://avd.aquasec.com/nvd/cve-2021-33624</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: Linux kernel BPF protection against speculative execution attacks can be bypassed to read arbitrary kernel memory
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In kernel/bpf/verifier.c in the Linux kernel before 5.12.13, a branch can be mispredicted (e.g., because of type confusion) and consequently an unprivileged BPF program can read arbitrary memory locations via a side-channel attack, aka CID-9183671af6db.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-33624
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-33624](https://avd.aquasec.com/nvd/cve-2021-33624)
	In kernel/bpf/verifier.c in the Linux kernel before 5.12.13, a branch can be mispredicted (e.g., because of type confusion) and consequently an unprivileged BPF program can read arbitrary memory locations via a side-channel attack, aka CID-9183671af6db.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-34556
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-34556](https://avd.aquasec.com/nvd/cve-2021-34556)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-34556
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-34556">https://avd.aquasec.com/nvd/cve-2021-34556</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: BPF program can obtain sensitive information from kernel memory via a speculative store bypass side-channel attack because of the possibility of uninitialized memory locations on the BPF stack
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the Linux kernel through 5.13.7, an unprivileged BPF program can obtain sensitive information from kernel memory via a Speculative Store Bypass side-channel attack because the protection mechanism neglects the possibility of uninitialized memory locations on the BPF stack.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-34556
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-34556](https://avd.aquasec.com/nvd/cve-2021-34556)
	In the Linux kernel through 5.13.7, an unprivileged BPF program can obtain sensitive information from kernel memory via a Speculative Store Bypass side-channel attack because the protection mechanism neglects the possibility of uninitialized memory locations on the BPF stack.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-35477
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-35477](https://avd.aquasec.com/nvd/cve-2021-35477)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-35477
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-35477">https://avd.aquasec.com/nvd/cve-2021-35477</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: BPF program can obtain sensitive information from kernel memory via a speculative store bypass side-channel attack because the technique used by the BPF verifier to manage speculation is unreliable
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the Linux kernel through 5.13.7, an unprivileged BPF program can obtain sensitive information from kernel memory via a Speculative Store Bypass side-channel attack because a certain preempting store operation does not necessarily occur before a store operation that has an attacker-controlled value.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-35477
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-35477](https://avd.aquasec.com/nvd/cve-2021-35477)
	In the Linux kernel through 5.13.7, an unprivileged BPF program can obtain sensitive information from kernel memory via a Speculative Store Bypass side-channel attack because a certain preempting store operation does not necessarily occur before a store operation that has an attacker-controlled value.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-3864
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-3864](https://avd.aquasec.com/nvd/cve-2021-3864)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-3864
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-3864">https://avd.aquasec.com/nvd/cve-2021-3864</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: descendant&amp;#39;s dumpable setting with certain SUID binaries
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in the way the dumpable flag setting was handled when certain SUID binaries executed its descendants. The prerequisite is a SUID binary that sets real UID equal to effective UID, and real GID equal to effective GID. The descendant will then have a dumpable value set to 1. As a result, if the descendant process crashes and core_pattern is set to a relative value, its core dump is stored in the current directory with uid:gid permissions. An unprivileged local user with eligible root SUID binary could use this flaw to place core dumps into root-owned directories, potentially resulting in escalation of privileges.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-3864
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-3864](https://avd.aquasec.com/nvd/cve-2021-3864)
	A flaw was found in the way the dumpable flag setting was handled when certain SUID binaries executed its descendants. The prerequisite is a SUID binary that sets real UID equal to effective UID, and real GID equal to effective GID. The descendant will then have a dumpable value set to 1. As a result, if the descendant process crashes and core_pattern is set to a relative value, its core dump is stored in the current directory with uid:gid permissions. An unprivileged local user with eligible root SUID binary could use this flaw to place core dumps into root-owned directories, potentially resulting in escalation of privileges.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-39800
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-39800](https://avd.aquasec.com/nvd/cve-2021-39800)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-39800
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-39800">https://avd.aquasec.com/nvd/cve-2021-39800</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In ion_ioctl of ion-ioctl.c, there is a possible way to leak kernel head data due to a use after free. This could lead to local information disclosure with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-208277166References: Upstream kernel
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-39800
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-39800](https://avd.aquasec.com/nvd/cve-2021-39800)
	In ion_ioctl of ion-ioctl.c, there is a possible way to leak kernel head data due to a use after free. This could lead to local information disclosure with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-208277166References: Upstream kernel
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-4148
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-4148](https://avd.aquasec.com/nvd/cve-2021-4148)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-4148
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-4148">https://avd.aquasec.com/nvd/cve-2021-4148</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: Improper implementation of block_invalidatepage() allows users to crash the kernel
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in the Linux kernel&amp;#39;s block_invalidatepage in fs/buffer.c in the filesystem. A missing sanity check may allow a local attacker with user privilege to cause a denial of service (DOS) problem.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-4148
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-4148](https://avd.aquasec.com/nvd/cve-2021-4148)
	A vulnerability was found in the Linux kernel&#39;s block_invalidatepage in fs/buffer.c in the filesystem. A missing sanity check may allow a local attacker with user privilege to cause a denial of service (DOS) problem.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-4150
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-4150](https://avd.aquasec.com/nvd/cve-2021-4150)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-4150
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-4150">https://avd.aquasec.com/nvd/cve-2021-4150</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: Block subsystem mishandles reference counts
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A use-after-free flaw was found in the add_partition in block/partitions/core.c in the Linux kernel. A local attacker with user privileges could cause a denial of service on the system. The issue results from the lack of code cleanup when device_add call fails when adding a partition to the disk.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-4150
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-4150](https://avd.aquasec.com/nvd/cve-2021-4150)
	A use-after-free flaw was found in the add_partition in block/partitions/core.c in the Linux kernel. A local attacker with user privileges could cause a denial of service on the system. The issue results from the lack of code cleanup when device_add call fails when adding a partition to the disk.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-4218
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-4218](https://avd.aquasec.com/nvd/cve-2021-4218)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-4218
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-4218">https://avd.aquasec.com/nvd/cve-2021-4218</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: sysctl parameter read causes kernel panic ( rpcrdma module )
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in the Linux kernel’s implementation of reading the SVC RDMA counters. Reading the counter sysctl panics the system. This flaw allows a local attacker with local access to cause a denial of service while the system reboots. The issue is specific to CentOS/RHEL.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-4218
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-4218](https://avd.aquasec.com/nvd/cve-2021-4218)
	A flaw was found in the Linux kernel’s implementation of reading the SVC RDMA counters. Reading the counter sysctl panics the system. This flaw allows a local attacker with local access to cause a denial of service while the system reboots. The issue is specific to CentOS/RHEL.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-44879
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-44879](https://avd.aquasec.com/nvd/cve-2021-44879)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-44879
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-44879">https://avd.aquasec.com/nvd/cve-2021-44879</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: NULL pointer dereference in folio_mark_dirty() via a crafted f2fs image
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In gc_data_segment in fs/f2fs/gc.c in the Linux kernel before 5.16.3, special files are not considered, leading to a move_data_page NULL pointer dereference.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-44879
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-44879](https://avd.aquasec.com/nvd/cve-2021-44879)
	In gc_data_segment in fs/f2fs/gc.c in the Linux kernel before 5.16.3, special files are not considered, leading to a move_data_page NULL pointer dereference.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-0168
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0168](https://avd.aquasec.com/nvd/cve-2022-0168)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0168
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0168">https://avd.aquasec.com/nvd/cve-2022-0168</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: smb2_ioctl_query_info NULL pointer dereference
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A denial of service (DOS) issue was found in the Linux kernel’s smb2_ioctl_query_info function in the fs/cifs/smb2ops.c Common Internet File System (CIFS) due to an incorrect return from the memdup_user function. This flaw allows a local, privileged (CAP_SYS_ADMIN) attacker to crash the system.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0168
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-0168](https://avd.aquasec.com/nvd/cve-2022-0168)
	A denial of service (DOS) issue was found in the Linux kernel’s smb2_ioctl_query_info function in the fs/cifs/smb2ops.c Common Internet File System (CIFS) due to an incorrect return from the memdup_user function. This flaw allows a local, privileged (CAP_SYS_ADMIN) attacker to crash the system.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-0382
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0382](https://avd.aquasec.com/nvd/cve-2022-0382)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0382
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0382">https://avd.aquasec.com/nvd/cve-2022-0382</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: information leak due to uninitialized memory in __tipc_sendmsg() in net/tipc/socket.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An information leak flaw was found due to uninitialized memory in the Linux kernel&amp;#39;s TIPC protocol subsystem, in the way a user sends a TIPC datagram to one or more destinations. This flaw allows a local user to read some kernel memory. This issue is limited to no more than 7 bytes, and the user cannot control what is read. This flaw affects the Linux kernel versions prior to 5.17-rc1.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0382
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-0382](https://avd.aquasec.com/nvd/cve-2022-0382)
	An information leak flaw was found due to uninitialized memory in the Linux kernel&#39;s TIPC protocol subsystem, in the way a user sends a TIPC datagram to one or more destinations. This flaw allows a local user to read some kernel memory. This issue is limited to no more than 7 bytes, and the user cannot control what is read. This flaw affects the Linux kernel versions prior to 5.17-rc1.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-0400
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0400](https://avd.aquasec.com/nvd/cve-2022-0400)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0400
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0400">https://avd.aquasec.com/nvd/cve-2022-0400</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: Out of bounds read in the smc protocol stack
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An out-of-bounds read vulnerability was discovered in linux kernel in the smc protocol stack, causing remote dos.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0400
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-0400](https://avd.aquasec.com/nvd/cve-2022-0400)
	An out-of-bounds read vulnerability was discovered in linux kernel in the smc protocol stack, causing remote dos.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-0480
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0480](https://avd.aquasec.com/nvd/cve-2022-0480)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0480
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0480">https://avd.aquasec.com/nvd/cve-2022-0480</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: memcg does not limit the number of POSIX file locks allowing memory exhaustion
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in the filelock_init in fs/locks.c function in the Linux kernel. This issue can lead to host memory exhaustion due to memcg not limiting the number of Portable Operating System Interface (POSIX) file locks.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0480
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-0480](https://avd.aquasec.com/nvd/cve-2022-0480)
	A flaw was found in the filelock_init in fs/locks.c function in the Linux kernel. This issue can lead to host memory exhaustion due to memcg not limiting the number of Portable Operating System Interface (POSIX) file locks.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-0812
Severity: MEDIUM
Fixed Version: 4.15.0-194.205
Link: [CVE-2022-0812](https://avd.aquasec.com/nvd/cve-2022-0812)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0812
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0812">https://avd.aquasec.com/nvd/cve-2022-0812</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: NFS over RDMA random memory leakage
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An information leak flaw was found in NFS over RDMA in the net/sunrpc/xprtrdma/rpc_rdma.c in the Linux Kernel. This flaw allows an attacker with normal user privileges to leak kernel information.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0812
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-194.205
	Link: [CVE-2022-0812](https://avd.aquasec.com/nvd/cve-2022-0812)
	An information leak flaw was found in NFS over RDMA in the net/sunrpc/xprtrdma/rpc_rdma.c in the Linux Kernel. This flaw allows an attacker with normal user privileges to leak kernel information.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-1012
Severity: MEDIUM
Fixed Version: 4.15.0-194.205
Link: [CVE-2022-1012](https://avd.aquasec.com/nvd/cve-2022-1012)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1012
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1012">https://avd.aquasec.com/nvd/cve-2022-1012</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: Small table perturb size in the TCP source port generation algorithm can lead to information leak
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A memory leak problem was found in the TCP source port generation algorithm in net/ipv4/tcp.c due to the small table perturb size. This flaw may allow an attacker to information leak and may cause a denial of service problem.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1012
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-194.205
	Link: [CVE-2022-1012](https://avd.aquasec.com/nvd/cve-2022-1012)
	A memory leak problem was found in the TCP source port generation algorithm in net/ipv4/tcp.c due to the small table perturb size. This flaw may allow an attacker to information leak and may cause a denial of service problem.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-1263
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1263](https://avd.aquasec.com/nvd/cve-2022-1263)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1263
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1263">https://avd.aquasec.com/nvd/cve-2022-1263</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: KVM: NULL pointer dereference in kvm_dirty_ring_push in virt/kvm/dirty_ring.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A NULL pointer dereference issue was found in KVM when releasing a vCPU with dirty ring support enabled. This flaw allows an unprivileged local attacker on the host to issue specific ioctl calls, causing a kernel oops condition that results in a denial of service.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1263
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-1263](https://avd.aquasec.com/nvd/cve-2022-1263)
	A NULL pointer dereference issue was found in KVM when releasing a vCPU with dirty ring support enabled. This flaw allows an unprivileged local attacker on the host to issue specific ioctl calls, causing a kernel oops condition that results in a denial of service.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-1280
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1280](https://avd.aquasec.com/nvd/cve-2022-1280)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1280
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1280">https://avd.aquasec.com/nvd/cve-2022-1280</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: concurrency use-after-free between drm_setmaster_ioctl and drm_mode_getresources
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A use-after-free vulnerability was found in drm_lease_held in drivers/gpu/drm/drm_lease.c in the Linux kernel due to a race problem. This flaw allows a local user privilege attacker to cause a denial of service (DoS) or a kernel information leak.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1280
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-1280](https://avd.aquasec.com/nvd/cve-2022-1280)
	A use-after-free vulnerability was found in drm_lease_held in drivers/gpu/drm/drm_lease.c in the Linux kernel due to a race problem. This flaw allows a local user privilege attacker to cause a denial of service (DoS) or a kernel information leak.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-1508
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1508](https://avd.aquasec.com/nvd/cve-2022-1508)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1508
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1508">https://avd.aquasec.com/nvd/cve-2022-1508</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: out-of-bounds read in iov_iter_revert() in lib/iov_iter.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An out-of-bounds read flaw was found in the Linux kernel’s io_uring module in the way a user triggers the io_read() function with some special parameters. This flaw allows a local user to read some memory out of bounds.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1508
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-1508](https://avd.aquasec.com/nvd/cve-2022-1508)
	An out-of-bounds read flaw was found in the Linux kernel’s io_uring module in the way a user triggers the io_read() function with some special parameters. This flaw allows a local user to read some memory out of bounds.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-20148
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-20148](https://avd.aquasec.com/nvd/cve-2022-20148)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-20148
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-20148">https://avd.aquasec.com/nvd/cve-2022-20148</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: Use after free in f2fs_available_memory
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In TBD of TBD, there is a possible use-after-free due to a race condition. This could lead to local escalation of privilege in the kernel with System execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-219513976References: Upstream kernel
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-20148
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-20148](https://avd.aquasec.com/nvd/cve-2022-20148)
	In TBD of TBD, there is a possible use-after-free due to a race condition. This could lead to local escalation of privilege in the kernel with System execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-219513976References: Upstream kernel
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-20166
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-20166](https://avd.aquasec.com/nvd/cve-2022-20166)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-20166
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-20166">https://avd.aquasec.com/nvd/cve-2022-20166</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: Fix possible buffer overflow in sysfs reading.
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In various methods of kernel base drivers, there is a possible out of bounds write due to a heap buffer overflow. This could lead to local escalation of privilege with System execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-182388481References: Upstream kernel
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-20166
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-20166](https://avd.aquasec.com/nvd/cve-2022-20166)
	In various methods of kernel base drivers, there is a possible out of bounds write due to a heap buffer overflow. This could lead to local escalation of privilege with System execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-182388481References: Upstream kernel
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-20369
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-20369](https://avd.aquasec.com/nvd/cve-2022-20369)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-20369
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-20369">https://avd.aquasec.com/nvd/cve-2022-20369</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: v4l2-mem2mem: Apply DST_QUEUE_OFF_BASE on MMAP buffers across ioctls
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In v4l2_m2m_querybuf of v4l2-mem2mem.c, there is a possible out of bounds write due to improper input validation. This could lead to local escalation of privilege with System execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-223375145References: Upstream kernel
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-20369
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-20369](https://avd.aquasec.com/nvd/cve-2022-20369)
	In v4l2_m2m_querybuf of v4l2-mem2mem.c, there is a possible out of bounds write due to improper input validation. This could lead to local escalation of privilege with System execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-223375145References: Upstream kernel
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-20422
Severity: MEDIUM
Fixed Version: 4.15.0-197.208
Link: [CVE-2022-20422](https://avd.aquasec.com/nvd/cve-2022-20422)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-20422
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-20422">https://avd.aquasec.com/nvd/cve-2022-20422</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    In emulation_proc_handler of armv8_deprecated.c, there is a possible w ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In emulation_proc_handler of armv8_deprecated.c, there is a possible way to corrupt memory due to a race condition. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-237540956References: Upstream kernel
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-20422
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-197.208
	Link: [CVE-2022-20422](https://avd.aquasec.com/nvd/cve-2022-20422)
	In emulation_proc_handler of armv8_deprecated.c, there is a possible way to corrupt memory due to a race condition. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-237540956References: Upstream kernel
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-2153
Severity: MEDIUM
Fixed Version: 4.15.0-197.208
Link: [CVE-2022-2153](https://avd.aquasec.com/nvd/cve-2022-2153)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2153
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2153">https://avd.aquasec.com/nvd/cve-2022-2153</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: KVM: NULL pointer dereference in kvm_irq_delivery_to_apic_fast()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in the Linux kernel’s KVM when attempting to set a SynIC IRQ. This issue makes it possible for a misbehaving VMM to write to SYNIC/STIMER MSRs, causing a NULL pointer dereference. This flaw allows an unprivileged local attacker on the host to issue specific ioctl calls, causing a kernel oops condition that results in a denial of service.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2153
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-197.208
	Link: [CVE-2022-2153](https://avd.aquasec.com/nvd/cve-2022-2153)
	A flaw was found in the Linux kernel’s KVM when attempting to set a SynIC IRQ. This issue makes it possible for a misbehaving VMM to write to SYNIC/STIMER MSRs, causing a NULL pointer dereference. This flaw allows an unprivileged local attacker on the host to issue specific ioctl calls, causing a kernel oops condition that results in a denial of service.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-23041
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-23041](https://avd.aquasec.com/nvd/cve-2022-23041)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-23041
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-23041">https://avd.aquasec.com/nvd/cve-2022-23041</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Linux PV device frontends vulnerable to attacks by backends T[his CNA  ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Linux PV device frontends vulnerable to attacks by backends T[his CNA information record relates to multiple CVEs; the text explains which aspects/vulnerabilities correspond to which CVE.] Several Linux PV device frontends are using the grant table interfaces for removing access rights of the backends in ways being subject to race conditions, resulting in potential data leaks, data corruption by malicious backends, and denial of service triggered by malicious backends: blkfront, netfront, scsifront and the gntalloc driver are testing whether a grant reference is still in use. If this is not the case, they assume that a following removal of the granted access will always succeed, which is not true in case the backend has mapped the granted page between those two operations. As a result the backend can keep access to the memory page of the guest no matter how the page will be used after the frontend I/O has finished. The xenbus driver has a similar problem, as it doesn&amp;#39;t check the success of removing the granted access of a shared ring buffer. blkfront: CVE-2022-23036 netfront: CVE-2022-23037 scsifront: CVE-2022-23038 gntalloc: CVE-2022-23039 xenbus: CVE-2022-23040 blkfront, netfront, scsifront, usbfront, dmabuf, xenbus, 9p, kbdfront, and pvcalls are using a functionality to delay freeing a grant reference until it is no longer in use, but the freeing of the related data page is not synchronized with dropping the granted access. As a result the backend can keep access to the memory page even after it has been freed and then re-used for a different purpose. CVE-2022-23041 netfront will fail a BUG_ON() assertion if it fails to revoke access in the rx path. This will result in a Denial of Service (DoS) situation of the guest which can be triggered by the backend. CVE-2022-23042
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-23041
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-23041](https://avd.aquasec.com/nvd/cve-2022-23041)
	Linux PV device frontends vulnerable to attacks by backends T[his CNA information record relates to multiple CVEs; the text explains which aspects/vulnerabilities correspond to which CVE.] Several Linux PV device frontends are using the grant table interfaces for removing access rights of the backends in ways being subject to race conditions, resulting in potential data leaks, data corruption by malicious backends, and denial of service triggered by malicious backends: blkfront, netfront, scsifront and the gntalloc driver are testing whether a grant reference is still in use. If this is not the case, they assume that a following removal of the granted access will always succeed, which is not true in case the backend has mapped the granted page between those two operations. As a result the backend can keep access to the memory page of the guest no matter how the page will be used after the frontend I/O has finished. The xenbus driver has a similar problem, as it doesn&#39;t check the success of removing the granted access of a shared ring buffer. blkfront: CVE-2022-23036 netfront: CVE-2022-23037 scsifront: CVE-2022-23038 gntalloc: CVE-2022-23039 xenbus: CVE-2022-23040 blkfront, netfront, scsifront, usbfront, dmabuf, xenbus, 9p, kbdfront, and pvcalls are using a functionality to delay freeing a grant reference until it is no longer in use, but the freeing of the related data page is not synchronized with dropping the granted access. As a result the backend can keep access to the memory page even after it has been freed and then re-used for a different purpose. CVE-2022-23041 netfront will fail a BUG_ON() assertion if it fails to revoke access in the rx path. This will result in a Denial of Service (DoS) situation of the guest which can be triggered by the backend. CVE-2022-23042
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-2318
Severity: MEDIUM
Fixed Version: 4.15.0-194.205
Link: [CVE-2022-2318](https://avd.aquasec.com/nvd/cve-2022-2318)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2318
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2318">https://avd.aquasec.com/nvd/cve-2022-2318</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Kernel: A use-after-free vulnerabilities caused by timer handler in net/rose/rose_timer.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    There are use-after-free vulnerabilities caused by timer handler in net/rose/rose_timer.c of linux that allow attackers to crash linux kernel without any privileges.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2318
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-194.205
	Link: [CVE-2022-2318](https://avd.aquasec.com/nvd/cve-2022-2318)
	There are use-after-free vulnerabilities caused by timer handler in net/rose/rose_timer.c of linux that allow attackers to crash linux kernel without any privileges.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-26365
Severity: MEDIUM
Fixed Version: 4.15.0-194.205
Link: [CVE-2022-26365](https://avd.aquasec.com/nvd/cve-2022-26365)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-26365
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-26365">https://avd.aquasec.com/nvd/cve-2022-26365</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Linux disk/nic frontends data leaks T[his CNA information record relat ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Linux disk/nic frontends data leaks T[his CNA information record relates to multiple CVEs; the text explains which aspects/vulnerabilities correspond to which CVE.] Linux Block and Network PV device frontends don&amp;#39;t zero memory regions before sharing them with the backend (CVE-2022-26365, CVE-2022-33740). Additionally the granularity of the grant table doesn&amp;#39;t allow sharing less than a 4K page, leading to unrelated data residing in the same 4K page as data shared with a backend being accessible by such backend (CVE-2022-33741, CVE-2022-33742).
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-26365
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-194.205
	Link: [CVE-2022-26365](https://avd.aquasec.com/nvd/cve-2022-26365)
	Linux disk/nic frontends data leaks T[his CNA information record relates to multiple CVEs; the text explains which aspects/vulnerabilities correspond to which CVE.] Linux Block and Network PV device frontends don&#39;t zero memory regions before sharing them with the backend (CVE-2022-26365, CVE-2022-33740). Additionally the granularity of the grant table doesn&#39;t allow sharing less than a 4K page, leading to unrelated data residing in the same 4K page as data shared with a backend being accessible by such backend (CVE-2022-33741, CVE-2022-33742).
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-26373
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-26373](https://avd.aquasec.com/nvd/cve-2022-26373)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-26373
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-26373">https://avd.aquasec.com/nvd/cve-2022-26373</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    hw: cpu: Intel: Post-barrier Return Stack Buffer Predictions
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Non-transparent sharing of return predictor targets between contexts in some Intel(R) Processors may allow an authorized user to potentially enable information disclosure via local access.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-26373
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-26373](https://avd.aquasec.com/nvd/cve-2022-26373)
	Non-transparent sharing of return predictor targets between contexts in some Intel(R) Processors may allow an authorized user to potentially enable information disclosure via local access.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-2978
Severity: MEDIUM
Fixed Version: 4.15.0-197.208
Link: [CVE-2022-2978](https://avd.aquasec.com/nvd/cve-2022-2978)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2978
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2978">https://avd.aquasec.com/nvd/cve-2022-2978</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: use-after-free in nilfs_mdt_destroy
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw use after free in the Linux kernel NILFS file system was found in the way user triggers function security_inode_alloc to fail with following call to function nilfs_mdt_destroy. A local user could use this flaw to crash the system or potentially escalate their privileges on the system.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2978
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-197.208
	Link: [CVE-2022-2978](https://avd.aquasec.com/nvd/cve-2022-2978)
	A flaw use after free in the Linux kernel NILFS file system was found in the way user triggers function security_inode_alloc to fail with following call to function nilfs_mdt_destroy. A local user could use this flaw to crash the system or potentially escalate their privileges on the system.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-29900
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-29900](https://avd.aquasec.com/nvd/cve-2022-29900)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-29900
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-29900">https://avd.aquasec.com/nvd/cve-2022-29900</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    CVE-2022-23816 CVE-2022-29900 hw: cpu: AMD: RetBleed Arbitrary Speculative Code Execution with Return Instructions
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Mis-trained branch predictions for return instructions may allow arbitrary speculative code execution under certain microarchitecture-dependent conditions.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-29900
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-29900](https://avd.aquasec.com/nvd/cve-2022-29900)
	Mis-trained branch predictions for return instructions may allow arbitrary speculative code execution under certain microarchitecture-dependent conditions.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-29901
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-29901](https://avd.aquasec.com/nvd/cve-2022-29901)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-29901
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-29901">https://avd.aquasec.com/nvd/cve-2022-29901</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    hw: cpu: Intel: RetBleed Arbitrary Speculative Code Execution with Return Instructions
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Intel microprocessor generations 6 to 8 are affected by a new Spectre variant that is able to bypass their retpoline mitigation in the kernel to leak arbitrary data. An attacker with unprivileged user access can hijack return instructions to achieve arbitrary speculative code execution under certain microarchitecture-dependent conditions.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-29901
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-29901](https://avd.aquasec.com/nvd/cve-2022-29901)
	Intel microprocessor generations 6 to 8 are affected by a new Spectre variant that is able to bypass their retpoline mitigation in the kernel to leak arbitrary data. An attacker with unprivileged user access can hijack return instructions to achieve arbitrary speculative code execution under certain microarchitecture-dependent conditions.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-2991
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2991](https://avd.aquasec.com/nvd/cve-2022-2991)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2991
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2991">https://avd.aquasec.com/nvd/cve-2022-2991</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: heap-based overflow in LightNVM Subsystem may lead to privilege escalation
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A heap-based buffer overflow was found in the Linux kernel&amp;#39;s LightNVM subsystem. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. This vulnerability allows a local attacker to escalate privileges and execute arbitrary code in the context of the kernel. The attacker must first obtain the ability to execute high-privileged code on the target system to exploit this vulnerability.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2991
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-2991](https://avd.aquasec.com/nvd/cve-2022-2991)
	A heap-based buffer overflow was found in the Linux kernel&#39;s LightNVM subsystem. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. This vulnerability allows a local attacker to escalate privileges and execute arbitrary code in the context of the kernel. The attacker must first obtain the ability to execute high-privileged code on the target system to exploit this vulnerability.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-3028
Severity: MEDIUM
Fixed Version: 4.15.0-197.208
Link: [CVE-2022-3028](https://avd.aquasec.com/nvd/cve-2022-3028)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3028
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3028">https://avd.aquasec.com/nvd/cve-2022-3028</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: race condition in xfrm_probe_algs can lead to out-of-bounds read/write
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A race condition was found in the Linux kernel&amp;#39;s IP framework for transforming packets (XFRM subsystem) when multiple calls to xfrm_probe_algs occurred simultaneously. This flaw could allow a local attacker to potentially trigger an out-of-bounds write or leak kernel heap memory by performing an out-of-bounds read and copying it into a socket.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3028
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-197.208
	Link: [CVE-2022-3028](https://avd.aquasec.com/nvd/cve-2022-3028)
	A race condition was found in the Linux kernel&#39;s IP framework for transforming packets (XFRM subsystem) when multiple calls to xfrm_probe_algs occurred simultaneously. This flaw could allow a local attacker to potentially trigger an out-of-bounds write or leak kernel heap memory by performing an out-of-bounds read and copying it into a socket.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-32296
Severity: MEDIUM
Fixed Version: 4.15.0-194.205
Link: [CVE-2022-32296](https://avd.aquasec.com/nvd/cve-2022-32296)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-32296
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-32296">https://avd.aquasec.com/nvd/cve-2022-32296</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: insufficient TCP source port randomness leads to client identification
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Linux kernel before 5.17.9 allows TCP servers to identify clients by observing what source ports are used. This occurs because of use of Algorithm 4 (&amp;#34;Double-Hash Port Selection Algorithm&amp;#34;) of RFC 6056.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-32296
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-194.205
	Link: [CVE-2022-32296](https://avd.aquasec.com/nvd/cve-2022-32296)
	The Linux kernel before 5.17.9 allows TCP servers to identify clients by observing what source ports are used. This occurs because of use of Algorithm 4 (&#34;Double-Hash Port Selection Algorithm&#34;) of RFC 6056.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-3239
Severity: MEDIUM
Fixed Version: 4.15.0-200.211
Link: [CVE-2022-3239](https://avd.aquasec.com/nvd/cve-2022-3239)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3239
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3239">https://avd.aquasec.com/nvd/cve-2022-3239</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Kernel: media: em28xx: initialize refcount before kref_get
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw use after free in the Linux kernel video4linux driver was found in the way user triggers em28xx_usb_probe() for the Empia 28xx based TV cards. A local user could use this flaw to crash the system or potentially escalate their privileges on the system.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3239
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-200.211
	Link: [CVE-2022-3239](https://avd.aquasec.com/nvd/cve-2022-3239)
	A flaw use after free in the Linux kernel video4linux driver was found in the way user triggers em28xx_usb_probe() for the Empia 28xx based TV cards. A local user could use this flaw to crash the system or potentially escalate their privileges on the system.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-33740
Severity: MEDIUM
Fixed Version: 4.15.0-194.205
Link: [CVE-2022-33740](https://avd.aquasec.com/nvd/cve-2022-33740)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-33740
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-33740">https://avd.aquasec.com/nvd/cve-2022-33740</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Linux disk/nic frontends data leaks T[his CNA information record relat ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Linux disk/nic frontends data leaks T[his CNA information record relates to multiple CVEs; the text explains which aspects/vulnerabilities correspond to which CVE.] Linux Block and Network PV device frontends don&amp;#39;t zero memory regions before sharing them with the backend (CVE-2022-26365, CVE-2022-33740). Additionally the granularity of the grant table doesn&amp;#39;t allow sharing less than a 4K page, leading to unrelated data residing in the same 4K page as data shared with a backend being accessible by such backend (CVE-2022-33741, CVE-2022-33742).
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-33740
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-194.205
	Link: [CVE-2022-33740](https://avd.aquasec.com/nvd/cve-2022-33740)
	Linux disk/nic frontends data leaks T[his CNA information record relates to multiple CVEs; the text explains which aspects/vulnerabilities correspond to which CVE.] Linux Block and Network PV device frontends don&#39;t zero memory regions before sharing them with the backend (CVE-2022-26365, CVE-2022-33740). Additionally the granularity of the grant table doesn&#39;t allow sharing less than a 4K page, leading to unrelated data residing in the same 4K page as data shared with a backend being accessible by such backend (CVE-2022-33741, CVE-2022-33742).
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-33741
Severity: MEDIUM
Fixed Version: 4.15.0-194.205
Link: [CVE-2022-33741](https://avd.aquasec.com/nvd/cve-2022-33741)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-33741
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-33741">https://avd.aquasec.com/nvd/cve-2022-33741</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Linux disk/nic frontends data leaks T[his CNA information record relat ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Linux disk/nic frontends data leaks T[his CNA information record relates to multiple CVEs; the text explains which aspects/vulnerabilities correspond to which CVE.] Linux Block and Network PV device frontends don&amp;#39;t zero memory regions before sharing them with the backend (CVE-2022-26365, CVE-2022-33740). Additionally the granularity of the grant table doesn&amp;#39;t allow sharing less than a 4K page, leading to unrelated data residing in the same 4K page as data shared with a backend being accessible by such backend (CVE-2022-33741, CVE-2022-33742).
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-33741
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-194.205
	Link: [CVE-2022-33741](https://avd.aquasec.com/nvd/cve-2022-33741)
	Linux disk/nic frontends data leaks T[his CNA information record relates to multiple CVEs; the text explains which aspects/vulnerabilities correspond to which CVE.] Linux Block and Network PV device frontends don&#39;t zero memory regions before sharing them with the backend (CVE-2022-26365, CVE-2022-33740). Additionally the granularity of the grant table doesn&#39;t allow sharing less than a 4K page, leading to unrelated data residing in the same 4K page as data shared with a backend being accessible by such backend (CVE-2022-33741, CVE-2022-33742).
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-33742
Severity: MEDIUM
Fixed Version: 4.15.0-194.205
Link: [CVE-2022-33742](https://avd.aquasec.com/nvd/cve-2022-33742)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-33742
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-33742">https://avd.aquasec.com/nvd/cve-2022-33742</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Linux disk/nic frontends data leaks T[his CNA information record relat ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Linux disk/nic frontends data leaks T[his CNA information record relates to multiple CVEs; the text explains which aspects/vulnerabilities correspond to which CVE.] Linux Block and Network PV device frontends don&amp;#39;t zero memory regions before sharing them with the backend (CVE-2022-26365, CVE-2022-33740). Additionally the granularity of the grant table doesn&amp;#39;t allow sharing less than a 4K page, leading to unrelated data residing in the same 4K page as data shared with a backend being accessible by such backend (CVE-2022-33741, CVE-2022-33742).
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-33742
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-194.205
	Link: [CVE-2022-33742](https://avd.aquasec.com/nvd/cve-2022-33742)
	Linux disk/nic frontends data leaks T[his CNA information record relates to multiple CVEs; the text explains which aspects/vulnerabilities correspond to which CVE.] Linux Block and Network PV device frontends don&#39;t zero memory regions before sharing them with the backend (CVE-2022-26365, CVE-2022-33740). Additionally the granularity of the grant table doesn&#39;t allow sharing less than a 4K page, leading to unrelated data residing in the same 4K page as data shared with a backend being accessible by such backend (CVE-2022-33741, CVE-2022-33742).
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-33744
Severity: MEDIUM
Fixed Version: 4.15.0-194.205
Link: [CVE-2022-33744](https://avd.aquasec.com/nvd/cve-2022-33744)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-33744
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-33744">https://avd.aquasec.com/nvd/cve-2022-33744</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Arm guests can cause Dom0 DoS via PV devices When mapping pages of gue ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Arm guests can cause Dom0 DoS via PV devices When mapping pages of guests on Arm, dom0 is using an rbtree to keep track of the foreign mappings. Updating of that rbtree is not always done completely with the related lock held, resulting in a small race window, which can be used by unprivileged guests via PV devices to cause inconsistencies of the rbtree. These inconsistencies can lead to Denial of Service (DoS) of dom0, e.g. by causing crashes or the inability to perform further mappings of other guests&amp;#39; memory pages.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-33744
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-194.205
	Link: [CVE-2022-33744](https://avd.aquasec.com/nvd/cve-2022-33744)
	Arm guests can cause Dom0 DoS via PV devices When mapping pages of guests on Arm, dom0 is using an rbtree to keep track of the foreign mappings. Updating of that rbtree is not always done completely with the related lock held, resulting in a small race window, which can be used by unprivileged guests via PV devices to cause inconsistencies of the rbtree. These inconsistencies can lead to Denial of Service (DoS) of dom0, e.g. by causing crashes or the inability to perform further mappings of other guests&#39; memory pages.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-3524
Severity: MEDIUM
Fixed Version: 4.15.0-200.211
Link: [CVE-2022-3524](https://avd.aquasec.com/nvd/cve-2022-3524)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3524
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3524">https://avd.aquasec.com/nvd/cve-2022-3524</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: memory leak in ipv6_renew_options()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in Linux Kernel. It has been declared as problematic. Affected by this vulnerability is the function ipv6_renew_options of the component IPv6 Handler. The manipulation leads to memory leak. The attack can be launched remotely. It is recommended to apply a patch to fix this issue. The identifier VDB-211021 was assigned to this vulnerability.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3524
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-200.211
	Link: [CVE-2022-3524](https://avd.aquasec.com/nvd/cve-2022-3524)
	A vulnerability was found in Linux Kernel. It has been declared as problematic. Affected by this vulnerability is the function ipv6_renew_options of the component IPv6 Handler. The manipulation leads to memory leak. The attack can be launched remotely. It is recommended to apply a patch to fix this issue. The identifier VDB-211021 was assigned to this vulnerability.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-3545
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-3545](https://avd.aquasec.com/nvd/cve-2022-3545)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3545
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3545">https://avd.aquasec.com/nvd/cve-2022-3545</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    A vulnerability has been found in Linux Kernel and classified as criti ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability has been found in Linux Kernel and classified as critical. Affected by this vulnerability is the function area_cache_get of the file drivers/net/ethernet/netronome/nfp/nfpcore/nfp_cppcore.c of the component IPsec. The manipulation leads to use after free. It is recommended to apply a patch to fix this issue. The identifier VDB-211045 was assigned to this vulnerability.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3545
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-3545](https://avd.aquasec.com/nvd/cve-2022-3545)
	A vulnerability has been found in Linux Kernel and classified as critical. Affected by this vulnerability is the function area_cache_get of the file drivers/net/ethernet/netronome/nfp/nfpcore/nfp_cppcore.c of the component IPsec. The manipulation leads to use after free. It is recommended to apply a patch to fix this issue. The identifier VDB-211045 was assigned to this vulnerability.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-3564
Severity: MEDIUM
Fixed Version: 4.15.0-200.211
Link: [CVE-2022-3564](https://avd.aquasec.com/nvd/cve-2022-3564)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3564
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3564">https://avd.aquasec.com/nvd/cve-2022-3564</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: use-after-free caused by l2cap_reassemble_sdu() in net/bluetooth/l2cap_core.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability classified as critical was found in Linux Kernel. Affected by this vulnerability is the function l2cap_reassemble_sdu of the file net/bluetooth/l2cap_core.c of the component Bluetooth. The manipulation leads to use after free. It is recommended to apply a patch to fix this issue. The associated identifier of this vulnerability is VDB-211087.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3564
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-200.211
	Link: [CVE-2022-3564](https://avd.aquasec.com/nvd/cve-2022-3564)
	A vulnerability classified as critical was found in Linux Kernel. Affected by this vulnerability is the function l2cap_reassemble_sdu of the file net/bluetooth/l2cap_core.c of the component Bluetooth. The manipulation leads to use after free. It is recommended to apply a patch to fix this issue. The associated identifier of this vulnerability is VDB-211087.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-3566
Severity: MEDIUM
Fixed Version: 4.15.0-200.211
Link: [CVE-2022-3566](https://avd.aquasec.com/nvd/cve-2022-3566)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3566
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3566">https://avd.aquasec.com/nvd/cve-2022-3566</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: data races around icsk-&amp;gt;icsk_af_ops in do_ipv6_setsockopt
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability, which was classified as problematic, was found in Linux Kernel. This affects the function tcp_getsockopt/tcp_setsockopt of the component TCP Handler. The manipulation leads to race condition. It is recommended to apply a patch to fix this issue. The identifier VDB-211089 was assigned to this vulnerability.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3566
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-200.211
	Link: [CVE-2022-3566](https://avd.aquasec.com/nvd/cve-2022-3566)
	A vulnerability, which was classified as problematic, was found in Linux Kernel. This affects the function tcp_getsockopt/tcp_setsockopt of the component TCP Handler. The manipulation leads to race condition. It is recommended to apply a patch to fix this issue. The identifier VDB-211089 was assigned to this vulnerability.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-3567
Severity: MEDIUM
Fixed Version: 4.15.0-200.211
Link: [CVE-2022-3567](https://avd.aquasec.com/nvd/cve-2022-3567)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3567
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3567">https://avd.aquasec.com/nvd/cve-2022-3567</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: data races around sk-&amp;gt;sk_prot
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability has been found in Linux Kernel and classified as problematic. This vulnerability affects the function inet6_stream_ops/inet6_dgram_ops of the component IPv6 Handler. The manipulation leads to race condition. It is recommended to apply a patch to fix this issue. VDB-211090 is the identifier assigned to this vulnerability.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3567
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-200.211
	Link: [CVE-2022-3567](https://avd.aquasec.com/nvd/cve-2022-3567)
	A vulnerability has been found in Linux Kernel and classified as problematic. This vulnerability affects the function inet6_stream_ops/inet6_dgram_ops of the component IPv6 Handler. The manipulation leads to race condition. It is recommended to apply a patch to fix this issue. VDB-211090 is the identifier assigned to this vulnerability.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-3594
Severity: MEDIUM
Fixed Version: 4.15.0-200.211
Link: [CVE-2022-3594](https://avd.aquasec.com/nvd/cve-2022-3594)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3594
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3594">https://avd.aquasec.com/nvd/cve-2022-3594</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: Rate limit overflow messages in r8152 in intr_callback
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in Linux Kernel. It has been declared as problematic. Affected by this vulnerability is the function intr_callback of the file drivers/net/usb/r8152.c of the component BPF. The manipulation leads to logging of excessive data. The attack can be launched remotely. It is recommended to apply a patch to fix this issue. The associated identifier of this vulnerability is VDB-211363.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3594
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-200.211
	Link: [CVE-2022-3594](https://avd.aquasec.com/nvd/cve-2022-3594)
	A vulnerability was found in Linux Kernel. It has been declared as problematic. Affected by this vulnerability is the function intr_callback of the file drivers/net/usb/r8152.c of the component BPF. The manipulation leads to logging of excessive data. The attack can be launched remotely. It is recommended to apply a patch to fix this issue. The associated identifier of this vulnerability is VDB-211363.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-3635
Severity: MEDIUM
Fixed Version: 4.15.0-197.208
Link: [CVE-2022-3635](https://avd.aquasec.com/nvd/cve-2022-3635)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3635
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3635">https://avd.aquasec.com/nvd/cve-2022-3635</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: use after in tst_timer in drivers/atm/idt77252.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability, which was classified as critical, has been found in Linux Kernel. Affected by this issue is the function tst_timer of the file drivers/atm/idt77252.c of the component IPsec. The manipulation leads to use after free. It is recommended to apply a patch to fix this issue. VDB-211934 is the identifier assigned to this vulnerability.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3635
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-197.208
	Link: [CVE-2022-3635](https://avd.aquasec.com/nvd/cve-2022-3635)
	A vulnerability, which was classified as critical, has been found in Linux Kernel. Affected by this issue is the function tst_timer of the file drivers/atm/idt77252.c of the component IPsec. The manipulation leads to use after free. It is recommended to apply a patch to fix this issue. VDB-211934 is the identifier assigned to this vulnerability.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-3640
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-3640](https://avd.aquasec.com/nvd/cve-2022-3640)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3640
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3640">https://avd.aquasec.com/nvd/cve-2022-3640</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: use after free flaw in l2cap_conn_del in net/bluetooth/l2cap_core.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability, which was classified as critical, was found in Linux Kernel. Affected is the function l2cap_conn_del of the file net/bluetooth/l2cap_core.c of the component Bluetooth. The manipulation leads to use after free. It is recommended to apply a patch to fix this issue. The identifier of this vulnerability is VDB-211944.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3640
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-3640](https://avd.aquasec.com/nvd/cve-2022-3640)
	A vulnerability, which was classified as critical, was found in Linux Kernel. Affected is the function l2cap_conn_del of the file net/bluetooth/l2cap_core.c of the component Bluetooth. The manipulation leads to use after free. It is recommended to apply a patch to fix this issue. The identifier of this vulnerability is VDB-211944.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-3643
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-3643](https://avd.aquasec.com/nvd/cve-2022-3643)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3643
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3643">https://avd.aquasec.com/nvd/cve-2022-3643</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Guests can trigger NIC interface reset/abort/crash via netback It is p ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Guests can trigger NIC interface reset/abort/crash via netback It is possible for a guest to trigger a NIC interface reset/abort/crash in a Linux based network backend by sending certain kinds of packets. It appears to be an (unwritten?) assumption in the rest of the Linux network stack that packet protocol headers are all contained within the linear section of the SKB and some NICs behave badly if this is not the case. This has been reported to occur with Cisco (enic) and Broadcom NetXtrem II BCM5780 (bnx2x) though it may be an issue with other NICs/drivers as well. In case the frontend is sending requests with split headers, netback will forward those violating above mentioned assumption to the networking core, resulting in said misbehavior.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3643
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-3643](https://avd.aquasec.com/nvd/cve-2022-3643)
	Guests can trigger NIC interface reset/abort/crash via netback It is possible for a guest to trigger a NIC interface reset/abort/crash in a Linux based network backend by sending certain kinds of packets. It appears to be an (unwritten?) assumption in the rest of the Linux network stack that packet protocol headers are all contained within the linear section of the SKB and some NICs behave badly if this is not the case. This has been reported to occur with Cisco (enic) and Broadcom NetXtrem II BCM5780 (bnx2x) though it may be an issue with other NICs/drivers as well. In case the frontend is sending requests with split headers, netback will forward those violating above mentioned assumption to the networking core, resulting in said misbehavior.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-36879
Severity: MEDIUM
Fixed Version: 4.15.0-197.208
Link: [CVE-2022-36879](https://avd.aquasec.com/nvd/cve-2022-36879)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-36879
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-36879">https://avd.aquasec.com/nvd/cve-2022-36879</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: xfrm_expand_policies() in net/xfrm/xfrm_policy.c can cause a refcount to be dropped twice
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in the Linux kernel through 5.18.14. xfrm_expand_policies in net/xfrm/xfrm_policy.c can cause a refcount to be dropped twice.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-36879
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-197.208
	Link: [CVE-2022-36879](https://avd.aquasec.com/nvd/cve-2022-36879)
	An issue was discovered in the Linux kernel through 5.18.14. xfrm_expand_policies in net/xfrm/xfrm_policy.c can cause a refcount to be dropped twice.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-39842
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-39842](https://avd.aquasec.com/nvd/cve-2022-39842)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-39842
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-39842">https://avd.aquasec.com/nvd/cve-2022-39842</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Kernel: A type conflict of size_t versus int cause an integer overflow in pxa3xx_gcu_write
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ** DISPUTED ** An issue was discovered in the Linux kernel before 5.19. In pxa3xx_gcu_write in drivers/video/fbdev/pxa3xx-gcu.c, the count parameter has a type conflict of size_t versus int, causing an integer overflow and bypassing the size check. After that, because it is used as the third argument to copy_from_user(), a heap overflow may occur. NOTE: the original discoverer disputes that the overflow can actually happen.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-39842
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-39842](https://avd.aquasec.com/nvd/cve-2022-39842)
	** DISPUTED ** An issue was discovered in the Linux kernel before 5.19. In pxa3xx_gcu_write in drivers/video/fbdev/pxa3xx-gcu.c, the count parameter has a type conflict of size_t versus int, causing an integer overflow and bypassing the size check. After that, because it is used as the third argument to copy_from_user(), a heap overflow may occur. NOTE: the original discoverer disputes that the overflow can actually happen.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-40768
Severity: MEDIUM
Fixed Version: 4.15.0-197.208
Link: [CVE-2022-40768](https://avd.aquasec.com/nvd/cve-2022-40768)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-40768
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-40768">https://avd.aquasec.com/nvd/cve-2022-40768</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: leak of sensitive information due to uninitialized data in stex_queuecommand_lck() in drivers/scsi/stex.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    drivers/scsi/stex.c in the Linux kernel through 5.19.9 allows local users to obtain sensitive information from kernel memory because stex_queuecommand_lck lacks a memset for the PASSTHRU_CMD case.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-40768
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 4.15.0-197.208
	Link: [CVE-2022-40768](https://avd.aquasec.com/nvd/cve-2022-40768)
	drivers/scsi/stex.c in the Linux kernel through 5.19.9 allows local users to obtain sensitive information from kernel memory because stex_queuecommand_lck lacks a memset for the PASSTHRU_CMD case.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-4139
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-4139](https://avd.aquasec.com/nvd/cve-2022-4139)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-4139
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-4139">https://avd.aquasec.com/nvd/cve-2022-4139</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: i915: Incorrect GPU TLB flush can lead to random memory access
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An incorrect TLB flush issue was found in the Linux kernel?s GPU i915 kernel driver, potentially leading to random memory corruption or data leaks. This flaw could allow a local user to crash the system or escalate their privileges on the system.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-4139
	Severity: MEDIUM
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-4139](https://avd.aquasec.com/nvd/cve-2022-4139)
	An incorrect TLB flush issue was found in the Linux kernel?s GPU i915 kernel driver, potentially leading to random memory corruption or data leaks. This flaw could allow a local user to crash the system or escalate their privileges on the system.
    </details>



---

Package: nodejs
Installed Version: 12.22.12-1nodesource1
Vulnerability CVE-2018-12115
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2018-12115](https://avd.aquasec.com/nvd/cve-2018-12115)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-12115
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-12115">https://avd.aquasec.com/nvd/cve-2018-12115</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    nodejs: Out of bounds (OOB) write via UCS-2 encoding
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In all versions of Node.js prior to 6.14.4, 8.11.4 and 10.9.0 when used with UCS-2 encoding (recognized by Node.js under the names `&amp;#39;ucs2&amp;#39;`, `&amp;#39;ucs-2&amp;#39;`, `&amp;#39;utf16le&amp;#39;` and `&amp;#39;utf-16le&amp;#39;`), `Buffer#write()` can be abused to write outside of the bounds of a single `Buffer`. Writes that start from the second-to-last position of a buffer cause a miscalculation of the maximum length of the input bytes to be written.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-12115
	Severity: MEDIUM
	Package: nodejs
	Fixed Version: 
	Link: [CVE-2018-12115](https://avd.aquasec.com/nvd/cve-2018-12115)
	In all versions of Node.js prior to 6.14.4, 8.11.4 and 10.9.0 when used with UCS-2 encoding (recognized by Node.js under the names `&#39;ucs2&#39;`, `&#39;ucs-2&#39;`, `&#39;utf16le&#39;` and `&#39;utf-16le&#39;`), `Buffer#write()` can be abused to write outside of the bounds of a single `Buffer`. Writes that start from the second-to-last position of a buffer cause a miscalculation of the maximum length of the input bytes to be written.
    </details>



---

Package: nodejs
Installed Version: 12.22.12-1nodesource1
Vulnerability CVE-2018-12116
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2018-12116](https://avd.aquasec.com/nvd/cve-2018-12116)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-12116
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-12116">https://avd.aquasec.com/nvd/cve-2018-12116</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    nodejs: HTTP request splitting
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Node.js: All versions prior to Node.js 6.15.0 and 8.14.0: HTTP request splitting: If Node.js can be convinced to use unsanitized user-provided Unicode data for the `path` option of an HTTP request, then data can be provided which will trigger a second, unexpected, and user-defined HTTP request to made to the same server.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-12116
	Severity: MEDIUM
	Package: nodejs
	Fixed Version: 
	Link: [CVE-2018-12116](https://avd.aquasec.com/nvd/cve-2018-12116)
	Node.js: All versions prior to Node.js 6.15.0 and 8.14.0: HTTP request splitting: If Node.js can be convinced to use unsanitized user-provided Unicode data for the `path` option of an HTTP request, then data can be provided which will trigger a second, unexpected, and user-defined HTTP request to made to the same server.
    </details>



---

Package: nodejs
Installed Version: 12.22.12-1nodesource1
Vulnerability CVE-2018-12121
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2018-12121](https://avd.aquasec.com/nvd/cve-2018-12121)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-12121
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-12121">https://avd.aquasec.com/nvd/cve-2018-12121</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    nodejs: Denial of Service with large HTTP headers
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Node.js: All versions prior to Node.js 6.15.0, 8.14.0, 10.14.0 and 11.3.0: Denial of Service with large HTTP headers: By using a combination of many requests with maximum sized headers (almost 80 KB per connection), and carefully timed completion of the headers, it is possible to cause the HTTP server to abort from heap allocation failure. Attack potential is mitigated by the use of a load balancer or other proxy layer.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-12121
	Severity: MEDIUM
	Package: nodejs
	Fixed Version: 
	Link: [CVE-2018-12121](https://avd.aquasec.com/nvd/cve-2018-12121)
	Node.js: All versions prior to Node.js 6.15.0, 8.14.0, 10.14.0 and 11.3.0: Denial of Service with large HTTP headers: By using a combination of many requests with maximum sized headers (almost 80 KB per connection), and carefully timed completion of the headers, it is possible to cause the HTTP server to abort from heap allocation failure. Attack potential is mitigated by the use of a load balancer or other proxy layer.
    </details>



---

Package: nodejs
Installed Version: 12.22.12-1nodesource1
Vulnerability CVE-2018-12122
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2018-12122](https://avd.aquasec.com/nvd/cve-2018-12122)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-12122
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-12122">https://avd.aquasec.com/nvd/cve-2018-12122</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    nodejs: Slowloris HTTP Denial of Service
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Node.js: All versions prior to Node.js 6.15.0, 8.14.0, 10.14.0 and 11.3.0: Slowloris HTTP Denial of Service: An attacker can cause a Denial of Service (DoS) by sending headers very slowly keeping HTTP or HTTPS connections and associated resources alive for a long period of time.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-12122
	Severity: MEDIUM
	Package: nodejs
	Fixed Version: 
	Link: [CVE-2018-12122](https://avd.aquasec.com/nvd/cve-2018-12122)
	Node.js: All versions prior to Node.js 6.15.0, 8.14.0, 10.14.0 and 11.3.0: Slowloris HTTP Denial of Service: An attacker can cause a Denial of Service (DoS) by sending headers very slowly keeping HTTP or HTTPS connections and associated resources alive for a long period of time.
    </details>



---

Package: nodejs
Installed Version: 12.22.12-1nodesource1
Vulnerability CVE-2018-7160
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2018-7160](https://avd.aquasec.com/nvd/cve-2018-7160)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-7160
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-7160">https://avd.aquasec.com/nvd/cve-2018-7160</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    nodejs: Inspector DNS rebinding vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The Node.js inspector, in 6.x and later is vulnerable to a DNS rebinding attack which could be exploited to perform remote code execution. An attack is possible from malicious websites open in a web browser on the same computer, or another computer with network access to the computer running the Node.js process. A malicious website could use a DNS rebinding attack to trick the web browser to bypass same-origin-policy checks and to allow HTTP connections to localhost or to hosts on the local network. If a Node.js process with the debug port active is running on localhost or on a host on the local network, the malicious website could connect to it as a debugger, and get full code execution access.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-7160
	Severity: MEDIUM
	Package: nodejs
	Fixed Version: 
	Link: [CVE-2018-7160](https://avd.aquasec.com/nvd/cve-2018-7160)
	The Node.js inspector, in 6.x and later is vulnerable to a DNS rebinding attack which could be exploited to perform remote code execution. An attack is possible from malicious websites open in a web browser on the same computer, or another computer with network access to the computer running the Node.js process. A malicious website could use a DNS rebinding attack to trick the web browser to bypass same-origin-policy checks and to allow HTTP connections to localhost or to hosts on the local network. If a Node.js process with the debug port active is running on localhost or on a host on the local network, the malicious website could connect to it as a debugger, and get full code execution access.
    </details>



---

Package: nodejs
Installed Version: 12.22.12-1nodesource1
Vulnerability CVE-2018-7167
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2018-7167](https://avd.aquasec.com/nvd/cve-2018-7167)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-7167
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-7167">https://avd.aquasec.com/nvd/cve-2018-7167</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    nodejs: Denial of Service by calling Buffer.fill() or Buffer.alloc() with specially crafted parameters
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Calling Buffer.fill() or Buffer.alloc() with some parameters can lead to a hang which could result in a Denial of Service. In order to address this vulnerability, the implementations of Buffer.alloc() and Buffer.fill() were updated so that they zero fill instead of hanging in these cases. All versions of Node.js 6.x (LTS &amp;#34;Boron&amp;#34;), 8.x (LTS &amp;#34;Carbon&amp;#34;), and 9.x are vulnerable. All versions of Node.js 10.x (Current) are NOT vulnerable.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-7167
	Severity: MEDIUM
	Package: nodejs
	Fixed Version: 
	Link: [CVE-2018-7167](https://avd.aquasec.com/nvd/cve-2018-7167)
	Calling Buffer.fill() or Buffer.alloc() with some parameters can lead to a hang which could result in a Denial of Service. In order to address this vulnerability, the implementations of Buffer.alloc() and Buffer.fill() were updated so that they zero fill instead of hanging in these cases. All versions of Node.js 6.x (LTS &#34;Boron&#34;), 8.x (LTS &#34;Carbon&#34;), and 9.x are vulnerable. All versions of Node.js 10.x (Current) are NOT vulnerable.
    </details>



---

Package: nodejs
Installed Version: 12.22.12-1nodesource1
Vulnerability CVE-2019-5737
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2019-5737](https://avd.aquasec.com/nvd/cve-2019-5737)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-5737
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-5737">https://avd.aquasec.com/nvd/cve-2019-5737</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    nodejs: Insufficient Slowloris fix causing DoS via server.headersTimeout bypass
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In Node.js including 6.x before 6.17.0, 8.x before 8.15.1, 10.x before 10.15.2, and 11.x before 11.10.1, an attacker can cause a Denial of Service (DoS) by establishing an HTTP or HTTPS connection in keep-alive mode and by sending headers very slowly. This keeps the connection and associated resources alive for a long period of time. Potential attacks are mitigated by the use of a load balancer or other proxy layer. This vulnerability is an extension of CVE-2018-12121, addressed in November and impacts all active Node.js release lines including 6.x before 6.17.0, 8.x before 8.15.1, 10.x before 10.15.2, and 11.x before 11.10.1.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-5737
	Severity: MEDIUM
	Package: nodejs
	Fixed Version: 
	Link: [CVE-2019-5737](https://avd.aquasec.com/nvd/cve-2019-5737)
	In Node.js including 6.x before 6.17.0, 8.x before 8.15.1, 10.x before 10.15.2, and 11.x before 11.10.1, an attacker can cause a Denial of Service (DoS) by establishing an HTTP or HTTPS connection in keep-alive mode and by sending headers very slowly. This keeps the connection and associated resources alive for a long period of time. Potential attacks are mitigated by the use of a load balancer or other proxy layer. This vulnerability is an extension of CVE-2018-12121, addressed in November and impacts all active Node.js release lines including 6.x before 6.17.0, 8.x before 8.15.1, 10.x before 10.15.2, and 11.x before 11.10.1.
    </details>



---

Package: nodejs
Installed Version: 12.22.12-1nodesource1
Vulnerability CVE-2022-32212
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-32212](https://avd.aquasec.com/nvd/cve-2022-32212)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-32212
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-32212">https://avd.aquasec.com/nvd/cve-2022-32212</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    nodejs: DNS rebinding in --inspect via invalid IP addresses
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A OS Command Injection vulnerability exists in Node.js versions &amp;lt;14.20.0, &amp;lt;16.16.0, &amp;lt;18.5.0 due to an insufficient IsAllowedHost check that can easily be bypassed because IsIPAddress does not properly check if an IP address is invalid before making DBS requests allowing rebinding attacks.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-32212
	Severity: MEDIUM
	Package: nodejs
	Fixed Version: 
	Link: [CVE-2022-32212](https://avd.aquasec.com/nvd/cve-2022-32212)
	A OS Command Injection vulnerability exists in Node.js versions &lt;14.20.0, &lt;16.16.0, &lt;18.5.0 due to an insufficient IsAllowedHost check that can easily be bypassed because IsIPAddress does not properly check if an IP address is invalid before making DBS requests allowing rebinding attacks.
    </details>



---

Package: perl
Installed Version: 5.26.1-6ubuntu0.5
Vulnerability CVE-2020-16156
Severity: MEDIUM
Fixed Version: 5.26.1-6ubuntu0.6
Link: [CVE-2020-16156](https://avd.aquasec.com/nvd/cve-2020-16156)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-16156
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-16156">https://avd.aquasec.com/nvd/cve-2020-16156</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    perl-CPAN: Bypass of verification of signatures in CHECKSUMS files
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    CPAN 2.28 allows Signature Verification Bypass.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-16156
	Severity: MEDIUM
	Package: perl-modules-5.26
	Fixed Version: 5.26.1-6ubuntu0.6
	Link: [CVE-2020-16156](https://avd.aquasec.com/nvd/cve-2020-16156)
	CPAN 2.28 allows Signature Verification Bypass.
    </details>



---

Package: perl-base
Installed Version: 5.26.1-6ubuntu0.5
Vulnerability CVE-2020-16156
Severity: MEDIUM
Fixed Version: 5.26.1-6ubuntu0.6
Link: [CVE-2020-16156](https://avd.aquasec.com/nvd/cve-2020-16156)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-16156
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-16156">https://avd.aquasec.com/nvd/cve-2020-16156</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    perl-CPAN: Bypass of verification of signatures in CHECKSUMS files
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    CPAN 2.28 allows Signature Verification Bypass.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-16156
	Severity: MEDIUM
	Package: perl-modules-5.26
	Fixed Version: 5.26.1-6ubuntu0.6
	Link: [CVE-2020-16156](https://avd.aquasec.com/nvd/cve-2020-16156)
	CPAN 2.28 allows Signature Verification Bypass.
    </details>



---

Package: perl-modules-5.26
Installed Version: 5.26.1-6ubuntu0.5
Vulnerability CVE-2020-16156
Severity: MEDIUM
Fixed Version: 5.26.1-6ubuntu0.6
Link: [CVE-2020-16156](https://avd.aquasec.com/nvd/cve-2020-16156)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-16156
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-16156">https://avd.aquasec.com/nvd/cve-2020-16156</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    perl-CPAN: Bypass of verification of signatures in CHECKSUMS files
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    CPAN 2.28 allows Signature Verification Bypass.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-16156
	Severity: MEDIUM
	Package: perl-modules-5.26
	Fixed Version: 5.26.1-6ubuntu0.6
	Link: [CVE-2020-16156](https://avd.aquasec.com/nvd/cve-2020-16156)
	CPAN 2.28 allows Signature Verification Bypass.
    </details>



---

Package: python2.7
Installed Version: 2.7.17-1~18.04ubuntu1.8
Vulnerability CVE-2022-45061
Severity: MEDIUM
Fixed Version: 2.7.17-1~18.04ubuntu1.10
Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-45061
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-45061">https://avd.aquasec.com/nvd/cve-2022-45061</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Python: CPU denial of service via inefficient IDNA decoder
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-45061
	Severity: MEDIUM
	Package: python3.6-minimal
	Fixed Version: 3.6.9-1~18.04ubuntu1.9
	Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)
	An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>



---

Package: python2.7-dev
Installed Version: 2.7.17-1~18.04ubuntu1.8
Vulnerability CVE-2022-45061
Severity: MEDIUM
Fixed Version: 2.7.17-1~18.04ubuntu1.10
Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-45061
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-45061">https://avd.aquasec.com/nvd/cve-2022-45061</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Python: CPU denial of service via inefficient IDNA decoder
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-45061
	Severity: MEDIUM
	Package: python3.6-minimal
	Fixed Version: 3.6.9-1~18.04ubuntu1.9
	Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)
	An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>



---

Package: python2.7-minimal
Installed Version: 2.7.17-1~18.04ubuntu1.8
Vulnerability CVE-2022-45061
Severity: MEDIUM
Fixed Version: 2.7.17-1~18.04ubuntu1.10
Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-45061
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-45061">https://avd.aquasec.com/nvd/cve-2022-45061</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Python: CPU denial of service via inefficient IDNA decoder
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-45061
	Severity: MEDIUM
	Package: python3.6-minimal
	Fixed Version: 3.6.9-1~18.04ubuntu1.9
	Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)
	An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>



---

Package: python3.6
Installed Version: 3.6.9-1~18.04ubuntu1.8
Vulnerability CVE-2022-45061
Severity: MEDIUM
Fixed Version: 3.6.9-1~18.04ubuntu1.9
Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-45061
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-45061">https://avd.aquasec.com/nvd/cve-2022-45061</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Python: CPU denial of service via inefficient IDNA decoder
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-45061
	Severity: MEDIUM
	Package: python3.6-minimal
	Fixed Version: 3.6.9-1~18.04ubuntu1.9
	Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)
	An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>



---

Package: python3.6-minimal
Installed Version: 3.6.9-1~18.04ubuntu1.8
Vulnerability CVE-2022-45061
Severity: MEDIUM
Fixed Version: 3.6.9-1~18.04ubuntu1.9
Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-45061
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-45061">https://avd.aquasec.com/nvd/cve-2022-45061</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Python: CPU denial of service via inefficient IDNA decoder
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-45061
	Severity: MEDIUM
	Package: python3.6-minimal
	Fixed Version: 3.6.9-1~18.04ubuntu1.9
	Link: [CVE-2022-45061](https://avd.aquasec.com/nvd/cve-2022-45061)
	An issue was discovered in Python before 3.11.1. An unnecessary quadratic algorithm exists in one path when processing some inputs to the IDNA (RFC 3490) decoder, such that a crafted, unreasonably long name being presented to the decoder could lead to a CPU denial of service. Hostnames are often supplied by remote servers that could be controlled by a malicious actor; in such a scenario, they could trigger excessive CPU consumption on the client attempting to make use of an attacker-supplied supposed hostname. For example, the attack payload could be placed in the Location header of an HTTP response with status code 302. A fix is planned in 3.11.1, 3.10.9, 3.9.16, 3.8.16, and 3.7.16.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2021-4192
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-4192](https://avd.aquasec.com/nvd/cve-2021-4192)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-4192
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-4192">https://avd.aquasec.com/nvd/cve-2021-4192</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in win_linetabsize()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    vim is vulnerable to Use After Free
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-4192
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2021-4192](https://avd.aquasec.com/nvd/cve-2021-4192)
	vim is vulnerable to Use After Free
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0213
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0213](https://avd.aquasec.com/nvd/cve-2022-0213)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0213
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0213">https://avd.aquasec.com/nvd/cve-2022-0213</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: vim is vulnerable to out of bounds read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    vim is vulnerable to Heap-based Buffer Overflow
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0213
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0213](https://avd.aquasec.com/nvd/cve-2022-0213)
	vim is vulnerable to Heap-based Buffer Overflow
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0261
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0261](https://avd.aquasec.com/nvd/cve-2022-0261)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0261
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0261">https://avd.aquasec.com/nvd/cve-2022-0261</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in block_insert() in src/ops.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0261
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0261](https://avd.aquasec.com/nvd/cve-2022-0261)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0318
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0318](https://avd.aquasec.com/nvd/cve-2022-0318)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0318
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0318">https://avd.aquasec.com/nvd/cve-2022-0318</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in utf_head_off() in mbyte.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0318
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0318](https://avd.aquasec.com/nvd/cve-2022-0318)
	Heap-based Buffer Overflow in vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0319
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0319](https://avd.aquasec.com/nvd/cve-2022-0319)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0319
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0319">https://avd.aquasec.com/nvd/cve-2022-0319</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-based out-of-bounds read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0319
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0319](https://avd.aquasec.com/nvd/cve-2022-0319)
	Out-of-bounds Read in vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0351
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0351](https://avd.aquasec.com/nvd/cve-2022-0351)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0351
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0351">https://avd.aquasec.com/nvd/cve-2022-0351</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: access of memory location before start of buffer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Access of Memory Location Before Start of Buffer in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0351
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0351](https://avd.aquasec.com/nvd/cve-2022-0351)
	Access of Memory Location Before Start of Buffer in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0359
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0359](https://avd.aquasec.com/nvd/cve-2022-0359)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0359
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0359">https://avd.aquasec.com/nvd/cve-2022-0359</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in init_ccline() in ex_getln.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0359
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0359](https://avd.aquasec.com/nvd/cve-2022-0359)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0361
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0361](https://avd.aquasec.com/nvd/cve-2022-0361)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0361
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0361">https://avd.aquasec.com/nvd/cve-2022-0361</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Illegal memory access when copying lines in visual mode leads to heap buffer overflow
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0361
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0361](https://avd.aquasec.com/nvd/cve-2022-0361)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0368
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0368](https://avd.aquasec.com/nvd/cve-2022-0368)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0368
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0368">https://avd.aquasec.com/nvd/cve-2022-0368</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Out-of-bounds Read in vim
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0368
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0368](https://avd.aquasec.com/nvd/cve-2022-0368)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0392
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0392](https://avd.aquasec.com/nvd/cve-2022-0392)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0392
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0392">https://avd.aquasec.com/nvd/cve-2022-0392</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in getexmodeline() in ex_getln.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0392
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0392](https://avd.aquasec.com/nvd/cve-2022-0392)
	Heap-based Buffer Overflow in GitHub repository vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0408
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0408](https://avd.aquasec.com/nvd/cve-2022-0408)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0408
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0408">https://avd.aquasec.com/nvd/cve-2022-0408</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Stack-based Buffer Overflow in spellsuggest.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Stack-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0408
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0408](https://avd.aquasec.com/nvd/cve-2022-0408)
	Stack-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0413
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0413](https://avd.aquasec.com/nvd/cve-2022-0413)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0413
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0413">https://avd.aquasec.com/nvd/cve-2022-0413</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use after free in src/ex_cmds.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0413
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0413](https://avd.aquasec.com/nvd/cve-2022-0413)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0554
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0554](https://avd.aquasec.com/nvd/cve-2022-0554)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0554
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0554">https://avd.aquasec.com/nvd/cve-2022-0554</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use of Out-of-range Pointer Offset in vim
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0554
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0554](https://avd.aquasec.com/nvd/cve-2022-0554)
	Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0572
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0572](https://avd.aquasec.com/nvd/cve-2022-0572)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0572
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0572">https://avd.aquasec.com/nvd/cve-2022-0572</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap overflow in ex_retab() may lead to crash
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0572
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0572](https://avd.aquasec.com/nvd/cve-2022-0572)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0685
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0685](https://avd.aquasec.com/nvd/cve-2022-0685)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0685
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0685">https://avd.aquasec.com/nvd/cve-2022-0685</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    : vim: Use of Out-of-range Pointer Offset in vim
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4418.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0685
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0685](https://avd.aquasec.com/nvd/cve-2022-0685)
	Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4418.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0714
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0714](https://avd.aquasec.com/nvd/cve-2022-0714)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0714
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0714">https://avd.aquasec.com/nvd/cve-2022-0714</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer overflow
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4436.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0714
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0714](https://avd.aquasec.com/nvd/cve-2022-0714)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4436.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1629
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1629](https://avd.aquasec.com/nvd/cve-2022-1629)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1629
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1629">https://avd.aquasec.com/nvd/cve-2022-1629</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in function find_next_quote
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in function find_next_quote in GitHub repository vim/vim prior to 8.2.4925. This vulnerabilities are capable of crashing software, Modify Memory, and possible remote execution
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1629
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1629](https://avd.aquasec.com/nvd/cve-2022-1629)
	Buffer Over-read in function find_next_quote in GitHub repository vim/vim prior to 8.2.4925. This vulnerabilities are capable of crashing software, Modify Memory, and possible remote execution
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1674
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1674](https://avd.aquasec.com/nvd/cve-2022-1674)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1674
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1674">https://avd.aquasec.com/nvd/cve-2022-1674</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: NULL pointer dereference in vim_regexec_string() of regexp.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 in GitHub repository vim/vim prior to 8.2.4938. NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 allows attackers to cause a denial of service (application crash) via a crafted input.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1674
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1674](https://avd.aquasec.com/nvd/cve-2022-1674)
	NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 in GitHub repository vim/vim prior to 8.2.4938. NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 allows attackers to cause a denial of service (application crash) via a crafted input.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1720
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1720](https://avd.aquasec.com/nvd/cve-2022-1720)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1720
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1720">https://avd.aquasec.com/nvd/cve-2022-1720</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in grab_file_name() in findfile.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in function grab_file_name in GitHub repository vim/vim prior to 8.2.4956. This vulnerability is capable of crashing the software, memory modification, and possible remote execution.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1720
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1720](https://avd.aquasec.com/nvd/cve-2022-1720)
	Buffer Over-read in function grab_file_name in GitHub repository vim/vim prior to 8.2.4956. This vulnerability is capable of crashing the software, memory modification, and possible remote execution.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1851
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1851](https://avd.aquasec.com/nvd/cve-2022-1851)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1851
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1851">https://avd.aquasec.com/nvd/cve-2022-1851</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bounds read in gchar_cursor() in misc1.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1851
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1851](https://avd.aquasec.com/nvd/cve-2022-1851)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1927
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1927](https://avd.aquasec.com/nvd/cve-2022-1927)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1927
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1927">https://avd.aquasec.com/nvd/cve-2022-1927</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in utf_ptr2char() in mbyte.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1927
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1927](https://avd.aquasec.com/nvd/cve-2022-1927)
	Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1942
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1942](https://avd.aquasec.com/nvd/cve-2022-1942)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1942
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1942">https://avd.aquasec.com/nvd/cve-2022-1942</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out of bounds write in vim_regsub_both()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1942
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1942](https://avd.aquasec.com/nvd/cve-2022-1942)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1968
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1968](https://avd.aquasec.com/nvd/cve-2022-1968)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1968
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1968">https://avd.aquasec.com/nvd/cve-2022-1968</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in function utf_ptr2char at mbyte.c:1794
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1968
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1968](https://avd.aquasec.com/nvd/cve-2022-1968)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2175
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2175](https://avd.aquasec.com/nvd/cve-2022-2175)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2175
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2175">https://avd.aquasec.com/nvd/cve-2022-2175</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in put_on_cmdline() at ex_getln.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2175
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2175](https://avd.aquasec.com/nvd/cve-2022-2175)
	Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2183
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2183](https://avd.aquasec.com/nvd/cve-2022-2183)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2183
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2183">https://avd.aquasec.com/nvd/cve-2022-2183</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bounds read through get_lisp_indent() in function get_lisp_indent
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2183
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2183](https://avd.aquasec.com/nvd/cve-2022-2183)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2304
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2304](https://avd.aquasec.com/nvd/cve-2022-2304)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2304
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2304">https://avd.aquasec.com/nvd/cve-2022-2304</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: stack buffer overflow in spell_dump_compl() at spell.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Stack-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2304
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2304](https://avd.aquasec.com/nvd/cve-2022-2304)
	Stack-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2343
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2343](https://avd.aquasec.com/nvd/cve-2022-2343)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2343
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2343">https://avd.aquasec.com/nvd/cve-2022-2343</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-based buffer overflow in ins_compl_add() in insexpand.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.0044.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2343
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2343](https://avd.aquasec.com/nvd/cve-2022-2343)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.0044.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2345
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2345](https://avd.aquasec.com/nvd/cve-2022-2345)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2345
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2345">https://avd.aquasec.com/nvd/cve-2022-2345</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in skipwhite() in charset.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 9.0.0046.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2345
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2345](https://avd.aquasec.com/nvd/cve-2022-2345)
	Use After Free in GitHub repository vim/vim prior to 9.0.0046.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2923
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2923](https://avd.aquasec.com/nvd/cve-2022-2923)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2923
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2923">https://avd.aquasec.com/nvd/cve-2022-2923</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: null pointer dereference in function sug_filltree
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    NULL Pointer Dereference in GitHub repository vim/vim prior to 9.0.0240.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2923
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2923](https://avd.aquasec.com/nvd/cve-2022-2923)
	NULL Pointer Dereference in GitHub repository vim/vim prior to 9.0.0240.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2946
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2946](https://avd.aquasec.com/nvd/cve-2022-2946)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2946
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2946">https://avd.aquasec.com/nvd/cve-2022-2946</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use after free in function vim_vsnprintf_typval
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 9.0.0246.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2946
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2946](https://avd.aquasec.com/nvd/cve-2022-2946)
	Use After Free in GitHub repository vim/vim prior to 9.0.0246.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2021-4192
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-4192](https://avd.aquasec.com/nvd/cve-2021-4192)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-4192
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-4192">https://avd.aquasec.com/nvd/cve-2021-4192</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in win_linetabsize()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    vim is vulnerable to Use After Free
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-4192
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2021-4192](https://avd.aquasec.com/nvd/cve-2021-4192)
	vim is vulnerable to Use After Free
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0213
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0213](https://avd.aquasec.com/nvd/cve-2022-0213)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0213
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0213">https://avd.aquasec.com/nvd/cve-2022-0213</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: vim is vulnerable to out of bounds read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    vim is vulnerable to Heap-based Buffer Overflow
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0213
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0213](https://avd.aquasec.com/nvd/cve-2022-0213)
	vim is vulnerable to Heap-based Buffer Overflow
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0261
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0261](https://avd.aquasec.com/nvd/cve-2022-0261)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0261
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0261">https://avd.aquasec.com/nvd/cve-2022-0261</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in block_insert() in src/ops.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0261
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0261](https://avd.aquasec.com/nvd/cve-2022-0261)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0318
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0318](https://avd.aquasec.com/nvd/cve-2022-0318)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0318
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0318">https://avd.aquasec.com/nvd/cve-2022-0318</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in utf_head_off() in mbyte.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0318
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0318](https://avd.aquasec.com/nvd/cve-2022-0318)
	Heap-based Buffer Overflow in vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0319
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0319](https://avd.aquasec.com/nvd/cve-2022-0319)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0319
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0319">https://avd.aquasec.com/nvd/cve-2022-0319</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-based out-of-bounds read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0319
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0319](https://avd.aquasec.com/nvd/cve-2022-0319)
	Out-of-bounds Read in vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0351
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0351](https://avd.aquasec.com/nvd/cve-2022-0351)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0351
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0351">https://avd.aquasec.com/nvd/cve-2022-0351</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: access of memory location before start of buffer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Access of Memory Location Before Start of Buffer in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0351
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0351](https://avd.aquasec.com/nvd/cve-2022-0351)
	Access of Memory Location Before Start of Buffer in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0359
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0359](https://avd.aquasec.com/nvd/cve-2022-0359)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0359
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0359">https://avd.aquasec.com/nvd/cve-2022-0359</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in init_ccline() in ex_getln.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0359
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0359](https://avd.aquasec.com/nvd/cve-2022-0359)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0361
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0361](https://avd.aquasec.com/nvd/cve-2022-0361)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0361
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0361">https://avd.aquasec.com/nvd/cve-2022-0361</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Illegal memory access when copying lines in visual mode leads to heap buffer overflow
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0361
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0361](https://avd.aquasec.com/nvd/cve-2022-0361)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0368
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0368](https://avd.aquasec.com/nvd/cve-2022-0368)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0368
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0368">https://avd.aquasec.com/nvd/cve-2022-0368</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Out-of-bounds Read in vim
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0368
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0368](https://avd.aquasec.com/nvd/cve-2022-0368)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0392
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0392](https://avd.aquasec.com/nvd/cve-2022-0392)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0392
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0392">https://avd.aquasec.com/nvd/cve-2022-0392</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in getexmodeline() in ex_getln.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0392
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0392](https://avd.aquasec.com/nvd/cve-2022-0392)
	Heap-based Buffer Overflow in GitHub repository vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0408
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0408](https://avd.aquasec.com/nvd/cve-2022-0408)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0408
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0408">https://avd.aquasec.com/nvd/cve-2022-0408</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Stack-based Buffer Overflow in spellsuggest.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Stack-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0408
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0408](https://avd.aquasec.com/nvd/cve-2022-0408)
	Stack-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0413
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0413](https://avd.aquasec.com/nvd/cve-2022-0413)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0413
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0413">https://avd.aquasec.com/nvd/cve-2022-0413</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use after free in src/ex_cmds.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0413
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0413](https://avd.aquasec.com/nvd/cve-2022-0413)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0554
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0554](https://avd.aquasec.com/nvd/cve-2022-0554)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0554
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0554">https://avd.aquasec.com/nvd/cve-2022-0554</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use of Out-of-range Pointer Offset in vim
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0554
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0554](https://avd.aquasec.com/nvd/cve-2022-0554)
	Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0572
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0572](https://avd.aquasec.com/nvd/cve-2022-0572)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0572
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0572">https://avd.aquasec.com/nvd/cve-2022-0572</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap overflow in ex_retab() may lead to crash
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0572
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0572](https://avd.aquasec.com/nvd/cve-2022-0572)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0685
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0685](https://avd.aquasec.com/nvd/cve-2022-0685)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0685
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0685">https://avd.aquasec.com/nvd/cve-2022-0685</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    : vim: Use of Out-of-range Pointer Offset in vim
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4418.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0685
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0685](https://avd.aquasec.com/nvd/cve-2022-0685)
	Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4418.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0714
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0714](https://avd.aquasec.com/nvd/cve-2022-0714)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0714
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0714">https://avd.aquasec.com/nvd/cve-2022-0714</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer overflow
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4436.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0714
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0714](https://avd.aquasec.com/nvd/cve-2022-0714)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4436.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1629
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1629](https://avd.aquasec.com/nvd/cve-2022-1629)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1629
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1629">https://avd.aquasec.com/nvd/cve-2022-1629</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in function find_next_quote
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in function find_next_quote in GitHub repository vim/vim prior to 8.2.4925. This vulnerabilities are capable of crashing software, Modify Memory, and possible remote execution
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1629
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1629](https://avd.aquasec.com/nvd/cve-2022-1629)
	Buffer Over-read in function find_next_quote in GitHub repository vim/vim prior to 8.2.4925. This vulnerabilities are capable of crashing software, Modify Memory, and possible remote execution
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1674
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1674](https://avd.aquasec.com/nvd/cve-2022-1674)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1674
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1674">https://avd.aquasec.com/nvd/cve-2022-1674</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: NULL pointer dereference in vim_regexec_string() of regexp.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 in GitHub repository vim/vim prior to 8.2.4938. NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 allows attackers to cause a denial of service (application crash) via a crafted input.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1674
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1674](https://avd.aquasec.com/nvd/cve-2022-1674)
	NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 in GitHub repository vim/vim prior to 8.2.4938. NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 allows attackers to cause a denial of service (application crash) via a crafted input.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1720
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1720](https://avd.aquasec.com/nvd/cve-2022-1720)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1720
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1720">https://avd.aquasec.com/nvd/cve-2022-1720</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in grab_file_name() in findfile.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in function grab_file_name in GitHub repository vim/vim prior to 8.2.4956. This vulnerability is capable of crashing the software, memory modification, and possible remote execution.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1720
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1720](https://avd.aquasec.com/nvd/cve-2022-1720)
	Buffer Over-read in function grab_file_name in GitHub repository vim/vim prior to 8.2.4956. This vulnerability is capable of crashing the software, memory modification, and possible remote execution.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1851
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1851](https://avd.aquasec.com/nvd/cve-2022-1851)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1851
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1851">https://avd.aquasec.com/nvd/cve-2022-1851</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bounds read in gchar_cursor() in misc1.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1851
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1851](https://avd.aquasec.com/nvd/cve-2022-1851)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1927
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1927](https://avd.aquasec.com/nvd/cve-2022-1927)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1927
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1927">https://avd.aquasec.com/nvd/cve-2022-1927</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in utf_ptr2char() in mbyte.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1927
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1927](https://avd.aquasec.com/nvd/cve-2022-1927)
	Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1942
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1942](https://avd.aquasec.com/nvd/cve-2022-1942)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1942
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1942">https://avd.aquasec.com/nvd/cve-2022-1942</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out of bounds write in vim_regsub_both()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1942
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1942](https://avd.aquasec.com/nvd/cve-2022-1942)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1968
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1968](https://avd.aquasec.com/nvd/cve-2022-1968)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1968
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1968">https://avd.aquasec.com/nvd/cve-2022-1968</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in function utf_ptr2char at mbyte.c:1794
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1968
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1968](https://avd.aquasec.com/nvd/cve-2022-1968)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2175
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2175](https://avd.aquasec.com/nvd/cve-2022-2175)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2175
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2175">https://avd.aquasec.com/nvd/cve-2022-2175</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in put_on_cmdline() at ex_getln.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2175
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2175](https://avd.aquasec.com/nvd/cve-2022-2175)
	Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2183
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2183](https://avd.aquasec.com/nvd/cve-2022-2183)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2183
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2183">https://avd.aquasec.com/nvd/cve-2022-2183</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bounds read through get_lisp_indent() in function get_lisp_indent
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2183
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2183](https://avd.aquasec.com/nvd/cve-2022-2183)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2304
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2304](https://avd.aquasec.com/nvd/cve-2022-2304)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2304
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2304">https://avd.aquasec.com/nvd/cve-2022-2304</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: stack buffer overflow in spell_dump_compl() at spell.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Stack-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2304
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2304](https://avd.aquasec.com/nvd/cve-2022-2304)
	Stack-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2343
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2343](https://avd.aquasec.com/nvd/cve-2022-2343)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2343
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2343">https://avd.aquasec.com/nvd/cve-2022-2343</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-based buffer overflow in ins_compl_add() in insexpand.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.0044.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2343
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2343](https://avd.aquasec.com/nvd/cve-2022-2343)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.0044.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2345
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2345](https://avd.aquasec.com/nvd/cve-2022-2345)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2345
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2345">https://avd.aquasec.com/nvd/cve-2022-2345</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in skipwhite() in charset.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 9.0.0046.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2345
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2345](https://avd.aquasec.com/nvd/cve-2022-2345)
	Use After Free in GitHub repository vim/vim prior to 9.0.0046.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2923
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2923](https://avd.aquasec.com/nvd/cve-2022-2923)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2923
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2923">https://avd.aquasec.com/nvd/cve-2022-2923</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: null pointer dereference in function sug_filltree
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    NULL Pointer Dereference in GitHub repository vim/vim prior to 9.0.0240.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2923
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2923](https://avd.aquasec.com/nvd/cve-2022-2923)
	NULL Pointer Dereference in GitHub repository vim/vim prior to 9.0.0240.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2946
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2946](https://avd.aquasec.com/nvd/cve-2022-2946)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2946
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2946">https://avd.aquasec.com/nvd/cve-2022-2946</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use after free in function vim_vsnprintf_typval
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 9.0.0246.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2946
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2946](https://avd.aquasec.com/nvd/cve-2022-2946)
	Use After Free in GitHub repository vim/vim prior to 9.0.0246.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2021-4192
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-4192](https://avd.aquasec.com/nvd/cve-2021-4192)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-4192
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-4192">https://avd.aquasec.com/nvd/cve-2021-4192</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in win_linetabsize()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    vim is vulnerable to Use After Free
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-4192
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2021-4192](https://avd.aquasec.com/nvd/cve-2021-4192)
	vim is vulnerable to Use After Free
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0213
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0213](https://avd.aquasec.com/nvd/cve-2022-0213)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0213
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0213">https://avd.aquasec.com/nvd/cve-2022-0213</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: vim is vulnerable to out of bounds read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    vim is vulnerable to Heap-based Buffer Overflow
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0213
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0213](https://avd.aquasec.com/nvd/cve-2022-0213)
	vim is vulnerable to Heap-based Buffer Overflow
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0261
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0261](https://avd.aquasec.com/nvd/cve-2022-0261)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0261
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0261">https://avd.aquasec.com/nvd/cve-2022-0261</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in block_insert() in src/ops.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0261
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0261](https://avd.aquasec.com/nvd/cve-2022-0261)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0318
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0318](https://avd.aquasec.com/nvd/cve-2022-0318)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0318
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0318">https://avd.aquasec.com/nvd/cve-2022-0318</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in utf_head_off() in mbyte.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0318
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0318](https://avd.aquasec.com/nvd/cve-2022-0318)
	Heap-based Buffer Overflow in vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0319
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0319](https://avd.aquasec.com/nvd/cve-2022-0319)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0319
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0319">https://avd.aquasec.com/nvd/cve-2022-0319</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-based out-of-bounds read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0319
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0319](https://avd.aquasec.com/nvd/cve-2022-0319)
	Out-of-bounds Read in vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0351
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0351](https://avd.aquasec.com/nvd/cve-2022-0351)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0351
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0351">https://avd.aquasec.com/nvd/cve-2022-0351</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: access of memory location before start of buffer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Access of Memory Location Before Start of Buffer in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0351
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0351](https://avd.aquasec.com/nvd/cve-2022-0351)
	Access of Memory Location Before Start of Buffer in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0359
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0359](https://avd.aquasec.com/nvd/cve-2022-0359)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0359
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0359">https://avd.aquasec.com/nvd/cve-2022-0359</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in init_ccline() in ex_getln.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0359
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0359](https://avd.aquasec.com/nvd/cve-2022-0359)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0361
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0361](https://avd.aquasec.com/nvd/cve-2022-0361)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0361
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0361">https://avd.aquasec.com/nvd/cve-2022-0361</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Illegal memory access when copying lines in visual mode leads to heap buffer overflow
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0361
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0361](https://avd.aquasec.com/nvd/cve-2022-0361)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0368
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0368](https://avd.aquasec.com/nvd/cve-2022-0368)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0368
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0368">https://avd.aquasec.com/nvd/cve-2022-0368</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Out-of-bounds Read in vim
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0368
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0368](https://avd.aquasec.com/nvd/cve-2022-0368)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0392
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0392](https://avd.aquasec.com/nvd/cve-2022-0392)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0392
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0392">https://avd.aquasec.com/nvd/cve-2022-0392</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in getexmodeline() in ex_getln.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0392
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0392](https://avd.aquasec.com/nvd/cve-2022-0392)
	Heap-based Buffer Overflow in GitHub repository vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0408
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0408](https://avd.aquasec.com/nvd/cve-2022-0408)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0408
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0408">https://avd.aquasec.com/nvd/cve-2022-0408</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Stack-based Buffer Overflow in spellsuggest.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Stack-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0408
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0408](https://avd.aquasec.com/nvd/cve-2022-0408)
	Stack-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0413
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0413](https://avd.aquasec.com/nvd/cve-2022-0413)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0413
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0413">https://avd.aquasec.com/nvd/cve-2022-0413</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use after free in src/ex_cmds.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0413
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0413](https://avd.aquasec.com/nvd/cve-2022-0413)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0554
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0554](https://avd.aquasec.com/nvd/cve-2022-0554)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0554
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0554">https://avd.aquasec.com/nvd/cve-2022-0554</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use of Out-of-range Pointer Offset in vim
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0554
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0554](https://avd.aquasec.com/nvd/cve-2022-0554)
	Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0572
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0572](https://avd.aquasec.com/nvd/cve-2022-0572)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0572
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0572">https://avd.aquasec.com/nvd/cve-2022-0572</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap overflow in ex_retab() may lead to crash
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0572
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0572](https://avd.aquasec.com/nvd/cve-2022-0572)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0685
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0685](https://avd.aquasec.com/nvd/cve-2022-0685)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0685
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0685">https://avd.aquasec.com/nvd/cve-2022-0685</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    : vim: Use of Out-of-range Pointer Offset in vim
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4418.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0685
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0685](https://avd.aquasec.com/nvd/cve-2022-0685)
	Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4418.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0714
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0714](https://avd.aquasec.com/nvd/cve-2022-0714)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0714
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0714">https://avd.aquasec.com/nvd/cve-2022-0714</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer overflow
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4436.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0714
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0714](https://avd.aquasec.com/nvd/cve-2022-0714)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4436.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1629
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1629](https://avd.aquasec.com/nvd/cve-2022-1629)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1629
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1629">https://avd.aquasec.com/nvd/cve-2022-1629</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in function find_next_quote
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in function find_next_quote in GitHub repository vim/vim prior to 8.2.4925. This vulnerabilities are capable of crashing software, Modify Memory, and possible remote execution
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1629
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1629](https://avd.aquasec.com/nvd/cve-2022-1629)
	Buffer Over-read in function find_next_quote in GitHub repository vim/vim prior to 8.2.4925. This vulnerabilities are capable of crashing software, Modify Memory, and possible remote execution
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1674
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1674](https://avd.aquasec.com/nvd/cve-2022-1674)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1674
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1674">https://avd.aquasec.com/nvd/cve-2022-1674</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: NULL pointer dereference in vim_regexec_string() of regexp.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 in GitHub repository vim/vim prior to 8.2.4938. NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 allows attackers to cause a denial of service (application crash) via a crafted input.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1674
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1674](https://avd.aquasec.com/nvd/cve-2022-1674)
	NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 in GitHub repository vim/vim prior to 8.2.4938. NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 allows attackers to cause a denial of service (application crash) via a crafted input.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1720
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1720](https://avd.aquasec.com/nvd/cve-2022-1720)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1720
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1720">https://avd.aquasec.com/nvd/cve-2022-1720</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in grab_file_name() in findfile.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in function grab_file_name in GitHub repository vim/vim prior to 8.2.4956. This vulnerability is capable of crashing the software, memory modification, and possible remote execution.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1720
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1720](https://avd.aquasec.com/nvd/cve-2022-1720)
	Buffer Over-read in function grab_file_name in GitHub repository vim/vim prior to 8.2.4956. This vulnerability is capable of crashing the software, memory modification, and possible remote execution.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1851
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1851](https://avd.aquasec.com/nvd/cve-2022-1851)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1851
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1851">https://avd.aquasec.com/nvd/cve-2022-1851</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bounds read in gchar_cursor() in misc1.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1851
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1851](https://avd.aquasec.com/nvd/cve-2022-1851)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1927
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1927](https://avd.aquasec.com/nvd/cve-2022-1927)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1927
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1927">https://avd.aquasec.com/nvd/cve-2022-1927</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in utf_ptr2char() in mbyte.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1927
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1927](https://avd.aquasec.com/nvd/cve-2022-1927)
	Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1942
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1942](https://avd.aquasec.com/nvd/cve-2022-1942)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1942
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1942">https://avd.aquasec.com/nvd/cve-2022-1942</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out of bounds write in vim_regsub_both()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1942
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1942](https://avd.aquasec.com/nvd/cve-2022-1942)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1968
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1968](https://avd.aquasec.com/nvd/cve-2022-1968)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1968
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1968">https://avd.aquasec.com/nvd/cve-2022-1968</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in function utf_ptr2char at mbyte.c:1794
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1968
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1968](https://avd.aquasec.com/nvd/cve-2022-1968)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2175
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2175](https://avd.aquasec.com/nvd/cve-2022-2175)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2175
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2175">https://avd.aquasec.com/nvd/cve-2022-2175</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in put_on_cmdline() at ex_getln.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2175
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2175](https://avd.aquasec.com/nvd/cve-2022-2175)
	Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2183
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2183](https://avd.aquasec.com/nvd/cve-2022-2183)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2183
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2183">https://avd.aquasec.com/nvd/cve-2022-2183</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bounds read through get_lisp_indent() in function get_lisp_indent
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2183
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2183](https://avd.aquasec.com/nvd/cve-2022-2183)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2304
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2304](https://avd.aquasec.com/nvd/cve-2022-2304)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2304
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2304">https://avd.aquasec.com/nvd/cve-2022-2304</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: stack buffer overflow in spell_dump_compl() at spell.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Stack-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2304
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2304](https://avd.aquasec.com/nvd/cve-2022-2304)
	Stack-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2343
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2343](https://avd.aquasec.com/nvd/cve-2022-2343)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2343
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2343">https://avd.aquasec.com/nvd/cve-2022-2343</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-based buffer overflow in ins_compl_add() in insexpand.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.0044.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2343
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2343](https://avd.aquasec.com/nvd/cve-2022-2343)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.0044.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2345
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2345](https://avd.aquasec.com/nvd/cve-2022-2345)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2345
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2345">https://avd.aquasec.com/nvd/cve-2022-2345</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in skipwhite() in charset.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 9.0.0046.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2345
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2345](https://avd.aquasec.com/nvd/cve-2022-2345)
	Use After Free in GitHub repository vim/vim prior to 9.0.0046.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2923
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2923](https://avd.aquasec.com/nvd/cve-2022-2923)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2923
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2923">https://avd.aquasec.com/nvd/cve-2022-2923</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: null pointer dereference in function sug_filltree
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    NULL Pointer Dereference in GitHub repository vim/vim prior to 9.0.0240.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2923
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2923](https://avd.aquasec.com/nvd/cve-2022-2923)
	NULL Pointer Dereference in GitHub repository vim/vim prior to 9.0.0240.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2946
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2946](https://avd.aquasec.com/nvd/cve-2022-2946)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2946
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2946">https://avd.aquasec.com/nvd/cve-2022-2946</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use after free in function vim_vsnprintf_typval
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 9.0.0246.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2946
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2946](https://avd.aquasec.com/nvd/cve-2022-2946)
	Use After Free in GitHub repository vim/vim prior to 9.0.0246.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2021-4192
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2021-4192](https://avd.aquasec.com/nvd/cve-2021-4192)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-4192
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-4192">https://avd.aquasec.com/nvd/cve-2021-4192</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in win_linetabsize()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    vim is vulnerable to Use After Free
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-4192
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2021-4192](https://avd.aquasec.com/nvd/cve-2021-4192)
	vim is vulnerable to Use After Free
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0213
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0213](https://avd.aquasec.com/nvd/cve-2022-0213)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0213
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0213">https://avd.aquasec.com/nvd/cve-2022-0213</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: vim is vulnerable to out of bounds read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    vim is vulnerable to Heap-based Buffer Overflow
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0213
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0213](https://avd.aquasec.com/nvd/cve-2022-0213)
	vim is vulnerable to Heap-based Buffer Overflow
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0261
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0261](https://avd.aquasec.com/nvd/cve-2022-0261)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0261
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0261">https://avd.aquasec.com/nvd/cve-2022-0261</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in block_insert() in src/ops.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0261
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0261](https://avd.aquasec.com/nvd/cve-2022-0261)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0318
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0318](https://avd.aquasec.com/nvd/cve-2022-0318)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0318
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0318">https://avd.aquasec.com/nvd/cve-2022-0318</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in utf_head_off() in mbyte.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0318
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0318](https://avd.aquasec.com/nvd/cve-2022-0318)
	Heap-based Buffer Overflow in vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0319
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0319](https://avd.aquasec.com/nvd/cve-2022-0319)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0319
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0319">https://avd.aquasec.com/nvd/cve-2022-0319</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-based out-of-bounds read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0319
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0319](https://avd.aquasec.com/nvd/cve-2022-0319)
	Out-of-bounds Read in vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0351
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0351](https://avd.aquasec.com/nvd/cve-2022-0351)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0351
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0351">https://avd.aquasec.com/nvd/cve-2022-0351</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: access of memory location before start of buffer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Access of Memory Location Before Start of Buffer in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0351
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0351](https://avd.aquasec.com/nvd/cve-2022-0351)
	Access of Memory Location Before Start of Buffer in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0359
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0359](https://avd.aquasec.com/nvd/cve-2022-0359)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0359
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0359">https://avd.aquasec.com/nvd/cve-2022-0359</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in init_ccline() in ex_getln.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0359
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0359](https://avd.aquasec.com/nvd/cve-2022-0359)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0361
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0361](https://avd.aquasec.com/nvd/cve-2022-0361)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0361
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0361">https://avd.aquasec.com/nvd/cve-2022-0361</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Illegal memory access when copying lines in visual mode leads to heap buffer overflow
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0361
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0361](https://avd.aquasec.com/nvd/cve-2022-0361)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0368
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0368](https://avd.aquasec.com/nvd/cve-2022-0368)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0368
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0368">https://avd.aquasec.com/nvd/cve-2022-0368</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Out-of-bounds Read in vim
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0368
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0368](https://avd.aquasec.com/nvd/cve-2022-0368)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0392
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0392](https://avd.aquasec.com/nvd/cve-2022-0392)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0392
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0392">https://avd.aquasec.com/nvd/cve-2022-0392</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based buffer overflow in getexmodeline() in ex_getln.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0392
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0392](https://avd.aquasec.com/nvd/cve-2022-0392)
	Heap-based Buffer Overflow in GitHub repository vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0408
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0408](https://avd.aquasec.com/nvd/cve-2022-0408)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0408
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0408">https://avd.aquasec.com/nvd/cve-2022-0408</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Stack-based Buffer Overflow in spellsuggest.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Stack-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0408
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0408](https://avd.aquasec.com/nvd/cve-2022-0408)
	Stack-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0413
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0413](https://avd.aquasec.com/nvd/cve-2022-0413)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0413
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0413">https://avd.aquasec.com/nvd/cve-2022-0413</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use after free in src/ex_cmds.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0413
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0413](https://avd.aquasec.com/nvd/cve-2022-0413)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0554
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0554](https://avd.aquasec.com/nvd/cve-2022-0554)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0554
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0554">https://avd.aquasec.com/nvd/cve-2022-0554</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use of Out-of-range Pointer Offset in vim
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0554
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0554](https://avd.aquasec.com/nvd/cve-2022-0554)
	Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0572
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0572](https://avd.aquasec.com/nvd/cve-2022-0572)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0572
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0572">https://avd.aquasec.com/nvd/cve-2022-0572</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap overflow in ex_retab() may lead to crash
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0572
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0572](https://avd.aquasec.com/nvd/cve-2022-0572)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0685
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0685](https://avd.aquasec.com/nvd/cve-2022-0685)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0685
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0685">https://avd.aquasec.com/nvd/cve-2022-0685</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    : vim: Use of Out-of-range Pointer Offset in vim
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4418.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0685
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0685](https://avd.aquasec.com/nvd/cve-2022-0685)
	Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4418.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0714
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-0714](https://avd.aquasec.com/nvd/cve-2022-0714)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0714
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0714">https://avd.aquasec.com/nvd/cve-2022-0714</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer overflow
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4436.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0714
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0714](https://avd.aquasec.com/nvd/cve-2022-0714)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4436.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1629
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1629](https://avd.aquasec.com/nvd/cve-2022-1629)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1629
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1629">https://avd.aquasec.com/nvd/cve-2022-1629</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in function find_next_quote
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in function find_next_quote in GitHub repository vim/vim prior to 8.2.4925. This vulnerabilities are capable of crashing software, Modify Memory, and possible remote execution
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1629
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1629](https://avd.aquasec.com/nvd/cve-2022-1629)
	Buffer Over-read in function find_next_quote in GitHub repository vim/vim prior to 8.2.4925. This vulnerabilities are capable of crashing software, Modify Memory, and possible remote execution
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1674
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1674](https://avd.aquasec.com/nvd/cve-2022-1674)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1674
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1674">https://avd.aquasec.com/nvd/cve-2022-1674</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: NULL pointer dereference in vim_regexec_string() of regexp.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 in GitHub repository vim/vim prior to 8.2.4938. NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 allows attackers to cause a denial of service (application crash) via a crafted input.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1674
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1674](https://avd.aquasec.com/nvd/cve-2022-1674)
	NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 in GitHub repository vim/vim prior to 8.2.4938. NULL Pointer Dereference in function vim_regexec_string at regexp.c:2733 allows attackers to cause a denial of service (application crash) via a crafted input.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1720
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1720](https://avd.aquasec.com/nvd/cve-2022-1720)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1720
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1720">https://avd.aquasec.com/nvd/cve-2022-1720</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in grab_file_name() in findfile.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in function grab_file_name in GitHub repository vim/vim prior to 8.2.4956. This vulnerability is capable of crashing the software, memory modification, and possible remote execution.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1720
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1720](https://avd.aquasec.com/nvd/cve-2022-1720)
	Buffer Over-read in function grab_file_name in GitHub repository vim/vim prior to 8.2.4956. This vulnerability is capable of crashing the software, memory modification, and possible remote execution.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1851
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1851](https://avd.aquasec.com/nvd/cve-2022-1851)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1851
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1851">https://avd.aquasec.com/nvd/cve-2022-1851</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bounds read in gchar_cursor() in misc1.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1851
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1851](https://avd.aquasec.com/nvd/cve-2022-1851)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1927
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1927](https://avd.aquasec.com/nvd/cve-2022-1927)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1927
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1927">https://avd.aquasec.com/nvd/cve-2022-1927</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in utf_ptr2char() in mbyte.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1927
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1927](https://avd.aquasec.com/nvd/cve-2022-1927)
	Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1942
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1942](https://avd.aquasec.com/nvd/cve-2022-1942)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1942
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1942">https://avd.aquasec.com/nvd/cve-2022-1942</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out of bounds write in vim_regsub_both()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1942
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1942](https://avd.aquasec.com/nvd/cve-2022-1942)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1968
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-1968](https://avd.aquasec.com/nvd/cve-2022-1968)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1968
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1968">https://avd.aquasec.com/nvd/cve-2022-1968</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in function utf_ptr2char at mbyte.c:1794
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1968
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1968](https://avd.aquasec.com/nvd/cve-2022-1968)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2175
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2175](https://avd.aquasec.com/nvd/cve-2022-2175)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2175
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2175">https://avd.aquasec.com/nvd/cve-2022-2175</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: buffer over-read in put_on_cmdline() at ex_getln.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2175
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2175](https://avd.aquasec.com/nvd/cve-2022-2175)
	Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2183
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2183](https://avd.aquasec.com/nvd/cve-2022-2183)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2183
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2183">https://avd.aquasec.com/nvd/cve-2022-2183</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bounds read through get_lisp_indent() in function get_lisp_indent
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2183
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2183](https://avd.aquasec.com/nvd/cve-2022-2183)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2304
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2304](https://avd.aquasec.com/nvd/cve-2022-2304)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2304
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2304">https://avd.aquasec.com/nvd/cve-2022-2304</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: stack buffer overflow in spell_dump_compl() at spell.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Stack-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2304
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2304](https://avd.aquasec.com/nvd/cve-2022-2304)
	Stack-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2343
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2343](https://avd.aquasec.com/nvd/cve-2022-2343)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2343
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2343">https://avd.aquasec.com/nvd/cve-2022-2343</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-based buffer overflow in ins_compl_add() in insexpand.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.0044.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2343
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2343](https://avd.aquasec.com/nvd/cve-2022-2343)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.0044.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2345
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2345](https://avd.aquasec.com/nvd/cve-2022-2345)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2345
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2345">https://avd.aquasec.com/nvd/cve-2022-2345</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in skipwhite() in charset.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 9.0.0046.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2345
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2345](https://avd.aquasec.com/nvd/cve-2022-2345)
	Use After Free in GitHub repository vim/vim prior to 9.0.0046.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2923
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2923](https://avd.aquasec.com/nvd/cve-2022-2923)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2923
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2923">https://avd.aquasec.com/nvd/cve-2022-2923</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: null pointer dereference in function sug_filltree
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    NULL Pointer Dereference in GitHub repository vim/vim prior to 9.0.0240.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2923
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2923](https://avd.aquasec.com/nvd/cve-2022-2923)
	NULL Pointer Dereference in GitHub repository vim/vim prior to 9.0.0240.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2946
Severity: MEDIUM
Fixed Version: 
Link: [CVE-2022-2946](https://avd.aquasec.com/nvd/cve-2022-2946)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2946
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2946">https://avd.aquasec.com/nvd/cve-2022-2946</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use after free in function vim_vsnprintf_typval
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 9.0.0246.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2946
	Severity: MEDIUM
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2946](https://avd.aquasec.com/nvd/cve-2022-2946)
	Use After Free in GitHub repository vim/vim prior to 9.0.0246.
    </details>



---

Package: Django
Installed Version: 1.11.29
Vulnerability CVE-2021-33203
Severity: MEDIUM
Fixed Version: 2.2.24, 3.1.12, 3.2.4
Link: [CVE-2021-33203](https://avd.aquasec.com/nvd/cve-2021-33203)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Django-1.11.29.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-33203
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-33203">https://avd.aquasec.com/nvd/cve-2021-33203</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    django: Potential directory traversal via ``admindocs``
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Django before 2.2.24, 3.x before 3.1.12, and 3.2.x before 3.2.4 has a potential directory traversal via django.contrib.admindocs. Staff members could use the TemplateDetailView view to check the existence of arbitrary files. Additionally, if (and only if) the default admindocs templates have been customized by application developers to also show file contents, then not only the existence but also the file contents would have been exposed. In other words, there is directory traversal outside of the template root directories.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    4.9
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-33203
	Severity: MEDIUM
	Package: Django
	Fixed Version: 2.2.24, 3.1.12, 3.2.4
	Link: [CVE-2021-33203](https://avd.aquasec.com/nvd/cve-2021-33203)
	Django before 2.2.24, 3.x before 3.1.12, and 3.2.x before 3.2.4 has a potential directory traversal via django.contrib.admindocs. Staff members could use the TemplateDetailView view to check the existence of arbitrary files. Additionally, if (and only if) the default admindocs templates have been customized by application developers to also show file contents, then not only the existence but also the file contents would have been exposed. In other words, there is directory traversal outside of the template root directories.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2020-10177
Severity: MEDIUM
Fixed Version: 7.1.0
Link: [CVE-2020-10177](https://avd.aquasec.com/nvd/cve-2020-10177)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-10177
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-10177">https://avd.aquasec.com/nvd/cve-2020-10177</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: multiple out-of-bounds reads in libImaging/FliDecode.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Pillow before 7.1.0 has multiple out-of-bounds reads in libImaging/FliDecode.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-10177
	Severity: MEDIUM
	Package: Pillow
	Fixed Version: 7.1.0
	Link: [CVE-2020-10177](https://avd.aquasec.com/nvd/cve-2020-10177)
	Pillow before 7.1.0 has multiple out-of-bounds reads in libImaging/FliDecode.c.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2020-10378
Severity: MEDIUM
Fixed Version: 7.1.0
Link: [CVE-2020-10378](https://avd.aquasec.com/nvd/cve-2020-10378)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-10378
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-10378">https://avd.aquasec.com/nvd/cve-2020-10378</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: an out-of-bounds read in libImaging/PcxDecode.c can occur when reading PCX files
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In libImaging/PcxDecode.c in Pillow before 7.1.0, an out-of-bounds read can occur when reading PCX files where state-&amp;gt;shuffle is instructed to read beyond state-&amp;gt;buffer.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-10378
	Severity: MEDIUM
	Package: Pillow
	Fixed Version: 7.1.0
	Link: [CVE-2020-10378](https://avd.aquasec.com/nvd/cve-2020-10378)
	In libImaging/PcxDecode.c in Pillow before 7.1.0, an out-of-bounds read can occur when reading PCX files where state-&gt;shuffle is instructed to read beyond state-&gt;buffer.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2020-10994
Severity: MEDIUM
Fixed Version: 7.0.0
Link: [CVE-2020-10994](https://avd.aquasec.com/nvd/cve-2020-10994)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-10994
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-10994">https://avd.aquasec.com/nvd/cve-2020-10994</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: multiple out-of-bounds reads via a crafted JP2 file
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In libImaging/Jpeg2KDecode.c in Pillow before 7.1.0, there are multiple out-of-bounds reads via a crafted JP2 file.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-10994
	Severity: MEDIUM
	Package: Pillow
	Fixed Version: 7.0.0
	Link: [CVE-2020-10994](https://avd.aquasec.com/nvd/cve-2020-10994)
	In libImaging/Jpeg2KDecode.c in Pillow before 7.1.0, there are multiple out-of-bounds reads via a crafted JP2 file.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2020-35655
Severity: MEDIUM
Fixed Version: 8.1.0
Link: [CVE-2020-35655](https://avd.aquasec.com/nvd/cve-2020-35655)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-35655
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-35655">https://avd.aquasec.com/nvd/cve-2020-35655</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Buffer over-read in SGI RLE image reader
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In Pillow before 8.1.0, SGIRleDecode has a 4-byte buffer over-read when decoding crafted SGI RLE image files because offsets and length tables are mishandled.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.4
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-35655
	Severity: MEDIUM
	Package: Pillow
	Fixed Version: 8.1.0
	Link: [CVE-2020-35655](https://avd.aquasec.com/nvd/cve-2020-35655)
	In Pillow before 8.1.0, SGIRleDecode has a 4-byte buffer over-read when decoding crafted SGI RLE image files because offsets and length tables are mishandled.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-25292
Severity: MEDIUM
Fixed Version: 8.1.1
Link: [CVE-2021-25292](https://avd.aquasec.com/nvd/cve-2021-25292)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-25292
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-25292">https://avd.aquasec.com/nvd/cve-2021-25292</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Regular expression DoS in PDF format parser
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Pillow before 8.1.1. The PDF parser allows a regular expression DoS (ReDoS) attack via a crafted PDF file because of a catastrophic backtracking regex.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    6.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-25292
	Severity: MEDIUM
	Package: Pillow
	Fixed Version: 8.1.1
	Link: [CVE-2021-25292](https://avd.aquasec.com/nvd/cve-2021-25292)
	An issue was discovered in Pillow before 8.1.1. The PDF parser allows a regular expression DoS (ReDoS) attack via a crafted PDF file because of a catastrophic backtracking regex.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-28675
Severity: MEDIUM
Fixed Version: 8.2.0
Link: [CVE-2021-28675](https://avd.aquasec.com/nvd/cve-2021-28675)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-28675
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-28675">https://avd.aquasec.com/nvd/cve-2021-28675</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Excessive memory allocation in PSD image reader
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Pillow before 8.2.0. PSDImagePlugin.PsdImageFile lacked a sanity check on the number of input layers relative to the size of the data block. This could lead to a DoS on Image.open prior to Image.load.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-28675
	Severity: MEDIUM
	Package: Pillow
	Fixed Version: 8.2.0
	Link: [CVE-2021-28675](https://avd.aquasec.com/nvd/cve-2021-28675)
	An issue was discovered in Pillow before 8.2.0. PSDImagePlugin.PsdImageFile lacked a sanity check on the number of input layers relative to the size of the data block. This could lead to a DoS on Image.open prior to Image.load.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2021-28678
Severity: MEDIUM
Fixed Version: 8.2.0
Link: [CVE-2021-28678](https://avd.aquasec.com/nvd/cve-2021-28678)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-28678
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-28678">https://avd.aquasec.com/nvd/cve-2021-28678</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: Excessive looping in BLP image reader
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in Pillow before 8.2.0. For BLP data, BlpImagePlugin did not properly check that reads (after jumping to file offsets) returned data. This could lead to a DoS where the decoder could be run a large number of times on empty data.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-28678
	Severity: MEDIUM
	Package: Pillow
	Fixed Version: 8.2.0
	Link: [CVE-2021-28678](https://avd.aquasec.com/nvd/cve-2021-28678)
	An issue was discovered in Pillow before 8.2.0. For BLP data, BlpImagePlugin did not properly check that reads (after jumping to file offsets) returned data. This could lead to a DoS where the decoder could be run a large number of times on empty data.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2022-22815
Severity: MEDIUM
Fixed Version: 9.0.0
Link: [CVE-2022-22815](https://avd.aquasec.com/nvd/cve-2022-22815)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-22815
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-22815">https://avd.aquasec.com/nvd/cve-2022-22815</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: improperly initializes ImagePath.Path in path_getbbox() in path.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    path_getbbox in path.c in Pillow before 9.0.0 improperly initializes ImagePath.Path.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    6.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-22815
	Severity: MEDIUM
	Package: Pillow
	Fixed Version: 9.0.0
	Link: [CVE-2022-22815](https://avd.aquasec.com/nvd/cve-2022-22815)
	path_getbbox in path.c in Pillow before 9.0.0 improperly initializes ImagePath.Path.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability CVE-2022-22816
Severity: MEDIUM
Fixed Version: 9.0.0
Link: [CVE-2022-22816](https://avd.aquasec.com/nvd/cve-2022-22816)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-22816
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-22816">https://avd.aquasec.com/nvd/cve-2022-22816</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pillow: buffer over-read during initialization of ImagePath.Path in path_getbbox() in path.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    path_getbbox in path.c in Pillow before 9.0.0 has a buffer over-read during initialization of ImagePath.Path.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    6.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-22816
	Severity: MEDIUM
	Package: Pillow
	Fixed Version: 9.0.0
	Link: [CVE-2022-22816](https://avd.aquasec.com/nvd/cve-2022-22816)
	path_getbbox in path.c in Pillow before 9.0.0 has a buffer over-read during initialization of ImagePath.Path.
    </details>



---

Package: Pillow
Installed Version: 6.2.2
Vulnerability GHSA-jgpv-4h4c-xhw3
Severity: MEDIUM
Fixed Version: 8.1.2
Link: [GHSA-jgpv-4h4c-xhw3](https://github.com/advisories/GHSA-jgpv-4h4c-xhw3)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/Pillow-6.2.2.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    GHSA-jgpv-4h4c-xhw3
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://github.com/advisories/GHSA-jgpv-4h4c-xhw3">https://github.com/advisories/GHSA-jgpv-4h4c-xhw3</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Uncontrolled Resource Consumption in pillow
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ### Impact
	_Pillow before 8.1.1 allows attackers to cause a denial of service (memory consumption) because the reported size of a contained image is not properly checked for a BLP container, and thus an attempted memory allocation can be very large._
	
	### Patches
	_An issue was discovered in Pillow before 6.2.0. When reading specially crafted invalid image files, the library can either allocate very large amounts of memory or take an extremely long period of time to process the image._
	
	### Workarounds
	_An issue was discovered in Pillow before 6.2.0. When reading specially crafted invalid image files, the library can either allocate very large amounts of memory or take an extremely long period of time to process the image._
	
	### References
	https://nvd.nist.gov/vuln/detail/CVE-2021-27921
	
	### For more information
	If you have any questions or comments about this advisory:
	* Open an issue in [example link to repo](http://example.com)
	* Email us at [example email address](mailto:example@example.com)
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    7.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability GHSA-jgpv-4h4c-xhw3
	Severity: MEDIUM
	Package: Pillow
	Fixed Version: 8.1.2
	Link: [GHSA-jgpv-4h4c-xhw3](https://github.com/advisories/GHSA-jgpv-4h4c-xhw3)
	### Impact
	_Pillow before 8.1.1 allows attackers to cause a denial of service (memory consumption) because the reported size of a contained image is not properly checked for a BLP container, and thus an attempted memory allocation can be very large._
	
	### Patches
	_An issue was discovered in Pillow before 6.2.0. When reading specially crafted invalid image files, the library can either allocate very large amounts of memory or take an extremely long period of time to process the image._
	
	### Workarounds
	_An issue was discovered in Pillow before 6.2.0. When reading specially crafted invalid image files, the library can either allocate very large amounts of memory or take an extremely long period of time to process the image._
	
	### References
	https://nvd.nist.gov/vuln/detail/CVE-2021-27921
	
	### For more information
	If you have any questions or comments about this advisory:
	* Open an issue in [example link to repo](http://example.com)
	* Email us at [example email address](mailto:example@example.com)
    </details>



---

Package: PyPDF2
Installed Version: 1.26.0
Vulnerability CVE-2022-24859
Severity: MEDIUM
Fixed Version: 1.27.5
Link: [CVE-2022-24859](https://avd.aquasec.com/nvd/cve-2022-24859)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/PyPDF2-1.26.0.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-24859
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-24859">https://avd.aquasec.com/nvd/cve-2022-24859</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    PyPDF2: infinite loop vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    PyPDF2 is an open source python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. In versions prior to 1.27.5 an attacker who uses this vulnerability can craft a PDF which leads to an infinite loop if the PyPDF2 if the code attempts to get the content stream. The reason is that the last while-loop in `ContentStream._readInlineImage` only terminates when it finds the `EI` token, but never actually checks if the stream has already ended. This issue has been resolved in version `1.27.5`. Users unable to upgrade should validate and PDFs prior to iterating over their content stream.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-24859
	Severity: MEDIUM
	Package: PyPDF2
	Fixed Version: 1.27.5
	Link: [CVE-2022-24859](https://avd.aquasec.com/nvd/cve-2022-24859)
	PyPDF2 is an open source python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. In versions prior to 1.27.5 an attacker who uses this vulnerability can craft a PDF which leads to an infinite loop if the PyPDF2 if the code attempts to get the content stream. The reason is that the last while-loop in `ContentStream._readInlineImage` only terminates when it finds the `EI` token, but never actually checks if the stream has already ended. This issue has been resolved in version `1.27.5`. Users unable to upgrade should validate and PDFs prior to iterating over their content stream.
    </details>



---

Package: certifi
Installed Version: 2020.4.5.1
Vulnerability CVE-2022-23491
Severity: MEDIUM
Fixed Version: 2022.12.07
Link: [CVE-2022-23491](https://avd.aquasec.com/nvd/cve-2022-23491)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/certifi-2020.4.5.1.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-23491
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-23491">https://avd.aquasec.com/nvd/cve-2022-23491</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    Certifi removing TrustCor root certificate
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Certifi is a curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. Certifi 2022.12.07 removes root certificates from &amp;#34;TrustCor&amp;#34; from the root store. These are in the process of being removed from Mozilla&amp;#39;s trust store. TrustCor&amp;#39;s root certificates are being removed pursuant to an investigation prompted by media reporting that TrustCor&amp;#39;s ownership also operated a business that produced spyware. Conclusions of Mozilla&amp;#39;s investigation can be found in the linked google group discussion.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    6.8
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-23491
	Severity: MEDIUM
	Package: certifi
	Fixed Version: 2022.12.07
	Link: [CVE-2022-23491](https://avd.aquasec.com/nvd/cve-2022-23491)
	Certifi is a curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. Certifi 2022.12.07 removes root certificates from &#34;TrustCor&#34; from the root store. These are in the process of being removed from Mozilla&#39;s trust store. TrustCor&#39;s root certificates are being removed pursuant to an investigation prompted by media reporting that TrustCor&#39;s ownership also operated a business that produced spyware. Conclusions of Mozilla&#39;s investigation can be found in the linked google group discussion.
    </details>



---

Package: django-filter
Installed Version: 1.1.0
Vulnerability CVE-2020-15225
Severity: MEDIUM
Fixed Version: 2.4.0
Link: [CVE-2020-15225](https://avd.aquasec.com/nvd/cve-2020-15225)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/django_filter-1.1.0.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-15225
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-15225">https://avd.aquasec.com/nvd/cve-2020-15225</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-django-filter: Maliciously input using exponential format may cause denial of service
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    django-filter is a generic system for filtering Django QuerySets based on user selections. In django-filter before version 2.4.0, automatically generated `NumberFilter` instances, whose value was later converted to an integer, were subject to potential DoS from maliciously input using exponential format with sufficiently large exponents. Version 2.4.0+ applies a `MaxValueValidator` with a a default `limit_value` of 1e50 to the form field used by `NumberFilter` instances. In addition, `NumberFilter` implements the new `get_max_validator()` which should return a configured validator instance to customise the limit, or else `None` to disable the additional validation. Users may manually apply an equivalent validator if they are not able to upgrade.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    6.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-15225
	Severity: MEDIUM
	Package: django-filter
	Fixed Version: 2.4.0
	Link: [CVE-2020-15225](https://avd.aquasec.com/nvd/cve-2020-15225)
	django-filter is a generic system for filtering Django QuerySets based on user selections. In django-filter before version 2.4.0, automatically generated `NumberFilter` instances, whose value was later converted to an integer, were subject to potential DoS from maliciously input using exponential format with sufficiently large exponents. Version 2.4.0+ applies a `MaxValueValidator` with a a default `limit_value` of 1e50 to the form field used by `NumberFilter` instances. In addition, `NumberFilter` implements the new `get_max_validator()` which should return a configured validator instance to customise the limit, or else `None` to disable the additional validation. Users may manually apply an equivalent validator if they are not able to upgrade.
    </details>



---

Package: djangorestframework
Installed Version: 3.9.4
Vulnerability CVE-2020-25626
Severity: MEDIUM
Fixed Version: 3.11.2
Link: [CVE-2020-25626](https://avd.aquasec.com/nvd/cve-2020-25626)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/djangorestframework-3.9.4.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-25626
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-25626">https://avd.aquasec.com/nvd/cve-2020-25626</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    django-rest-framework: XSS Vulnerability in API viewer
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in Django REST Framework versions before 3.12.0 and before 3.11.2. When using the browseable API viewer, Django REST Framework fails to properly escape certain strings that can come from user input. This allows a user who can control those strings to inject malicious &amp;lt;script&amp;gt; tags, leading to a cross-site-scripting (XSS) vulnerability.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    6.1
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-25626
	Severity: MEDIUM
	Package: djangorestframework
	Fixed Version: 3.11.2
	Link: [CVE-2020-25626](https://avd.aquasec.com/nvd/cve-2020-25626)
	A flaw was found in Django REST Framework versions before 3.12.0 and before 3.11.2. When using the browseable API viewer, Django REST Framework fails to properly escape certain strings that can come from user input. This allows a user who can control those strings to inject malicious &lt;script&gt; tags, leading to a cross-site-scripting (XSS) vulnerability.
    </details>



---

Package: jwcrypto
Installed Version: 0.9.1
Vulnerability CVE-2022-3102
Severity: MEDIUM
Fixed Version: 1.4
Link: [CVE-2022-3102](https://avd.aquasec.com/nvd/cve-2022-3102)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/jwcrypto-0.9.1.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3102
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3102">https://avd.aquasec.com/nvd/cve-2022-3102</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    jwcrypto token substitution can lead to authentication bypass
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The JWT code can auto-detect the type of token being provided, and this can lead the application to incorrect conclusions about the trustworthiness of the token.
	Quoting the private disclosure we received : &amp;#34;Under certain circumstances, it is possible to substitute a [..] signed JWS with a JWE that is encrypted with the public key that is normally used for signature validation.&amp;#34;
	This substitution attack can occur only if the validating application also have access to the private key, normally used to sign the tokens, available during validation of the received JWT.
	The significance of this attacks depends on the use of the token, it may lead to authentication bypass or authorization bypass (respectively if claims are used to authenticate or authorize certain actions), because the attacker has full control of the data placed in the JWE and can inject any desired claim value.
	
	Several mitigating factors exist that can protect applications from this issue:
	- If the private key corresponding to the public key used to encrypt the JWE is not available to the application an exception will be raised.
	- If the JWK is specified with the &amp;#39;use&amp;#39; parameter set to &amp;#39;sig&amp;#39; (as expected for keys used only for signing/verification) an exception will be raised.
	- If the JWK is specified with the &amp;#39;key_ops&amp;#39; parameter set and it does not include the &amp;#39;decrypt&amp;#39; operation an exception will be raised.
	- Applications may check the token type before validation, in this case they would fail to detect an expected JWS
	
	Normally, signing and validation are done by different applications, so this scenario should be unlikely. However it is possible to have applications that both sign and validate tokens and do not separate JWKs in use, or do not set a JWK &amp;#39;use&amp;#39; type.
	
	Due to the mitigating factors, and the fact that specific operational constraints and conditions need to be in place to successfully exploit this issue to generate an authentication bypass, we rate this security issue as moderate. Other avenues may decide on a different rating based on use case, always verify what conditions apply to your use of the library to assess risk.
	
	Many thanks to Tom Tervoort of Secura for finding and reporting this issue.
	
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3102
	Severity: MEDIUM
	Package: jwcrypto
	Fixed Version: 1.4
	Link: [CVE-2022-3102](https://avd.aquasec.com/nvd/cve-2022-3102)
	The JWT code can auto-detect the type of token being provided, and this can lead the application to incorrect conclusions about the trustworthiness of the token.
	Quoting the private disclosure we received : &#34;Under certain circumstances, it is possible to substitute a [..] signed JWS with a JWE that is encrypted with the public key that is normally used for signature validation.&#34;
	This substitution attack can occur only if the validating application also have access to the private key, normally used to sign the tokens, available during validation of the received JWT.
	The significance of this attacks depends on the use of the token, it may lead to authentication bypass or authorization bypass (respectively if claims are used to authenticate or authorize certain actions), because the attacker has full control of the data placed in the JWE and can inject any desired claim value.
	
	Several mitigating factors exist that can protect applications from this issue:
	- If the private key corresponding to the public key used to encrypt the JWE is not available to the application an exception will be raised.
	- If the JWK is specified with the &#39;use&#39; parameter set to &#39;sig&#39; (as expected for keys used only for signing/verification) an exception will be raised.
	- If the JWK is specified with the &#39;key_ops&#39; parameter set and it does not include the &#39;decrypt&#39; operation an exception will be raised.
	- Applications may check the token type before validation, in this case they would fail to detect an expected JWS
	
	Normally, signing and validation are done by different applications, so this scenario should be unlikely. However it is possible to have applications that both sign and validate tokens and do not separate JWKs in use, or do not set a JWK &#39;use&#39; type.
	
	Due to the mitigating factors, and the fact that specific operational constraints and conditions need to be in place to successfully exploit this issue to generate an authentication bypass, we rate this security issue as moderate. Other avenues may decide on a different rating based on use case, always verify what conditions apply to your use of the library to assess risk.
	
	Many thanks to Tom Tervoort of Secura for finding and reporting this issue.
	
    </details>



---

Package: numpy
Installed Version: 1.16.6
Vulnerability CVE-2021-41495
Severity: MEDIUM
Fixed Version: 1.19.1
Link: [CVE-2021-41495](https://avd.aquasec.com/nvd/cve-2021-41495)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/numpy-1.16.6.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-41495
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-41495">https://avd.aquasec.com/nvd/cve-2021-41495</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    numpy: NULL pointer dereference in numpy.sort in in the PyArray_DescrNew() due to missing return-value validation
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ** DISPUTED ** Null Pointer Dereference vulnerability exists in numpy.sort in NumPy &amp;amp;lt and 1.19 in the PyArray_DescrNew function due to missing return-value validation, which allows attackers to conduct DoS attacks by repetitively creating sort arrays. NOTE: While correct that validation is missing, an error can only occur due to an exhaustion of memory. If the user can exhaust memory, they are already privileged. Further, it should be practically impossible to construct an attack which can target the memory exhaustion to occur at exactly this place.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.3
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-41495
	Severity: MEDIUM
	Package: numpy
	Fixed Version: 1.19.1
	Link: [CVE-2021-41495](https://avd.aquasec.com/nvd/cve-2021-41495)
	** DISPUTED ** Null Pointer Dereference vulnerability exists in numpy.sort in NumPy &amp;lt and 1.19 in the PyArray_DescrNew function due to missing return-value validation, which allows attackers to conduct DoS attacks by repetitively creating sort arrays. NOTE: While correct that validation is missing, an error can only occur due to an exhaustion of memory. If the user can exhaust memory, they are already privileged. Further, it should be practically impossible to construct an attack which can target the memory exhaustion to occur at exactly this place.
    </details>



---

Package: numpy
Installed Version: 1.16.6
Vulnerability CVE-2021-41496
Severity: MEDIUM
Fixed Version: 1.19.0
Link: [CVE-2021-41496](https://avd.aquasec.com/nvd/cve-2021-41496)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/numpy-1.16.6.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-41496
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-41496">https://avd.aquasec.com/nvd/cve-2021-41496</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    numpy: buffer overflow in the array_from_pyobj() in fortranobject.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ** DISPUTED ** Buffer overflow in the array_from_pyobj function of fortranobject.c in NumPy &amp;lt; 1.19, which allows attackers to conduct a Denial of Service attacks by carefully constructing an array with negative values. NOTE: The vendor does not agree this is a vulnerability; the negative dimensions can only be created by an already privileged user (or internally).
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-41496
	Severity: MEDIUM
	Package: numpy
	Fixed Version: 1.19.0
	Link: [CVE-2021-41496](https://avd.aquasec.com/nvd/cve-2021-41496)
	** DISPUTED ** Buffer overflow in the array_from_pyobj function of fortranobject.c in NumPy &lt; 1.19, which allows attackers to conduct a Denial of Service attacks by carefully constructing an array with negative values. NOTE: The vendor does not agree this is a vulnerability; the negative dimensions can only be created by an already privileged user (or internally).
    </details>



---

Package: pip
Installed Version: 20.3.4
Vulnerability CVE-2021-3572
Severity: MEDIUM
Fixed Version: 21.1
Link: [CVE-2021-3572](https://avd.aquasec.com/nvd/cve-2021-3572)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/pip-20.3.4.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-3572
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-3572">https://avd.aquasec.com/nvd/cve-2021-3572</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pip: Incorrect handling of unicode separators in git references
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in python-pip in the way it handled Unicode separators in git references. A remote attacker could possibly use this issue to install a different revision on a repository. The highest threat from this vulnerability is to data integrity. This is fixed in python-pip version 21.1.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.7
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-3572
	Severity: MEDIUM
	Package: pip
	Fixed Version: 21.1
	Link: [CVE-2021-3572](https://avd.aquasec.com/nvd/cve-2021-3572)
	A flaw was found in python-pip in the way it handled Unicode separators in git references. A remote attacker could possibly use this issue to install a different revision on a repository. The highest threat from this vulnerability is to data integrity. This is fixed in python-pip version 21.1.
    </details>



---

Package: pysaml2
Installed Version: 4.9.0
Vulnerability CVE-2021-21238
Severity: MEDIUM
Fixed Version: 6.5.0
Link: [CVE-2021-21238](https://avd.aquasec.com/nvd/cve-2021-21238)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/pysaml2-4.9.0.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-21238
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-21238">https://avd.aquasec.com/nvd/cve-2021-21238</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pysaml2: processing of invalid SAML XML documents
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    PySAML2 is a pure python implementation of SAML Version 2 Standard. PySAML2 before 6.5.0 has an improper verification of cryptographic signature vulnerability. All users of pysaml2 that need to validate signed SAML documents are impacted. The vulnerability is a variant of XML Signature wrapping because it did not validate the SAML document against an XML schema. This allowed invalid XML documents to be processed and such a document can trick pysaml2 with a wrapped signature. This is fixed in PySAML2 6.5.0.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    6.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-21238
	Severity: MEDIUM
	Package: pysaml2
	Fixed Version: 6.5.0
	Link: [CVE-2021-21238](https://avd.aquasec.com/nvd/cve-2021-21238)
	PySAML2 is a pure python implementation of SAML Version 2 Standard. PySAML2 before 6.5.0 has an improper verification of cryptographic signature vulnerability. All users of pysaml2 that need to validate signed SAML documents are impacted. The vulnerability is a variant of XML Signature wrapping because it did not validate the SAML document against an XML schema. This allowed invalid XML documents to be processed and such a document can trick pysaml2 with a wrapped signature. This is fixed in PySAML2 6.5.0.
    </details>



---

Package: pysaml2
Installed Version: 4.9.0
Vulnerability CVE-2021-21239
Severity: MEDIUM
Fixed Version: 6.5.0
Link: [CVE-2021-21239](https://avd.aquasec.com/nvd/cve-2021-21239)

### Locations
#### **Physical Location**
- usr/local/lib/python2.7/dist-packages/pysaml2-4.9.0.dist-info/METADATA


- Line 1







### Level

- Warning


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-21239
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-21239">https://avd.aquasec.com/nvd/cve-2021-21239</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pysaml2: An improper verification of cryptographic signature
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    PySAML2 is a pure python implementation of SAML Version 2 Standard. PySAML2 before 6.5.0 has an improper verification of cryptographic signature vulnerability. Users of pysaml2 that use the default CryptoBackendXmlSec1 backend and need to verify signed SAML documents are impacted. PySAML2 does not ensure that a signed SAML document is correctly signed. The default CryptoBackendXmlSec1 backend is using the xmlsec1 binary to verify the signature of signed SAML documents, but by default xmlsec1 accepts any type of key found within the given document. xmlsec1 needs to be configured explicitly to only use only _x509 certificates_ for the verification process of the SAML document signature. This is fixed in PySAML2 6.5.0.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    6.5
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-21239
	Severity: MEDIUM
	Package: pysaml2
	Fixed Version: 6.5.0
	Link: [CVE-2021-21239](https://avd.aquasec.com/nvd/cve-2021-21239)
	PySAML2 is a pure python implementation of SAML Version 2 Standard. PySAML2 before 6.5.0 has an improper verification of cryptographic signature vulnerability. Users of pysaml2 that use the default CryptoBackendXmlSec1 backend and need to verify signed SAML documents are impacted. PySAML2 does not ensure that a signed SAML document is correctly signed. The default CryptoBackendXmlSec1 backend is using the xmlsec1 binary to verify the signature of signed SAML documents, but by default xmlsec1 accepts any type of key found within the given document. xmlsec1 needs to be configured explicitly to only use only _x509 certificates_ for the verification process of the SAML document signature. This is fixed in PySAML2 6.5.0.
    </details>



---

Package: binutils
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2017-13716
Severity: LOW
Fixed Version: 
Link: [CVE-2017-13716](https://avd.aquasec.com/nvd/cve-2017-13716)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2017-13716
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2017-13716">https://avd.aquasec.com/nvd/cve-2017-13716</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: Memory leak with the C++ symbol demangler routine in libiberty
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The C++ symbol demangler routine in cplus-dem.c in libiberty, as distributed in GNU Binutils 2.29, allows remote attackers to cause a denial of service (excessive memory allocation and application crash) via a crafted file, as demonstrated by a call from the Binary File Descriptor (BFD) library (aka libbfd).
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2017-13716
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2017-13716](https://avd.aquasec.com/nvd/cve-2017-13716)
	The C++ symbol demangler routine in cplus-dem.c in libiberty, as distributed in GNU Binutils 2.29, allows remote attackers to cause a denial of service (excessive memory allocation and application crash) via a crafted file, as demonstrated by a call from the Binary File Descriptor (BFD) library (aka libbfd).
    </details>



---

Package: binutils
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2018-20657
Severity: LOW
Fixed Version: 
Link: [CVE-2018-20657](https://avd.aquasec.com/nvd/cve-2018-20657)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-20657
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-20657">https://avd.aquasec.com/nvd/cve-2018-20657</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libiberty: Memory leak in demangle_template function resulting in a denial of service
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The demangle_template function in cplus-dem.c in GNU libiberty, as distributed in GNU Binutils 2.31.1, has a memory leak via a crafted string, leading to a denial of service (memory consumption), as demonstrated by cxxfilt, a related issue to CVE-2018-12698.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-20657
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2018-20657](https://avd.aquasec.com/nvd/cve-2018-20657)
	The demangle_template function in cplus-dem.c in GNU libiberty, as distributed in GNU Binutils 2.31.1, has a memory leak via a crafted string, leading to a denial of service (memory consumption), as demonstrated by cxxfilt, a related issue to CVE-2018-12698.
    </details>



---

Package: binutils
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2019-1010204
Severity: LOW
Fixed Version: 
Link: [CVE-2019-1010204](https://avd.aquasec.com/nvd/cve-2019-1010204)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-1010204
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-1010204">https://avd.aquasec.com/nvd/cve-2019-1010204</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: Improper Input Validation, Signed/Unsigned Comparison, Out-of-bounds Read in gold/fileread.cc and elfcpp/elfcpp_file.h leads to denial of service
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    GNU binutils gold gold v1.11-v1.16 (GNU binutils v2.21-v2.31.1) is affected by: Improper Input Validation, Signed/Unsigned Comparison, Out-of-bounds Read. The impact is: Denial of service. The component is: gold/fileread.cc:497, elfcpp/elfcpp_file.h:644. The attack vector is: An ELF file with an invalid e_shoff header field must be opened.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-1010204
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2019-1010204](https://avd.aquasec.com/nvd/cve-2019-1010204)
	GNU binutils gold gold v1.11-v1.16 (GNU binutils v2.21-v2.31.1) is affected by: Improper Input Validation, Signed/Unsigned Comparison, Out-of-bounds Read. The impact is: Denial of service. The component is: gold/fileread.cc:497, elfcpp/elfcpp_file.h:644. The attack vector is: An ELF file with an invalid e_shoff header field must be opened.
    </details>



---

Package: binutils
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2021-45078
Severity: LOW
Fixed Version: 
Link: [CVE-2021-45078](https://avd.aquasec.com/nvd/cve-2021-45078)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-45078
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-45078">https://avd.aquasec.com/nvd/cve-2021-45078</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: out-of-bounds write in stab_xcoff_builtin_type() in stabs.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    stab_xcoff_builtin_type in stabs.c in GNU Binutils through 2.37 allows attackers to cause a denial of service (heap-based buffer overflow) or possibly have unspecified other impact, as demonstrated by an out-of-bounds write. NOTE: this issue exists because of an incorrect fix for CVE-2018-12699.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-45078
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2021-45078](https://avd.aquasec.com/nvd/cve-2021-45078)
	stab_xcoff_builtin_type in stabs.c in GNU Binutils through 2.37 allows attackers to cause a denial of service (heap-based buffer overflow) or possibly have unspecified other impact, as demonstrated by an out-of-bounds write. NOTE: this issue exists because of an incorrect fix for CVE-2018-12699.
    </details>



---

Package: binutils
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2021-46195
Severity: LOW
Fixed Version: 
Link: [CVE-2021-46195](https://avd.aquasec.com/nvd/cve-2021-46195)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-46195
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-46195">https://avd.aquasec.com/nvd/cve-2021-46195</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gcc: uncontrolled recursion in libiberty/rust-demangle.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    GCC v12.0 was discovered to contain an uncontrolled recursion via the component libiberty/rust-demangle.c. This vulnerability allows attackers to cause a Denial of Service (DoS) by consuming excessive CPU and memory resources.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-46195
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2021-46195](https://avd.aquasec.com/nvd/cve-2021-46195)
	GCC v12.0 was discovered to contain an uncontrolled recursion via the component libiberty/rust-demangle.c. This vulnerability allows attackers to cause a Denial of Service (DoS) by consuming excessive CPU and memory resources.
    </details>



---

Package: binutils-common
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2017-13716
Severity: LOW
Fixed Version: 
Link: [CVE-2017-13716](https://avd.aquasec.com/nvd/cve-2017-13716)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2017-13716
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2017-13716">https://avd.aquasec.com/nvd/cve-2017-13716</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: Memory leak with the C++ symbol demangler routine in libiberty
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The C++ symbol demangler routine in cplus-dem.c in libiberty, as distributed in GNU Binutils 2.29, allows remote attackers to cause a denial of service (excessive memory allocation and application crash) via a crafted file, as demonstrated by a call from the Binary File Descriptor (BFD) library (aka libbfd).
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2017-13716
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2017-13716](https://avd.aquasec.com/nvd/cve-2017-13716)
	The C++ symbol demangler routine in cplus-dem.c in libiberty, as distributed in GNU Binutils 2.29, allows remote attackers to cause a denial of service (excessive memory allocation and application crash) via a crafted file, as demonstrated by a call from the Binary File Descriptor (BFD) library (aka libbfd).
    </details>



---

Package: binutils-common
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2018-20657
Severity: LOW
Fixed Version: 
Link: [CVE-2018-20657](https://avd.aquasec.com/nvd/cve-2018-20657)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-20657
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-20657">https://avd.aquasec.com/nvd/cve-2018-20657</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libiberty: Memory leak in demangle_template function resulting in a denial of service
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The demangle_template function in cplus-dem.c in GNU libiberty, as distributed in GNU Binutils 2.31.1, has a memory leak via a crafted string, leading to a denial of service (memory consumption), as demonstrated by cxxfilt, a related issue to CVE-2018-12698.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-20657
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2018-20657](https://avd.aquasec.com/nvd/cve-2018-20657)
	The demangle_template function in cplus-dem.c in GNU libiberty, as distributed in GNU Binutils 2.31.1, has a memory leak via a crafted string, leading to a denial of service (memory consumption), as demonstrated by cxxfilt, a related issue to CVE-2018-12698.
    </details>



---

Package: binutils-common
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2019-1010204
Severity: LOW
Fixed Version: 
Link: [CVE-2019-1010204](https://avd.aquasec.com/nvd/cve-2019-1010204)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-1010204
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-1010204">https://avd.aquasec.com/nvd/cve-2019-1010204</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: Improper Input Validation, Signed/Unsigned Comparison, Out-of-bounds Read in gold/fileread.cc and elfcpp/elfcpp_file.h leads to denial of service
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    GNU binutils gold gold v1.11-v1.16 (GNU binutils v2.21-v2.31.1) is affected by: Improper Input Validation, Signed/Unsigned Comparison, Out-of-bounds Read. The impact is: Denial of service. The component is: gold/fileread.cc:497, elfcpp/elfcpp_file.h:644. The attack vector is: An ELF file with an invalid e_shoff header field must be opened.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-1010204
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2019-1010204](https://avd.aquasec.com/nvd/cve-2019-1010204)
	GNU binutils gold gold v1.11-v1.16 (GNU binutils v2.21-v2.31.1) is affected by: Improper Input Validation, Signed/Unsigned Comparison, Out-of-bounds Read. The impact is: Denial of service. The component is: gold/fileread.cc:497, elfcpp/elfcpp_file.h:644. The attack vector is: An ELF file with an invalid e_shoff header field must be opened.
    </details>



---

Package: binutils-common
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2021-45078
Severity: LOW
Fixed Version: 
Link: [CVE-2021-45078](https://avd.aquasec.com/nvd/cve-2021-45078)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-45078
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-45078">https://avd.aquasec.com/nvd/cve-2021-45078</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: out-of-bounds write in stab_xcoff_builtin_type() in stabs.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    stab_xcoff_builtin_type in stabs.c in GNU Binutils through 2.37 allows attackers to cause a denial of service (heap-based buffer overflow) or possibly have unspecified other impact, as demonstrated by an out-of-bounds write. NOTE: this issue exists because of an incorrect fix for CVE-2018-12699.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-45078
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2021-45078](https://avd.aquasec.com/nvd/cve-2021-45078)
	stab_xcoff_builtin_type in stabs.c in GNU Binutils through 2.37 allows attackers to cause a denial of service (heap-based buffer overflow) or possibly have unspecified other impact, as demonstrated by an out-of-bounds write. NOTE: this issue exists because of an incorrect fix for CVE-2018-12699.
    </details>



---

Package: binutils-common
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2021-46195
Severity: LOW
Fixed Version: 
Link: [CVE-2021-46195](https://avd.aquasec.com/nvd/cve-2021-46195)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-46195
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-46195">https://avd.aquasec.com/nvd/cve-2021-46195</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gcc: uncontrolled recursion in libiberty/rust-demangle.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    GCC v12.0 was discovered to contain an uncontrolled recursion via the component libiberty/rust-demangle.c. This vulnerability allows attackers to cause a Denial of Service (DoS) by consuming excessive CPU and memory resources.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-46195
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2021-46195](https://avd.aquasec.com/nvd/cve-2021-46195)
	GCC v12.0 was discovered to contain an uncontrolled recursion via the component libiberty/rust-demangle.c. This vulnerability allows attackers to cause a Denial of Service (DoS) by consuming excessive CPU and memory resources.
    </details>



---

Package: binutils-x86-64-linux-gnu
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2017-13716
Severity: LOW
Fixed Version: 
Link: [CVE-2017-13716](https://avd.aquasec.com/nvd/cve-2017-13716)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2017-13716
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2017-13716">https://avd.aquasec.com/nvd/cve-2017-13716</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: Memory leak with the C++ symbol demangler routine in libiberty
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The C++ symbol demangler routine in cplus-dem.c in libiberty, as distributed in GNU Binutils 2.29, allows remote attackers to cause a denial of service (excessive memory allocation and application crash) via a crafted file, as demonstrated by a call from the Binary File Descriptor (BFD) library (aka libbfd).
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2017-13716
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2017-13716](https://avd.aquasec.com/nvd/cve-2017-13716)
	The C++ symbol demangler routine in cplus-dem.c in libiberty, as distributed in GNU Binutils 2.29, allows remote attackers to cause a denial of service (excessive memory allocation and application crash) via a crafted file, as demonstrated by a call from the Binary File Descriptor (BFD) library (aka libbfd).
    </details>



---

Package: binutils-x86-64-linux-gnu
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2018-20657
Severity: LOW
Fixed Version: 
Link: [CVE-2018-20657](https://avd.aquasec.com/nvd/cve-2018-20657)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-20657
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-20657">https://avd.aquasec.com/nvd/cve-2018-20657</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libiberty: Memory leak in demangle_template function resulting in a denial of service
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The demangle_template function in cplus-dem.c in GNU libiberty, as distributed in GNU Binutils 2.31.1, has a memory leak via a crafted string, leading to a denial of service (memory consumption), as demonstrated by cxxfilt, a related issue to CVE-2018-12698.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-20657
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2018-20657](https://avd.aquasec.com/nvd/cve-2018-20657)
	The demangle_template function in cplus-dem.c in GNU libiberty, as distributed in GNU Binutils 2.31.1, has a memory leak via a crafted string, leading to a denial of service (memory consumption), as demonstrated by cxxfilt, a related issue to CVE-2018-12698.
    </details>



---

Package: binutils-x86-64-linux-gnu
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2019-1010204
Severity: LOW
Fixed Version: 
Link: [CVE-2019-1010204](https://avd.aquasec.com/nvd/cve-2019-1010204)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-1010204
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-1010204">https://avd.aquasec.com/nvd/cve-2019-1010204</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: Improper Input Validation, Signed/Unsigned Comparison, Out-of-bounds Read in gold/fileread.cc and elfcpp/elfcpp_file.h leads to denial of service
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    GNU binutils gold gold v1.11-v1.16 (GNU binutils v2.21-v2.31.1) is affected by: Improper Input Validation, Signed/Unsigned Comparison, Out-of-bounds Read. The impact is: Denial of service. The component is: gold/fileread.cc:497, elfcpp/elfcpp_file.h:644. The attack vector is: An ELF file with an invalid e_shoff header field must be opened.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-1010204
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2019-1010204](https://avd.aquasec.com/nvd/cve-2019-1010204)
	GNU binutils gold gold v1.11-v1.16 (GNU binutils v2.21-v2.31.1) is affected by: Improper Input Validation, Signed/Unsigned Comparison, Out-of-bounds Read. The impact is: Denial of service. The component is: gold/fileread.cc:497, elfcpp/elfcpp_file.h:644. The attack vector is: An ELF file with an invalid e_shoff header field must be opened.
    </details>



---

Package: binutils-x86-64-linux-gnu
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2021-45078
Severity: LOW
Fixed Version: 
Link: [CVE-2021-45078](https://avd.aquasec.com/nvd/cve-2021-45078)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-45078
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-45078">https://avd.aquasec.com/nvd/cve-2021-45078</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: out-of-bounds write in stab_xcoff_builtin_type() in stabs.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    stab_xcoff_builtin_type in stabs.c in GNU Binutils through 2.37 allows attackers to cause a denial of service (heap-based buffer overflow) or possibly have unspecified other impact, as demonstrated by an out-of-bounds write. NOTE: this issue exists because of an incorrect fix for CVE-2018-12699.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-45078
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2021-45078](https://avd.aquasec.com/nvd/cve-2021-45078)
	stab_xcoff_builtin_type in stabs.c in GNU Binutils through 2.37 allows attackers to cause a denial of service (heap-based buffer overflow) or possibly have unspecified other impact, as demonstrated by an out-of-bounds write. NOTE: this issue exists because of an incorrect fix for CVE-2018-12699.
    </details>



---

Package: binutils-x86-64-linux-gnu
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2021-46195
Severity: LOW
Fixed Version: 
Link: [CVE-2021-46195](https://avd.aquasec.com/nvd/cve-2021-46195)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-46195
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-46195">https://avd.aquasec.com/nvd/cve-2021-46195</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gcc: uncontrolled recursion in libiberty/rust-demangle.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    GCC v12.0 was discovered to contain an uncontrolled recursion via the component libiberty/rust-demangle.c. This vulnerability allows attackers to cause a Denial of Service (DoS) by consuming excessive CPU and memory resources.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-46195
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2021-46195](https://avd.aquasec.com/nvd/cve-2021-46195)
	GCC v12.0 was discovered to contain an uncontrolled recursion via the component libiberty/rust-demangle.c. This vulnerability allows attackers to cause a Denial of Service (DoS) by consuming excessive CPU and memory resources.
    </details>



---

Package: coreutils
Installed Version: 8.28-1ubuntu1
Vulnerability CVE-2016-2781
Severity: LOW
Fixed Version: 
Link: [CVE-2016-2781](https://avd.aquasec.com/nvd/cve-2016-2781)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2016-2781
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2016-2781">https://avd.aquasec.com/nvd/cve-2016-2781</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    coreutils: Non-privileged session can escape to the parent session in chroot
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    chroot in GNU coreutils, when used with --userspec, allows local users to escape to the parent session via a crafted TIOCSTI ioctl call, which pushes characters to the terminal&amp;#39;s input buffer.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2016-2781
	Severity: LOW
	Package: coreutils
	Fixed Version: 
	Link: [CVE-2016-2781](https://avd.aquasec.com/nvd/cve-2016-2781)
	chroot in GNU coreutils, when used with --userspec, allows local users to escape to the parent session via a crafted TIOCSTI ioctl call, which pushes characters to the terminal&#39;s input buffer.
    </details>



---

Package: dirmngr
Installed Version: 2.2.4-1ubuntu1.6
Vulnerability CVE-2022-3219
Severity: LOW
Fixed Version: 
Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3219
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3219">https://avd.aquasec.com/nvd/cve-2022-3219</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gnupg: denial of service issue (resource consumption) using compressed packets
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No description is available for this CVE.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3219
	Severity: LOW
	Package: gpgv
	Fixed Version: 
	Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)
	No description is available for this CVE.
    </details>



---

Package: git
Installed Version: 1:2.17.1-1ubuntu0.12
Vulnerability CVE-2018-1000021
Severity: LOW
Fixed Version: 
Link: [CVE-2018-1000021](https://avd.aquasec.com/nvd/cve-2018-1000021)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-1000021
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-1000021">https://avd.aquasec.com/nvd/cve-2018-1000021</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    git: client prints server-sent ANSI escape codes to the terminal, allowing for unverified messages to potentially execute arbitrary commands
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    GIT version 2.15.1 and earlier contains a Input Validation Error vulnerability in Client that can result in problems including messing up terminal configuration to RCE. This attack appear to be exploitable via The user must interact with a malicious git server, (or have their traffic modified in a MITM attack).
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-1000021
	Severity: LOW
	Package: git-man
	Fixed Version: 
	Link: [CVE-2018-1000021](https://avd.aquasec.com/nvd/cve-2018-1000021)
	GIT version 2.15.1 and earlier contains a Input Validation Error vulnerability in Client that can result in problems including messing up terminal configuration to RCE. This attack appear to be exploitable via The user must interact with a malicious git server, (or have their traffic modified in a MITM attack).
    </details>



---

Package: git-man
Installed Version: 1:2.17.1-1ubuntu0.12
Vulnerability CVE-2018-1000021
Severity: LOW
Fixed Version: 
Link: [CVE-2018-1000021](https://avd.aquasec.com/nvd/cve-2018-1000021)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-1000021
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-1000021">https://avd.aquasec.com/nvd/cve-2018-1000021</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    git: client prints server-sent ANSI escape codes to the terminal, allowing for unverified messages to potentially execute arbitrary commands
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    GIT version 2.15.1 and earlier contains a Input Validation Error vulnerability in Client that can result in problems including messing up terminal configuration to RCE. This attack appear to be exploitable via The user must interact with a malicious git server, (or have their traffic modified in a MITM attack).
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-1000021
	Severity: LOW
	Package: git-man
	Fixed Version: 
	Link: [CVE-2018-1000021](https://avd.aquasec.com/nvd/cve-2018-1000021)
	GIT version 2.15.1 and earlier contains a Input Validation Error vulnerability in Client that can result in problems including messing up terminal configuration to RCE. This attack appear to be exploitable via The user must interact with a malicious git server, (or have their traffic modified in a MITM attack).
    </details>



---

Package: gnupg
Installed Version: 2.2.4-1ubuntu1.6
Vulnerability CVE-2022-3219
Severity: LOW
Fixed Version: 
Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3219
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3219">https://avd.aquasec.com/nvd/cve-2022-3219</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gnupg: denial of service issue (resource consumption) using compressed packets
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No description is available for this CVE.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3219
	Severity: LOW
	Package: gpgv
	Fixed Version: 
	Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)
	No description is available for this CVE.
    </details>



---

Package: gnupg-l10n
Installed Version: 2.2.4-1ubuntu1.6
Vulnerability CVE-2022-3219
Severity: LOW
Fixed Version: 
Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3219
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3219">https://avd.aquasec.com/nvd/cve-2022-3219</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gnupg: denial of service issue (resource consumption) using compressed packets
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No description is available for this CVE.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3219
	Severity: LOW
	Package: gpgv
	Fixed Version: 
	Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)
	No description is available for this CVE.
    </details>



---

Package: gnupg-utils
Installed Version: 2.2.4-1ubuntu1.6
Vulnerability CVE-2022-3219
Severity: LOW
Fixed Version: 
Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3219
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3219">https://avd.aquasec.com/nvd/cve-2022-3219</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gnupg: denial of service issue (resource consumption) using compressed packets
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No description is available for this CVE.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3219
	Severity: LOW
	Package: gpgv
	Fixed Version: 
	Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)
	No description is available for this CVE.
    </details>



---

Package: gpg
Installed Version: 2.2.4-1ubuntu1.6
Vulnerability CVE-2022-3219
Severity: LOW
Fixed Version: 
Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3219
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3219">https://avd.aquasec.com/nvd/cve-2022-3219</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gnupg: denial of service issue (resource consumption) using compressed packets
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No description is available for this CVE.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3219
	Severity: LOW
	Package: gpgv
	Fixed Version: 
	Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)
	No description is available for this CVE.
    </details>



---

Package: gpg-agent
Installed Version: 2.2.4-1ubuntu1.6
Vulnerability CVE-2022-3219
Severity: LOW
Fixed Version: 
Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3219
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3219">https://avd.aquasec.com/nvd/cve-2022-3219</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gnupg: denial of service issue (resource consumption) using compressed packets
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No description is available for this CVE.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3219
	Severity: LOW
	Package: gpgv
	Fixed Version: 
	Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)
	No description is available for this CVE.
    </details>



---

Package: gpg-wks-client
Installed Version: 2.2.4-1ubuntu1.6
Vulnerability CVE-2022-3219
Severity: LOW
Fixed Version: 
Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3219
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3219">https://avd.aquasec.com/nvd/cve-2022-3219</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gnupg: denial of service issue (resource consumption) using compressed packets
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No description is available for this CVE.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3219
	Severity: LOW
	Package: gpgv
	Fixed Version: 
	Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)
	No description is available for this CVE.
    </details>



---

Package: gpg-wks-server
Installed Version: 2.2.4-1ubuntu1.6
Vulnerability CVE-2022-3219
Severity: LOW
Fixed Version: 
Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3219
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3219">https://avd.aquasec.com/nvd/cve-2022-3219</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gnupg: denial of service issue (resource consumption) using compressed packets
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No description is available for this CVE.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3219
	Severity: LOW
	Package: gpgv
	Fixed Version: 
	Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)
	No description is available for this CVE.
    </details>



---

Package: gpgconf
Installed Version: 2.2.4-1ubuntu1.6
Vulnerability CVE-2022-3219
Severity: LOW
Fixed Version: 
Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3219
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3219">https://avd.aquasec.com/nvd/cve-2022-3219</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gnupg: denial of service issue (resource consumption) using compressed packets
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No description is available for this CVE.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3219
	Severity: LOW
	Package: gpgv
	Fixed Version: 
	Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)
	No description is available for this CVE.
    </details>



---

Package: gpgsm
Installed Version: 2.2.4-1ubuntu1.6
Vulnerability CVE-2022-3219
Severity: LOW
Fixed Version: 
Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3219
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3219">https://avd.aquasec.com/nvd/cve-2022-3219</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gnupg: denial of service issue (resource consumption) using compressed packets
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No description is available for this CVE.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3219
	Severity: LOW
	Package: gpgv
	Fixed Version: 
	Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)
	No description is available for this CVE.
    </details>



---

Package: gpgv
Installed Version: 2.2.4-1ubuntu1.6
Vulnerability CVE-2022-3219
Severity: LOW
Fixed Version: 
Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3219
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3219">https://avd.aquasec.com/nvd/cve-2022-3219</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gnupg: denial of service issue (resource consumption) using compressed packets
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No description is available for this CVE.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3219
	Severity: LOW
	Package: gpgv
	Fixed Version: 
	Link: [CVE-2022-3219](https://avd.aquasec.com/nvd/cve-2022-3219)
	No description is available for this CVE.
    </details>



---

Package: libasn1-8-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2019-12098
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-12098
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-12098">https://avd.aquasec.com/nvd/cve-2019-12098</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymou ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-12098
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)
	In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>



---

Package: libasn1-8-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-3671
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-3671
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-3671">https://avd.aquasec.com/nvd/cve-2021-3671</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: Null pointer dereference on missing sname in TGS-REQ
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-3671
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)
	A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>



---

Package: libbinutils
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2017-13716
Severity: LOW
Fixed Version: 
Link: [CVE-2017-13716](https://avd.aquasec.com/nvd/cve-2017-13716)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2017-13716
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2017-13716">https://avd.aquasec.com/nvd/cve-2017-13716</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: Memory leak with the C++ symbol demangler routine in libiberty
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The C++ symbol demangler routine in cplus-dem.c in libiberty, as distributed in GNU Binutils 2.29, allows remote attackers to cause a denial of service (excessive memory allocation and application crash) via a crafted file, as demonstrated by a call from the Binary File Descriptor (BFD) library (aka libbfd).
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2017-13716
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2017-13716](https://avd.aquasec.com/nvd/cve-2017-13716)
	The C++ symbol demangler routine in cplus-dem.c in libiberty, as distributed in GNU Binutils 2.29, allows remote attackers to cause a denial of service (excessive memory allocation and application crash) via a crafted file, as demonstrated by a call from the Binary File Descriptor (BFD) library (aka libbfd).
    </details>



---

Package: libbinutils
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2018-20657
Severity: LOW
Fixed Version: 
Link: [CVE-2018-20657](https://avd.aquasec.com/nvd/cve-2018-20657)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-20657
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-20657">https://avd.aquasec.com/nvd/cve-2018-20657</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libiberty: Memory leak in demangle_template function resulting in a denial of service
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The demangle_template function in cplus-dem.c in GNU libiberty, as distributed in GNU Binutils 2.31.1, has a memory leak via a crafted string, leading to a denial of service (memory consumption), as demonstrated by cxxfilt, a related issue to CVE-2018-12698.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-20657
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2018-20657](https://avd.aquasec.com/nvd/cve-2018-20657)
	The demangle_template function in cplus-dem.c in GNU libiberty, as distributed in GNU Binutils 2.31.1, has a memory leak via a crafted string, leading to a denial of service (memory consumption), as demonstrated by cxxfilt, a related issue to CVE-2018-12698.
    </details>



---

Package: libbinutils
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2019-1010204
Severity: LOW
Fixed Version: 
Link: [CVE-2019-1010204](https://avd.aquasec.com/nvd/cve-2019-1010204)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-1010204
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-1010204">https://avd.aquasec.com/nvd/cve-2019-1010204</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: Improper Input Validation, Signed/Unsigned Comparison, Out-of-bounds Read in gold/fileread.cc and elfcpp/elfcpp_file.h leads to denial of service
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    GNU binutils gold gold v1.11-v1.16 (GNU binutils v2.21-v2.31.1) is affected by: Improper Input Validation, Signed/Unsigned Comparison, Out-of-bounds Read. The impact is: Denial of service. The component is: gold/fileread.cc:497, elfcpp/elfcpp_file.h:644. The attack vector is: An ELF file with an invalid e_shoff header field must be opened.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-1010204
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2019-1010204](https://avd.aquasec.com/nvd/cve-2019-1010204)
	GNU binutils gold gold v1.11-v1.16 (GNU binutils v2.21-v2.31.1) is affected by: Improper Input Validation, Signed/Unsigned Comparison, Out-of-bounds Read. The impact is: Denial of service. The component is: gold/fileread.cc:497, elfcpp/elfcpp_file.h:644. The attack vector is: An ELF file with an invalid e_shoff header field must be opened.
    </details>



---

Package: libbinutils
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2021-45078
Severity: LOW
Fixed Version: 
Link: [CVE-2021-45078](https://avd.aquasec.com/nvd/cve-2021-45078)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-45078
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-45078">https://avd.aquasec.com/nvd/cve-2021-45078</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    binutils: out-of-bounds write in stab_xcoff_builtin_type() in stabs.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    stab_xcoff_builtin_type in stabs.c in GNU Binutils through 2.37 allows attackers to cause a denial of service (heap-based buffer overflow) or possibly have unspecified other impact, as demonstrated by an out-of-bounds write. NOTE: this issue exists because of an incorrect fix for CVE-2018-12699.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-45078
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2021-45078](https://avd.aquasec.com/nvd/cve-2021-45078)
	stab_xcoff_builtin_type in stabs.c in GNU Binutils through 2.37 allows attackers to cause a denial of service (heap-based buffer overflow) or possibly have unspecified other impact, as demonstrated by an out-of-bounds write. NOTE: this issue exists because of an incorrect fix for CVE-2018-12699.
    </details>



---

Package: libbinutils
Installed Version: 2.30-21ubuntu1~18.04.7
Vulnerability CVE-2021-46195
Severity: LOW
Fixed Version: 
Link: [CVE-2021-46195](https://avd.aquasec.com/nvd/cve-2021-46195)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-46195
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-46195">https://avd.aquasec.com/nvd/cve-2021-46195</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gcc: uncontrolled recursion in libiberty/rust-demangle.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    GCC v12.0 was discovered to contain an uncontrolled recursion via the component libiberty/rust-demangle.c. This vulnerability allows attackers to cause a Denial of Service (DoS) by consuming excessive CPU and memory resources.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-46195
	Severity: LOW
	Package: libbinutils
	Fixed Version: 
	Link: [CVE-2021-46195](https://avd.aquasec.com/nvd/cve-2021-46195)
	GCC v12.0 was discovered to contain an uncontrolled recursion via the component libiberty/rust-demangle.c. This vulnerability allows attackers to cause a Denial of Service (DoS) by consuming excessive CPU and memory resources.
    </details>



---

Package: libc-bin
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2009-5155
Severity: LOW
Fixed Version: 
Link: [CVE-2009-5155](https://avd.aquasec.com/nvd/cve-2009-5155)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2009-5155
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2009-5155">https://avd.aquasec.com/nvd/cve-2009-5155</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    glibc: parse_reg_exp in posix/regcomp.c misparses alternatives leading to denial of service or trigger incorrect result
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the GNU C Library (aka glibc or libc6) before 2.28, parse_reg_exp in posix/regcomp.c misparses alternatives, which allows attackers to cause a denial of service (assertion failure and application exit) or trigger an incorrect result by attempting a regular-expression match.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2009-5155
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2009-5155](https://avd.aquasec.com/nvd/cve-2009-5155)
	In the GNU C Library (aka glibc or libc6) before 2.28, parse_reg_exp in posix/regcomp.c misparses alternatives, which allows attackers to cause a denial of service (assertion failure and application exit) or trigger an incorrect result by attempting a regular-expression match.
    </details>



---

Package: libc-bin
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2015-8985
Severity: LOW
Fixed Version: 
Link: [CVE-2015-8985](https://avd.aquasec.com/nvd/cve-2015-8985)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2015-8985
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2015-8985">https://avd.aquasec.com/nvd/cve-2015-8985</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    glibc: potential denial of service in pop_fail_stack()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The pop_fail_stack function in the GNU C Library (aka glibc or libc6) allows context-dependent attackers to cause a denial of service (assertion failure and application crash) via vectors related to extended regular expression processing.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2015-8985
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2015-8985](https://avd.aquasec.com/nvd/cve-2015-8985)
	The pop_fail_stack function in the GNU C Library (aka glibc or libc6) allows context-dependent attackers to cause a denial of service (assertion failure and application crash) via vectors related to extended regular expression processing.
    </details>



---

Package: libc-bin
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2016-20013
Severity: LOW
Fixed Version: 
Link: [CVE-2016-20013](https://avd.aquasec.com/nvd/cve-2016-20013)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2016-20013
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2016-20013">https://avd.aquasec.com/nvd/cve-2016-20013</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    sha256crypt and sha512crypt through 0.6 allow attackers to cause a denial of service (CPU consumption) because the algorithm&amp;#39;s runtime is proportional to the square of the length of the password.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2016-20013
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2016-20013](https://avd.aquasec.com/nvd/cve-2016-20013)
	sha256crypt and sha512crypt through 0.6 allow attackers to cause a denial of service (CPU consumption) because the algorithm&#39;s runtime is proportional to the square of the length of the password.
    </details>



---

Package: libc-dev-bin
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2009-5155
Severity: LOW
Fixed Version: 
Link: [CVE-2009-5155](https://avd.aquasec.com/nvd/cve-2009-5155)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2009-5155
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2009-5155">https://avd.aquasec.com/nvd/cve-2009-5155</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    glibc: parse_reg_exp in posix/regcomp.c misparses alternatives leading to denial of service or trigger incorrect result
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the GNU C Library (aka glibc or libc6) before 2.28, parse_reg_exp in posix/regcomp.c misparses alternatives, which allows attackers to cause a denial of service (assertion failure and application exit) or trigger an incorrect result by attempting a regular-expression match.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2009-5155
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2009-5155](https://avd.aquasec.com/nvd/cve-2009-5155)
	In the GNU C Library (aka glibc or libc6) before 2.28, parse_reg_exp in posix/regcomp.c misparses alternatives, which allows attackers to cause a denial of service (assertion failure and application exit) or trigger an incorrect result by attempting a regular-expression match.
    </details>



---

Package: libc-dev-bin
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2015-8985
Severity: LOW
Fixed Version: 
Link: [CVE-2015-8985](https://avd.aquasec.com/nvd/cve-2015-8985)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2015-8985
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2015-8985">https://avd.aquasec.com/nvd/cve-2015-8985</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    glibc: potential denial of service in pop_fail_stack()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The pop_fail_stack function in the GNU C Library (aka glibc or libc6) allows context-dependent attackers to cause a denial of service (assertion failure and application crash) via vectors related to extended regular expression processing.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2015-8985
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2015-8985](https://avd.aquasec.com/nvd/cve-2015-8985)
	The pop_fail_stack function in the GNU C Library (aka glibc or libc6) allows context-dependent attackers to cause a denial of service (assertion failure and application crash) via vectors related to extended regular expression processing.
    </details>



---

Package: libc-dev-bin
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2016-20013
Severity: LOW
Fixed Version: 
Link: [CVE-2016-20013](https://avd.aquasec.com/nvd/cve-2016-20013)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2016-20013
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2016-20013">https://avd.aquasec.com/nvd/cve-2016-20013</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    sha256crypt and sha512crypt through 0.6 allow attackers to cause a denial of service (CPU consumption) because the algorithm&amp;#39;s runtime is proportional to the square of the length of the password.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2016-20013
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2016-20013](https://avd.aquasec.com/nvd/cve-2016-20013)
	sha256crypt and sha512crypt through 0.6 allow attackers to cause a denial of service (CPU consumption) because the algorithm&#39;s runtime is proportional to the square of the length of the password.
    </details>



---

Package: libc6
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2009-5155
Severity: LOW
Fixed Version: 
Link: [CVE-2009-5155](https://avd.aquasec.com/nvd/cve-2009-5155)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2009-5155
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2009-5155">https://avd.aquasec.com/nvd/cve-2009-5155</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    glibc: parse_reg_exp in posix/regcomp.c misparses alternatives leading to denial of service or trigger incorrect result
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the GNU C Library (aka glibc or libc6) before 2.28, parse_reg_exp in posix/regcomp.c misparses alternatives, which allows attackers to cause a denial of service (assertion failure and application exit) or trigger an incorrect result by attempting a regular-expression match.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2009-5155
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2009-5155](https://avd.aquasec.com/nvd/cve-2009-5155)
	In the GNU C Library (aka glibc or libc6) before 2.28, parse_reg_exp in posix/regcomp.c misparses alternatives, which allows attackers to cause a denial of service (assertion failure and application exit) or trigger an incorrect result by attempting a regular-expression match.
    </details>



---

Package: libc6
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2015-8985
Severity: LOW
Fixed Version: 
Link: [CVE-2015-8985](https://avd.aquasec.com/nvd/cve-2015-8985)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2015-8985
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2015-8985">https://avd.aquasec.com/nvd/cve-2015-8985</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    glibc: potential denial of service in pop_fail_stack()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The pop_fail_stack function in the GNU C Library (aka glibc or libc6) allows context-dependent attackers to cause a denial of service (assertion failure and application crash) via vectors related to extended regular expression processing.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2015-8985
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2015-8985](https://avd.aquasec.com/nvd/cve-2015-8985)
	The pop_fail_stack function in the GNU C Library (aka glibc or libc6) allows context-dependent attackers to cause a denial of service (assertion failure and application crash) via vectors related to extended regular expression processing.
    </details>



---

Package: libc6
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2016-20013
Severity: LOW
Fixed Version: 
Link: [CVE-2016-20013](https://avd.aquasec.com/nvd/cve-2016-20013)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2016-20013
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2016-20013">https://avd.aquasec.com/nvd/cve-2016-20013</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    sha256crypt and sha512crypt through 0.6 allow attackers to cause a denial of service (CPU consumption) because the algorithm&amp;#39;s runtime is proportional to the square of the length of the password.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2016-20013
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2016-20013](https://avd.aquasec.com/nvd/cve-2016-20013)
	sha256crypt and sha512crypt through 0.6 allow attackers to cause a denial of service (CPU consumption) because the algorithm&#39;s runtime is proportional to the square of the length of the password.
    </details>



---

Package: libc6-dev
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2009-5155
Severity: LOW
Fixed Version: 
Link: [CVE-2009-5155](https://avd.aquasec.com/nvd/cve-2009-5155)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2009-5155
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2009-5155">https://avd.aquasec.com/nvd/cve-2009-5155</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    glibc: parse_reg_exp in posix/regcomp.c misparses alternatives leading to denial of service or trigger incorrect result
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the GNU C Library (aka glibc or libc6) before 2.28, parse_reg_exp in posix/regcomp.c misparses alternatives, which allows attackers to cause a denial of service (assertion failure and application exit) or trigger an incorrect result by attempting a regular-expression match.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2009-5155
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2009-5155](https://avd.aquasec.com/nvd/cve-2009-5155)
	In the GNU C Library (aka glibc or libc6) before 2.28, parse_reg_exp in posix/regcomp.c misparses alternatives, which allows attackers to cause a denial of service (assertion failure and application exit) or trigger an incorrect result by attempting a regular-expression match.
    </details>



---

Package: libc6-dev
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2015-8985
Severity: LOW
Fixed Version: 
Link: [CVE-2015-8985](https://avd.aquasec.com/nvd/cve-2015-8985)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2015-8985
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2015-8985">https://avd.aquasec.com/nvd/cve-2015-8985</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    glibc: potential denial of service in pop_fail_stack()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The pop_fail_stack function in the GNU C Library (aka glibc or libc6) allows context-dependent attackers to cause a denial of service (assertion failure and application crash) via vectors related to extended regular expression processing.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2015-8985
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2015-8985](https://avd.aquasec.com/nvd/cve-2015-8985)
	The pop_fail_stack function in the GNU C Library (aka glibc or libc6) allows context-dependent attackers to cause a denial of service (assertion failure and application crash) via vectors related to extended regular expression processing.
    </details>



---

Package: libc6-dev
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2016-20013
Severity: LOW
Fixed Version: 
Link: [CVE-2016-20013](https://avd.aquasec.com/nvd/cve-2016-20013)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2016-20013
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2016-20013">https://avd.aquasec.com/nvd/cve-2016-20013</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    sha256crypt and sha512crypt through 0.6 allow attackers to cause a denial of service (CPU consumption) because the algorithm&amp;#39;s runtime is proportional to the square of the length of the password.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2016-20013
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2016-20013](https://avd.aquasec.com/nvd/cve-2016-20013)
	sha256crypt and sha512crypt through 0.6 allow attackers to cause a denial of service (CPU consumption) because the algorithm&#39;s runtime is proportional to the square of the length of the password.
    </details>



---

Package: libgmp10
Installed Version: 2:6.1.2+dfsg-2
Vulnerability CVE-2021-43618
Severity: LOW
Fixed Version: 2:6.1.2+dfsg-2ubuntu0.1
Link: [CVE-2021-43618](https://avd.aquasec.com/nvd/cve-2021-43618)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-43618
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-43618">https://avd.aquasec.com/nvd/cve-2021-43618</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    gmp: Integer overflow and resultant buffer overflow via crafted input
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    GNU Multiple Precision Arithmetic Library (GMP) through 6.2.1 has an mpz/inp_raw.c integer overflow and resultant buffer overflow via crafted input, leading to a segmentation fault on 32-bit platforms.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-43618
	Severity: LOW
	Package: libgmp10
	Fixed Version: 2:6.1.2+dfsg-2ubuntu0.1
	Link: [CVE-2021-43618](https://avd.aquasec.com/nvd/cve-2021-43618)
	GNU Multiple Precision Arithmetic Library (GMP) through 6.2.1 has an mpz/inp_raw.c integer overflow and resultant buffer overflow via crafted input, leading to a segmentation fault on 32-bit platforms.
    </details>



---

Package: libgssapi3-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2019-12098
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-12098
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-12098">https://avd.aquasec.com/nvd/cve-2019-12098</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymou ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-12098
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)
	In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>



---

Package: libgssapi3-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-3671
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-3671
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-3671">https://avd.aquasec.com/nvd/cve-2021-3671</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: Null pointer dereference on missing sname in TGS-REQ
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-3671
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)
	A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>



---

Package: libhcrypto4-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2019-12098
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-12098
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-12098">https://avd.aquasec.com/nvd/cve-2019-12098</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymou ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-12098
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)
	In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>



---

Package: libhcrypto4-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-3671
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-3671
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-3671">https://avd.aquasec.com/nvd/cve-2021-3671</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: Null pointer dereference on missing sname in TGS-REQ
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-3671
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)
	A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>



---

Package: libheimbase1-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2019-12098
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-12098
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-12098">https://avd.aquasec.com/nvd/cve-2019-12098</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymou ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-12098
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)
	In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>



---

Package: libheimbase1-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-3671
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-3671
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-3671">https://avd.aquasec.com/nvd/cve-2021-3671</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: Null pointer dereference on missing sname in TGS-REQ
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-3671
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)
	A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>



---

Package: libheimntlm0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2019-12098
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-12098
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-12098">https://avd.aquasec.com/nvd/cve-2019-12098</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymou ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-12098
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)
	In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>



---

Package: libheimntlm0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-3671
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-3671
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-3671">https://avd.aquasec.com/nvd/cve-2021-3671</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: Null pointer dereference on missing sname in TGS-REQ
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-3671
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)
	A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>



---

Package: libhx509-5-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2019-12098
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-12098
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-12098">https://avd.aquasec.com/nvd/cve-2019-12098</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymou ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-12098
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)
	In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>



---

Package: libhx509-5-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-3671
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-3671
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-3671">https://avd.aquasec.com/nvd/cve-2021-3671</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: Null pointer dereference on missing sname in TGS-REQ
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-3671
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)
	A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>



---

Package: libjpeg-turbo8
Installed Version: 1.5.2-0ubuntu5.18.04.4
Vulnerability CVE-2018-11813
Severity: LOW
Fixed Version: 1.5.2-0ubuntu5.18.04.6
Link: [CVE-2018-11813](https://avd.aquasec.com/nvd/cve-2018-11813)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-11813
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-11813">https://avd.aquasec.com/nvd/cve-2018-11813</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libjpeg: &amp;#34;cjpeg&amp;#34; utility large loop because read_pixel in rdtarga.c mishandles EOF
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    libjpeg 9c has a large loop because read_pixel in rdtarga.c mishandles EOF.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-11813
	Severity: LOW
	Package: libjpeg-turbo8-dev
	Fixed Version: 1.5.2-0ubuntu5.18.04.6
	Link: [CVE-2018-11813](https://avd.aquasec.com/nvd/cve-2018-11813)
	libjpeg 9c has a large loop because read_pixel in rdtarga.c mishandles EOF.
    </details>



---

Package: libjpeg-turbo8
Installed Version: 1.5.2-0ubuntu5.18.04.4
Vulnerability CVE-2020-17541
Severity: LOW
Fixed Version: 1.5.2-0ubuntu5.18.04.6
Link: [CVE-2020-17541](https://avd.aquasec.com/nvd/cve-2020-17541)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-17541
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-17541">https://avd.aquasec.com/nvd/cve-2020-17541</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libjpeg-turbo: Stack-based buffer overflow in the &amp;#34;transform&amp;#34; component
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Libjpeg-turbo all version have a stack-based buffer overflow in the &amp;#34;transform&amp;#34; component. A remote attacker can send a malformed jpeg file to the service and cause arbitrary code execution or denial of service of the target service.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-17541
	Severity: LOW
	Package: libjpeg-turbo8-dev
	Fixed Version: 1.5.2-0ubuntu5.18.04.6
	Link: [CVE-2020-17541](https://avd.aquasec.com/nvd/cve-2020-17541)
	Libjpeg-turbo all version have a stack-based buffer overflow in the &#34;transform&#34; component. A remote attacker can send a malformed jpeg file to the service and cause arbitrary code execution or denial of service of the target service.
    </details>



---

Package: libjpeg-turbo8
Installed Version: 1.5.2-0ubuntu5.18.04.4
Vulnerability CVE-2022-32325
Severity: LOW
Fixed Version: 
Link: [CVE-2022-32325](https://avd.aquasec.com/nvd/cve-2022-32325)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-32325
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-32325">https://avd.aquasec.com/nvd/cve-2022-32325</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    JPEGOPTIM v1.4.7 was discovered to contain a segmentation violation wh ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    JPEGOPTIM v1.4.7 was discovered to contain a segmentation violation which is caused by a READ memory access at jpegoptim.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-32325
	Severity: LOW
	Package: libjpeg-turbo8-dev
	Fixed Version: 
	Link: [CVE-2022-32325](https://avd.aquasec.com/nvd/cve-2022-32325)
	JPEGOPTIM v1.4.7 was discovered to contain a segmentation violation which is caused by a READ memory access at jpegoptim.c.
    </details>



---

Package: libjpeg-turbo8-dev
Installed Version: 1.5.2-0ubuntu5.18.04.4
Vulnerability CVE-2018-11813
Severity: LOW
Fixed Version: 1.5.2-0ubuntu5.18.04.6
Link: [CVE-2018-11813](https://avd.aquasec.com/nvd/cve-2018-11813)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-11813
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-11813">https://avd.aquasec.com/nvd/cve-2018-11813</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libjpeg: &amp;#34;cjpeg&amp;#34; utility large loop because read_pixel in rdtarga.c mishandles EOF
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    libjpeg 9c has a large loop because read_pixel in rdtarga.c mishandles EOF.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-11813
	Severity: LOW
	Package: libjpeg-turbo8-dev
	Fixed Version: 1.5.2-0ubuntu5.18.04.6
	Link: [CVE-2018-11813](https://avd.aquasec.com/nvd/cve-2018-11813)
	libjpeg 9c has a large loop because read_pixel in rdtarga.c mishandles EOF.
    </details>



---

Package: libjpeg-turbo8-dev
Installed Version: 1.5.2-0ubuntu5.18.04.4
Vulnerability CVE-2020-17541
Severity: LOW
Fixed Version: 1.5.2-0ubuntu5.18.04.6
Link: [CVE-2020-17541](https://avd.aquasec.com/nvd/cve-2020-17541)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-17541
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-17541">https://avd.aquasec.com/nvd/cve-2020-17541</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libjpeg-turbo: Stack-based buffer overflow in the &amp;#34;transform&amp;#34; component
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Libjpeg-turbo all version have a stack-based buffer overflow in the &amp;#34;transform&amp;#34; component. A remote attacker can send a malformed jpeg file to the service and cause arbitrary code execution or denial of service of the target service.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-17541
	Severity: LOW
	Package: libjpeg-turbo8-dev
	Fixed Version: 1.5.2-0ubuntu5.18.04.6
	Link: [CVE-2020-17541](https://avd.aquasec.com/nvd/cve-2020-17541)
	Libjpeg-turbo all version have a stack-based buffer overflow in the &#34;transform&#34; component. A remote attacker can send a malformed jpeg file to the service and cause arbitrary code execution or denial of service of the target service.
    </details>



---

Package: libjpeg-turbo8-dev
Installed Version: 1.5.2-0ubuntu5.18.04.4
Vulnerability CVE-2022-32325
Severity: LOW
Fixed Version: 
Link: [CVE-2022-32325](https://avd.aquasec.com/nvd/cve-2022-32325)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-32325
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-32325">https://avd.aquasec.com/nvd/cve-2022-32325</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    JPEGOPTIM v1.4.7 was discovered to contain a segmentation violation wh ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    JPEGOPTIM v1.4.7 was discovered to contain a segmentation violation which is caused by a READ memory access at jpegoptim.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-32325
	Severity: LOW
	Package: libjpeg-turbo8-dev
	Fixed Version: 
	Link: [CVE-2022-32325](https://avd.aquasec.com/nvd/cve-2022-32325)
	JPEGOPTIM v1.4.7 was discovered to contain a segmentation violation which is caused by a READ memory access at jpegoptim.c.
    </details>



---

Package: libkrb5-26-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2019-12098
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-12098
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-12098">https://avd.aquasec.com/nvd/cve-2019-12098</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymou ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-12098
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)
	In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>



---

Package: libkrb5-26-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-3671
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-3671
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-3671">https://avd.aquasec.com/nvd/cve-2021-3671</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: Null pointer dereference on missing sname in TGS-REQ
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-3671
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)
	A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>



---

Package: libncurses5
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2019-17594
Severity: LOW
Fixed Version: 
Link: [CVE-2019-17594](https://avd.aquasec.com/nvd/cve-2019-17594)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-17594
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-17594">https://avd.aquasec.com/nvd/cve-2019-17594</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in the _nc_find_entry function in tinfo/comp_hash.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    There is a heap-based buffer over-read in the _nc_find_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-17594
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2019-17594](https://avd.aquasec.com/nvd/cve-2019-17594)
	There is a heap-based buffer over-read in the _nc_find_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>



---

Package: libncurses5
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2019-17595
Severity: LOW
Fixed Version: 
Link: [CVE-2019-17595](https://avd.aquasec.com/nvd/cve-2019-17595)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-17595
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-17595">https://avd.aquasec.com/nvd/cve-2019-17595</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in the fmt_entry function in tinfo/comp_hash.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    There is a heap-based buffer over-read in the fmt_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-17595
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2019-17595](https://avd.aquasec.com/nvd/cve-2019-17595)
	There is a heap-based buffer over-read in the fmt_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>



---

Package: libncurses5
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2021-39537
Severity: LOW
Fixed Version: 
Link: [CVE-2021-39537](https://avd.aquasec.com/nvd/cve-2021-39537)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-39537
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-39537">https://avd.aquasec.com/nvd/cve-2021-39537</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in _nc_captoinfo() in captoinfo.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in ncurses through v6.2-1. _nc_captoinfo in captoinfo.c has a heap-based buffer overflow.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-39537
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2021-39537](https://avd.aquasec.com/nvd/cve-2021-39537)
	An issue was discovered in ncurses through v6.2-1. _nc_captoinfo in captoinfo.c has a heap-based buffer overflow.
    </details>



---

Package: libncurses5
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2022-29458
Severity: LOW
Fixed Version: 
Link: [CVE-2022-29458](https://avd.aquasec.com/nvd/cve-2022-29458)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-29458
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-29458">https://avd.aquasec.com/nvd/cve-2022-29458</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: segfaulting OOB read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ncurses 6.3 before patch 20220416 has an out-of-bounds read and segmentation violation in convert_strings in tinfo/read_entry.c in the terminfo library.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-29458
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2022-29458](https://avd.aquasec.com/nvd/cve-2022-29458)
	ncurses 6.3 before patch 20220416 has an out-of-bounds read and segmentation violation in convert_strings in tinfo/read_entry.c in the terminfo library.
    </details>



---

Package: libncursesw5
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2019-17594
Severity: LOW
Fixed Version: 
Link: [CVE-2019-17594](https://avd.aquasec.com/nvd/cve-2019-17594)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-17594
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-17594">https://avd.aquasec.com/nvd/cve-2019-17594</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in the _nc_find_entry function in tinfo/comp_hash.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    There is a heap-based buffer over-read in the _nc_find_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-17594
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2019-17594](https://avd.aquasec.com/nvd/cve-2019-17594)
	There is a heap-based buffer over-read in the _nc_find_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>



---

Package: libncursesw5
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2019-17595
Severity: LOW
Fixed Version: 
Link: [CVE-2019-17595](https://avd.aquasec.com/nvd/cve-2019-17595)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-17595
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-17595">https://avd.aquasec.com/nvd/cve-2019-17595</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in the fmt_entry function in tinfo/comp_hash.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    There is a heap-based buffer over-read in the fmt_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-17595
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2019-17595](https://avd.aquasec.com/nvd/cve-2019-17595)
	There is a heap-based buffer over-read in the fmt_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>



---

Package: libncursesw5
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2021-39537
Severity: LOW
Fixed Version: 
Link: [CVE-2021-39537](https://avd.aquasec.com/nvd/cve-2021-39537)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-39537
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-39537">https://avd.aquasec.com/nvd/cve-2021-39537</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in _nc_captoinfo() in captoinfo.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in ncurses through v6.2-1. _nc_captoinfo in captoinfo.c has a heap-based buffer overflow.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-39537
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2021-39537](https://avd.aquasec.com/nvd/cve-2021-39537)
	An issue was discovered in ncurses through v6.2-1. _nc_captoinfo in captoinfo.c has a heap-based buffer overflow.
    </details>



---

Package: libncursesw5
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2022-29458
Severity: LOW
Fixed Version: 
Link: [CVE-2022-29458](https://avd.aquasec.com/nvd/cve-2022-29458)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-29458
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-29458">https://avd.aquasec.com/nvd/cve-2022-29458</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: segfaulting OOB read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ncurses 6.3 before patch 20220416 has an out-of-bounds read and segmentation violation in convert_strings in tinfo/read_entry.c in the terminfo library.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-29458
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2022-29458](https://avd.aquasec.com/nvd/cve-2022-29458)
	ncurses 6.3 before patch 20220416 has an out-of-bounds read and segmentation violation in convert_strings in tinfo/read_entry.c in the terminfo library.
    </details>



---

Package: libpcre16-3
Installed Version: 2:8.39-9ubuntu0.1
Vulnerability CVE-2017-11164
Severity: LOW
Fixed Version: 
Link: [CVE-2017-11164](https://avd.aquasec.com/nvd/cve-2017-11164)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2017-11164
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2017-11164">https://avd.aquasec.com/nvd/cve-2017-11164</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    pcre: OP_KETRMAX feature in the match function in pcre_exec.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In PCRE 8.41, the OP_KETRMAX feature in the match function in pcre_exec.c allows stack exhaustion (uncontrolled recursion) when processing a crafted regular expression.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2017-11164
	Severity: LOW
	Package: libpcrecpp0v5
	Fixed Version: 
	Link: [CVE-2017-11164](https://avd.aquasec.com/nvd/cve-2017-11164)
	In PCRE 8.41, the OP_KETRMAX feature in the match function in pcre_exec.c allows stack exhaustion (uncontrolled recursion) when processing a crafted regular expression.
    </details>



---

Package: libpcre3
Installed Version: 2:8.39-9ubuntu0.1
Vulnerability CVE-2017-11164
Severity: LOW
Fixed Version: 
Link: [CVE-2017-11164](https://avd.aquasec.com/nvd/cve-2017-11164)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2017-11164
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2017-11164">https://avd.aquasec.com/nvd/cve-2017-11164</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    pcre: OP_KETRMAX feature in the match function in pcre_exec.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In PCRE 8.41, the OP_KETRMAX feature in the match function in pcre_exec.c allows stack exhaustion (uncontrolled recursion) when processing a crafted regular expression.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2017-11164
	Severity: LOW
	Package: libpcrecpp0v5
	Fixed Version: 
	Link: [CVE-2017-11164](https://avd.aquasec.com/nvd/cve-2017-11164)
	In PCRE 8.41, the OP_KETRMAX feature in the match function in pcre_exec.c allows stack exhaustion (uncontrolled recursion) when processing a crafted regular expression.
    </details>



---

Package: libpcre3-dev
Installed Version: 2:8.39-9ubuntu0.1
Vulnerability CVE-2017-11164
Severity: LOW
Fixed Version: 
Link: [CVE-2017-11164](https://avd.aquasec.com/nvd/cve-2017-11164)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2017-11164
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2017-11164">https://avd.aquasec.com/nvd/cve-2017-11164</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    pcre: OP_KETRMAX feature in the match function in pcre_exec.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In PCRE 8.41, the OP_KETRMAX feature in the match function in pcre_exec.c allows stack exhaustion (uncontrolled recursion) when processing a crafted regular expression.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2017-11164
	Severity: LOW
	Package: libpcrecpp0v5
	Fixed Version: 
	Link: [CVE-2017-11164](https://avd.aquasec.com/nvd/cve-2017-11164)
	In PCRE 8.41, the OP_KETRMAX feature in the match function in pcre_exec.c allows stack exhaustion (uncontrolled recursion) when processing a crafted regular expression.
    </details>



---

Package: libpcre32-3
Installed Version: 2:8.39-9ubuntu0.1
Vulnerability CVE-2017-11164
Severity: LOW
Fixed Version: 
Link: [CVE-2017-11164](https://avd.aquasec.com/nvd/cve-2017-11164)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2017-11164
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2017-11164">https://avd.aquasec.com/nvd/cve-2017-11164</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    pcre: OP_KETRMAX feature in the match function in pcre_exec.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In PCRE 8.41, the OP_KETRMAX feature in the match function in pcre_exec.c allows stack exhaustion (uncontrolled recursion) when processing a crafted regular expression.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2017-11164
	Severity: LOW
	Package: libpcrecpp0v5
	Fixed Version: 
	Link: [CVE-2017-11164](https://avd.aquasec.com/nvd/cve-2017-11164)
	In PCRE 8.41, the OP_KETRMAX feature in the match function in pcre_exec.c allows stack exhaustion (uncontrolled recursion) when processing a crafted regular expression.
    </details>



---

Package: libpcrecpp0v5
Installed Version: 2:8.39-9ubuntu0.1
Vulnerability CVE-2017-11164
Severity: LOW
Fixed Version: 
Link: [CVE-2017-11164](https://avd.aquasec.com/nvd/cve-2017-11164)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2017-11164
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2017-11164">https://avd.aquasec.com/nvd/cve-2017-11164</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    pcre: OP_KETRMAX feature in the match function in pcre_exec.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In PCRE 8.41, the OP_KETRMAX feature in the match function in pcre_exec.c allows stack exhaustion (uncontrolled recursion) when processing a crafted regular expression.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2017-11164
	Severity: LOW
	Package: libpcrecpp0v5
	Fixed Version: 
	Link: [CVE-2017-11164](https://avd.aquasec.com/nvd/cve-2017-11164)
	In PCRE 8.41, the OP_KETRMAX feature in the match function in pcre_exec.c allows stack exhaustion (uncontrolled recursion) when processing a crafted regular expression.
    </details>



---

Package: libpng16-16
Installed Version: 1.6.34-1ubuntu0.18.04.2
Vulnerability CVE-2018-14048
Severity: LOW
Fixed Version: 
Link: [CVE-2018-14048](https://avd.aquasec.com/nvd/cve-2018-14048)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-14048
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-14048">https://avd.aquasec.com/nvd/cve-2018-14048</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libpng: Segmentation fault in png.c:png_free_data function causing denial of service
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue has been found in libpng 1.6.34. It is a SEGV in the function png_free_data in png.c, related to the recommended error handling for png_read_image.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-14048
	Severity: LOW
	Package: libpng16-16
	Fixed Version: 
	Link: [CVE-2018-14048](https://avd.aquasec.com/nvd/cve-2018-14048)
	An issue has been found in libpng 1.6.34. It is a SEGV in the function png_free_data in png.c, related to the recommended error handling for png_read_image.
    </details>



---

Package: libpng16-16
Installed Version: 1.6.34-1ubuntu0.18.04.2
Vulnerability CVE-2022-3857
Severity: LOW
Fixed Version: 
Link: [CVE-2022-3857](https://avd.aquasec.com/nvd/cve-2022-3857)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3857
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3857">https://avd.aquasec.com/nvd/cve-2022-3857</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    libpng: Null pointer dereference leads to segmentation fault
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    No description is available for this CVE.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3857
	Severity: LOW
	Package: libpng16-16
	Fixed Version: 
	Link: [CVE-2022-3857](https://avd.aquasec.com/nvd/cve-2022-3857)
	No description is available for this CVE.
    </details>



---

Package: libpython3.6
Installed Version: 3.6.9-1~18.04ubuntu1.8
Vulnerability CVE-2021-28861
Severity: LOW
Fixed Version: 
Link: [CVE-2021-28861](https://avd.aquasec.com/nvd/cve-2021-28861)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-28861
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-28861">https://avd.aquasec.com/nvd/cve-2021-28861</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python: open redirection vulnerability in lib/http/server.py may lead to information disclosure
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ** DISPUTED ** Python 3.x through 3.10 has an open redirection vulnerability in lib/http/server.py due to no protection against multiple (/) at the beginning of URI path which may leads to information disclosure. NOTE: this is disputed by a third party because the http.server.html documentation page states &amp;#34;Warning: http.server is not recommended for production. It only implements basic security checks.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-28861
	Severity: LOW
	Package: python3.6-minimal
	Fixed Version: 
	Link: [CVE-2021-28861](https://avd.aquasec.com/nvd/cve-2021-28861)
	** DISPUTED ** Python 3.x through 3.10 has an open redirection vulnerability in lib/http/server.py due to no protection against multiple (/) at the beginning of URI path which may leads to information disclosure. NOTE: this is disputed by a third party because the http.server.html documentation page states &#34;Warning: http.server is not recommended for production. It only implements basic security checks.&#34;
    </details>



---

Package: libpython3.6-minimal
Installed Version: 3.6.9-1~18.04ubuntu1.8
Vulnerability CVE-2021-28861
Severity: LOW
Fixed Version: 
Link: [CVE-2021-28861](https://avd.aquasec.com/nvd/cve-2021-28861)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-28861
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-28861">https://avd.aquasec.com/nvd/cve-2021-28861</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python: open redirection vulnerability in lib/http/server.py may lead to information disclosure
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ** DISPUTED ** Python 3.x through 3.10 has an open redirection vulnerability in lib/http/server.py due to no protection against multiple (/) at the beginning of URI path which may leads to information disclosure. NOTE: this is disputed by a third party because the http.server.html documentation page states &amp;#34;Warning: http.server is not recommended for production. It only implements basic security checks.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-28861
	Severity: LOW
	Package: python3.6-minimal
	Fixed Version: 
	Link: [CVE-2021-28861](https://avd.aquasec.com/nvd/cve-2021-28861)
	** DISPUTED ** Python 3.x through 3.10 has an open redirection vulnerability in lib/http/server.py due to no protection against multiple (/) at the beginning of URI path which may leads to information disclosure. NOTE: this is disputed by a third party because the http.server.html documentation page states &#34;Warning: http.server is not recommended for production. It only implements basic security checks.&#34;
    </details>



---

Package: libpython3.6-stdlib
Installed Version: 3.6.9-1~18.04ubuntu1.8
Vulnerability CVE-2021-28861
Severity: LOW
Fixed Version: 
Link: [CVE-2021-28861](https://avd.aquasec.com/nvd/cve-2021-28861)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-28861
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-28861">https://avd.aquasec.com/nvd/cve-2021-28861</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python: open redirection vulnerability in lib/http/server.py may lead to information disclosure
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ** DISPUTED ** Python 3.x through 3.10 has an open redirection vulnerability in lib/http/server.py due to no protection against multiple (/) at the beginning of URI path which may leads to information disclosure. NOTE: this is disputed by a third party because the http.server.html documentation page states &amp;#34;Warning: http.server is not recommended for production. It only implements basic security checks.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-28861
	Severity: LOW
	Package: python3.6-minimal
	Fixed Version: 
	Link: [CVE-2021-28861](https://avd.aquasec.com/nvd/cve-2021-28861)
	** DISPUTED ** Python 3.x through 3.10 has an open redirection vulnerability in lib/http/server.py due to no protection against multiple (/) at the beginning of URI path which may leads to information disclosure. NOTE: this is disputed by a third party because the http.server.html documentation page states &#34;Warning: http.server is not recommended for production. It only implements basic security checks.&#34;
    </details>



---

Package: libroken18-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2019-12098
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-12098
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-12098">https://avd.aquasec.com/nvd/cve-2019-12098</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymou ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-12098
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)
	In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>



---

Package: libroken18-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-3671
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-3671
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-3671">https://avd.aquasec.com/nvd/cve-2021-3671</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: Null pointer dereference on missing sname in TGS-REQ
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-3671
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)
	A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>



---

Package: libtinfo5
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2019-17594
Severity: LOW
Fixed Version: 
Link: [CVE-2019-17594](https://avd.aquasec.com/nvd/cve-2019-17594)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-17594
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-17594">https://avd.aquasec.com/nvd/cve-2019-17594</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in the _nc_find_entry function in tinfo/comp_hash.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    There is a heap-based buffer over-read in the _nc_find_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-17594
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2019-17594](https://avd.aquasec.com/nvd/cve-2019-17594)
	There is a heap-based buffer over-read in the _nc_find_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>



---

Package: libtinfo5
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2019-17595
Severity: LOW
Fixed Version: 
Link: [CVE-2019-17595](https://avd.aquasec.com/nvd/cve-2019-17595)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-17595
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-17595">https://avd.aquasec.com/nvd/cve-2019-17595</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in the fmt_entry function in tinfo/comp_hash.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    There is a heap-based buffer over-read in the fmt_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-17595
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2019-17595](https://avd.aquasec.com/nvd/cve-2019-17595)
	There is a heap-based buffer over-read in the fmt_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>



---

Package: libtinfo5
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2021-39537
Severity: LOW
Fixed Version: 
Link: [CVE-2021-39537](https://avd.aquasec.com/nvd/cve-2021-39537)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-39537
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-39537">https://avd.aquasec.com/nvd/cve-2021-39537</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in _nc_captoinfo() in captoinfo.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in ncurses through v6.2-1. _nc_captoinfo in captoinfo.c has a heap-based buffer overflow.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-39537
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2021-39537](https://avd.aquasec.com/nvd/cve-2021-39537)
	An issue was discovered in ncurses through v6.2-1. _nc_captoinfo in captoinfo.c has a heap-based buffer overflow.
    </details>



---

Package: libtinfo5
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2022-29458
Severity: LOW
Fixed Version: 
Link: [CVE-2022-29458](https://avd.aquasec.com/nvd/cve-2022-29458)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-29458
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-29458">https://avd.aquasec.com/nvd/cve-2022-29458</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: segfaulting OOB read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ncurses 6.3 before patch 20220416 has an out-of-bounds read and segmentation violation in convert_strings in tinfo/read_entry.c in the terminfo library.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-29458
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2022-29458](https://avd.aquasec.com/nvd/cve-2022-29458)
	ncurses 6.3 before patch 20220416 has an out-of-bounds read and segmentation violation in convert_strings in tinfo/read_entry.c in the terminfo library.
    </details>



---

Package: libwind0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2019-12098
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-12098
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-12098">https://avd.aquasec.com/nvd/cve-2019-12098</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymou ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-12098
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2019-12098](https://avd.aquasec.com/nvd/cve-2019-12098)
	In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.
    </details>



---

Package: libwind0-heimdal
Installed Version: 7.5.0+dfsg-1
Vulnerability CVE-2021-3671
Severity: LOW
Fixed Version: 7.5.0+dfsg-1ubuntu0.1
Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-3671
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-3671">https://avd.aquasec.com/nvd/cve-2021-3671</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    samba: Null pointer dereference on missing sname in TGS-REQ
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-3671
	Severity: LOW
	Package: libwind0-heimdal
	Fixed Version: 7.5.0+dfsg-1ubuntu0.1
	Link: [CVE-2021-3671](https://avd.aquasec.com/nvd/cve-2021-3671)
	A null pointer de-reference was found in the way samba kerberos server handled missing sname in TGS-REQ (Ticket Granting Server - Request). An authenticated user could use this flaw to crash the samba server.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2016-10723
Severity: LOW
Fixed Version: 
Link: [CVE-2016-10723](https://avd.aquasec.com/nvd/cve-2016-10723)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2016-10723
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2016-10723">https://avd.aquasec.com/nvd/cve-2016-10723</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ** DISPUTED ** An issue was discovered in the Linux kernel through 4.1 ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ** DISPUTED ** An issue was discovered in the Linux kernel through 4.17.2. Since the page allocator does not yield CPU resources to the owner of the oom_lock mutex, a local unprivileged user can trivially lock up the system forever by wasting CPU resources from the page allocator (e.g., via concurrent page fault events) when the global OOM killer is invoked. NOTE: the software maintainer has not accepted certain proposed patches, in part because of a viewpoint that &amp;#34;the underlying problem is non-trivial to handle.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2016-10723
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2016-10723](https://avd.aquasec.com/nvd/cve-2016-10723)
	** DISPUTED ** An issue was discovered in the Linux kernel through 4.17.2. Since the page allocator does not yield CPU resources to the owner of the oom_lock mutex, a local unprivileged user can trivially lock up the system forever by wasting CPU resources from the page allocator (e.g., via concurrent page fault events) when the global OOM killer is invoked. NOTE: the software maintainer has not accepted certain proposed patches, in part because of a viewpoint that &#34;the underlying problem is non-trivial to handle.&#34;
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2017-0537
Severity: LOW
Fixed Version: 
Link: [CVE-2017-0537](https://avd.aquasec.com/nvd/cve-2017-0537)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2017-0537
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2017-0537">https://avd.aquasec.com/nvd/cve-2017-0537</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An information disclosure vulnerability in the kernel USB gadget driver could enable a local malicious application to access data outside of its permission levels. This issue is rated as Moderate because it first requires compromising a privileged process. Product: Android. Versions: Kernel-3.18. Android ID: A-31614969.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2017-0537
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2017-0537](https://avd.aquasec.com/nvd/cve-2017-0537)
	An information disclosure vulnerability in the kernel USB gadget driver could enable a local malicious application to access data outside of its permission levels. This issue is rated as Moderate because it first requires compromising a privileged process. Product: Android. Versions: Kernel-3.18. Android ID: A-31614969.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2017-13165
Severity: LOW
Fixed Version: 
Link: [CVE-2017-13165](https://avd.aquasec.com/nvd/cve-2017-13165)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2017-13165
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2017-13165">https://avd.aquasec.com/nvd/cve-2017-13165</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An elevation of privilege vulnerability in the kernel file system. Product: Android. Versions: Android kernel. Android ID A-31269937.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2017-13165
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2017-13165](https://avd.aquasec.com/nvd/cve-2017-13165)
	An elevation of privilege vulnerability in the kernel file system. Product: Android. Versions: Android kernel. Android ID A-31269937.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2017-13693
Severity: LOW
Fixed Version: 
Link: [CVE-2017-13693](https://avd.aquasec.com/nvd/cve-2017-13693)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2017-13693
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2017-13693">https://avd.aquasec.com/nvd/cve-2017-13693</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ACPI operand cache leak in dsutils.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The acpi_ds_create_operands() function in drivers/acpi/acpica/dsutils.c in the Linux kernel through 4.12.9 does not flush the operand cache and causes a kernel stack dump, which allows local users to obtain sensitive information from kernel memory and bypass the KASLR protection mechanism (in the kernel through 4.9) via a crafted ACPI table.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2017-13693
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2017-13693](https://avd.aquasec.com/nvd/cve-2017-13693)
	The acpi_ds_create_operands() function in drivers/acpi/acpica/dsutils.c in the Linux kernel through 4.12.9 does not flush the operand cache and causes a kernel stack dump, which allows local users to obtain sensitive information from kernel memory and bypass the KASLR protection mechanism (in the kernel through 4.9) via a crafted ACPI table.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2018-1121
Severity: LOW
Fixed Version: 
Link: [CVE-2018-1121](https://avd.aquasec.com/nvd/cve-2018-1121)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-1121
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-1121">https://avd.aquasec.com/nvd/cve-2018-1121</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    procps-ng, procps: process hiding through race condition enumerating /proc
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    procps-ng, procps is vulnerable to a process hiding through race condition. Since the kernel&amp;#39;s proc_pid_readdir() returns PID entries in ascending numeric order, a process occupying a high PID can use inotify events to determine when the process list is being scanned, and fork/exec to obtain a lower PID, thus avoiding enumeration. An unprivileged attacker can hide a process from procps-ng&amp;#39;s utilities by exploiting a race condition in reading /proc/PID entries. This vulnerability affects procps and procps-ng up to version 3.3.15, newer versions might be affected also.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-1121
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2018-1121](https://avd.aquasec.com/nvd/cve-2018-1121)
	procps-ng, procps is vulnerable to a process hiding through race condition. Since the kernel&#39;s proc_pid_readdir() returns PID entries in ascending numeric order, a process occupying a high PID can use inotify events to determine when the process list is being scanned, and fork/exec to obtain a lower PID, thus avoiding enumeration. An unprivileged attacker can hide a process from procps-ng&#39;s utilities by exploiting a race condition in reading /proc/PID entries. This vulnerability affects procps and procps-ng up to version 3.3.15, newer versions might be affected also.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2018-12928
Severity: LOW
Fixed Version: 
Link: [CVE-2018-12928](https://avd.aquasec.com/nvd/cve-2018-12928)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-12928
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-12928">https://avd.aquasec.com/nvd/cve-2018-12928</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: NULL pointer dereference in hfs_ext_read_extent in hfs.ko
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the Linux kernel 4.15.0, a NULL pointer dereference was discovered in hfs_ext_read_extent in hfs.ko. This can occur during a mount of a crafted hfs filesystem.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-12928
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2018-12928](https://avd.aquasec.com/nvd/cve-2018-12928)
	In the Linux kernel 4.15.0, a NULL pointer dereference was discovered in hfs_ext_read_extent in hfs.ko. This can occur during a mount of a crafted hfs filesystem.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2018-12929
Severity: LOW
Fixed Version: 
Link: [CVE-2018-12929](https://avd.aquasec.com/nvd/cve-2018-12929)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-12929
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-12929">https://avd.aquasec.com/nvd/cve-2018-12929</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: use-after-free in ntfs_read_locked_inode in the ntfs.ko
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ntfs_read_locked_inode in the ntfs.ko filesystem driver in the Linux kernel 4.15.0 allows attackers to trigger a use-after-free read and possibly cause a denial of service (kernel oops or panic) via a crafted ntfs filesystem.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-12929
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2018-12929](https://avd.aquasec.com/nvd/cve-2018-12929)
	ntfs_read_locked_inode in the ntfs.ko filesystem driver in the Linux kernel 4.15.0 allows attackers to trigger a use-after-free read and possibly cause a denial of service (kernel oops or panic) via a crafted ntfs filesystem.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2018-12930
Severity: LOW
Fixed Version: 
Link: [CVE-2018-12930](https://avd.aquasec.com/nvd/cve-2018-12930)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-12930
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-12930">https://avd.aquasec.com/nvd/cve-2018-12930</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: stack-based out-of-bounds write in ntfs_end_buffer_async_read in the ntfs.ko
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ntfs_end_buffer_async_read in the ntfs.ko filesystem driver in the Linux kernel 4.15.0 allows attackers to trigger a stack-based out-of-bounds write and cause a denial of service (kernel oops or panic) or possibly have unspecified other impact via a crafted ntfs filesystem.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-12930
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2018-12930](https://avd.aquasec.com/nvd/cve-2018-12930)
	ntfs_end_buffer_async_read in the ntfs.ko filesystem driver in the Linux kernel 4.15.0 allows attackers to trigger a stack-based out-of-bounds write and cause a denial of service (kernel oops or panic) or possibly have unspecified other impact via a crafted ntfs filesystem.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2018-12931
Severity: LOW
Fixed Version: 
Link: [CVE-2018-12931](https://avd.aquasec.com/nvd/cve-2018-12931)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-12931
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-12931">https://avd.aquasec.com/nvd/cve-2018-12931</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: stack-based out-of-bounds write in ntfs_attr_find in the ntfs.ko
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ntfs_attr_find in the ntfs.ko filesystem driver in the Linux kernel 4.15.0 allows attackers to trigger a stack-based out-of-bounds write and cause a denial of service (kernel oops or panic) or possibly have unspecified other impact via a crafted ntfs filesystem.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-12931
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2018-12931](https://avd.aquasec.com/nvd/cve-2018-12931)
	ntfs_attr_find in the ntfs.ko filesystem driver in the Linux kernel 4.15.0 allows attackers to trigger a stack-based out-of-bounds write and cause a denial of service (kernel oops or panic) or possibly have unspecified other impact via a crafted ntfs filesystem.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2019-14899
Severity: LOW
Fixed Version: 
Link: [CVE-2019-14899](https://avd.aquasec.com/nvd/cve-2019-14899)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-14899
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-14899">https://avd.aquasec.com/nvd/cve-2019-14899</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    VPN: an attacker can inject data into the TCP stream which allows a hijack of active connections inside the VPN tunnel
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was discovered in Linux, FreeBSD, OpenBSD, MacOS, iOS, and Android that allows a malicious access point, or an adjacent user, to determine if a connected user is using a VPN, make positive inferences about the websites they are visiting, and determine the correct sequence and acknowledgement numbers in use, allowing the bad actor to inject data into the TCP stream. This provides everything that is needed for an attacker to hijack active connections inside the VPN tunnel.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-14899
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2019-14899](https://avd.aquasec.com/nvd/cve-2019-14899)
	A vulnerability was discovered in Linux, FreeBSD, OpenBSD, MacOS, iOS, and Android that allows a malicious access point, or an adjacent user, to determine if a connected user is using a VPN, make positive inferences about the websites they are visiting, and determine the correct sequence and acknowledgement numbers in use, allowing the bad actor to inject data into the TCP stream. This provides everything that is needed for an attacker to hijack active connections inside the VPN tunnel.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2019-15213
Severity: LOW
Fixed Version: 
Link: [CVE-2019-15213](https://avd.aquasec.com/nvd/cve-2019-15213)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-15213
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-15213">https://avd.aquasec.com/nvd/cve-2019-15213</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: use-after-free caused by malicious USB device in drivers/media/usb/dvb-usb/dvb-usb-init.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in the Linux kernel before 5.2.3. There is a use-after-free caused by a malicious USB device in the drivers/media/usb/dvb-usb/dvb-usb-init.c driver.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-15213
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2019-15213](https://avd.aquasec.com/nvd/cve-2019-15213)
	An issue was discovered in the Linux kernel before 5.2.3. There is a use-after-free caused by a malicious USB device in the drivers/media/usb/dvb-usb/dvb-usb-init.c driver.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2019-16230
Severity: LOW
Fixed Version: 
Link: [CVE-2019-16230](https://avd.aquasec.com/nvd/cve-2019-16230)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-16230
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-16230">https://avd.aquasec.com/nvd/cve-2019-16230</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: null pointer dereference in drivers/gpu/drm/radeon/radeon_display.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ** DISPUTED ** drivers/gpu/drm/radeon/radeon_display.c in the Linux kernel 5.2.14 does not check the alloc_workqueue return value, leading to a NULL pointer dereference. NOTE: A third-party software maintainer states that the work queue allocation is happening during device initialization, which for a graphics card occurs during boot. It is not attacker controllable and OOM at that time is highly unlikely.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-16230
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2019-16230](https://avd.aquasec.com/nvd/cve-2019-16230)
	** DISPUTED ** drivers/gpu/drm/radeon/radeon_display.c in the Linux kernel 5.2.14 does not check the alloc_workqueue return value, leading to a NULL pointer dereference. NOTE: A third-party software maintainer states that the work queue allocation is happening during device initialization, which for a graphics card occurs during boot. It is not attacker controllable and OOM at that time is highly unlikely.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2019-19378
Severity: LOW
Fixed Version: 
Link: [CVE-2019-19378](https://avd.aquasec.com/nvd/cve-2019-19378)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-19378
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-19378">https://avd.aquasec.com/nvd/cve-2019-19378</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: out-of-bounds write in index_rbio_pages in fs/btrfs/raid56.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the Linux kernel 5.0.21, mounting a crafted btrfs filesystem image can lead to slab-out-of-bounds write access in index_rbio_pages in fs/btrfs/raid56.c.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-19378
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2019-19378](https://avd.aquasec.com/nvd/cve-2019-19378)
	In the Linux kernel 5.0.21, mounting a crafted btrfs filesystem image can lead to slab-out-of-bounds write access in index_rbio_pages in fs/btrfs/raid56.c.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2019-19814
Severity: LOW
Fixed Version: 
Link: [CVE-2019-19814](https://avd.aquasec.com/nvd/cve-2019-19814)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-19814
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-19814">https://avd.aquasec.com/nvd/cve-2019-19814</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: out-of-bounds write in __remove_dirty_segment in fs/f2fs/segment.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the Linux kernel 5.0.21, mounting a crafted f2fs filesystem image can cause __remove_dirty_segment slab-out-of-bounds write access because an array is bounded by the number of dirty types (8) but the array index can exceed this.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-19814
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2019-19814](https://avd.aquasec.com/nvd/cve-2019-19814)
	In the Linux kernel 5.0.21, mounting a crafted f2fs filesystem image can cause __remove_dirty_segment slab-out-of-bounds write access because an array is bounded by the number of dirty types (8) but the array index can exceed this.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2019-19815
Severity: LOW
Fixed Version: 
Link: [CVE-2019-19815](https://avd.aquasec.com/nvd/cve-2019-19815)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-19815
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-19815">https://avd.aquasec.com/nvd/cve-2019-19815</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: NULL pointer dereference in f2fs_recover_fsync_data in fs/f2fs/recovery.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the Linux kernel 5.0.21, mounting a crafted f2fs filesystem image can cause a NULL pointer dereference in f2fs_recover_fsync_data in fs/f2fs/recovery.c. This is related to F2FS_P_SB in fs/f2fs/f2fs.h.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-19815
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2019-19815](https://avd.aquasec.com/nvd/cve-2019-19815)
	In the Linux kernel 5.0.21, mounting a crafted f2fs filesystem image can cause a NULL pointer dereference in f2fs_recover_fsync_data in fs/f2fs/recovery.c. This is related to F2FS_P_SB in fs/f2fs/f2fs.h.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2019-20425
Severity: LOW
Fixed Version: 
Link: [CVE-2019-20425](https://avd.aquasec.com/nvd/cve-2019-20425)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-20425
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-20425">https://avd.aquasec.com/nvd/cve-2019-20425</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the Lustre file system before 2.12.3, the ptlrpc module has an out-of-bounds access and panic due to the lack of validation for specific fields of packets sent by a client. In the function lustre_msg_string, there is no validation of a certain length value derived from lustre_msg_buflen_v2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-20425
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2019-20425](https://avd.aquasec.com/nvd/cve-2019-20425)
	In the Lustre file system before 2.12.3, the ptlrpc module has an out-of-bounds access and panic due to the lack of validation for specific fields of packets sent by a client. In the function lustre_msg_string, there is no validation of a certain length value derived from lustre_msg_buflen_v2.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2019-20429
Severity: LOW
Fixed Version: 
Link: [CVE-2019-20429](https://avd.aquasec.com/nvd/cve-2019-20429)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-20429
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-20429">https://avd.aquasec.com/nvd/cve-2019-20429</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the Lustre file system before 2.12.3, the ptlrpc module has an out-of-bounds read and panic (via a modified lm_bufcount field) due to the lack of validation for specific fields of packets sent by a client. This is caused by interaction between sptlrpc_svc_unwrap_request and lustre_msg_hdr_size_v2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-20429
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2019-20429](https://avd.aquasec.com/nvd/cve-2019-20429)
	In the Lustre file system before 2.12.3, the ptlrpc module has an out-of-bounds read and panic (via a modified lm_bufcount field) due to the lack of validation for specific fields of packets sent by a client. This is caused by interaction between sptlrpc_svc_unwrap_request and lustre_msg_hdr_size_v2.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2020-11725
Severity: LOW
Fixed Version: 
Link: [CVE-2020-11725](https://avd.aquasec.com/nvd/cve-2020-11725)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-11725
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-11725">https://avd.aquasec.com/nvd/cve-2020-11725</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: improper handling of private_size*count multiplication due to count=info-&amp;gt;owner typo
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ** DISPUTED ** snd_ctl_elem_add in sound/core/control.c in the Linux kernel through 5.6.3 has a count=info-&amp;gt;owner line, which later affects a private_size*count multiplication for unspecified &amp;#34;interesting side effects.&amp;#34; NOTE: kernel engineers dispute this finding, because it could be relevant only if new callers were added that were unfamiliar with the misuse of the info-&amp;gt;owner field to represent data unrelated to the &amp;#34;owner&amp;#34; concept. The existing callers, SNDRV_CTL_IOCTL_ELEM_ADD and SNDRV_CTL_IOCTL_ELEM_REPLACE, have been designed to misuse the info-&amp;gt;owner field in a safe way.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-11725
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2020-11725](https://avd.aquasec.com/nvd/cve-2020-11725)
	** DISPUTED ** snd_ctl_elem_add in sound/core/control.c in the Linux kernel through 5.6.3 has a count=info-&gt;owner line, which later affects a private_size*count multiplication for unspecified &#34;interesting side effects.&#34; NOTE: kernel engineers dispute this finding, because it could be relevant only if new callers were added that were unfamiliar with the misuse of the info-&gt;owner field to represent data unrelated to the &#34;owner&#34; concept. The existing callers, SNDRV_CTL_IOCTL_ELEM_ADD and SNDRV_CTL_IOCTL_ELEM_REPLACE, have been designed to misuse the info-&gt;owner field in a safe way.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2020-12363
Severity: LOW
Fixed Version: 
Link: [CVE-2020-12363](https://avd.aquasec.com/nvd/cve-2020-12363)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-12363
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-12363">https://avd.aquasec.com/nvd/cve-2020-12363</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: Improper input validation in some Intel(R) Graphics Drivers
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Improper input validation in some Intel(R) Graphics Drivers for Windows* before version 26.20.100.7212 and before Linux kernel version 5.5 may allow a privileged user to potentially enable a denial of service via local access.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-12363
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2020-12363](https://avd.aquasec.com/nvd/cve-2020-12363)
	Improper input validation in some Intel(R) Graphics Drivers for Windows* before version 26.20.100.7212 and before Linux kernel version 5.5 may allow a privileged user to potentially enable a denial of service via local access.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2020-12364
Severity: LOW
Fixed Version: 
Link: [CVE-2020-12364](https://avd.aquasec.com/nvd/cve-2020-12364)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-12364
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-12364">https://avd.aquasec.com/nvd/cve-2020-12364</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: Null pointer dereference in some Intel(R) Graphics Drivers
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Null pointer reference in some Intel(R) Graphics Drivers for Windows* before version 26.20.100.7212 and before version Linux kernel version 5.5 may allow a privileged user to potentially enable a denial of service via local access.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-12364
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2020-12364](https://avd.aquasec.com/nvd/cve-2020-12364)
	Null pointer reference in some Intel(R) Graphics Drivers for Windows* before version 26.20.100.7212 and before version Linux kernel version 5.5 may allow a privileged user to potentially enable a denial of service via local access.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2020-14304
Severity: LOW
Fixed Version: 
Link: [CVE-2020-14304](https://avd.aquasec.com/nvd/cve-2020-14304)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-14304
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-14304">https://avd.aquasec.com/nvd/cve-2020-14304</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: ethtool when reading eeprom of device could lead to memory leak
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A memory disclosure flaw was found in the Linux kernel&amp;#39;s ethernet drivers, in the way it read data from the EEPROM of the device. This flaw allows a local user to read uninitialized values from the kernel memory. The highest threat from this vulnerability is to confidentiality.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-14304
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2020-14304](https://avd.aquasec.com/nvd/cve-2020-14304)
	A memory disclosure flaw was found in the Linux kernel&#39;s ethernet drivers, in the way it read data from the EEPROM of the device. This flaw allows a local user to read uninitialized values from the kernel memory. The highest threat from this vulnerability is to confidentiality.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2020-27820
Severity: LOW
Fixed Version: 
Link: [CVE-2020-27820](https://avd.aquasec.com/nvd/cve-2020-27820)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-27820
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-27820">https://avd.aquasec.com/nvd/cve-2020-27820</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: use-after-free in nouveau kernel module
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in Linux kernel, where a use-after-frees in nouveau&amp;#39;s postclose() handler could happen if removing device (that is not common to remove video card physically without power-off, but same happens if &amp;#34;unbind&amp;#34; the driver).
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-27820
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2020-27820](https://avd.aquasec.com/nvd/cve-2020-27820)
	A vulnerability was found in Linux kernel, where a use-after-frees in nouveau&#39;s postclose() handler could happen if removing device (that is not common to remove video card physically without power-off, but same happens if &#34;unbind&#34; the driver).
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2020-35501
Severity: LOW
Fixed Version: 
Link: [CVE-2020-35501](https://avd.aquasec.com/nvd/cve-2020-35501)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-35501
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-35501">https://avd.aquasec.com/nvd/cve-2020-35501</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: audit not logging access to syscall open_by_handle_at for users with CAP_DAC_READ_SEARCH capability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in the Linux kernels implementation of audit rules, where a syscall can unexpectedly not be correctly not be logged by the audit subsystem
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-35501
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2020-35501](https://avd.aquasec.com/nvd/cve-2020-35501)
	A flaw was found in the Linux kernels implementation of audit rules, where a syscall can unexpectedly not be correctly not be logged by the audit subsystem
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-32078
Severity: LOW
Fixed Version: 
Link: [CVE-2021-32078](https://avd.aquasec.com/nvd/cve-2021-32078)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-32078
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-32078">https://avd.aquasec.com/nvd/cve-2021-32078</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: out-of-bounds read in arch/arm/mach-footbridge/personal-pci.c due to improper input validation
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An Out-of-Bounds Read was discovered in arch/arm/mach-footbridge/personal-pci.c in the Linux kernel through 5.12.11 because of the lack of a check for a value that shouldn&amp;#39;t be negative, e.g., access to element -2 of an array, aka CID-298a58e165e4.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-32078
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-32078](https://avd.aquasec.com/nvd/cve-2021-32078)
	An Out-of-Bounds Read was discovered in arch/arm/mach-footbridge/personal-pci.c in the Linux kernel through 5.12.11 because of the lack of a check for a value that shouldn&#39;t be negative, e.g., access to element -2 of an array, aka CID-298a58e165e4.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-34981
Severity: LOW
Fixed Version: 
Link: [CVE-2021-34981](https://avd.aquasec.com/nvd/cve-2021-34981)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-34981
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-34981">https://avd.aquasec.com/nvd/cve-2021-34981</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: Bluetooth CMTP Module Double Free Privilege Escalation Vulnerability
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in the Linux kernel&amp;#39;s CAPI over Bluetooth connection code. An attacker with a local account can escalate privileges when CAPI (ISDN) hardware connection fails.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-34981
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-34981](https://avd.aquasec.com/nvd/cve-2021-34981)
	A flaw was found in the Linux kernel&#39;s CAPI over Bluetooth connection code. An attacker with a local account can escalate privileges when CAPI (ISDN) hardware connection fails.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-3669
Severity: LOW
Fixed Version: 
Link: [CVE-2021-3669](https://avd.aquasec.com/nvd/cve-2021-3669)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-3669
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-3669">https://avd.aquasec.com/nvd/cve-2021-3669</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: reading /proc/sysvipc/shm does not scale with large shared memory segment counts
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in the Linux kernel. Measuring usage of the shared memory does not scale with large shared memory segment counts which could lead to resource exhaustion and DoS.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-3669
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-3669](https://avd.aquasec.com/nvd/cve-2021-3669)
	A flaw was found in the Linux kernel. Measuring usage of the shared memory does not scale with large shared memory segment counts which could lead to resource exhaustion and DoS.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-39686
Severity: LOW
Fixed Version: 
Link: [CVE-2021-39686](https://avd.aquasec.com/nvd/cve-2021-39686)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-39686
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-39686">https://avd.aquasec.com/nvd/cve-2021-39686</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: race condition in the Android binder driver could lead to incorrect security checks
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In several functions of binder.c, there is a possible way to represent the wrong domain to SELinux due to a race condition. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-200688826References: Upstream kernel
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-39686
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-39686](https://avd.aquasec.com/nvd/cve-2021-39686)
	In several functions of binder.c, there is a possible way to represent the wrong domain to SELinux due to a race condition. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-200688826References: Upstream kernel
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2021-39801
Severity: LOW
Fixed Version: 
Link: [CVE-2021-39801](https://avd.aquasec.com/nvd/cve-2021-39801)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-39801
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-39801">https://avd.aquasec.com/nvd/cve-2021-39801</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In ion_ioctl of ion-ioctl.c, there is a possible use after free due to improper locking. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-209791720References: Upstream kernel
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-39801
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2021-39801](https://avd.aquasec.com/nvd/cve-2021-39801)
	In ion_ioctl of ion-ioctl.c, there is a possible use after free due to improper locking. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-209791720References: Upstream kernel
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-0854
Severity: LOW
Fixed Version: 
Link: [CVE-2022-0854](https://avd.aquasec.com/nvd/cve-2022-0854)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0854
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0854">https://avd.aquasec.com/nvd/cve-2022-0854</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: swiotlb information leak with DMA_FROM_DEVICE
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A memory leak flaw was found in the Linux kernel’s DMA subsystem, in the way a user calls DMA_FROM_DEVICE. This flaw allows a local user to read random memory from the kernel space.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0854
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-0854](https://avd.aquasec.com/nvd/cve-2022-0854)
	A memory leak flaw was found in the Linux kernel’s DMA subsystem, in the way a user calls DMA_FROM_DEVICE. This flaw allows a local user to read random memory from the kernel space.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-20132
Severity: LOW
Fixed Version: 
Link: [CVE-2022-20132](https://avd.aquasec.com/nvd/cve-2022-20132)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-20132
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-20132">https://avd.aquasec.com/nvd/cve-2022-20132</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    In lg_probe and related functions of hid-lg.c and other USB HID files, ...
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In lg_probe and related functions of hid-lg.c and other USB HID files, there is a possible out of bounds read due to improper input validation. This could lead to local information disclosure if a malicious USB HID device were plugged in, with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-188677105References: Upstream kernel
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-20132
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 
	Link: [CVE-2022-20132](https://avd.aquasec.com/nvd/cve-2022-20132)
	In lg_probe and related functions of hid-lg.c and other USB HID files, there is a possible out of bounds read due to improper input validation. This could lead to local information disclosure if a malicious USB HID device were plugged in, with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android kernelAndroid ID: A-188677105References: Upstream kernel
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-3565
Severity: LOW
Fixed Version: 4.15.0-200.211
Link: [CVE-2022-3565](https://avd.aquasec.com/nvd/cve-2022-3565)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3565
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3565">https://avd.aquasec.com/nvd/cve-2022-3565</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: use-after-free in l1oip timer handlers
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability, which was classified as critical, has been found in Linux Kernel. Affected by this issue is the function del_timer of the file drivers/isdn/mISDN/l1oip_core.c of the component Bluetooth. The manipulation leads to use after free. It is recommended to apply a patch to fix this issue. The identifier of this vulnerability is VDB-211088.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3565
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 4.15.0-200.211
	Link: [CVE-2022-3565](https://avd.aquasec.com/nvd/cve-2022-3565)
	A vulnerability, which was classified as critical, has been found in Linux Kernel. Affected by this issue is the function del_timer of the file drivers/isdn/mISDN/l1oip_core.c of the component Bluetooth. The manipulation leads to use after free. It is recommended to apply a patch to fix this issue. The identifier of this vulnerability is VDB-211088.
    </details>



---

Package: linux-libc-dev
Installed Version: 4.15.0-193.204
Vulnerability CVE-2022-3621
Severity: LOW
Fixed Version: 4.15.0-200.211
Link: [CVE-2022-3621](https://avd.aquasec.com/nvd/cve-2022-3621)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-3621
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-3621">https://avd.aquasec.com/nvd/cve-2022-3621</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    kernel: nilfs2: NULL pointer dereference in nilfs_bmap_lookup_at_level in fs/nilfs2/inode.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A vulnerability was found in Linux Kernel. It has been classified as problematic. Affected is the function nilfs_bmap_lookup_at_level of the file fs/nilfs2/inode.c of the component nilfs2. The manipulation leads to null pointer dereference. It is possible to launch the attack remotely. It is recommended to apply a patch to fix this issue. The identifier of this vulnerability is VDB-211920.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-3621
	Severity: LOW
	Package: linux-libc-dev
	Fixed Version: 4.15.0-200.211
	Link: [CVE-2022-3621](https://avd.aquasec.com/nvd/cve-2022-3621)
	A vulnerability was found in Linux Kernel. It has been classified as problematic. Affected is the function nilfs_bmap_lookup_at_level of the file fs/nilfs2/inode.c of the component nilfs2. The manipulation leads to null pointer dereference. It is possible to launch the attack remotely. It is recommended to apply a patch to fix this issue. The identifier of this vulnerability is VDB-211920.
    </details>



---

Package: login
Installed Version: 1:4.5-1ubuntu2.3
Vulnerability CVE-2013-4235
Severity: LOW
Fixed Version: 
Link: [CVE-2013-4235](https://avd.aquasec.com/nvd/cve-2013-4235)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2013-4235
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2013-4235">https://avd.aquasec.com/nvd/cve-2013-4235</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    shadow-utils: TOCTOU race conditions by copying and removing directory trees
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    shadow: TOCTOU (time-of-check time-of-use) race condition when copying and removing directory trees
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2013-4235
	Severity: LOW
	Package: passwd
	Fixed Version: 
	Link: [CVE-2013-4235](https://avd.aquasec.com/nvd/cve-2013-4235)
	shadow: TOCTOU (time-of-check time-of-use) race condition when copying and removing directory trees
    </details>



---

Package: multiarch-support
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2009-5155
Severity: LOW
Fixed Version: 
Link: [CVE-2009-5155](https://avd.aquasec.com/nvd/cve-2009-5155)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2009-5155
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2009-5155">https://avd.aquasec.com/nvd/cve-2009-5155</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    glibc: parse_reg_exp in posix/regcomp.c misparses alternatives leading to denial of service or trigger incorrect result
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    In the GNU C Library (aka glibc or libc6) before 2.28, parse_reg_exp in posix/regcomp.c misparses alternatives, which allows attackers to cause a denial of service (assertion failure and application exit) or trigger an incorrect result by attempting a regular-expression match.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2009-5155
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2009-5155](https://avd.aquasec.com/nvd/cve-2009-5155)
	In the GNU C Library (aka glibc or libc6) before 2.28, parse_reg_exp in posix/regcomp.c misparses alternatives, which allows attackers to cause a denial of service (assertion failure and application exit) or trigger an incorrect result by attempting a regular-expression match.
    </details>



---

Package: multiarch-support
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2015-8985
Severity: LOW
Fixed Version: 
Link: [CVE-2015-8985](https://avd.aquasec.com/nvd/cve-2015-8985)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2015-8985
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2015-8985">https://avd.aquasec.com/nvd/cve-2015-8985</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    glibc: potential denial of service in pop_fail_stack()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The pop_fail_stack function in the GNU C Library (aka glibc or libc6) allows context-dependent attackers to cause a denial of service (assertion failure and application crash) via vectors related to extended regular expression processing.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2015-8985
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2015-8985](https://avd.aquasec.com/nvd/cve-2015-8985)
	The pop_fail_stack function in the GNU C Library (aka glibc or libc6) allows context-dependent attackers to cause a denial of service (assertion failure and application crash) via vectors related to extended regular expression processing.
    </details>



---

Package: multiarch-support
Installed Version: 2.27-3ubuntu1.6
Vulnerability CVE-2016-20013
Severity: LOW
Fixed Version: 
Link: [CVE-2016-20013](https://avd.aquasec.com/nvd/cve-2016-20013)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2016-20013
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2016-20013">https://avd.aquasec.com/nvd/cve-2016-20013</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    sha256crypt and sha512crypt through 0.6 allow attackers to cause a denial of service (CPU consumption) because the algorithm&amp;#39;s runtime is proportional to the square of the length of the password.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2016-20013
	Severity: LOW
	Package: multiarch-support
	Fixed Version: 
	Link: [CVE-2016-20013](https://avd.aquasec.com/nvd/cve-2016-20013)
	sha256crypt and sha512crypt through 0.6 allow attackers to cause a denial of service (CPU consumption) because the algorithm&#39;s runtime is proportional to the square of the length of the password.
    </details>



---

Package: ncurses-base
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2019-17594
Severity: LOW
Fixed Version: 
Link: [CVE-2019-17594](https://avd.aquasec.com/nvd/cve-2019-17594)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-17594
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-17594">https://avd.aquasec.com/nvd/cve-2019-17594</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in the _nc_find_entry function in tinfo/comp_hash.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    There is a heap-based buffer over-read in the _nc_find_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-17594
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2019-17594](https://avd.aquasec.com/nvd/cve-2019-17594)
	There is a heap-based buffer over-read in the _nc_find_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>



---

Package: ncurses-base
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2019-17595
Severity: LOW
Fixed Version: 
Link: [CVE-2019-17595](https://avd.aquasec.com/nvd/cve-2019-17595)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-17595
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-17595">https://avd.aquasec.com/nvd/cve-2019-17595</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in the fmt_entry function in tinfo/comp_hash.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    There is a heap-based buffer over-read in the fmt_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-17595
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2019-17595](https://avd.aquasec.com/nvd/cve-2019-17595)
	There is a heap-based buffer over-read in the fmt_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>



---

Package: ncurses-base
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2021-39537
Severity: LOW
Fixed Version: 
Link: [CVE-2021-39537](https://avd.aquasec.com/nvd/cve-2021-39537)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-39537
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-39537">https://avd.aquasec.com/nvd/cve-2021-39537</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in _nc_captoinfo() in captoinfo.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in ncurses through v6.2-1. _nc_captoinfo in captoinfo.c has a heap-based buffer overflow.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-39537
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2021-39537](https://avd.aquasec.com/nvd/cve-2021-39537)
	An issue was discovered in ncurses through v6.2-1. _nc_captoinfo in captoinfo.c has a heap-based buffer overflow.
    </details>



---

Package: ncurses-base
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2022-29458
Severity: LOW
Fixed Version: 
Link: [CVE-2022-29458](https://avd.aquasec.com/nvd/cve-2022-29458)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-29458
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-29458">https://avd.aquasec.com/nvd/cve-2022-29458</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: segfaulting OOB read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ncurses 6.3 before patch 20220416 has an out-of-bounds read and segmentation violation in convert_strings in tinfo/read_entry.c in the terminfo library.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-29458
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2022-29458](https://avd.aquasec.com/nvd/cve-2022-29458)
	ncurses 6.3 before patch 20220416 has an out-of-bounds read and segmentation violation in convert_strings in tinfo/read_entry.c in the terminfo library.
    </details>



---

Package: ncurses-bin
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2019-17594
Severity: LOW
Fixed Version: 
Link: [CVE-2019-17594](https://avd.aquasec.com/nvd/cve-2019-17594)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-17594
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-17594">https://avd.aquasec.com/nvd/cve-2019-17594</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in the _nc_find_entry function in tinfo/comp_hash.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    There is a heap-based buffer over-read in the _nc_find_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-17594
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2019-17594](https://avd.aquasec.com/nvd/cve-2019-17594)
	There is a heap-based buffer over-read in the _nc_find_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>



---

Package: ncurses-bin
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2019-17595
Severity: LOW
Fixed Version: 
Link: [CVE-2019-17595](https://avd.aquasec.com/nvd/cve-2019-17595)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2019-17595
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2019-17595">https://avd.aquasec.com/nvd/cve-2019-17595</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in the fmt_entry function in tinfo/comp_hash.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    There is a heap-based buffer over-read in the fmt_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2019-17595
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2019-17595](https://avd.aquasec.com/nvd/cve-2019-17595)
	There is a heap-based buffer over-read in the fmt_entry function in tinfo/comp_hash.c in the terminfo library in ncurses before 6.1-20191012.
    </details>



---

Package: ncurses-bin
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2021-39537
Severity: LOW
Fixed Version: 
Link: [CVE-2021-39537](https://avd.aquasec.com/nvd/cve-2021-39537)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-39537
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-39537">https://avd.aquasec.com/nvd/cve-2021-39537</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: heap-based buffer overflow in _nc_captoinfo() in captoinfo.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An issue was discovered in ncurses through v6.2-1. _nc_captoinfo in captoinfo.c has a heap-based buffer overflow.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-39537
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2021-39537](https://avd.aquasec.com/nvd/cve-2021-39537)
	An issue was discovered in ncurses through v6.2-1. _nc_captoinfo in captoinfo.c has a heap-based buffer overflow.
    </details>



---

Package: ncurses-bin
Installed Version: 6.1-1ubuntu1.18.04
Vulnerability CVE-2022-29458
Severity: LOW
Fixed Version: 
Link: [CVE-2022-29458](https://avd.aquasec.com/nvd/cve-2022-29458)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-29458
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-29458">https://avd.aquasec.com/nvd/cve-2022-29458</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    ncurses: segfaulting OOB read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ncurses 6.3 before patch 20220416 has an out-of-bounds read and segmentation violation in convert_strings in tinfo/read_entry.c in the terminfo library.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-29458
	Severity: LOW
	Package: ncurses-bin
	Fixed Version: 
	Link: [CVE-2022-29458](https://avd.aquasec.com/nvd/cve-2022-29458)
	ncurses 6.3 before patch 20220416 has an out-of-bounds read and segmentation violation in convert_strings in tinfo/read_entry.c in the terminfo library.
    </details>



---

Package: nodejs
Installed Version: 12.22.12-1nodesource1
Vulnerability CVE-2018-12123
Severity: LOW
Fixed Version: 
Link: [CVE-2018-12123](https://avd.aquasec.com/nvd/cve-2018-12123)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-12123
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-12123">https://avd.aquasec.com/nvd/cve-2018-12123</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    nodejs: Hostname spoofing in URL parser for javascript protocol
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Node.js: All versions prior to Node.js 6.15.0, 8.14.0, 10.14.0 and 11.3.0: Hostname spoofing in URL parser for javascript protocol: If a Node.js application is using url.parse() to determine the URL hostname, that hostname can be spoofed by using a mixed case &amp;#34;javascript:&amp;#34; (e.g. &amp;#34;javAscript:&amp;#34;) protocol (other protocols are not affected). If security decisions are made about the URL based on the hostname, they may be incorrect.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-12123
	Severity: LOW
	Package: nodejs
	Fixed Version: 
	Link: [CVE-2018-12123](https://avd.aquasec.com/nvd/cve-2018-12123)
	Node.js: All versions prior to Node.js 6.15.0, 8.14.0, 10.14.0 and 11.3.0: Hostname spoofing in URL parser for javascript protocol: If a Node.js application is using url.parse() to determine the URL hostname, that hostname can be spoofed by using a mixed case &#34;javascript:&#34; (e.g. &#34;javAscript:&#34;) protocol (other protocols are not affected). If security decisions are made about the URL based on the hostname, they may be incorrect.
    </details>



---

Package: nodejs
Installed Version: 12.22.12-1nodesource1
Vulnerability CVE-2018-7159
Severity: LOW
Fixed Version: 
Link: [CVE-2018-7159](https://avd.aquasec.com/nvd/cve-2018-7159)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-7159
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-7159">https://avd.aquasec.com/nvd/cve-2018-7159</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    nodejs: HTTP parser allowed for spaces inside Content-Length header values
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The HTTP parser in all current versions of Node.js ignores spaces in the `Content-Length` header, allowing input such as `Content-Length: 1 2` to be interpreted as having a value of `12`. The HTTP specification does not allow for spaces in the `Content-Length` value and the Node.js HTTP parser has been brought into line on this particular difference. The security risk of this flaw to Node.js users is considered to be VERY LOW as it is difficult, and may be impossible, to craft an attack that makes use of this flaw in a way that could not already be achieved by supplying an incorrect value for `Content-Length`. Vulnerabilities may exist in user-code that make incorrect assumptions about the potential accuracy of this value compared to the actual length of the data supplied. Node.js users crafting lower-level HTTP utilities are advised to re-check the length of any input supplied after parsing is complete.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-7159
	Severity: LOW
	Package: nodejs
	Fixed Version: 
	Link: [CVE-2018-7159](https://avd.aquasec.com/nvd/cve-2018-7159)
	The HTTP parser in all current versions of Node.js ignores spaces in the `Content-Length` header, allowing input such as `Content-Length: 1 2` to be interpreted as having a value of `12`. The HTTP specification does not allow for spaces in the `Content-Length` value and the Node.js HTTP parser has been brought into line on this particular difference. The security risk of this flaw to Node.js users is considered to be VERY LOW as it is difficult, and may be impossible, to craft an attack that makes use of this flaw in a way that could not already be achieved by supplying an incorrect value for `Content-Length`. Vulnerabilities may exist in user-code that make incorrect assumptions about the potential accuracy of this value compared to the actual length of the data supplied. Node.js users crafting lower-level HTTP utilities are advised to re-check the length of any input supplied after parsing is complete.
    </details>



---

Package: openssh-client
Installed Version: 1:7.6p1-4ubuntu0.7
Vulnerability CVE-2020-14145
Severity: LOW
Fixed Version: 
Link: [CVE-2020-14145](https://avd.aquasec.com/nvd/cve-2020-14145)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2020-14145
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2020-14145">https://avd.aquasec.com/nvd/cve-2020-14145</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    openssh: Observable discrepancy leading to an information leak in the algorithm negotiation
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    The client side in OpenSSH 5.7 through 8.4 has an Observable Discrepancy leading to an information leak in the algorithm negotiation. This allows man-in-the-middle attackers to target initial connection attempts (where no host key for the server has been cached by the client). NOTE: some reports state that 8.5 and 8.6 are also affected.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2020-14145
	Severity: LOW
	Package: openssh-client
	Fixed Version: 
	Link: [CVE-2020-14145](https://avd.aquasec.com/nvd/cve-2020-14145)
	The client side in OpenSSH 5.7 through 8.4 has an Observable Discrepancy leading to an information leak in the algorithm negotiation. This allows man-in-the-middle attackers to target initial connection attempts (where no host key for the server has been cached by the client). NOTE: some reports state that 8.5 and 8.6 are also affected.
    </details>



---

Package: openssh-client
Installed Version: 1:7.6p1-4ubuntu0.7
Vulnerability CVE-2021-41617
Severity: LOW
Fixed Version: 
Link: [CVE-2021-41617](https://avd.aquasec.com/nvd/cve-2021-41617)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-41617
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-41617">https://avd.aquasec.com/nvd/cve-2021-41617</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    openssh: privilege escalation when AuthorizedKeysCommand or AuthorizedPrincipalsCommand are configured
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    sshd in OpenSSH 6.2 through 8.x before 8.8, when certain non-default configurations are used, allows privilege escalation because supplemental groups are not initialized as expected. Helper programs for AuthorizedKeysCommand and AuthorizedPrincipalsCommand may run with privileges associated with group memberships of the sshd process, if the configuration specifies running the command as a different user.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-41617
	Severity: LOW
	Package: openssh-client
	Fixed Version: 
	Link: [CVE-2021-41617](https://avd.aquasec.com/nvd/cve-2021-41617)
	sshd in OpenSSH 6.2 through 8.x before 8.8, when certain non-default configurations are used, allows privilege escalation because supplemental groups are not initialized as expected. Helper programs for AuthorizedKeysCommand and AuthorizedPrincipalsCommand may run with privileges associated with group memberships of the sshd process, if the configuration specifies running the command as a different user.
    </details>



---

Package: passwd
Installed Version: 1:4.5-1ubuntu2.3
Vulnerability CVE-2013-4235
Severity: LOW
Fixed Version: 
Link: [CVE-2013-4235](https://avd.aquasec.com/nvd/cve-2013-4235)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2013-4235
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2013-4235">https://avd.aquasec.com/nvd/cve-2013-4235</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    shadow-utils: TOCTOU race conditions by copying and removing directory trees
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    shadow: TOCTOU (time-of-check time-of-use) race condition when copying and removing directory trees
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2013-4235
	Severity: LOW
	Package: passwd
	Fixed Version: 
	Link: [CVE-2013-4235](https://avd.aquasec.com/nvd/cve-2013-4235)
	shadow: TOCTOU (time-of-check time-of-use) race condition when copying and removing directory trees
    </details>



---

Package: patch
Installed Version: 2.7.6-2ubuntu1.1
Vulnerability CVE-2018-6952
Severity: LOW
Fixed Version: 
Link: [CVE-2018-6952](https://avd.aquasec.com/nvd/cve-2018-6952)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2018-6952
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2018-6952">https://avd.aquasec.com/nvd/cve-2018-6952</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    patch: Double free of memory in pch.c:another_hunk() causes a crash
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A double free exists in the another_hunk function in pch.c in GNU patch through 2.7.6.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2018-6952
	Severity: LOW
	Package: patch
	Fixed Version: 
	Link: [CVE-2018-6952](https://avd.aquasec.com/nvd/cve-2018-6952)
	A double free exists in the another_hunk function in pch.c in GNU patch through 2.7.6.
    </details>



---

Package: patch
Installed Version: 2.7.6-2ubuntu1.1
Vulnerability CVE-2021-45261
Severity: LOW
Fixed Version: 
Link: [CVE-2021-45261](https://avd.aquasec.com/nvd/cve-2021-45261)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-45261
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-45261">https://avd.aquasec.com/nvd/cve-2021-45261</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    patch: Invalid Pointer via another_hunk function
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    An Invalid Pointer vulnerability exists in GNU patch 2.7 via the another_hunk function, which causes a Denial of Service.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-45261
	Severity: LOW
	Package: patch
	Fixed Version: 
	Link: [CVE-2021-45261](https://avd.aquasec.com/nvd/cve-2021-45261)
	An Invalid Pointer vulnerability exists in GNU patch 2.7 via the another_hunk function, which causes a Denial of Service.
    </details>



---

Package: python-pip
Installed Version: 9.0.1-2.3~ubuntu1.18.04.5
Vulnerability CVE-2021-3572
Severity: LOW
Fixed Version: 
Link: [CVE-2021-3572](https://avd.aquasec.com/nvd/cve-2021-3572)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-3572
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-3572">https://avd.aquasec.com/nvd/cve-2021-3572</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pip: Incorrect handling of unicode separators in git references
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in python-pip in the way it handled Unicode separators in git references. A remote attacker could possibly use this issue to install a different revision on a repository. The highest threat from this vulnerability is to data integrity. This is fixed in python-pip version 21.1.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.7
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-3572
	Severity: MEDIUM
	Package: pip
	Fixed Version: 21.1
	Link: [CVE-2021-3572](https://avd.aquasec.com/nvd/cve-2021-3572)
	A flaw was found in python-pip in the way it handled Unicode separators in git references. A remote attacker could possibly use this issue to install a different revision on a repository. The highest threat from this vulnerability is to data integrity. This is fixed in python-pip version 21.1.
    </details>



---

Package: python-pip-whl
Installed Version: 9.0.1-2.3~ubuntu1.18.04.5
Vulnerability CVE-2021-3572
Severity: LOW
Fixed Version: 
Link: [CVE-2021-3572](https://avd.aquasec.com/nvd/cve-2021-3572)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-3572
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-3572">https://avd.aquasec.com/nvd/cve-2021-3572</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python-pip: Incorrect handling of unicode separators in git references
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    A flaw was found in python-pip in the way it handled Unicode separators in git references. A remote attacker could possibly use this issue to install a different revision on a repository. The highest threat from this vulnerability is to data integrity. This is fixed in python-pip version 21.1.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    5.7
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-3572
	Severity: MEDIUM
	Package: pip
	Fixed Version: 21.1
	Link: [CVE-2021-3572](https://avd.aquasec.com/nvd/cve-2021-3572)
	A flaw was found in python-pip in the way it handled Unicode separators in git references. A remote attacker could possibly use this issue to install a different revision on a repository. The highest threat from this vulnerability is to data integrity. This is fixed in python-pip version 21.1.
    </details>



---

Package: python3.6
Installed Version: 3.6.9-1~18.04ubuntu1.8
Vulnerability CVE-2021-28861
Severity: LOW
Fixed Version: 
Link: [CVE-2021-28861](https://avd.aquasec.com/nvd/cve-2021-28861)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-28861
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-28861">https://avd.aquasec.com/nvd/cve-2021-28861</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python: open redirection vulnerability in lib/http/server.py may lead to information disclosure
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ** DISPUTED ** Python 3.x through 3.10 has an open redirection vulnerability in lib/http/server.py due to no protection against multiple (/) at the beginning of URI path which may leads to information disclosure. NOTE: this is disputed by a third party because the http.server.html documentation page states &amp;#34;Warning: http.server is not recommended for production. It only implements basic security checks.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-28861
	Severity: LOW
	Package: python3.6-minimal
	Fixed Version: 
	Link: [CVE-2021-28861](https://avd.aquasec.com/nvd/cve-2021-28861)
	** DISPUTED ** Python 3.x through 3.10 has an open redirection vulnerability in lib/http/server.py due to no protection against multiple (/) at the beginning of URI path which may leads to information disclosure. NOTE: this is disputed by a third party because the http.server.html documentation page states &#34;Warning: http.server is not recommended for production. It only implements basic security checks.&#34;
    </details>



---

Package: python3.6-minimal
Installed Version: 3.6.9-1~18.04ubuntu1.8
Vulnerability CVE-2021-28861
Severity: LOW
Fixed Version: 
Link: [CVE-2021-28861](https://avd.aquasec.com/nvd/cve-2021-28861)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-28861
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-28861">https://avd.aquasec.com/nvd/cve-2021-28861</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    python: open redirection vulnerability in lib/http/server.py may lead to information disclosure
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    ** DISPUTED ** Python 3.x through 3.10 has an open redirection vulnerability in lib/http/server.py due to no protection against multiple (/) at the beginning of URI path which may leads to information disclosure. NOTE: this is disputed by a third party because the http.server.html documentation page states &amp;#34;Warning: http.server is not recommended for production. It only implements basic security checks.&amp;#34;
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-28861
	Severity: LOW
	Package: python3.6-minimal
	Fixed Version: 
	Link: [CVE-2021-28861](https://avd.aquasec.com/nvd/cve-2021-28861)
	** DISPUTED ** Python 3.x through 3.10 has an open redirection vulnerability in lib/http/server.py due to no protection against multiple (/) at the beginning of URI path which may leads to information disclosure. NOTE: this is disputed by a third party because the http.server.html documentation page states &#34;Warning: http.server is not recommended for production. It only implements basic security checks.&#34;
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2021-4193
Severity: LOW
Fixed Version: 
Link: [CVE-2021-4193](https://avd.aquasec.com/nvd/cve-2021-4193)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-4193
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-4193">https://avd.aquasec.com/nvd/cve-2021-4193</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bound read in getvcol()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    vim is vulnerable to Out-of-bounds Read
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-4193
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2021-4193](https://avd.aquasec.com/nvd/cve-2021-4193)
	vim is vulnerable to Out-of-bounds Read
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0443
Severity: LOW
Fixed Version: 
Link: [CVE-2022-0443](https://avd.aquasec.com/nvd/cve-2022-0443)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0443
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0443">https://avd.aquasec.com/nvd/cve-2022-0443</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-use-after-free in enter_buffer() of src/buffer.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0443
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0443](https://avd.aquasec.com/nvd/cve-2022-0443)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0729
Severity: LOW
Fixed Version: 
Link: [CVE-2022-0729](https://avd.aquasec.com/nvd/cve-2022-0729)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0729
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0729">https://avd.aquasec.com/nvd/cve-2022-0729</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use of Out-of-range Pointer Offset
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4440.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0729
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0729](https://avd.aquasec.com/nvd/cve-2022-0729)
	Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4440.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1733
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1733](https://avd.aquasec.com/nvd/cve-2022-1733)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1733
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1733">https://avd.aquasec.com/nvd/cve-2022-1733</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based Buffer Overflow in cindent.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4968.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1733
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1733](https://avd.aquasec.com/nvd/cve-2022-1733)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4968.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1735
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1735](https://avd.aquasec.com/nvd/cve-2022-1735)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1735
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1735">https://avd.aquasec.com/nvd/cve-2022-1735</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: changing text in visual mode may cause invalid memory access that lead to a heap buffer overflow
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Classic Buffer Overflow in GitHub repository vim/vim prior to 8.2.4969.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1735
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1735](https://avd.aquasec.com/nvd/cve-2022-1735)
	Classic Buffer Overflow in GitHub repository vim/vim prior to 8.2.4969.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1785
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1785](https://avd.aquasec.com/nvd/cve-2022-1785)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1785
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1785">https://avd.aquasec.com/nvd/cve-2022-1785</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Out-of-bounds Write
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Write in GitHub repository vim/vim prior to 8.2.4977.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1785
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1785](https://avd.aquasec.com/nvd/cve-2022-1785)
	Out-of-bounds Write in GitHub repository vim/vim prior to 8.2.4977.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1796
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1796](https://avd.aquasec.com/nvd/cve-2022-1796)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1796
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1796">https://avd.aquasec.com/nvd/cve-2022-1796</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use After Free
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.4979.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1796
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1796](https://avd.aquasec.com/nvd/cve-2022-1796)
	Use After Free in GitHub repository vim/vim prior to 8.2.4979.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1898
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1898](https://avd.aquasec.com/nvd/cve-2022-1898)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1898
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1898">https://avd.aquasec.com/nvd/cve-2022-1898</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in find_pattern_in_path() in search.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1898
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1898](https://avd.aquasec.com/nvd/cve-2022-1898)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2124
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2124](https://avd.aquasec.com/nvd/cve-2022-2124)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2124
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2124">https://avd.aquasec.com/nvd/cve-2022-2124</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out of bounds read in current_quote()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2124
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2124](https://avd.aquasec.com/nvd/cve-2022-2124)
	Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2125
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2125](https://avd.aquasec.com/nvd/cve-2022-2125)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2125
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2125">https://avd.aquasec.com/nvd/cve-2022-2125</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based Buffer Overflow in get_lisp_indent()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2125
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2125](https://avd.aquasec.com/nvd/cve-2022-2125)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2126
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2126](https://avd.aquasec.com/nvd/cve-2022-2126)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2126
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2126">https://avd.aquasec.com/nvd/cve-2022-2126</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out of bounds read in suggest_trie_walk()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2126
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2126](https://avd.aquasec.com/nvd/cve-2022-2126)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2129
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2129](https://avd.aquasec.com/nvd/cve-2022-2129)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2129
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2129">https://avd.aquasec.com/nvd/cve-2022-2129</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out of bounds write in vim_regsub_both()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Write in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2129
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2129](https://avd.aquasec.com/nvd/cve-2022-2129)
	Out-of-bounds Write in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2206
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2206](https://avd.aquasec.com/nvd/cve-2022-2206)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2206
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2206">https://avd.aquasec.com/nvd/cve-2022-2206</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bound read in function msg_outtrans_attr
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2206
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2206](https://avd.aquasec.com/nvd/cve-2022-2206)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2581
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2581](https://avd.aquasec.com/nvd/cve-2022-2581)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2581
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2581">https://avd.aquasec.com/nvd/cve-2022-2581</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Out-of-bounds Read in vim src/regexp.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 9.0.0104.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2581
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2581](https://avd.aquasec.com/nvd/cve-2022-2581)
	Out-of-bounds Read in GitHub repository vim/vim prior to 9.0.0104.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2845
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2845](https://avd.aquasec.com/nvd/cve-2022-2845)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2845
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2845">https://avd.aquasec.com/nvd/cve-2022-2845</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Buffer Under-read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in GitHub repository vim/vim prior to 9.0.0218.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2845
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2845](https://avd.aquasec.com/nvd/cve-2022-2845)
	Buffer Over-read in GitHub repository vim/vim prior to 9.0.0218.
    </details>



---

Package: vim
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2849
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2849](https://avd.aquasec.com/nvd/cve-2022-2849)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2849
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2849">https://avd.aquasec.com/nvd/cve-2022-2849</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-based buffer overflow in latin_ptr2len() at src/mbyte.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.0220.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2849
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2849](https://avd.aquasec.com/nvd/cve-2022-2849)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.0220.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2021-4193
Severity: LOW
Fixed Version: 
Link: [CVE-2021-4193](https://avd.aquasec.com/nvd/cve-2021-4193)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-4193
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-4193">https://avd.aquasec.com/nvd/cve-2021-4193</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bound read in getvcol()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    vim is vulnerable to Out-of-bounds Read
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-4193
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2021-4193](https://avd.aquasec.com/nvd/cve-2021-4193)
	vim is vulnerable to Out-of-bounds Read
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0443
Severity: LOW
Fixed Version: 
Link: [CVE-2022-0443](https://avd.aquasec.com/nvd/cve-2022-0443)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0443
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0443">https://avd.aquasec.com/nvd/cve-2022-0443</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-use-after-free in enter_buffer() of src/buffer.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0443
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0443](https://avd.aquasec.com/nvd/cve-2022-0443)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0729
Severity: LOW
Fixed Version: 
Link: [CVE-2022-0729](https://avd.aquasec.com/nvd/cve-2022-0729)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0729
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0729">https://avd.aquasec.com/nvd/cve-2022-0729</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use of Out-of-range Pointer Offset
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4440.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0729
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0729](https://avd.aquasec.com/nvd/cve-2022-0729)
	Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4440.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1733
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1733](https://avd.aquasec.com/nvd/cve-2022-1733)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1733
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1733">https://avd.aquasec.com/nvd/cve-2022-1733</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based Buffer Overflow in cindent.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4968.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1733
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1733](https://avd.aquasec.com/nvd/cve-2022-1733)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4968.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1735
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1735](https://avd.aquasec.com/nvd/cve-2022-1735)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1735
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1735">https://avd.aquasec.com/nvd/cve-2022-1735</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: changing text in visual mode may cause invalid memory access that lead to a heap buffer overflow
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Classic Buffer Overflow in GitHub repository vim/vim prior to 8.2.4969.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1735
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1735](https://avd.aquasec.com/nvd/cve-2022-1735)
	Classic Buffer Overflow in GitHub repository vim/vim prior to 8.2.4969.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1785
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1785](https://avd.aquasec.com/nvd/cve-2022-1785)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1785
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1785">https://avd.aquasec.com/nvd/cve-2022-1785</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Out-of-bounds Write
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Write in GitHub repository vim/vim prior to 8.2.4977.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1785
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1785](https://avd.aquasec.com/nvd/cve-2022-1785)
	Out-of-bounds Write in GitHub repository vim/vim prior to 8.2.4977.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1796
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1796](https://avd.aquasec.com/nvd/cve-2022-1796)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1796
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1796">https://avd.aquasec.com/nvd/cve-2022-1796</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use After Free
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.4979.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1796
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1796](https://avd.aquasec.com/nvd/cve-2022-1796)
	Use After Free in GitHub repository vim/vim prior to 8.2.4979.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1898
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1898](https://avd.aquasec.com/nvd/cve-2022-1898)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1898
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1898">https://avd.aquasec.com/nvd/cve-2022-1898</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in find_pattern_in_path() in search.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1898
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1898](https://avd.aquasec.com/nvd/cve-2022-1898)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2124
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2124](https://avd.aquasec.com/nvd/cve-2022-2124)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2124
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2124">https://avd.aquasec.com/nvd/cve-2022-2124</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out of bounds read in current_quote()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2124
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2124](https://avd.aquasec.com/nvd/cve-2022-2124)
	Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2125
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2125](https://avd.aquasec.com/nvd/cve-2022-2125)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2125
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2125">https://avd.aquasec.com/nvd/cve-2022-2125</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based Buffer Overflow in get_lisp_indent()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2125
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2125](https://avd.aquasec.com/nvd/cve-2022-2125)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2126
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2126](https://avd.aquasec.com/nvd/cve-2022-2126)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2126
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2126">https://avd.aquasec.com/nvd/cve-2022-2126</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out of bounds read in suggest_trie_walk()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2126
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2126](https://avd.aquasec.com/nvd/cve-2022-2126)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2129
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2129](https://avd.aquasec.com/nvd/cve-2022-2129)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2129
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2129">https://avd.aquasec.com/nvd/cve-2022-2129</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out of bounds write in vim_regsub_both()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Write in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2129
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2129](https://avd.aquasec.com/nvd/cve-2022-2129)
	Out-of-bounds Write in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2206
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2206](https://avd.aquasec.com/nvd/cve-2022-2206)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2206
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2206">https://avd.aquasec.com/nvd/cve-2022-2206</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bound read in function msg_outtrans_attr
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2206
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2206](https://avd.aquasec.com/nvd/cve-2022-2206)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2581
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2581](https://avd.aquasec.com/nvd/cve-2022-2581)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2581
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2581">https://avd.aquasec.com/nvd/cve-2022-2581</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Out-of-bounds Read in vim src/regexp.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 9.0.0104.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2581
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2581](https://avd.aquasec.com/nvd/cve-2022-2581)
	Out-of-bounds Read in GitHub repository vim/vim prior to 9.0.0104.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2845
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2845](https://avd.aquasec.com/nvd/cve-2022-2845)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2845
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2845">https://avd.aquasec.com/nvd/cve-2022-2845</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Buffer Under-read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in GitHub repository vim/vim prior to 9.0.0218.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2845
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2845](https://avd.aquasec.com/nvd/cve-2022-2845)
	Buffer Over-read in GitHub repository vim/vim prior to 9.0.0218.
    </details>



---

Package: vim-common
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2849
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2849](https://avd.aquasec.com/nvd/cve-2022-2849)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2849
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2849">https://avd.aquasec.com/nvd/cve-2022-2849</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-based buffer overflow in latin_ptr2len() at src/mbyte.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.0220.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2849
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2849](https://avd.aquasec.com/nvd/cve-2022-2849)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.0220.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2021-4193
Severity: LOW
Fixed Version: 
Link: [CVE-2021-4193](https://avd.aquasec.com/nvd/cve-2021-4193)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-4193
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-4193">https://avd.aquasec.com/nvd/cve-2021-4193</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bound read in getvcol()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    vim is vulnerable to Out-of-bounds Read
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-4193
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2021-4193](https://avd.aquasec.com/nvd/cve-2021-4193)
	vim is vulnerable to Out-of-bounds Read
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0443
Severity: LOW
Fixed Version: 
Link: [CVE-2022-0443](https://avd.aquasec.com/nvd/cve-2022-0443)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0443
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0443">https://avd.aquasec.com/nvd/cve-2022-0443</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-use-after-free in enter_buffer() of src/buffer.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0443
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0443](https://avd.aquasec.com/nvd/cve-2022-0443)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0729
Severity: LOW
Fixed Version: 
Link: [CVE-2022-0729](https://avd.aquasec.com/nvd/cve-2022-0729)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0729
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0729">https://avd.aquasec.com/nvd/cve-2022-0729</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use of Out-of-range Pointer Offset
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4440.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0729
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0729](https://avd.aquasec.com/nvd/cve-2022-0729)
	Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4440.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1733
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1733](https://avd.aquasec.com/nvd/cve-2022-1733)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1733
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1733">https://avd.aquasec.com/nvd/cve-2022-1733</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based Buffer Overflow in cindent.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4968.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1733
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1733](https://avd.aquasec.com/nvd/cve-2022-1733)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4968.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1735
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1735](https://avd.aquasec.com/nvd/cve-2022-1735)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1735
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1735">https://avd.aquasec.com/nvd/cve-2022-1735</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: changing text in visual mode may cause invalid memory access that lead to a heap buffer overflow
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Classic Buffer Overflow in GitHub repository vim/vim prior to 8.2.4969.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1735
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1735](https://avd.aquasec.com/nvd/cve-2022-1735)
	Classic Buffer Overflow in GitHub repository vim/vim prior to 8.2.4969.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1785
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1785](https://avd.aquasec.com/nvd/cve-2022-1785)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1785
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1785">https://avd.aquasec.com/nvd/cve-2022-1785</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Out-of-bounds Write
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Write in GitHub repository vim/vim prior to 8.2.4977.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1785
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1785](https://avd.aquasec.com/nvd/cve-2022-1785)
	Out-of-bounds Write in GitHub repository vim/vim prior to 8.2.4977.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1796
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1796](https://avd.aquasec.com/nvd/cve-2022-1796)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1796
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1796">https://avd.aquasec.com/nvd/cve-2022-1796</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use After Free
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.4979.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1796
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1796](https://avd.aquasec.com/nvd/cve-2022-1796)
	Use After Free in GitHub repository vim/vim prior to 8.2.4979.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1898
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1898](https://avd.aquasec.com/nvd/cve-2022-1898)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1898
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1898">https://avd.aquasec.com/nvd/cve-2022-1898</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: use-after-free in find_pattern_in_path() in search.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-1898
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-1898](https://avd.aquasec.com/nvd/cve-2022-1898)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2124
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2124](https://avd.aquasec.com/nvd/cve-2022-2124)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2124
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2124">https://avd.aquasec.com/nvd/cve-2022-2124</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out of bounds read in current_quote()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2124
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2124](https://avd.aquasec.com/nvd/cve-2022-2124)
	Buffer Over-read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2125
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2125](https://avd.aquasec.com/nvd/cve-2022-2125)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2125
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2125">https://avd.aquasec.com/nvd/cve-2022-2125</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based Buffer Overflow in get_lisp_indent()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2125
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2125](https://avd.aquasec.com/nvd/cve-2022-2125)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2126
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2126](https://avd.aquasec.com/nvd/cve-2022-2126)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2126
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2126">https://avd.aquasec.com/nvd/cve-2022-2126</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out of bounds read in suggest_trie_walk()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2126
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2126](https://avd.aquasec.com/nvd/cve-2022-2126)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2129
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2129](https://avd.aquasec.com/nvd/cve-2022-2129)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2129
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2129">https://avd.aquasec.com/nvd/cve-2022-2129</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out of bounds write in vim_regsub_both()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Write in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2129
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2129](https://avd.aquasec.com/nvd/cve-2022-2129)
	Out-of-bounds Write in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2206
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2206](https://avd.aquasec.com/nvd/cve-2022-2206)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2206
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2206">https://avd.aquasec.com/nvd/cve-2022-2206</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bound read in function msg_outtrans_attr
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2206
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2206](https://avd.aquasec.com/nvd/cve-2022-2206)
	Out-of-bounds Read in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2581
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2581](https://avd.aquasec.com/nvd/cve-2022-2581)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2581
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2581">https://avd.aquasec.com/nvd/cve-2022-2581</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Out-of-bounds Read in vim src/regexp.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Out-of-bounds Read in GitHub repository vim/vim prior to 9.0.0104.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2581
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2581](https://avd.aquasec.com/nvd/cve-2022-2581)
	Out-of-bounds Read in GitHub repository vim/vim prior to 9.0.0104.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2845
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2845](https://avd.aquasec.com/nvd/cve-2022-2845)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2845
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2845">https://avd.aquasec.com/nvd/cve-2022-2845</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Buffer Under-read
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Buffer Over-read in GitHub repository vim/vim prior to 9.0.0218.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2845
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2845](https://avd.aquasec.com/nvd/cve-2022-2845)
	Buffer Over-read in GitHub repository vim/vim prior to 9.0.0218.
    </details>



---

Package: vim-runtime
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-2849
Severity: LOW
Fixed Version: 
Link: [CVE-2022-2849](https://avd.aquasec.com/nvd/cve-2022-2849)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-2849
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-2849">https://avd.aquasec.com/nvd/cve-2022-2849</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-based buffer overflow in latin_ptr2len() at src/mbyte.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.0220.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-2849
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-2849](https://avd.aquasec.com/nvd/cve-2022-2849)
	Heap-based Buffer Overflow in GitHub repository vim/vim prior to 9.0.0220.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2021-4193
Severity: LOW
Fixed Version: 
Link: [CVE-2021-4193](https://avd.aquasec.com/nvd/cve-2021-4193)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2021-4193
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2021-4193">https://avd.aquasec.com/nvd/cve-2021-4193</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: out-of-bound read in getvcol()
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    vim is vulnerable to Out-of-bounds Read
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2021-4193
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2021-4193](https://avd.aquasec.com/nvd/cve-2021-4193)
	vim is vulnerable to Out-of-bounds Read
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0443
Severity: LOW
Fixed Version: 
Link: [CVE-2022-0443](https://avd.aquasec.com/nvd/cve-2022-0443)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0443
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0443">https://avd.aquasec.com/nvd/cve-2022-0443</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: heap-use-after-free in enter_buffer() of src/buffer.c
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0443
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0443](https://avd.aquasec.com/nvd/cve-2022-0443)
	Use After Free in GitHub repository vim/vim prior to 8.2.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-0729
Severity: LOW
Fixed Version: 
Link: [CVE-2022-0729](https://avd.aquasec.com/nvd/cve-2022-0729)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-0729
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-0729">https://avd.aquasec.com/nvd/cve-2022-0729</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Use of Out-of-range Pointer Offset
    </details>


+ <details>
    <summary>Full Description</summary>
    <br>
    Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4440.
    </details>


+ <details>
    <summary>Precision</summary>
    <br>
    very-high
    </details>


+ <details>
    <summary>Security-severity</summary>
    <br>
    2.0
    </details>





+ <details>
    <summary>Help</summary>
    <br>
    Vulnerability CVE-2022-0729
	Severity: LOW
	Package: xxd
	Fixed Version: 
	Link: [CVE-2022-0729](https://avd.aquasec.com/nvd/cve-2022-0729)
	Use of Out-of-range Pointer Offset in GitHub repository vim/vim prior to 8.2.4440.
    </details>



---

Package: xxd
Installed Version: 2:8.0.1453-1ubuntu1.9
Vulnerability CVE-2022-1733
Severity: LOW
Fixed Version: 
Link: [CVE-2022-1733](https://avd.aquasec.com/nvd/cve-2022-1733)

### Locations
#### **Physical Location**
- bioinformaticsua/catalogue


- Line 1







### Level

- Note


### Rule Information

+ <details>
  <summary>Rule Id</summary>
  <br>
    CVE-2022-1733
  </details>


+ <details>
    <summary>Help Uri</summary>
    <br>
    <a href="https://avd.aquasec.com/nvd/cve-2022-1733">https://avd.aquasec.com/nvd/cve-2022-1733</a>
    </details>


+ <details>
    <summary>Short Description</summary>
    <br>
    vim: Heap-based Buffer Overflow in cindent.c
    </details>




