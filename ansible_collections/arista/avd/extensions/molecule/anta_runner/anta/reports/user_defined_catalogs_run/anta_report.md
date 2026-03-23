# 📊 ANTA Report <a id="anta-report"></a>

**Table of Contents:**

- [ANTA Report](#anta-report)
  - [Test Results Summary](#test-results-summary)
    - [Summary Totals](#summary-totals)
    - [Summary Totals Device Under Test](#summary-totals-device-under-test)
    - [Summary Totals Per Category](#summary-totals-per-category)
  - [Test Results](#test-results)

## 📉 Test Results Summary <a id="test-results-summary"></a>

### 🔢 Summary Totals <a id="summary-totals"></a>

| Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- |
| 81 | 0 | 0 | 0 | 0 |

### 🔌 Summary Totals Device Under Test <a id="summary-totals-device-under-test"></a>

| Device | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error | Categories Skipped | Categories Failed |
| :- | :- | :- | :- | :- | :- | :- | :- |
| **dc1-leaf1a** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc1-leaf1b** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc1-leaf1c** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc1-leaf2a** | 8 | 0 | 0 | 0 | 0 | - | - |
| **dc1-leaf2c** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc1-spine1** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc1-spine2** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc1-svc-leaf1a** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc1-svc-leaf1b** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc1-wan1** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc1-wan2** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc1-wan3** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc2-leaf1a** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc2-leaf1b** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc2-leaf1c** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc2-leaf2a** | 8 | 0 | 0 | 0 | 0 | - | - |
| **dc2-leaf2b** | 8 | 0 | 0 | 0 | 0 | - | - |
| **dc2-leaf2c** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc2-leaf3a.arista.com** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc2-leaf3b.arista.com** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc2-spine1** | 3 | 0 | 0 | 0 | 0 | - | - |
| **dc2-spine2** | 3 | 0 | 0 | 0 | 0 | - | - |

### 🗂️ Summary Totals Per Category <a id="summary-totals-per-category"></a>

| Test Category | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- | :- |
| **Software** | 66 | 0 | 0 | 0 | 0 |
| **VXLAN** | 15 | 0 | 0 | 0 | 0 |

## 🧪 Test Results <a id="test-results"></a>

| Device | Categories | Test | Description | Result | Messages |
| :- | :- | :- | :- | :- | :- |
| dc1-leaf1a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc1-leaf1a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc1-leaf1a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc1-leaf1b | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc1-leaf1b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc1-leaf1b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc1-leaf1c | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc1-leaf1c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc1-leaf1c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc1-leaf2a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc1-leaf2a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc1-leaf2a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlan1ConnSettings | Verifies Vxlan1 source interface and UDP port. | Unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | Unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | Unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN, VNI-VRF bindings of the Vxlan1 interface. | Unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanVtep | Verifies Vxlan1 VTEP peers. | Unset | - |
| dc1-leaf2c | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc1-leaf2c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc1-leaf2c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc1-spine1 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc1-spine1 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc1-spine1 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc1-spine2 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc1-spine2 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc1-spine2 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc1-svc-leaf1a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc1-svc-leaf1a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc1-svc-leaf1a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc1-svc-leaf1b | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc1-svc-leaf1b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc1-svc-leaf1b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc1-wan1 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc1-wan1 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc1-wan1 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc1-wan2 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc1-wan2 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc1-wan2 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc1-wan3 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc1-wan3 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc1-wan3 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc2-leaf1a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc2-leaf1a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc2-leaf1a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc2-leaf1b | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc2-leaf1b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc2-leaf1b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc2-leaf1c | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc2-leaf1c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc2-leaf1c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc2-leaf2a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc2-leaf2a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc2-leaf2a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlan1ConnSettings | Verifies Vxlan1 source interface and UDP port. | Unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | Unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | Unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN, VNI-VRF bindings of the Vxlan1 interface. | Unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanVtep | Verifies Vxlan1 VTEP peers. | Unset | - |
| dc2-leaf2b | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc2-leaf2b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc2-leaf2b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlan1ConnSettings | Verifies Vxlan1 source interface and UDP port. | Unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | Unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | Unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN, VNI-VRF bindings of the Vxlan1 interface. | Unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanVtep | Verifies Vxlan1 VTEP peers. | Unset | - |
| dc2-leaf2c | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc2-leaf2c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc2-leaf2c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc2-leaf3a.arista.com | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc2-leaf3a.arista.com | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc2-leaf3a.arista.com | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc2-leaf3b.arista.com | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc2-leaf3b.arista.com | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc2-leaf3b.arista.com | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc2-spine1 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc2-spine1 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc2-spine1 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
| dc2-spine2 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | Unset | - |
| dc2-spine2 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | Unset | - |
| dc2-spine2 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | Unset | - |
