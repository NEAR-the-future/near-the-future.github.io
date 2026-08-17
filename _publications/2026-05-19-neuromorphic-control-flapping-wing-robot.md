---
title: "Neuromorphic Control of a Flapping-Wing Robot on Resource-Constrained Hardware"
collection: publications
category: preprints
permalink: /publication/2026-05-19-neuromorphic-control-flapping-wing-robot
excerpt: "Neuromorphic control for flapping-wing robots on compact, resource-constrained hardware."
date: 2026-05-19
venue: "arXiv preprint arXiv:2605.19430"
authors: "Rim El Filali, Chenrui Feng, Chao Gao, and Weibin Gu"
paperurl: "https://arxiv.org/abs/2605.19430"
arxivurl: "https://arxiv.org/abs/2605.19430"
codeurl: "https://anonymous.4open.science/r/Espikify-76E3/"
---

<section class="paper-spotlight">
  <p class="paper-kicker">Preprint Spotlight</p>
  <p class="paper-lead">
    This work presents a hierarchical neuromorphic control framework for a flapping-wing micro aerial vehicle under severe onboard computing constraints. The system deploys lightweight spiking neural networks on an ESP32-class microcontroller for state estimation and closed-loop control.
  </p>

  <p class="paper-actions">
    <a href="https://arxiv.org/abs/2605.19430">arXiv</a>
    <a href="https://arxiv.org/pdf/2605.19430">PDF</a>
    <a href="https://anonymous.4open.science/r/Espikify-76E3/">Code</a>
  </p>
</section>

<figure class="paper-figure paper-figure--wide">
  <img src="/images/publications/neuromorphic_control_teaser.png" alt="Neuromorphic control framework, robot hardware, and flight demonstration">
  <figcaption>
    Original paper teaser figure showing the data-to-deployment workflow, the butterfly-inspired FWMAV hardware, and untethered flight demonstrations.
  </figcaption>
</figure>

## Why This Matters

Small flapping-wing robots face strict limits in payload, power, and onboard computation. Conventional neural controllers can be difficult to deploy directly on such platforms. Neuromorphic approaches offer a biologically inspired alternative that may reduce latency and power while preserving responsive behavior.

## Main Contributions

- Proposes a hierarchical neuromorphic control framework for a flapping-wing micro aerial vehicle.
- Deploys two lightweight spiking neural networks onboard: one for state estimation and one for control through central-pattern-generator modulation.
- Trains the controller by imitation learning and evaluates closed-loop pitch and heading tracking in untethered flight.
- Demonstrates spike-based computation on a low-cost, widely available ESP32 microcontroller rather than specialized neuromorphic hardware.

## Key Findings

- The SNN-based controller reduces reported inference latency from 1059 us to 680 us relative to an ANN baseline.
- The SNN-based controller reduces reported inference power from 0.033 W to 0.027 W relative to the same baseline.
- The experiments demonstrate fully onboard neuromorphic control for autonomous flapping-wing flight under stringent SWaP constraints.

<div class="paper-figure-grid">
  <figure class="paper-figure">
    <img src="/images/publications/neuromorphic_control_latency_power.png" alt="Latency and power comparison for SNN, ANN, and event-driven SNN inference">
    <figcaption>Original paper figure comparing inference latency and power on resource-constrained hardware.</figcaption>
  </figure>
</div>

## Citation

El Filali, Rim, Chenrui Feng, Chao Gao, and Weibin Gu. "Neuromorphic Control of a Flapping-Wing Robot on Resource-Constrained Hardware." *arXiv preprint arXiv:2605.19430* (2026).
