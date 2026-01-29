# Glossary

## Table of Contents

- [N](#n)

## N

### notification_timestamp

**Type**: String  
**Path**: `management_api_gnmi.transport.grpc.[].notification_timestamp`  
**Valid Values**: `send-time`, `last-change-time`  

Per the gNMI specification, the default timestamp field of a notification message is set to be
the time at which the value of the underlying data source changes or when the reported event takes place.
In order to facilitate integration in legacy environments oriented around polling style operations,
an option to support overriding the timestamp field to the send-time is available from EOS 4.27.0F.


---
