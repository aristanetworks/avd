# mac-security
# Table of Contents

- [MACsec](#macsec)
  - [MACsec Summary](#macsec-summary)
  - [MACsec Device Configuration](#macsec-device-configuration)

# MACsec

## MACsec Summary

License is installed.

FIPS restrictions enabled.

### MACsec Profiles Summary

**Profile A1:**

Settings:

| Cipher | Key-Server Priority | Rekey-Period | SCI |
| ------ | ------------------- | ------------ | --- |
| - | - | - | True |

Keys:


**Profile A2:**

Settings:

| Cipher | Key-Server Priority | Rekey-Period | SCI |
| ------ | ------------------- | ------------ | --- |
| - | - | - | - |

Keys:

| Key ID | Encrypted (Type 7) Key | Fallback |
| ------ | ---------------------- | -------- |
| 1234b | 12485744465E5A53 | - |

## MACsec Device Configuration

```eos
!
mac security
   license license1 123456
   fips restrictions
   !
   profile A1
      sci
   profile A2
      key 1234b 7 12485744465E5A53
```
