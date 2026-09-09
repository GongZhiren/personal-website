# Empirical data provenance

This revision introduces no new model-training result. Every empirical value in
`main.tex` is copied from the supplied manuscript or is a transparent arithmetic
summary of those values.

## Accuracy endpoints

- ViT-B/32 eight-task RegMean++: 84.2.
- ViT-B/32 E2E representative 12k run: 90.2.
- ViT-B/32 E2E four-seed 8k mean: 89.8 +/- 0.4.
- ViT-B/16 RegMean++ / E2E: 87.3 / 92.0 (single E2E run).
- ViT-L/14 eight-task RegMean++: 90.9.
- ViT-L/14 E2E representative / multi-seed: 94.3 / 94.2 +/- 0.1.
- ViT-L/14 TALL-20 best evaluated non-iterative baseline / E2E:
  83.4 / 92.9 +/- 0.2.

## Data-budget sweep, ViT-B/32

Distinct examples per task: 64, 128, 256, 512, 1024.

- E2E fixed set: 81.3, 83.5, 86.1, 87.7, 88.5.
- RegMean++ matched N: 83.3, 83.9, 84.4, 84.3, 84.5.
- E2E full-split reshuffling endpoint: 90.1.

## Iteration sweep, ViT-B/32

At learning rate 5e-6:

- 4k: 89.2;
- 8k: 90.1;
- 12k: 90.2.

Derived, not newly measured:

- gains over 84.2 RegMean++: +5.0, +5.9, +6.0;
- marginal gains: +0.9 and +0.1;
- fraction of the final six-point gain: 5.0/6.0 = 83.3%,
  5.9/6.0 = 98.3%.

## Measured runtime and memory endpoints

- ViT-B/32, eight tasks: 12k steps, about 35 min, about 8 GB.
- ViT-L/14, eight tasks: 8k steps, about 13 min, about 31 GB.
- ViT-L/14, twenty tasks: 16k steps, about 34 min, about 24 GB.
- RegMean/RegMean++ is described in the source as on the order of a minute;
  no more precise value is introduced.

No intermediate wall-clock is interpolated.

## Block-wise memory--accuracy results

ViT-B/32 group sizes 1, 2, 3, 4, 6, 12:

- accuracy: 85.3, 87.4, 88.4, 88.9, 89.2, 89.8;
- peak memory: 3.7, 3.9, 4.0, 4.2, 4.5, 5.4 GB.

The canonical full-streaming endpoint is 90.2 at about 8 GB.

ViT-L/14:

- one block: 92.0 at about 13 GB;
- four blocks: 93.0 at about 15 GB;
- full block-wise: 94.2 at about 31 GB.

## Difficulty axes

- ViT-B/32 E2E--RegMean++ margin at 2, 4, 6, 8 experts:
  +2.6, +3.3, +4.4, +6.0.
- ViT-B/32 twenty-expert margin: +13.7.
- TALL-20 margin over the best evaluated baseline:
  +9.5 on ViT-L/14, +12.0 on ViT-B/16, +13.7 on ViT-B/32.

## Target and residual controls

Target-by-initialization:

- B/32 pre-trained: KL 87.9, representation 89.5;
- B/32 task arithmetic: KL 88.0, representation 90.2;
- L/14 pre-trained: KL 92.3, representation 94.1;
- L/14 task arithmetic: KL 92.2, representation 94.3.

Residuals:

- summed layer-wise: 2.46 RegMean++, 2.11 E2E;
- final representation: 0.83 task arithmetic, 0.55 RegMean++, 0.23 E2E.

Sharpness-aware logit control (existing in-harness control, rho swept over
{0.02, 0.05, 0.10}; not an official SAMerging reproduction):

- ViT-B/32 best logit+SAM: 89.1;
- ViT-L/14 logit / logit+SAM: 92.4 / 92.9 (both below representation 94.3).

## Optimization-based control

- Layer-wise AdaMerging, ViT-B/32 eight tasks, same harness: 82.6,
  below closed-form RegMean++ (84.2). Indicates gradient computation alone is
  insufficient; AdaMerging additionally uses an entropy objective.

## Preliminary Flan-T5 GLUE probe

- Task arithmetic: 79.0;
- TIES: 80.2;
- RegMean: 83.0;
- iterative E2E: 81.9.

The manuscript retains the source caveat that RegMean and E2E use different
functional readouts in this experiment.

## New figure

`fig_budget_frontiers.pdf` plots the existing data-budget, selected-rate update,
and ViT-B/32 memory measurements listed above. It contains no fitted or
interpolated point.

No functional-loss value, uniform-deviation term, smoothness constant,
Polyak--Lojasiewicz constant, or numerical theoretical break-even time is
estimated from accuracy.
