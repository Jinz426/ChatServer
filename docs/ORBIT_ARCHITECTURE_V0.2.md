# ORBIT Architecture v0.2

ORBIT (Open Relational & Integrated Technology) is a proposed language and runtime model for expressing software, data, spatial relationships, evidence, resources and AI workflows in one machine-readable system.

## Design inspiration

ORBIT studies capabilities visible across the open-source ecosystem rather than copying implementations. Apple currently lists Swift, MLX, WebKit, Pkl, Core ML Tools and other projects in its open-source portfolio; its ecosystem also includes community projects such as LLVM/Clang, Jupyter and USD. Swift emphasizes safety and performance; MLX combines Python/Swift/C/C++ interfaces for machine learning on Apple silicon; Pkl focuses on typed declarative configuration; LLVM provides a source- and target-independent IR and optimizer suitable for implementing new languages. See the project notes and upstream licenses before incorporating any code.

## Language layers

```text
ORBIT source
   |
   v
Lexer
   |
   v
Parser
   |
   v
AST
   |
   +--> Semantic / type checking
   |
   +--> Unit + dimensional checking
   |
   +--> Evidence / provenance checking
   |
   v
ORBIT-IR
   |
   +--> JSON / graph interchange
   |
   +--> LLVM IR backend (future)
   |
   +--> WebAssembly backend (future)
   |
   +--> Native runtime (future)
```

## Core primitives

### Value
Ordinary typed values: strings, numbers, booleans, arrays, records.

### Quantity
A numeric value with a unit, such as `25 THB`, `12 bottle`, `5 km`, or `100 kWh`.

### Entity
A persistent object such as a person-independent product, building, road, organization, resource or place.

### Relation
A typed edge connecting entities: `located_in`, `produces`, `supplies`, `transports`, `contains`, `recycles`, `observed_at`.

### Observation
A time-stamped statement about an entity or location.

### Evidence
A provenance object that records where an observation came from and whether it is observed, sourced, derived, inferred or unknown.

### Flow
A directed movement of material, energy, money, information or people.

### Scenario
A hypothetical model that must remain explicitly separate from observed history.

## Example

```orbit
world BangkokDemo {
    location market @ 13.7563, 100.5018

    product water {
        quantity 12 bottle
        price 25 THB
    }

    evidence water_price {
        status sourced
        source "public_observation"
        confidence 0.80
    }

    flow water_source -> market
}
```

## Safety and trust model

ORBIT is not intended to grant automatic control over devices or networks. Network actions require explicit authorization. Private data should be minimized. Evidence provenance is first-class. Model agreement is not proof. Inference must remain distinguishable from observation.

## Roadmap

- [x] Initial syntax concept
- [x] Observation schema
- [x] Product schema
- [x] Evidence vocabulary
- [ ] Formal grammar
- [ ] Lexer prototype
- [ ] Parser prototype
- [ ] AST implementation
- [ ] Type and unit checker
- [ ] Evidence validator
- [ ] ORBIT-IR
- [ ] JSON/graph exporter
- [ ] LLVM backend research prototype
- [ ] WASM backend research prototype
- [ ] GIS primitives
- [ ] AI tool/runtime interface
- [ ] Reproducible test suite

## Licensing rule

The language specification can be original project material. Third-party source code, algorithms, dependencies and generated artifacts must retain their applicable licenses and notices. “Inspired by” does not mean “copied from.”
