# ANDROID-EXPERIENCE-ENGINE

## Final Design and Architectural Plan for Qwen3-0.6B

**Status:** Proposed final architecture  
**System family:** LUXERON Experience Engine / Woven Line / Qwen3-0.6B Neurosymbolic Harness  
**Primary role:** Compile a small, grammar-constrained application-and-mobile intent into a premium Android application whose user experience, durable state, device access, platform behavior and release evidence are independently constrained, synthesized, tested and certified.

---

## 0. Prior art

The prior-art check searched 477 repositories under LUXERON using three distinct queries:

1. deterministic Android application synthesis with Tauri, Kotlin, Rust, Euclid and DEMIURGE;
2. mobile experience engines built from UI ASTs and device-capability plugins;
3. Qwen small-model Android development harnesses using Tauri and Axum.

No strong match was found for a deterministic Android synthesis engine.

| Repository or system | Relationship | Existing contribution |
|---|---|---|
| WEB-EXPERIENCE-ENGINE | Direct parent | Shared experience IR, component foundry, UX compiler, design languages, React/Vite renderer and browser qualification |
| QWEN3-0.6B-NEUROSYMBOLIC-HARNESS | Direct parent | Grammar-constrained Qwen binding, Euclid reasoning plane, SAE/DEMIURGE ports, residual repair and certificates |
| EUCLID-OMEGA | Reused authority | Rust LCF-style proof kernel, proof search, replayable certificates and honest formal bounds |
| DEMIURGE-ENGINE | Reused authority | Stateless synthesis domains, authorization and finite-state-machine synthesis |
| STATEFUL-APP-ENGINE | Reused authority | Durable application state, schemas, workflows, migrations and stateful realization |
| LONG-HORIZON-CODING-HARNESS | Reused control plane | Macro FSM, per-module behavior trees, atomic attempts, budgets and resumable long-horizon execution |
| QWEN06-AUTONOMY-SHOWCASE | Evidence precedent | Independently gated software projects driven by Qwen3-0.6B, Euclid-Ω, DEMIURGE/SAE and LOOM |
| creditflow-atlas | Adjacent implementation | Existing Tauri and Axum application precedent, but not an Android synthesis engine |
| HARNESS-AUTONOMY-GAUNTLET | Qualification parent | Autonomous project-level evaluation and proof-of-capability discipline |

**Position of this document:** this is an extension of the shared Experience Engine and Sovereign Harness. It introduces an Android renderer, device-capability compiler, platform trust boundary and mobile qualification plane. It is not a duplicate web generator and must not create a second, divergent UX ontology.

---

## 1. Executive decision

The missing system is an **ANDROID-EXPERIENCE-ENGINE target plane** inside the shared Experience Engine.

Its opinionated production stack is:

| Technology | Authority |
|---|---|
| React + TypeScript + Vite | Deterministic presentation materialization |
| Tauri v2 Mobile | Android application host, WebView shell, typed command/event bridge, capability security and packaging |
| Rust | Portable application truth, policy, algorithms, storage/synchronization logic, certificate replay and service contracts |
| Kotlin | Android platform authority: device APIs, Activity and process lifecycle, permissions, WorkManager, intents and native surfaces |
| Axum | Real HTTP/network boundaries, normally remote; never the default in-process UI bus |
| Qwen3-0.6B | Untrusted, grammar-constrained intent-to-binding transducer |
| Master Librarian | Compiles the task-specific vocabulary, device capabilities, precedents, exclusions and evidence |
| Euclid-Ω | Mathematical reasoning, build-time proof search, constraint checking and runtime certificate replay |
| DEMIURGE | Stateless synthesis domains, authorization kernels and decidable finite-state logic |
| SAE | Stateful application semantics, persistence, transactions, migrations and offline workflow truth |
| LOOM | Polyglot assembly and cross-engine seam closure |
| Android and deterministic oracles | Independent release verdicts |

The primary transformation is:

~~~text
product brief + certified application semantics
        -> bounded MobileUXBinding
        -> UXContract + operation contracts
        -> DeviceBindingPlan + MobileUIPlan
        -> Euclid-Ω proofs and explicit bounds
        -> deterministic React/Vite + Tauri + Rust + Kotlin materialization
        -> Android, browser, device, security and mutation qualification
        -> replayable AndroidExperienceCertificate
~~~

The 0.6B model never writes trusted Kotlin, Rust, JSX, Gradle, Android Manifest entries, permission logic, shell commands, oracle code or signing configuration. It chooses stable identifiers and proposes bounded repairs over a frozen grammar.

---

## 2. Architectural principles

### 2.1 One Experience Engine, multiple target profiles

Web and Android share:

- ApplicationCapabilityManifest;
- DesignBrief;
- UXContract;
- DesignLanguage;
- ComponentManifest;
- semantic navigation, journey and action models;
- React/Vite component templates;
- catalog and license provenance;
- browser accessibility and visual conformance machinery;
- residual repair and certificate infrastructure.

Android adds:

