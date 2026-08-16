# ORBIT Language — Open Relational & Biological/Infrastructure Technology Language

## Status

Experimental language design, v0.1. It is a new language specification inspired by useful ideas found across modern systems, scripting, data, configuration, numerical and AI-oriented languages. It is **not** a merger or copy of their source code.

## Why a new language?

The project needs one language that can express:

- systems programming;
- safe concurrency;
- data and configuration;
- maps and spatial objects;
- resource and supply-chain graphs;
- AI observations and evidence;
- APIs and services;
- numerical/ML workloads;
- automation;
- human-readable declarations.

Apple's open-source ecosystem is a useful reference point: Swift targets safety/performance and broad systems-to-cloud use; LLVM provides a language-independent optimizer and code-generation infrastructure; WebKit combines C++, Objective-C/Objective-C++, Swift and Python; MLX combines Python, Swift, C and C++ bindings; Pkl demonstrates a typed declarative configuration language. These projects illustrate complementary design pressures rather than a reason to copy implementation code.

## Design principle

**One language, multiple representations.**

A program can be written as ordinary imperative code, a data declaration, a graph, or a spatial/resource model. The compiler lowers all forms into a typed intermediate representation (ORBIT-IR), which can target LLVM or another backend.

## Core features

### 1. Safety by default

- immutable bindings by default;
- explicit mutable state;
- optional types instead of implicit null;
- bounds-aware collections;
- ownership/borrowing model to be investigated;
- checked errors instead of invisible exceptions.

### 2. Human-readable syntax

```orbit
world Thailand {
    location Bangkok @ 13.7563, 100.5018

    market Chatuchak {
        product water {
            price 25 THB / 12 bottle
            evidence "public_observation"
        }
    }
}
```

### 3. Spatial primitives

```orbit
place factory @ 13.7563, 100.5018
route truck from warehouse -> market
zone farm area 120 ha
```

### 4. Evidence as a first-class value

```orbit
observation product "example-water" {
    observed_at "2026-08-17T12:00:00Z"
    source "public_observation"
    status observed
    confidence 0.82
}
```

### 5. Graph relationships

```orbit
link factory -> raw_material
link raw_material -> product
link product -> market
link market -> consumer
```

### 6. Resource flows

```orbit
flow water source reservoir -> factory
flow energy grid -> factory
flow material factory -> product
flow waste product -> recycler
```

### 7. AI declarations

```orbit
agent analyst {
    observe photo
    classify product, building, road
    require evidence
    separate observed, sourced, derived, inferred, unknown
}
```

## Type system sketch

Primitive types:

`Bool Int UInt Float Decimal String Bytes Time Duration`

Domain types:

`Money Currency Quantity Coordinate Distance Area Energy Material Product Place Route PersonRole Organization Evidence Confidence`

Generic types:

`List<T> Map<K,V> Set<T> Option<T> Result<T,E> Graph<N,E>`

## Units

Units are part of the type system where practical:

```orbit
price = 25 THB / 12 bottle
land = 120 ha
speed = 45 km/h
energy = 2.4 kWh
```

The compiler should reject incompatible unit operations.

## Concurrency

The first implementation should prefer structured concurrency and message passing over unrestricted shared mutable state.

```orbit
parallel {
    observe_map(region)
    observe_market(region)
    observe_transport(region)
}
```

## AI / knowledge graph model

ORBIT treats a knowledge graph as a native data structure:

```orbit
graph world {
    node factory
    node product
    node material
    edge produces(factory, product)
    edge requires(product, material)
}
```

## Compilation strategy

Recommended architecture:

```text
ORBIT source
    ↓
Lexer
    ↓
Parser
    ↓
AST
    ↓
Type + unit checker
    ↓
Evidence / effect checker
    ↓
ORBIT-IR
    ↓
LLVM IR / WASM / native backend
```

LLVM is particularly attractive because its documented IR and optimizer/code-generation infrastructure are explicitly intended to support the creation of new languages and compiler frontends.

## Interoperability

ORBIT should be able to call or generate:

- C ABI
- C++ where practical
- Swift interoperability on supported platforms
- Python extensions
- JavaScript/WASM interfaces
- JSON/YAML/TOML data
- SQL/database connectors
- HTTP APIs
- machine-learning runtimes

Interoperability is a boundary, not a license to copy implementation code from another project.

## Long-term idea

ORBIT is intended to become a language for describing both **software systems and real-world systems**:

`code + data + map + resource + evidence + graph + AI`

That makes it suitable for the Global World Knowledge project.

## Governance

The language should remain open, documented and independently testable. Third-party source code must retain its applicable license and attribution. The language itself should evolve through versioned specifications, tests and review.
