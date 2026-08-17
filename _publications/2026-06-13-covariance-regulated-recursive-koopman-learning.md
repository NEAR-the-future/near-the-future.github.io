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
  <img src="/images/research/modeling_control.jpg" alt="Modeling and control research theme illustration">
  <figcaption>
    The work targets online model adaptation for uncertain nonlinear dynamics, where a learned lifted predictor must remain useful as the system changes.
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

## Citation

Gu, Weibin, Chen Yang, Lu Shi, and Chao Gao. "Covariance-Regulated Recursive Koopman Learning for Nonlinear Systems with Uncertain Time-Varying Dynamics." *arXiv preprint arXiv:2606.15317* (2026).