- device capabilities;
- Android permission and consent states;
- Activity, process and WebView lifecycle;
- back and predictive-back behavior;
- background-work policy;
- intents, app links and native system surfaces;
- Android packaging, signing and release qualification;
- emulator and physical-device execution.

The first renderer profiles are:

~~~text
experience.react-vite.web
experience.react-vite.tauri-android
~~~

A future Compose renderer may refine the same semantic IR, but it is not part of the first production lane.

### 2.2 Rust owns application truth

Rust owns:

- domain invariants and policies;
- authorization decisions;
- deterministic algorithms;
- application state-machine execution;
- operation contracts;
- synchronization protocol and offline queue semantics;
- cryptographic verification and certificate replay;
- storage abstractions and canonical serialization;
- remote-service client contracts.

Kotlin does not become a second business-logic core. It executes platform operations and returns typed observations or results.

### 2.3 Kotlin owns Android authority

Kotlin owns platform-facing mechanisms:

- runtime permissions and permanent-denial states;
- Activity, process and plugin lifecycle events;
- camera, microphone, location, sensors, NFC and Bluetooth;
- biometrics and Android Keystore integration;
- notifications, foreground services and system dialogs;
- WorkManager and persistent background scheduling;
- intents, deep links, app links, sharing and file selection;
- Play Billing and platform-owned user journeys;
- widgets and other native surfaces.

Prefer an audited official Tauri plugin where it satisfies the contract. Introduce a custom Kotlin plugin only for an uncovered capability, and place it through the same manifest, permission, threading, lifecycle, security and mutation gates.

### 2.4 Tauri is the default trusted bridge

The normal foreground call path is:

~~~text
React UI
  -> allowlisted Tauri application command
  -> Rust policy and certificate checks
  -> typed Tauri mobile plugin call
  -> Kotlin Android adapter
  -> Android OS
~~~

Privileged low-level Kotlin plugin commands are not exposed directly to arbitrary JavaScript. Frontend code invokes application-level Rust commands. Rust performs the policy decision before calling the device adapter.

### 2.5 Axum owns actual network boundaries

Axum is not the default internal Android message bus.

| Mode | Policy |
|---|---|
| Embedded UI to Rust core | Tauri commands/events; no HTTP |
| Android client to multi-user or remote backend | Remote Axum service |
| Local external automation or another process must call the app | Loopback Axum permitted only under an explicit exception contract |
| Long-running background work | Android WorkManager or a justified Android Service governs lifecycle |
| Shared stateless logic | Plain Rust library/service, independent of transport |

A loopback Axum exception must prove the need for HTTP and must enforce loopback-only binding, ephemeral port allocation, per-launch authentication, origin restrictions, bounded request size, explicit shutdown, lifecycle recovery and negative security tests.

### 2.6 Build-time proof and runtime replay are separate

Euclid-Ω has two roles:

~~~text
BUILD TIME
formal model -> proof search -> proof object -> certificate

ANDROID RUNTIME
certificate + current typed inputs -> eo-kernel replay -> valid or invalid
~~~

General proof search is not required on every phone interaction. The runtime application normally embeds only the minimal proof parser, LCF-style replay kernel, schema hashes and policy inputs needed to validate certificates. Full on-device reasoning is an optional target profile subject to binary-size, latency, memory, thermal and battery qualification.

### 2.7 Formal claims are bounded

Euclid and DEMIURGE may prove:

- application authorization within a declared policy model;
- reachability and exclusion properties of finite state machines;
- navigation and back-stack invariants;
- safety and liveness properties under named assumptions;
- refinement between abstract workflows and concrete operation plans;
- permission-state consistency;
- constraint satisfiability and conflict absence.

They do not prove:

- Android itself is bug-free;
- a Kotlin adapter correctly implements an API without independent testing;
- the user understands or appreciates the interface;
- a granted Android permission implies current user intent;
- every hardware vendor behaves identically;
- a screenshot proves usability;
- arbitrary retrieved documentation is true.

Every certificate records assumptions, unproved seams and independent oracle references.

---

## 3. End-to-end topology

~~~text
Product brief / existing repository / certified retrieval evidence
                              |
                              v
                  Application Semantics Port
              SAE AppSpec             DEMIURGE Contract
                    \                    /
                     v                  v
              ApplicationCapabilityManifest
                              |
                              v
        Master Librarian + Experience/Device Catalog Retrieval
       bounded UI, operations, devices, invariants and exclusions
                              |
                              v
                  Qwen3-0.6B MobileUXBinding
             one strict JSON grammar, temperature zero
                              |
                              v
                 UX and Operation Contract Compiler
                              |
            +-----------------+-----------------+
            |                                   |
            v                                   v
       MobileUIPlan                    DeviceBindingPlan
            |                                   |
            +-----------------+-----------------+
                              |
                              v
                    Euclid-Ω proof boundary
        navigation / lifecycle / permissions / offline / refinement
                              |
                 PROVE       BOUND       ABSTAIN
                    |           |             |
                    |           v             v
                    |     typed residual   certified refusal
                    |           |
                    |    bounded JSON Patch repair
                    v
       Deterministic multi-target materialization
    React/Vite | Tauri | Rust | Kotlin | Gradle | Manifest
                              |
                              v
             LOOM assembly + ISTHMUS seam qualification
                              |
                              v
 schema | unit | property | mutation | browser | instrumentation
 device | accessibility | lifecycle | security | performance | release
                              |
                 PASS        FAIL        NO_RESULT
                    |           |             |
                    v           v             v
     AndroidExperienceCertificate  residual  abstention record
                    |
                    v
        CRUCIBLE -> Autonomy Gauntlet -> signed release candidate
