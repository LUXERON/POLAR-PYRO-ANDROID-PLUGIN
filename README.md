# Polar Pyro Android Target

This repository is the opinionated Android target plugin for the Polar Pyro neurosymbolic software forge. It turns a closed application contract and bounded mobile binding into a deterministic allocation plan for a React/Vite interface, Tauri v2 shell, authoritative Rust core, Kotlin device adapters, optional remote Axum services, and Android lifecycle work.

It is deliberately not a prompt-to-APK generator. Qwen3-0.6B selects identifiers from frozen catalogs; the compiler determines authority boundaries; owned renderers materialize source; Euclid-Ω states proof obligations; DEMIURGE, SAE, LOOM and ISTHMUS solve and compose their respective domains; Android and browser oracles decide whether a candidate may be promoted.

## The stack

| Layer | Authority |
| --- | --- |
| React + TypeScript + Vite | Presentation and accessible interaction only |
| Tauri v2 | Typed UI-to-native command boundary and packaging shell |
| Rust | Application truth, policy, state transitions, crypto and local services |
| Kotlin | Android SDK, Activity/lifecycle, permissions, sensors and platform callbacks |
| Axum | Authenticated remote service boundaries; never the default internal UI bus |
| WorkManager | Explicit durable Android background work |

This allocation prevents business rules from drifting into JSX or Kotlin callbacks. A capability that can be implemented portably remains in Rust. Kotlin enters only where the Android platform owns the contract. Axum enters only when there is an actual network boundary or a separately justified loopback exception.

## Compilation pipeline

```text
natural-language request + project evidence
                  |
        closed application contract
                  |
       Web Experience UI plan hash
                  |
        Qwen MobileUXBinding
                  |
       android.compile_build_plan
          /       |        \
 Rust/Tauri   Kotlin map   Axum map
          \       |        /
          Euclid obligations
                  |
 frozen source renderers + engine composition
                  |
 Gradle · Rust · device · a11y · security · mutation · signing gates
                  |
       Android release certificate
```

The current v1 compiler admits one target, `android.tauri-react-vite`, and four operation modes:

- `embedded_rust`: an in-process Tauri command backed by the Rust core;
- `device`: a registered Tauri/Kotlin platform capability with explicit Android permissions;
- `remote_axum`: a typed authenticated endpoint contract;
- `background`: an admitted WorkManager policy.

Every input field is closed. Application identity must match across the contract and binding. Device capabilities must be present in the supplied audited catalog. Permissions must be explicit `android.permission.*` symbols. A build plan must cite the exact SHA-256 of its parent Web Experience UI plan.

## Engine composition

- **Web Experience Engine** supplies the design language, routes, journeys, components and accessible UI plan. Android specializes it; it does not fork the UX ontology.
- **SAE** owns stateful application semantics: identities, authorization, persistence, workflows, sync and recovery.
- **DEMIURGE** synthesizes bounded stateless kernels and finite authorization/FSM domains.
- **Euclid-Ω** receives operation-refinement and permission-lifecycle obligations. Its proofs remain separately evidenced.
- **LOOM** composes the generated frontend, Rust core, Kotlin adapters and repository changes under non-regression gates.
- **ISTHMUS** verifies language/FFI and callback boundaries.
- **KINTSUGI/CRUCIBLE** repair and harden candidates without weakening the frozen contract.
- **TOAM** journals attempts, residuals and certificates; Git remains the software system of record.

## Trust boundary

A compiler `PASS` proves only that the requested operations have a closed, deterministic authority allocation and a non-empty evidence receipt. It does not prove that source compiles, a permission prompt works, an emulator behaves correctly, accessibility passes, an APK is signed, or Play policy is satisfied.

Release promotion requires independent evidence for every gate named in the output plan. `FAIL` and `NO_RESULT` never become success. Qwen cannot author shell commands, Gradle scripts, signing configuration, permissions, capability providers, endpoint contracts, tests, or its own oracle.

## Plugin capability

`dev.luxeron.engine.android@0.1.0` contributes `android.compile_build_plan` to the Polar Pyro `target.compiler` slot. The native JSON transport reads one request from standard input and writes one canonical receipt.

```powershell
python -m pip install -e .
Get-Content request.json | polar-android-plan
python -m pytest -q
```

The process exits `0` only for `PASS` and `2` for a closed validation failure.

## Repository map

```text
src/polar_pyro_android/compiler.py  Closed authority-plan compiler and CLI
tests/test_compiler.py              Contract and adversarial tests
docs/ARCHITECTURE.md                Full Android Experience architecture
plugin.manifest.json                Polar Pyro ABI/capability declaration
WHITEPAPER.md                       Design thesis and production boundary
```

## Production roadmap

1. Freeze versioned mobile binding, device catalog and endpoint schemas.
2. Add owned React/Vite/Tauri, Rust crate, Kotlin adapter and Gradle renderers.
3. Compile Euclid permission/lifecycle and operation-refinement requests.
4. Connect SAE, DEMIURGE, LOOM and ISTHMUS through typed receipts.
5. Run desktop web parity, Android emulator, physical-device and lifecycle gauntlets.
6. Add supply-chain, SBOM, secret, signing, Play-policy and reproducibility gates.
7. Promote only an exact Git candidate with a complete Android release certificate.

The detailed normative plan is in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).
