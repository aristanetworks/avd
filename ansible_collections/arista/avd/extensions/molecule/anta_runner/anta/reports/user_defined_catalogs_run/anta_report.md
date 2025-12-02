# ANTA Report

**Table of Contents:**

- [ANTA Report](#anta-report)
  - [Test Results Summary](#test-results-summary)
    - [Summary Totals](#summary-totals)
    - [Summary Totals Device Under Test](#summary-totals-device-under-test)
    - [Summary Totals Per Category](#summary-totals-per-category)
  - [Test Results](#test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Success | Total Tests Skipped | Total Tests Failure | Total Tests Error |
| ----------- | ------------------- | ------------------- | ------------------- | ------------------|
| 78 | 0 | 0 | 0 | 0 |

### Summary Totals Device Under Test

| Device Under Test | Total Tests | Tests Success | Tests Skipped | Tests Failure | Tests Error | Categories Skipped | Categories Failed |
| ------------------| ----------- | ------------- | ------------- | ------------- | ----------- | -------------------| ------------------|
| dc1-leaf1a | 3 | 0 | 0 | 0 | 0 | - | - |
| dc1-leaf1b | 3 | 0 | 0 | 0 | 0 | - | - |
| dc1-leaf1c | 3 | 0 | 0 | 0 | 0 | - | - |
| dc1-leaf2a | 8 | 0 | 0 | 0 | 0 | - | - |
| dc1-leaf2c | 3 | 0 | 0 | 0 | 0 | - | - |
| dc1-spine1 | 3 | 0 | 0 | 0 | 0 | - | - |
| dc1-spine2 | 3 | 0 | 0 | 0 | 0 | - | - |
| dc1-svc-leaf1a | 3 | 0 | 0 | 0 | 0 | - | - |
| dc1-svc-leaf1b | 3 | 0 | 0 | 0 | 0 | - | - |
| dc1-wan1 | 3 | 0 | 0 | 0 | 0 | - | - |
| dc1-wan2 | 3 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf1a | 3 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf1b | 3 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf1c | 3 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf2a | 8 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf2b | 8 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf2c | 3 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf3a.arista.com | 3 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf3b.arista.com | 3 | 0 | 0 | 0 | 0 | - | - |
| dc2-spine1 | 3 | 0 | 0 | 0 | 0 | - | - |
| dc2-spine2 | 3 | 0 | 0 | 0 | 0 | - | - |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Success | Tests Skipped | Tests Failure | Tests Error |
| ------------- | ----------- | ------------- | ------------- | ------------- | ----------- |
| Software | 63 | 0 | 0 | 0 | 0 |
| VXLAN | 15 | 0 | 0 | 0 | 0 |

## Test Results

| Device Under Test | Categories | Test | Description | Custom Field | Result | Messages |
| ----------------- | ---------- | ---- | ----------- | ------------ | ------ | -------- |
| dc1-leaf1a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-leaf1a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-leaf1a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-leaf1b | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-leaf1b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-leaf1b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-leaf1c | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-leaf1c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-leaf1c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-leaf2a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-leaf2a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-leaf2a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlan1ConnSettings | Verifies Vxlan1 source interface and UDP port. | - | unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | - | unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN, VNI-VRF bindings of the Vxlan1 interface. | - | unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanVtep | Verifies Vxlan1 VTEP peers. | - | unset | - |
| dc1-leaf2c | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-leaf2c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-leaf2c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-spine1 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-spine1 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-spine1 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-spine2 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-spine2 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-spine2 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-svc-leaf1a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-svc-leaf1a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-svc-leaf1a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-svc-leaf1b | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-svc-leaf1b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-svc-leaf1b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-wan1 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-wan1 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-wan1 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-wan2 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-wan2 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-wan2 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf1a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf1a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf1a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf1b | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf1b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf1b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf1c | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf1c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf1c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf2a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf2a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf2a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlan1ConnSettings | Verifies Vxlan1 source interface and UDP port. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN, VNI-VRF bindings of the Vxlan1 interface. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanVtep | Verifies Vxlan1 VTEP peers. | - | unset | - |
| dc2-leaf2b | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf2b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf2b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlan1ConnSettings | Verifies Vxlan1 source interface and UDP port. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN, VNI-VRF bindings of the Vxlan1 interface. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanVtep | Verifies Vxlan1 VTEP peers. | - | unset | - |
| dc2-leaf2c | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf2c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf2c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf3a.arista.com | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf3a.arista.com | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf3a.arista.com | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf3b.arista.com | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf3b.arista.com | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf3b.arista.com | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-spine1 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-spine1 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-spine1 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-spine2 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-spine2 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-spine2 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