~~~

PROVE, BOUND and ABSTAIN describe formal reasoning. PASS, FAIL and NO_RESULT describe independent evidence gates. Behavior-tree SUCCESS, FAILURE and RUNNING remain a third, separate control enum.

---

## 4. Trust and authorization boundary

A privileged device operation is allowed only if all required authorities agree:

~~~text
ALLOW_DEVICE_OPERATION =
    operation_contract_is_valid
    AND certificate_is_valid
    AND application_policy_allows
    AND Tauri_capability_scope_allows
    AND Android_runtime_permission_is_granted
    AND lifecycle_state_is_valid
    AND input_scope_is_valid
    AND required_user_consent_or_gesture_is_fresh
~~~

No single factor substitutes for another:

- DEMIURGE authorization does not grant an Android permission.
- Android permission does not prove the application role is authorized.
- A Tauri capability allowlist does not prove the current lifecycle state is safe.
- A previous user gesture does not remain fresh indefinitely.
- A proof certificate does not prove the Kotlin implementation is defect-free.

The trusted path is fail-closed. Unknown capability IDs, stale certificates, schema drift, lifecycle ambiguity, unavailable platform state, missing user consent and verifier errors all deny the operation or produce NO_RESULT.

---

## 5. Canonical intermediate representations

All artifacts use versioned schemas, canonical serialization, content hashes and explicit provenance. Repairs may alter only allowlisted fields and never mutate frozen task, schema, catalog, proof-kernel or oracle hashes.

### 5.1 Shared ApplicationCapabilityManifest

Produced by SAE or a DEMIURGE domain adapter:

~~~text
application and contract identity
entities, value objects and data classifications
queries, commands, effects and errors
roles, permissions and ownership predicates
workflow and state-machine definitions
durability and transaction requirements
offline and synchronization semantics
notification and background-work needs
deep-linkable resources
provenance and bounded assumptions
~~~

### 5.2 OperationContract

Operations are transport-independent:

~~~text
operation_id and semantic version
input and output schemas
preconditions, effects and error taxonomy
policy and certificate requirements
idempotency and retry semantics
data classification
foreground/background eligibility
required user gesture or consent
device capability, if any
remote service binding, if any
~~~

The target compiler maps one operation to a Tauri command, remote Axum route, background job or Kotlin device adapter without changing the operation's meaning.

### 5.3 MobileUXBinding

The only normal Android artifact authored by Qwen3-0.6B:

~~~json
{
  "schema_version": "mobile-ux-binding/1",
  "target": "android.tauri-react-vite",
  "archetype": "secure_workspace",
  "navigation": "adaptive_bottom_bar_and_rail",
  "design_language": "precision_dark",
  "density": "comfortable",
  "offline_profile": "read_write_queue",
  "views": {
    "vault": "protected_detail_workspace",
    "activity": "filterable_timeline"
  },
  "operation_bindings": [
    {
      "component_action": "vault.unlock",
      "operation_id": "vault.unlock"
    }
  ],
  "device_bindings": [
    {
      "operation_id": "vault.unlock",
      "capability_id": "android.biometric.authenticate.v1"
    }
  ]
}
~~~

It contains no route implementation, code, arbitrary permission string, manifest entry, Gradle dependency, package coordinate, raw URL, shell command or executable test.

### 5.4 DeviceCapabilityManifest

Every allowed Android capability records:

~~~text
stable capability ID and version
official or custom provider provenance
minSdk, targetSdk and hardware-feature constraints
manifest declarations
runtime permission state machine
Tauri permission and capability scopes
Kotlin command and event schemas
Rust application wrapper schema
thread, coroutine and dispatcher requirements
lifecycle and foreground/background restrictions
user-consent and freshness requirements
data classification and retention policy
failure, cancellation and timeout taxonomy
emulator and physical-device requirements
positive, negative, poison and mutation fixtures
license and dependency closure
~~~

### 5.5 PermissionContract

~~~text
application authorization predicate
Android manifest and runtime permissions
permission states and transitions
temporary, one-time and permanent denial handling
settings-redirection policy
foreground/background distinctions
data minimization and requested scope
user explanation and consent requirements
revocation and recovery behavior
~~~

### 5.6 LifecycleContract

