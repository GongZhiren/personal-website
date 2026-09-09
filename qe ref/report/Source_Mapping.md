# QE Report — Technical Story and Source Mapping

## Thesis-level narrative

The report is deliberately **not** a paper-by-paper compilation. It is organized around one PhD question:

> How can foundation models realize efficient, scalable, and reliable deployment under heterogeneous demands, and what internal evidence can guide that adaptation?

The report uses two diagnoses to establish the problem and then develops two technical thrusts.

1. **External diagnosis — XDomainBench.** Controlled cross-domain composition shows that strong constituent knowledge does not imply reliable performance when heterogeneous knowledge must be composed across turns. It defines the external deployment/reasoning pressure.
2. **Internal diagnosis — CoAx.** Self-repair shows that the model is not a static set of independently important units: interventions can recruit dormant computation, making importance conditional on what else remains available.
3. **Part I — Adaptive Model Execution.** SubspacePath Pruner -> CoCurve -> AnchorPath moves from scenario-conditioned pathways, to interaction-aware allocation, to continuation along a changing high-sparsity operating point.
4. **Part II — Adaptive Reasoning.** SoT -> LoTR moves from endogenous trajectory control (evidence and stopping) to state-matched internal pathway routing.
5. **Synthesis.** Scenario, reasoning state, pruning operating point, and intervention are all conditioning variables. The recurring methodological response is to replace static allocation with conditional, model-informed allocation while explicitly modeling interactions.

E2E-Merge is intentionally omitted from the technical narrative to preserve focus. Other collaborative work remains in the research-output section rather than being forced into the thesis story.

---

## XDomainBench — diagnostic foundation / external symptom
**Source:** supplied `XDomainBench.zip`

**Technical material retained**
- Interactive trajectory formulation and controlled composition order `k=1..4`.
- Domain mixture / difficulty as measurable trajectory variables.
- Minimal construction logic needed to distinguish constituent knowledge from compositional reasoning.
- Turn-1 evidence showing that composition difficulty exists before long-session accumulation.
- Multi-turn interpretation: trajectory effects can amplify the initial compositional burden.

**Role in QE**
Defines why heterogeneous real deployment/reasoning cannot be treated as a single homogeneous regime. It is intentionally concise: the benchmark is evidence for the research problem, not a third technical pillar.

**Project-source figures reused**
- benchmark design / controlled-composition figure.
- turn-1 composition analysis.

---

## CoAx — diagnostic foundation / internal symptom
**Source:** supplied `CoAx(1).zip`

**Technical material retained**
- Finite ablation effects before and after primary-set removal.
- Fisher-geometry energy used to compare output perturbations.
- Conditional co-ablation score as the change in candidate effect under intervention.
- Möbius/all-order interaction interpretation explaining why conditioning aggregates hidden higher-order interactions.
- Key empirical evidence: backup recovery, matched wrong-primary negative control, and causal hand-off/self-repair evidence.

**Role in QE**
Turns the external diagnosis inward: a model can reorganize computation after intervention, so a static independent-component view is insufficient. This becomes a conceptual bridge into interaction-aware model execution.

**Project-source figures reused**
- CoAx teaser / primary-to-backup phenomenon.
- conditional-score / method analysis panels.
- route/repair validation panel where useful.

---

## SubspacePath Pruner — core technical work I
**Source:** supplied `SubspacePath_Pruner.zip`

**Problem**
A frozen foundation model must serve coherent but heterogeneous deployment scenarios without scenario-specific labels or retraining. One global head ranking cannot express that scenario dependence.

**Technical material retained**
- Frozen-model mask formulation and semantic-axis representation.
- Domain-Basis Synthesis: orthogonality/coverage objective for a compact domain basis.
- Layer-wise probes that read axis relevance from residual representations.
- Representation–parameter coupling score mapping semantic axes to head-level pathways.
- Domain-invariant whitelist and its role in preserving general capability.
- Scenario-breadth statistic, cached importance mixture, and adaptive budget formula.
- End-to-end online compiler: scenario -> probe mixture -> head scores -> reusable executable mask.
- Main cross-domain/OOD results, compilation overhead, speedup/memory trade-off.
- Load-bearing ablations: random axes, no whitelist, no multi-domain mixing.

**Why this depth matters**
This is the first full constructive answer in the thesis: it shows concretely how an external context can be read through the model's representation and translated into an internal execution decision.

**Project-source figures/evidence reused**
- representation–pathway coupling figure.
- domain-basis / probe evidence.
- head-level pathway and whitelist evidence.
- method/pipeline figure.
- accuracy-efficiency trade-off figure.
- Exact result and ablation tables transcribed from the project source.

---

## CoCurve — core technical work II
**Source:** supplied `CoCurve.zip`

**Problem**
Scenario conditioning still does not justify assigning each structured unit an intrinsic scalar importance. Structured pruning removes sets, and the damage of a set need not be additive.

