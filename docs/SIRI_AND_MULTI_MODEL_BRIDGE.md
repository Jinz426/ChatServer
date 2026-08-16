# Siri + Multi-Model AI Bridge

## Goal

Connect the project's ORBIT / Global World Knowledge capabilities to Siri and to multiple AI providers through a permissioned application layer.

Apple's current developer guidance uses **App Intents** as the modern integration point for Apple Intelligence and Siri AI. App Intents expose app actions and entities so Siri, Spotlight and Shortcuts can discover them. Apple also documents the Foundation Models framework as a native Swift API that can work with Apple Foundation Models and model providers conforming to Apple's Language Model protocol.

## Architecture

```text
Siri / Apple Intelligence
          |
      App Intents
          |
     ORBIT Bridge
          |
   +------+-------+----------------+
   |              |                |
Apple model    Cloud model A    Cloud model B
   |              |                |
   +--------------+----------------+
                  |
          Evidence / Policy Layer
                  |
        Global World Knowledge
                  |
       GIS / Products / Prices
       Resources / Supply Chain
       History / Knowledge Graph
```

## Important boundary

The bridge does not grant Siri or any AI unrestricted device privileges. Each action is explicitly declared, permissioned and validated. Destructive or sensitive actions require confirmation.

The system should never silently upload private conversations, photos, contacts, credentials or device data to an external model. Data should be minimized and routed only to an authorized provider.

## App Intents surface

Initial intents should include:

- `AnalyzeObservationIntent`
- `AnalyzePhotoIntent`
- `FindProductPriceIntent`
- `TraceSupplyChainIntent`
- `CompareLocationsIntent`
- `ExplainCoordinateIntent`
- `QueryWorldKnowledgeIntent`
- `RunOrbitHardwareBenchmarkIntent`
- `ExportKnowledgeIntent`

Entities should include:

- `WorldCoordinate`
- `Observation`
- `Product`
- `Location`
- `Resource`
- `SupplyChainNode`
- `EvidenceRecord`
- `KnowledgeRecord`

## Multi-model adapter

The application should expose one internal interface and keep provider-specific code behind adapters:

```text
ORBIT Model Protocol
        |
  +-----+-----+----------------+
  |           |                |
Apple      Provider A       Provider B
adapter     adapter          adapter
```

Each adapter returns a common response envelope containing:

- provider
- model identifier
- timestamp
- input modality
- output
- evidence references
- confidence / uncertainty
- tool calls
- policy status

Model agreement is not proof. Evidence remains the source of truth.

## Siri examples

A user could say:

> "Siri, analyze this photo with ORBIT."

> "Siri, compare the prices of this product in the current markets."

> "Siri, explain what is around this location."

> "Siri, trace the known supply chain for this product."

> "Siri, run the ORBIT hardware benchmark."

The app receives a structured intent and performs only the operations declared by the intent.

## On-screen context

Where supported, App Intents entities can be associated with visible app content so the system can understand references such as "this photo" or "this product" without requiring the user to repeat identifiers.

## Future ORBIT language integration

ORBIT source can eventually describe intents declaratively:

```orbit
intent analyze_photo(photo: Image) -> Observation {
    requires permission("photos.read")
    uses vision
    output evidence
}
```

The ORBIT compiler can later generate Swift/App Intents scaffolding while preserving explicit permissions and human confirmation requirements.

## Provider neutrality

"All AI models" means a pluggable adapter architecture, not automatic access to every model on the Internet. A provider must expose an authorized API, SDK, local runtime, or Apple-compatible Language Model implementation before it can participate.

## References

- Apple App Intents documentation: https://developer.apple.com/documentation/appintents
- Apple Intelligence and Siri AI: https://developer.apple.com/documentation/appintents/apple-intelligence-and-siri-ai
- Apple Foundation Models: https://developer.apple.com/apple-intelligence/

## Next implementation steps

1. Create the Swift application shell.
2. Add App Intents entities and intents.
3. Build the ORBIT bridge service.
4. Implement a local model adapter first.
5. Add provider adapters one at a time.
6. Add evidence and privacy policy enforcement.
7. Add evaluation tests for Siri, Shortcuts and Spotlight.
8. Connect the bridge to the Global World Knowledge API.