~~~text
Activity and process states
WebView visibility and suspension states
initialization and restoration obligations
configuration-change behavior
process-death persistence boundary
new-intent and deep-link handling
back and predictive-back transitions
plugin load/unload ownership
resource cancellation and cleanup
invalid transition behavior
~~~

### 5.7 BackgroundWorkContract

~~~text
job identity and semantic operation
durability and retry policy
constraints: network, charging, idle and storage
deadline and staleness policy
idempotency key and duplicate suppression
WorkManager or foreground-service binding
progress and cancellation events
Rust execution requirement
JNI allowance when WebView is suspended
privacy, battery and notification obligations
~~~

### 5.8 PlatformInteractionContract

Defines intents, deep links, share targets, file pickers, system settings, native authentication screens, notifications and other platform-owned interactions:

~~~text
input origin and allowlist
URI and payload validation
expected platform result
cancel/error behavior
resume and restoration behavior
data classification
external-app trust boundary
test fixture and UI Automator journey
~~~

### 5.9 MobileUIPlan

Extends the shared UIPlan with:

~~~text
adaptive navigation profile
window-size and posture transformations
system-bar, cutout and safe-region policy
keyboard/IME and focus behavior
touch targets and gesture ownership
Android back behavior
offline, stale and synchronization states
permission-request and denied states
native-surface handoff states
font scaling, localization and RTL behavior
TalkBack obligations
~~~

### 5.10 DeviceBindingPlan

The deterministic join between application operations and Android capabilities:

~~~text
operation -> Rust application command
Rust command -> policy and proof checks
proof-approved command -> Tauri mobile plugin method
plugin method -> Kotlin adapter
adapter -> Android API
Android result -> typed domain event
timeouts, cancellation and residual mapping
~~~

### 5.11 AndroidExperienceCertificate

Minted only after all required gates pass:

~~~text
input, schema, catalog and source hashes
Qwen model, tokenizer, grammar and inference hashes
SAE, DEMIURGE and Euclid evidence
proof object hashes and replay results
Tauri, Rust, Kotlin, Gradle and Android toolchain pins
renderer and dependency lock hashes
Tauri capabilities and Android permission manifest
unit, property, mutation and seam verdicts
browser, instrumentation, UI Automator and device verdicts
Macrobenchmark and resource measurements
APK/AAB hashes, signing mode and SBOM
license and third-party notices
bounded assumptions, waivers and unsupported claims
~~~

---

## 6. Engine subsystems

### 6.1 Shared Experience Core

The web and Android targets consume the same semantic UX compiler, component ontology, design-language compiler, precedent registry and base React/Vite renderer.

Renderer-specific behavior lives behind explicit target interfaces:

~~~text
ExperienceRenderer
  - ReactViteWebTarget
  - ReactViteTauriAndroidTarget
  - future ComposeTarget
~~~

The base renderer must not hard-code browser-only navigation, storage, file access or external-link behavior. Those are platform ports selected by the target profile.

### 6.2 Android Master Librarian

The model receives a bounded AndroidCheatSheet:

~~~text
allowed application and operation IDs
allowed screen, navigation and layout recipes
allowed design languages and component IDs
allowed device capabilities
permission and lifecycle invariants
offline/background profiles
known exclusions and contradictions
evidence and provenance references
~~~

Retrieved Android documentation remains quarantined evidence. Only audited catalog releases enter the trusted vocabulary.

### 6.3 Device Capability Registry

The registry normalizes official Tauri plugins and approved custom Kotlin adapters. Registry ingestion is:

~~~text
official source/docs/license
  -> exact version and commit pin
  -> quarantined metadata extraction
  -> DeviceCapabilityManifest
  -> generated Rust/Kotlin/TypeScript DTO conformance
  -> permission, lifecycle, threading and security fixtures
  -> emulator and device qualification
  -> mutation adequacy
  -> signed immutable catalog release
~~~

The model never selects an unregistered Android class or raw permission.

### 6.4 Operation and Transport Compiler

The compiler takes semantic OperationContracts and chooses a target transport:

- embedded Rust operation -> Tauri command;
- device effect -> Tauri mobile plugin call;
- remote multi-user service -> authenticated client to Axum;
- persistent job -> WorkManager binding;
- exceptional local external API -> hardened loopback Axum adapter.

Transport is a compilation detail, not model-authored application meaning.

### 6.5 Rust Application Runtime

The Rust core exposes typed application commands and events. It owns policy, validation, state transitions, synchronization and certificate replay. It must be testable as an ordinary Rust library without Tauri, Android or a network server.

The runtime has no authority to grant Android permissions. It can only decide whether application policy allows a request and then ask the Kotlin adapter to evaluate platform authority.

### 6.6 Tauri Command Broker

The broker is the only normal frontend-to-core entry point. It:

- validates command schemas;
- maps frontend identity and window/webview identity;
- checks Tauri capability scope;
- invokes Rust application policy;
- verifies required certificates;
- calls the device adapter only after authorization;
- canonicalizes errors;
- records evidence without leaking secrets;
- rejects unknown, stale or replayed requests.

