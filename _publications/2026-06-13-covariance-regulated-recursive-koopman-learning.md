---
title: "Covariance-Regulated Recursive Koopman Learning for Nonlinear Systems with Uncertain Time-Varying Dynamics"
collection: publications
category: preprints
permalink: /publication/2026-06-13-covariance-regulated-recursive-koopman-learning
excerpt: "Recursive Koopman learning with covariance regulation for uncertain, time-varying nonlinear systems."
date: 2026-06-13
venue: "arXiv preprint arXiv:2606.15317"
authors: "Weibin Gu, Chen Yang, Lu Shi, and Chao Gao"
paperurl: "https://arxiv.org/abs/2606.15317"
arxivurl: "https://arxiv.org/abs/2606.15317"
---

<section class="paper-spotlight">
  <p class="paper-kicker">Preprint Spotlight</p>
  <p class="paper-lead">
    This work develops <strong>CR-RKL</strong>, a recursive Koopman learning method for nonlinear systems whose dynamics vary over time and fall outside the training distribution. The method updates a lifted linear predictor online while regulating covariance growth and avoiding parameter freezing.
  </p>

  <p class="paper-actions">
    <a href="https://arxiv.org/abs/2606.15317">arXiv</a>
    <a href="https://arxiv.org/pdf/2606.15317">PDF</a>
  </p>
</section>

<figure class="paper-figure paper-figure--wide">
  <img src="/images/publications/crrkl_framework.png" alt="CR-RKL covariance regulation and recursive Koopman learning framework">
  <figcaption>
    Original paper figure illustrating covariance windup, vanishing gain, trace-normalized uncertainty, and the CR-RKL recursive update pipeline.
  </figcaption>
</figure>

## Why This Matters

Robotic systems and autonomous platforms often operate under changing payloads, environments, contact conditions, and aerodynamic effects. Batch-identified models can quickly become stale. This paper studies how Koopman-based predictors can be updated recursively while controlling the uncertainty introduced by new measurements.

## Main Contributions

- Proposes a covariance-regulated recursive Koopman learning framework for nonlinear systems with uncertain, time-varying dynamics.
- Introduces two complementary covariance-regulation strategies: **error dead-zone gating** and **constant-trace normalization**.
- Addresses two recursive-estimation failure modes: covariance windup under low excitation and vanishing gain without forgetting.
- Validates online modeling on a differential-drive robot with wheel slip and Stribeck friction and on a 26-gram butterfly-inspired flapping-wing robot.
- Embeds the learned model in model predictive control to evaluate closed-loop tracking under uncertain dynamics.

## Key Findings

- CR-RKL maintains numerically stable online learning in settings where conventional recursive updates can become ill-conditioned.
- Constant-trace normalization preserves the geometric structure of uncertainty while preventing covariance explosion.
- The approach improves online modeling and supports reliable MPC tracking under uncertain, time-varying dynamics.

<div class="paper-figure-grid">
  <figure class="paper-figure">
    <img src="/images/publications/crrkl_fwmav_online_modeling.png" alt="CR-RKL online modeling benchmark for the flapping-wing robot">
    <figcaption>Original paper figure comparing online Koopman modeling performance for the flapping-wing robot across same-regime and cross-regime flight data.</figcaption>
  </figure>
</div>

## Citation

Gu, Weibin, Chen Yang, Lu Shi, and Chao Gao. "Covariance-Regulated Recursive Koopman Learning for Nonlinear Systems with Uncertain Time-Varying Dynamics." *arXiv preprint arXiv:2606.15317* (2026).