**Technical material retained**
- Output-grounded self-distillation KL risk around the dense model.
- Why zero risk and zero first derivative at the dense point make the second-order term the leading local object.
- Diagonal/off-diagonal decomposition: node saliency versus co-pruning curvature.
- Fisher/Gram identity estimating the interaction matrix from `M` single-unit ablations rather than `O(M^2)` pair sweeps.
- Shared attention/FFN cost budget and interaction-aware marginal criterion.
- Finite lambda solution path and held-out selection logic.
- Mechanistic evidence: cross-module coupling, long-range coupling, bridge units, and matched causal removal controls.
- Main language-model results, ratio sweep, physical latency/memory measurements, and VLM transfer.

**Why this depth matters**
It changes the mathematical object of model execution from a ranking of nodes to a risk over sets, directly implementing the non-separability exposed conceptually by the diagnostic section.

**Project-source figures/evidence reused**
- User-specified CoCurve overview image.
- interaction/anatomy and lambda-path figures.
- bridge/coupling evidence.
- pruning-ratio sweep.
- Exact result table transcribed from the source; unsupported/uncertain rows were deliberately excluded.

---

## AnchorPath — concise extreme-regime extension
**Source:** supplied `AnchorPath.zip`

**Technical material retained**
- High-sparsity collapse as a moving-operating-point problem rather than only a bad-score problem.
- Dense teacher/Fisher anchor plus current-state perturbations.
- Stagewise/nested continuation formulation and cost-normalized marginal.
- Exact headline high-sparsity comparison showing the largest benefit at the extreme pruning regime.

**Role in QE**
A boundary study: even a better criterion can fail if it is evaluated once and extrapolated too far. The allocation rule itself must update as the operating point moves. Kept brief to preserve focus.

**Project-source figures reused**
- AnchorPath method/continuation figure.
- headline high-sparsity result figure where appropriate.

---

## State of Thought (SoT) — core technical work III
**Source:** supplied `SoT.zip`

**Problem**
Test-time reasoning methods mostly prescribe an external procedure. Heterogeneous tasks and changing trajectories need different evidence and different amounts of computation.

**Technical material retained**
- Trajectory factorization and endogenous state definition from geometry/progress/direction/uncertainty.
- State-conditioned evidence operator and stopping operator.
- Closed-loop interpretation: the model state controls both what history remains active and whether reasoning continues.
- state-space/state-activation evidence.
- Main domain-level accuracy table across representative baselines.
- Generated-token and wall-clock efficiency comparison / Pareto frontier.
- Selected ablations showing that evidence selection, stopping, dynamics, geometry, and uncertainty are not interchangeable shortcuts.

**Why this depth matters**
SoT moves the thesis from parameter-space allocation to temporal allocation while preserving the same principle: computation should follow the model's current state rather than a fixed external script.

**Project-source figures/evidence reused**
- state-space visualization.
- state-conditioned evidence/activation visualization.
- accuracy-token-latency / Pareto figures.
- Exact result and ablation tables transcribed from source.

---

## LoTR — core technical work IV
**Source:** supplied `LoTR.zip`

**Problem**
A reasoning wrapper controls the outer trajectory but normally leaves the internal head pathway to the frozen backbone. SoT controls evidence and stopping; the next question is whether the step itself should be executed through a state-matched pathway.

**Technical material retained**
- Soft head-participation pathway formulation.
- Offline shared logic-state basis and soft state targets.
- Layer-specific probes for current logic-state mixture.
- Cached logic-conditioned head templates.
- Online soft composition/routing of the next-step pathway while leaving the outer reasoning paradigm unchanged.
- logic-trajectory/pathway-pattern evidence.
- Paired evaluation over eight outer paradigms, multiple benchmarks and backbones.
- Main paradigm-average results, latency/token trade-offs, and routing ablations.
- case-study evidence showing state/pathway adaptation at reasoning-step resolution.

**Why this depth matters**
It completes the strongest cross-paper symmetry in the QE: SubspacePath Pruner couples *scenario state -> pathway*, while LoTR couples *reasoning state -> pathway*. It also reconnects the two technical parts at the parameter level.

**Project-source figures/evidence reused**
- LoTR pipeline.
- logic-state trajectories and head-pathway patterns.
- quality-efficiency trade-off.
- case study.
- Exact result and ablation tables transcribed from source.

---

## Synthesis and future plan

The technical sections are followed by a thesis-level synthesis rather than another paper summary:
- **Conditionality:** context, intervention, pruning state, and reasoning state all legitimately change what computation is useful.
- **Relationality:** unit value can depend on what else is active, removed, or already executed.
- **Two timescales:** deployment-time structural allocation and test-time reasoning allocation are two manifestations of adaptive computation.
- **Efficiency and reliability:** both ultimately require estimating what is needed *now* and knowing when that estimate should not be trusted.

Future work remains deliberately two-pronged:
1. deepen adaptive model execution and adaptive reasoning toward stronger generalization, trustworthiness, and realized system efficiency;
2. extend the principles to agents, tools, memory, multimodal/physical-world inputs, and long-horizon interaction.

## Figure-use policy
Technical sections reuse project figures/tables from the supplied sources. The only custom figure is the thesis-level executive roadmap, whose purpose is navigation rather than technical evidence. Figures were selected for explanatory necessity; the report does not reproduce every experiment from every paper.