### 6.7 Kotlin Plugin Adapter Foundry

Each Kotlin adapter is small and single-purpose. It may translate Android callbacks, coroutines and lifecycle events into a typed platform result, but it may not recreate application policy.

Long-running native work must leave the Android main thread. Callback completion, cancellation, timeout and process restoration are explicit parts of the adapter contract.

### 6.8 Background Execution Bridge

Foreground calls use Rust-to-Kotlin Tauri plugin messages.

When persistent work must continue while the WebView is suspended:

1. Kotlin WorkManager owns scheduling and Android lifecycle.
2. The job consumes a canonical BackgroundWorkContract.
3. If shared Rust logic is required, Kotlin may call a narrow exported Rust function through JNI.
4. The JNI boundary is versioned, panic-contained, memory-owned explicitly and qualified by ISTHMUS.
5. Results are committed idempotently and surfaced to the UI as typed events when it resumes.

JNI is an exceptional platform seam, not the normal frontend transport.

### 6.9 Euclid-Ω Adapter

Build-time Euclid reasons about:

- navigation and critical-task reachability;
- protected-action exclusion;
- permission-state machines;
- lifecycle transition legality;
- back-stack safety;
- offline queue invariants;
- synchronization safety assumptions;
- background-job idempotency and termination;
- refinement from SAE/DEMIURGE semantics to UI and device plans.

Runtime eo-kernel replays the proof objects actually needed for policy-sensitive execution. The certificate declares whether a claim is fully proved, proved relative to named obligations, bounded or refused.

### 6.10 Deterministic Tauri Android Renderer

The renderer materializes:

- React/TypeScript/Vite source from MobileUIPlan;
- owned component templates and design-token CSS variables;
- Tauri configuration and application commands;
- Rust operation and event adapters;
- Tauri permission/capability files;
- Kotlin plugin binding stubs from the device registry;
- Android Manifest fragments from audited capability manifests;
- Gradle configuration from pinned templates;
- localization resources and platform icons;
- source maps from generated artifacts to plan nodes;
- reproducible dependency locks and SBOM inputs.

Unknown components, capabilities, operations, permissions, dependencies and configuration keys fail closed.

### 6.11 Axum Network Adapter

The Axum adapter compiles remote service OperationContracts into:

- versioned routes and DTOs;
- authentication and authorization middleware;
- bounded body and timeout policies;
- idempotency and retry semantics;
- error and telemetry contracts;
- OpenAPI or equivalent machine-readable contracts;
- client bindings consumed by the Android Rust core.

An Android application can work offline without Axum where its product semantics permit it. Axum is not required merely because the application contains Rust.

### 6.12 Residual Repair Loop

Failures become typed residuals such as:

~~~json
{
  "gate": "android_permission_fsm",
  "code": "PERMANENT_DENIAL_RECOVERY_MISSING",
  "path": "/device_bindings/0",
  "capability_id": "android.location.precise.v1",
  "allowed_patches": [
    "select_denial_recovery_recipe",
    "downgrade_capability_scope",
    "remove_optional_capability"
  ]
}
~~~

Qwen may patch only allowlisted binding fields. It cannot patch Kotlin, Rust, renderer templates, schemas, catalogs, proof code, manifest output or oracle logic.

---

## 7. Interaction of the Woven Line engines

| Engine/system | Android responsibility |
|---|---|
| LONG-HORIZON-CODING-HARNESS | Macro FSM, per-module behavior trees, budget, checkpoints, context isolation and atomic attempts |
| WEB-EXPERIENCE-ENGINE core | Shared UX compilation, design languages, component foundry and React/Vite materialization |
| SAE | Stateful application truth, database and migration contracts, offline persistence, transactions and restart invariants |
| DEMIURGE | Stateless algorithms, authorization, reducers, protocol kernels and decidable FSM synthesis |
| Euclid-Ω | Planning, proof search, lifecycle/permission/navigation reasoning and replayable certificates |
| LOOM | Assembles TypeScript, Rust, Kotlin, Gradle, manifests, resources and remote services |
| ISTHMUS | Tests TypeScript-Rust-Kotlin-JNI transparency, threading, ownership and error propagation |
| ROSETTA | Produces one polyglot fact graph across TypeScript, Rust and Kotlin |
| ORRERY | Analyzes dependency, capability, permission and lifecycle graphs |
| Graphify | Maps cross-engine, component, operation, device and test relationships |
| ARIADNE | Localizes Android build, runtime, lifecycle and journey failures |
| KINTSUGI | Applies preconditioned repairs under a non-regression ratchet |
| GRAFT | Adds the Android target or a new device capability to an existing application |
| CRUCIBLE | APK/AAB readiness, security, performance, SBOM, signing and packaging |
| AUGUR | Supplies ratified mobile UX precedents with applicability boundaries |
| SOVEREIGN-RETRIEVAL-ORACLE | Retrieves and quarantines Android/Tauri/provider evidence |
| TOAM Memory OS | Canonical Git-backed decision, evidence, residual and certificate ledger |
| HARNESS-AUTONOMY-GAUNTLET | Autonomous application-level qualification |

