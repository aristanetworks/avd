# 📊 ANTA Report <a id="anta-report"></a>

**Table of Contents:**

- [ANTA Report](#anta-report)
  - [Test Results Summary](#test-results-summary)
    - [Summary Totals](#summary-totals)
    - [Summary Totals Device Under Test](#summary-totals-device-under-test)
    - [Summary Totals Per Category](#summary-totals-per-category)
  - [Test Results](#test-results)

## 📉 Test Results Summary <a id="test-results-summary"></a>

>💡 **Note:** This report was generated with **Expanded Results** enabled. The summary sections below aggregate results at the test level, so individual checks (atomic results) are not counted in these totals.

### 🔢 Summary Totals <a id="summary-totals"></a>

| Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- |
| 15 | 0 | 0 | 0 | 0 |

### 🔌 Summary Totals Device Under Test <a id="summary-totals-device-under-test"></a>

| Device | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error | Categories Skipped | Categories Failed |
| :- | :- | :- | :- | :- | :- | :- | :- |
| **dc1-leaf2a** | 5 | 0 | 0 | 0 | 0 | - | - |
| **dc2-leaf2a** | 5 | 0 | 0 | 0 | 0 | - | - |
| **dc2-leaf2b** | 5 | 0 | 0 | 0 | 0 | - | - |

### 🗂️ Summary Totals Per Category <a id="summary-totals-per-category"></a>

| Test Category | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- | :- |
| **VXLAN** | 15 | 0 | 0 | 0 | 0 |

## 🧪 Test Results <a id="test-results"></a>

| Device | Categories | Test | Description | Custom Field | Result | Messages |
| :- | :- | :- | :- | :- | :- | :- |
| dc1-leaf2a | VXLAN | VerifyVxlan1ConnSettings | Verifies Vxlan1 source interface and UDP port. | - | Unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | - | Unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | Unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN, VNI-VRF bindings of the Vxlan1 interface. | - | Unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanVtep | Verifies Vxlan1 VTEP peers. | DC2 VXLAN VTEP reachability | Unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlan1ConnSettings | Verifies Vxlan1 source interface and UDP port. | - | Unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | - | Unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | Unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN, VNI-VRF bindings of the Vxlan1 interface. | - | Unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanVtep | Verifies Vxlan1 VTEP peers. | DC2 VXLAN VTEP reachability | Unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlan1ConnSettings | Verifies Vxlan1 source interface and UDP port. | - | Unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | - | Unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | Unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN, VNI-VRF bindings of the Vxlan1 interface. | - | Unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanVtep | Verifies Vxlan1 VTEP peers. | DC2 VXLAN VTEP reachability | Unset | - |
