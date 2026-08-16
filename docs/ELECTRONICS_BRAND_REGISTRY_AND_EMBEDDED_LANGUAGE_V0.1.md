# Global Electronics Brand Registry & EMBED Language v0.1

## 1. Purpose
Create a vendor-neutral registry for electronics brands, manufacturers, product families, components, standards, software/firmware interfaces, support lifecycles and official documentation. The registry is designed to connect electronics to the World Knowledge / ORBIT system.

This is a registry and interoperability layer, not a claim that every brand or product has already been ingested.

## 2. Brand registry scope
The registry should cover, subject to verifiable public sources:
- Consumer electronics
- Computers and servers
- Smartphones and tablets
- Networking equipment
- Telecommunications equipment
- Displays and televisions
- Cameras and imaging
- Audio equipment
- Wearables
- Smart-home / IoT
- Appliances with digital interfaces
- Industrial electronics
- Automotive electronics
- Robotics
- Semiconductor manufacturers
- Chip/IP vendors
- Storage and memory
- Power electronics
- Sensors
- Embedded controllers
- Development boards
- Electronic components
- Measurement/test equipment
- Satellite/space electronics
- Medical electronics where lawful public product data exists

## 3. Entity model
Each brand/product record should support:
- canonical entity ID
- brand name
- legal entity
- parent company
- country/jurisdiction
- official domain
- official product page
- product family
- model number
- SKU/part number
- hardware identifiers where publicly documented
- manufacturer
- OEM/ODM relationship when verifiable
- semiconductor/chipset
- CPU/GPU/NPU/MCU
- memory/storage
- connectivity
- operating system/firmware
- protocols/standards
- power requirements
- dimensions/weight where official
- manufacturing/market dates
- support/EOL dates
- certifications
- patents/trademarks where relevant
- official SDK/API/documentation
- data license
- source and provenance

## 4. Brand normalization
Brand names must not be used as unique identifiers. Use canonical IDs and maintain aliases, former names, transliterations, subsidiaries and parent-company relationships.

Model numbers must be treated separately from brand identity. Regional SKUs and revisions must be represented as distinct versions when technically or commercially significant.

## 5. EMBED language
Working name: **EMBED** — Electronics Model & Bridge Description.

EMBED is a small declarative interoperability language intended to describe what an electronic device exposes, requires and permits without granting unrestricted control.

Example:

```embed
DEVICE "example-device" {
  vendor "example-vendor"
  class "computer"
  interface usb
  interface network
  capability compute
  capability storage
  capability display

  permission read.system_info
  permission read.sensor
  permission write.file

  REQUIRE consent before write.file
}
```

## 6. EMBED principles
- Capability declaration before use
- Explicit permissions
- Least privilege
- Vendor-neutral interfaces
- Hardware capability discovery
- Versioned schemas
- Evidence/provenance for hardware claims
- No implicit privilege escalation
- Safe failure when an interface is unavailable
- Separate observation from control

## 7. Runtime architecture

```text
Device
  -> Hardware Capability Probe
  -> Device Profile
  -> EMBED Adapter
  -> Capability Graph
  -> Permission Check
  -> ORBIT Runtime
  -> AI / Application
```

EMBED should complement ORBIT rather than replace it:

`EMBED = device/interface description`

`ORBIT = world knowledge + computation + evidence + orchestration`

## 8. Adapter model
Adapters may target standards and documented interfaces such as:
- USB
- Bluetooth / BLE
- Wi-Fi
- Ethernet
- TCP/IP
- HTTP(S)
- MQTT
- Matter
- Thread
- Zigbee
- Modbus
- CAN/CAN-FD
- I2C
- SPI
- UART
- PCIe
- NVMe
- UEFI/ACPI where documented
- OS-native APIs
- Vendor SDKs/APIs where licensed

An adapter must declare its access level and required permissions.

## 9. Manufacturer and ecosystem layers

```text
Brand
  -> Legal Entity
  -> Parent Group
  -> Manufacturer / OEM / ODM
  -> Product Family
  -> Model / SKU
  -> Hardware Revision
  -> Firmware Version
  -> Software/API
  -> Components
  -> Standards
  -> Support Lifecycle
```

## 10. Global integration
Electronics records connect to:
- ISO identifiers
- country and jurisdiction registry
- company registry
- WIPO patents/trademarks
- semiconductor/component registry
- product/price database
- supply-chain graph
- energy/material footprint data where reliable
- recycling/end-of-life data
- repairability/support information
- official certifications
- telecom/network infrastructure

## 11. Security model
The registry does not provide universal remote control of devices. It describes capabilities and provides adapters only through documented, authorized interfaces.

Sensitive operations require explicit user/system authorization. Security-sensitive interfaces should require additional policy controls, authentication, auditing and safe defaults.

## 12. Data quality
Statuses:
- VERIFIED_OFFICIAL
- VERIFIED_MANUFACTURER
- STANDARD_DOCUMENTED
- THIRD_PARTY_VERIFIED
- UNVERIFIED
- HISTORICAL
- DISCONTINUED
- LICENSE_RESTRICTED

Every observation stores source, timestamp, version, methodology and license/access status.

## 13. Implementation roadmap
Phase 1:
- Brand/entity schema
- Product schema
- Capability schema
- EMBED grammar specification

Phase 2:
- EMBED lexer/parser
- Device profile format
- Capability checker
- Permission engine
- ORBIT bridge

Phase 3:
- USB/Bluetooth/network adapters
- Hardware capability probe
- Product recognition pipeline
- Documentation/source ingestion

Phase 4:
- Large global brand/product ingestion
- Lifecycle and supply-chain graph
- Cross-country product/price analysis
- Device interoperability dashboard

## 14. Completion rule
A brand registry is not considered complete because a list of brand names exists. Completion requires canonical identity, source provenance, product/entity resolution, lifecycle/versioning, license status and validation.