No engine self-certifies its own output. A proposer may emit properties or candidates; independent gates authorize promotion.

---

## 8. Independent verification stack

### 8.1 Contract and schema gate

- canonical JSON/schema validation;
- cross-language DTO golden tests;
- operation, component and capability closure;
- exact version and hash compatibility;
- rejection of unknown fields and identifiers;
- no model-authored executable verification.

### 8.2 Rust core gate

- unit, property and mutation tests;
- deterministic serialization and state-transition replay;
- authorization truth tables;
- offline queue and synchronization invariants;
- certificate replay and stale-certificate rejection;
- panic containment and resource budgets.

### 8.3 Kotlin and plugin gate

- Kotlin unit tests;
- Android instrumentation tests;
- permission grant, denial, permanent denial and revocation;
- Activity recreation, process death and new-intent handling;
- coroutine dispatcher and cancellation behavior;
- main-thread blocking/ANR poisons;
- typed error and timeout conformance.

### 8.4 Tauri seam gate

- frontend cannot call privileged raw plugin methods;
- capabilities are least-privilege and target-specific;
- TypeScript/Rust/Kotlin DTO parity;
- command/event cancellation and ordering;
- WebView reload and suspension recovery;
- untrusted remote content cannot acquire local authority.

### 8.5 Mobile UI and accessibility gate

- shared Storybook/browser component-state qualification;
- installed-application journeys with UI Automator;
- TalkBack-critical journeys;
- focus visibility and order;
- touch target sizing and gesture conflicts;
- font scaling, localization and RTL;
- keyboard/IME behavior;
- reduced motion and contrast;
- system dialogs and native handoff recovery.

### 8.6 Adaptive layout gate

The matrix includes:

- compact phone portrait and landscape;
- large phone;
- tablet;
- foldable postures and resizable windows where supported;
- system-bar and cutout variants;
- light/dark and high-contrast conditions;
- large fonts and display scaling;
- offline and flaky network states.

No critical action may be clipped, occluded, unreachable or dependent on one posture.

### 8.7 Lifecycle and background gate

- back and predictive-back transitions;
- home/background/foreground cycles;
- Activity recreation and process death;
- WorkManager persistence, retry and duplicate suppression;
- Doze and App Standby fixtures where relevant;
- notification tap and deep-link relaunch;
- foreground-service notification obligations;
- job cancellation and stale-result rejection.

### 8.8 Security and privacy gate

- least-privilege Android and Tauri permissions;
- no generic JavaScript-to-device bridge;
- deep-link, intent and file/URI validation;
- remote content and navigation allowlists;
- secret storage through an approved Keystore-backed adapter;
- TLS and remote-service authentication;
- no arbitrary shell, package, manifest or Gradle injection;
- repository-root and generated-path validation;
- sensitive log redaction;
- SSRF, oversized payload, redirect and origin poisons where networking exists.

### 8.9 Performance and resource gate

- release-like APK/AAB;
- Macrobenchmark startup and critical interactions;
- frame timing and WebView rendering behavior;
- Rust/Kotlin operation latency;
- memory, binary size and battery-sensitive work budgets;
- physical-device measurements for representative release claims;
- Baseline Profile evaluation where it materially improves measured journeys.

### 8.10 Release and supply-chain gate

- reproducible source and lockfiles;
- Android lint and release build;
- APK/AAB hash and signature verification;
- exact Rust, Node, Tauri, Kotlin, Gradle and Android toolchain pins;
- SBOM and third-party notices;
- license audit for plugins, components, icons, fonts and native libraries;
- target SDK and store-policy review;
- secret-free build artifacts.

### 8.11 Mutation adequacy gate

Critical mutations include:

- bypassed application authorization;
- direct JavaScript plugin invocation;
- stale proof certificate accepted;
- missing Android permission;
- permission denial treated as success;
- background job duplicated;
- lifecycle-invalid device call;
- main-thread blocking Kotlin command;
- malformed JNI ownership;
- wrong operation-to-device binding;
- predictive-back dead end;
- unrecoverable process death;
- tablet or foldable action occlusion;
- missing TalkBack label;
- insecure deep link;
- loopback Axum bound beyond localhost;
- missing loopback authentication;
- arbitrary remote WebView navigation;
- unlicensed plugin or asset.

Every critical mutant must be rejected in the same invocation. Equivalent mutants are classified explicitly.

---

## 9. Android execution profiles

### 9.1 Embedded offline-first application

~~~text
React/Vite WebView
  -> Tauri command
  -> Rust core
  -> local storage/sync queue
  -> Kotlin device adapters as needed
~~~

No Axum process is required.

### 9.2 Connected client with remote Rust services

~~~text
Android application
  -> Rust networking client
  -> authenticated remote Axum API
  -> server-side SAE/DEMIURGE services
~~~

Offline state and retries remain governed by SAE contracts.

### 9.3 Persistent background processing

