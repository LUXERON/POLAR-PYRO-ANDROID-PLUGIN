# A Proof-Carrying Android Compiler for a 0.6B Model

## Abstract

Direct mobile-code generation asks a small language model to simultaneously understand product semantics, visual design, distributed state, Android lifecycle, permissions, device APIs, Rust/Kotlin boundaries and release engineering. Polar Pyro reduces that open problem to constrained symbol selection. Its Android plugin compiles those symbols into an authority plan whose downstream implementation and behavior are independently verified.

## Thesis

The decisive unit is not generated source but a closed refinement chain:

```text
AppSpec -> Web UIPlan -> MobileUXBinding -> AndroidBuildPlan -> Candidate -> Certificate
```

Each arrow has a schema, canonical hash, admissible vocabulary, independent oracle and explicit failure semantics. This makes a 0.6B proposer useful without making it trusted.

## One application truth

Rust owns invariant-bearing application behavior. React renders projections and emits typed user intent. Kotlin adapts Android-owned lifecycle and device contracts. Tauri mediates the capability boundary. Axum serves remote authenticated clients. This is an authority allocation, not merely a technology preference: duplicating policy in TypeScript, Kotlin and Rust would create three conflicting systems of record.

The rule is mechanical:

- portable deterministic behavior belongs in Rust;
- Android framework behavior belongs in Kotlin;
- visual interaction belongs in React;
- remote protocols belong behind Axum;
- every cross-boundary value has a versioned schema.

## Why Web Experience remains the parent

Android is a deployment and interaction specialization of the same product semantics. The Web Experience Engine already closes roles, routes, tasks, design tokens, components and accessibility obligations. The Android plugin binds that exact UI plan by SHA-256, then introduces mobile navigation, touch, lifecycle, offline, permission and device constraints. It cannot invent a divergent application.

## Mathematical work

Euclid-Ω is used where the claim can be formalized: operation reachability, role and permission closure, lifecycle termination, denied-permission recovery, offline transition safety, sync convergence assumptions and bounded resource constraints. An obligation request is not a proof; the Euclid receipt and replay evidence must accompany release.

DEMIURGE handles decidable stateless synthesis and finite-state subdomains. SAE handles stateful applications. LOOM performs repository-scale composition. ISTHMUS validates Rust/Kotlin/TypeScript seams. None of these engines silently widens another engine's authority.

## Security model

The model cannot introduce arbitrary Maven/npm/crate dependencies, shell commands, signing keys, Android permissions, deep links, exported components or network endpoints. Catalog admission and side-effect grants precede materialization. Work occurs in an isolated Git transaction. Tests, static analysis, mutation testing, emulator/device behavior and security gates inspect the exact candidate commit. Secrets never enter the model context or TOAM journal.

## Evidence semantics

The compiler returns `PASS | FAIL`; unavailable downstream gates use `NO_RESULT`. `PASS` is always scoped. At this stage it means only:

1. the input matched the frozen contract;
2. every operation was allocated to an admitted implementation mode;
3. referenced device capabilities and permissions came from the supplied catalog;
4. the plan cited an exact parent UI plan;
5. evidence hashes were produced over canonical output.

It does not certify an APK. Production certification additionally requires build reproducibility, FFI/concurrency, permission/lifecycle, offline/sync, accessibility, performance, security, mutation, signing and physical-device evidence.

## Long-horizon execution

Every attempt freezes base commit, schemas, catalogs, engine versions and budget. Qwen proposes one bounded binding. The compiler and engines produce a candidate in an isolated worktree. Failed gates emit typed residuals; repair may change only admitted fields or candidate source within the transaction. A passing candidate is promoted atomically. Checkpoints restore only when all frozen hashes match. Git stores software truth; TOAM stores the retrievable decision and evidence history.

## Evaluation

The target is not benchmark theater. A production gauntlet includes cold start, background/foreground transitions, process death, rotation, permission denial and revocation, offline edits, reconnect conflict, upgrade/migration, device API failure, accessibility services, low-memory pressure and hostile inputs. Equivalent mutants must be identified; non-equivalent planted failures must be rejected in the same invocation.

Only applications generated through this unattended pipeline, with no direct product-source edits, count toward Polar Pyro's autonomy record.

## Current boundary

Version 0.1.0 implements and tests the deterministic authority-plan compiler and Polar Pyro plugin manifest. Frozen source renderers, Euclid adapters, full engine composition, emulator/device qualification and release signing remain downstream gates. This repository therefore makes a narrow verifiable claim instead of labeling an architectural skeleton production-ready.