~~~text
WorkManager
  -> Kotlin worker
  -> narrow JNI Rust core call if required
  -> idempotent state/evidence commit
  -> typed notification/event
~~~

The WebView is not assumed to be alive.

### 9.4 Exceptional local HTTP service

Allowed only when another local process or external client legitimately needs HTTP. The exception must be documented, threat-modeled and certified. A loopback server is never selected by Qwen merely because an operation resembles a REST route.

---

## 10. Repository architecture

The preferred final repository is a shared Experience Engine with target packages:

~~~text
EXPERIENCE-ENGINE/
  README.md
  LICENSE
  THIRD_PARTY_NOTICES.md
  schemas/
    shared/
      application-capability.schema.json
      operation-contract.schema.json
      design-brief.schema.json
      ux-contract.schema.json
      design-language.schema.json
      component-manifest.schema.json
      ui-plan.schema.json
      residual.schema.json
      experience-certificate.schema.json
    android/
      mobile-ux-binding.schema.json
      device-capability.schema.json
      permission-contract.schema.json
      lifecycle-contract.schema.json
      background-work-contract.schema.json
      platform-interaction.schema.json
      mobile-ui-plan.schema.json
      device-binding-plan.schema.json
      android-experience-certificate.schema.json
  src/experience_engine/
    ir/
    catalog/
    librarian/
    ux/
    reasoning/
    composition/
    repair/
    provenance/
    orchestration/
  renderers/
    react-vite-core/
    web/
    tauri-android/
  targets/android/
    operations/
    capabilities/
    permissions/
    lifecycle/
    background/
    platform/
    security/
    packaging/
  runtimes/
    rust-core/
    euclid-runtime/
    tauri-command-broker/
    axum-network-adapter/
  plugins/android/
    registry/
    official-adapters/
    custom-adapters/
  kotlin/
    dto/
    plugins/
    workers/
    instrumentation/
  catalog/
    shared-components/
    design-languages/
    mobile-layouts/
    android-capabilities/
    mobile-precedents/
  tests/
    unit/
    contracts/
    property/
    mutation/
    integration/
    browser/
    android-unit/
    instrumentation/
    ui-automator/
    adaptive/
    lifecycle/
    security/
    performance/
    release/
    e2e/
  fixtures/
    devices/
    permissions/
    lifecycle/
    background/
    intents/
    poisons/
  docs/
    architecture/
    adr/
    threat-model/
    qualification/
~~~

If WEB-EXPERIENCE-ENGINE remains a separate repository during migration, the Android package must consume versioned shared schemas and catalogs rather than copying them. The long-term destination is one shared core with independently releasable target adapters.

---

## 11. Architectural implementation sequence

### Phase A0 — Freeze shared and Android boundaries

Deliver:

- shared ExperienceRenderer interface;
- transport-independent OperationContract;
- Android trust model;
- Axum exception policy;
- build-time versus runtime Euclid decision;
- initial toolchain and license pins.

Exit:

- the existing React/Vite renderer has no unavoidable browser-only assumptions;
- no trusted path depends on model-authored code or commands.

### Phase A1 — Android contracts and canonicalization

Deliver the Android IR schemas, canonical serialization, hashes and cross-language fixtures.

Exit:

- TypeScript, Rust and Kotlin agree on golden DTOs;
- unknown fields, identifiers and version drift fail closed.

### Phase A2 — First device-capability foundry

Start with a narrow audited set:

- biometric authentication;
- secure storage;
- file selection/sharing;
- notifications;
- deep links;
- network state;
- camera or barcode capture;
- persistent background job.

Exit:

- every capability has permission, lifecycle, threading, security and mutation evidence;
- no raw Android API name appears in model output.

### Phase A3 — Tauri Android target materializer

Deliver deterministic generation of Tauri configuration, commands, capabilities, Android Manifest fragments, Gradle bindings, Kotlin stubs and reproducible development/release builds.

Exit:

- the same frozen plan produces equivalent source and package structure;
- unknown configuration cannot be emitted.

### Phase A4 — Mobile UX and adaptive compiler

Deliver Android navigation, back, permission, offline, posture, IME and native-handoff transformations over the shared UI plan.

Exit:

- every critical journey has success, cancel, denial, error and restoration states;
- phone, tablet and foldable constraints are satisfiable.

### Phase A5 — Euclid Android reasoning plane

Deliver permission, lifecycle, navigation, background-work and refinement proof adapters plus runtime certificate replay.

Exit:

- planted unauthorized paths, dead ends, lifecycle violations and non-idempotent background plans are rejected;
- proof replay succeeds without Qwen.

### Phase A6 — SAE, DEMIURGE and remote Axum composition

Deliver offline state, migrations, synchronization, stateless kernels, policy and optional remote services.

Exit:

- operation semantics remain identical across embedded and remote bindings;
- process death and retry do not corrupt durable truth.

### Phase A7 — Android oracle and mutation laboratory

Deliver UI Automator, instrumentation, adaptive layout, lifecycle, security, performance and release gates.

Exit:

- every critical mutation is killed;
- verifier failure yields NO_RESULT, never success.

### Phase A8 — Qwen3-0.6B binding and repair

Deliver one strict MobileUXBinding grammar, bounded Android cheat sheet, temperature-zero baseline, prompt-lookup acceleration qualification and typed JSON Patch repair.

Exit:

- Qwen cannot emit implementation or oracle code;
- frozen hashes survive repair;
- ambiguous cases abstain;
- retries change the candidate when a permitted repair exists.

### Phase A9 — Autonomous Android gauntlet

Run difficult stateless and stateful Android applications without handholding. The portfolio must cover:

- offline-first state;
- authentication and authorization;
- background work;
- notifications and deep links;
- at least three distinct device APIs;
- adaptive phone/tablet layouts;
- remote Axum service integration;
- process-death recovery;
- accessibility and performance.

Production readiness requires every selected application to pass application-specific deterministic oracles, Android release qualification and human review on representative physical devices. A desktop browser preview alone is not mobile acceptance.

---

## 12. Initial MVP vertical slice

The first credible slice is a **secure offline field-inspection application**:

1. SAE defines inspections, evidence, drafts, synchronization, assignments and durable workflow.
2. DEMIURGE synthesizes authorization and stateless validation kernels.
3. Euclid proves workflow reachability, protected-action exclusion, retry/idempotency and lifecycle obligations.
4. Qwen chooses a bounded operations-workspace UX, navigation and capability bindings.
5. React/Vite renders dashboard, assignments, inspection form, evidence capture, offline queue and synchronization status.
6. Tauri hosts the application and exposes only allowlisted application commands.
7. Kotlin adapters provide biometrics, camera capture, secure storage, network state, notifications and WorkManager synchronization.
8. Rust owns application policy, validation, offline queue semantics and certificate replay.
9. An optional remote Axum service receives synchronized inspections.
10. Android oracles test denial, offline work, process death, duplicate synchronization, deep-link notification launch, accessibility, adaptive layout and performance.

This slice exercises every trust boundary without requiring a broad device catalog.

---

## 13. Non-goals and honest limits

The first production version will not:

- use Axum as a default in-process UI bus;
- let Qwen invent Kotlin, Rust, JSX, permissions, dependencies or routes;
- claim absolute memory safety across Rust, JavaScript, Kotlin, JNI and Android;
- claim zero ambient authority without measured capability and permission enforcement;
- treat Android permission as application authorization;
- claim Euclid proves an Android adapter implementation;
- run full proof search on-device by default;
- allow privileged plugin methods to be called directly by arbitrary frontend code;
- promise instant iOS portability without Swift capability adapters;
- claim Radix primitives eliminate Android lifecycle defects;
- claim screenshots or machine gates prove beauty;
- support every Android device API in the initial catalog;
- introduce a Compose renderer before the Tauri React/Vite lane passes its conformance suite.

Applications whose primary experience depends on high-frequency native rendering, platform widgets, unusually deep native UI integration or WebView-incompatible performance constraints may require a future Compose target. Such a target must refine the same UX and operation contracts rather than creating a separate reasoning system.

---

## 14. Final system invariants

> No model-authored Android decision becomes executable authority merely because it is plausible. Every accepted UI node, application operation, device capability, permission, lifecycle transition, background job and network binding must belong to a pinned vocabulary, refine declared application semantics, satisfy the formal properties that are actually decidable, pass independent runtime and mutation oracles, and carry replayable provenance.

> Kotlin owns Android authority. Rust owns application truth. Tauri owns the trusted in-process bridge. React/Vite owns deterministic presentation. Axum owns actual network boundaries. Euclid proves and replays. DEMIURGE synthesizes decidable stateless kernels. SAE realizes durable state. LOOM assembles the polyglot product. Independent oracles alone authorize release.

These invariants make the architecture suitable for a 0.6B controller: the model is powerful because the system shrinks its decision surface to typed, retrieved and independently verified choices.

---

## 15. Authoritative implementation references

- Tauri mobile plugin development and Kotlin/Rust boundary: <https://v2.tauri.app/develop/plugins/develop-mobile/>
- Tauri permissions and capabilities: <https://v2.tauri.app/security/permissions/>
- Tauri official plugin catalog: <https://v2.tauri.app/plugin/>
- Android application architecture: <https://developer.android.com/topic/architecture>
- Android persistent background work and WorkManager: <https://developer.android.com/develop/background-work/background-tasks/persistent>
- Android UI Automator: <https://developer.android.com/training/testing/other-components/ui-automator>
- Android Macrobenchmark: <https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview>
- Axum documentation: <https://docs.rs/axum/latest/axum/>
- Existing shared web architecture: ../WEB%20ENGINE%20IDEAS/FINAL_WEB_EXPERIENCE_ENGINE_ARCHITECTURE.md
- Euclid-Ω Rust proof kernel: ../external/EUCLID-OMEGA/crates/eo-kernel/

