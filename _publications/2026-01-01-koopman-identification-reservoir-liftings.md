---
title: "Koopman Identification of Nonlinear Systems via Reservoir Liftings"
collection: publications
category: manuscripts
permalink: /publication/2026-01-01-koopman-identification-reservoir-liftings
excerpt: "Koopman identification of nonlinear systems using reservoir liftings."
date: 2026-06-01
venue: "IEEE Control Systems Letters"
authors: "Weibin Gu, Chen Yang, and Lu Shi"
paperurl: "https://ieeexplore.ieee.org/document/11547162"
arxivurl: "https://arxiv.org/abs/2605.04917"
codeurl: "https://github.com/NEAR-the-future/RC-Koopman"
citation: "Gu, Weibin, Chen Yang, and Lu Shi. &quot;Koopman Identification of Nonlinear Systems via Reservoir Liftings.&quot; <i>IEEE Control Systems Letters</i> (2026)."
---

<section class="paper-spotlight">
  <p class="paper-kicker">Paper Spotlight</p>
  <p class="paper-lead">
    This work introduces <strong>RC-Koopman</strong>, a Koopman identification framework that uses reservoir dynamics as a stateful lifting dictionary for nonlinear dynamical systems. The key idea is to let the reservoir encode fading-memory histories while a finite-dimensional Koopman model is identified by linear regression.
  </p>

  <p class="paper-actions">
    <a href="https://ieeexplore.ieee.org/document/11547162">IEEE Xplore</a>
    <a href="https://arxiv.org/abs/2605.04917">arXiv</a>
    <a href="https://github.com/NEAR-the-future/RC-Koopman">Code</a>
  </p>
</section>

<figure class="paper-figure paper-figure--wide">
  <img src="/images/publications/rckoopman.png" alt="Schematic of the RC-Koopman framework">
  <figcaption>
    RC-Koopman maps measurements into a high-dimensional reservoir state, augments it with the measured state or output, and identifies finite-dimensional Koopman operators from time-shifted data.
  </figcaption>
</figure>

## Why This Matters

Koopman operator theory offers a principled way to represent nonlinear dynamics through linear evolution in a lifted space. In practice, however, performance depends heavily on the choice of observables, the treatment of memory, and numerical conditioning. RC-Koopman addresses these issues by using a reservoir as a stable, history-dependent dictionary.

## Main Contributions

- Formulates reservoir dynamics as a **stateful Koopman dictionary** whose memory depth is controlled by the reservoir spectral radius.
- Uses the **Echo State Property** to support well-posed lifted representations and improve numerical conditioning.
- Provides a **correlation-based spectral-radius selection rule** that aligns reservoir memory with dominant system time scales.
- Characterizes how finite reservoir memory affects which Koopman eigenfunctions are observable from the lifted features.
- Evaluates the approach against EDMD and Hankel/HAVOK-style lifting on nonlinear benchmark systems.

## Key Findings

- RC-Koopman achieves a practical balance between reconstruction accuracy and dynamical stability.
- Reservoir liftings produce better-conditioned feature representations than ill-conditioned dictionary or delay-coordinate alternatives in the reported benchmarks.
- Spectral-radius tuning is important: too little memory misses slow components, while excessive memory can introduce unreliable long-lived modes.
- The selected reservoir memory horizon aligns the identified Koopman spectrum with observable system time scales.

<div class="paper-figure-grid">
  <figure class="paper-figure">
    <img src="/images/publications/koopman_reconstructed_trajectories.png" alt="Comparison of ground truth and reconstructed dynamics">
    <figcaption>Reconstructed dynamics on nonlinear benchmarks, including a Duffing oscillator and a differential-drive robot model.</figcaption>
  </figure>

  <figure class="paper-figure">
    <img src="/images/publications/koopman_eigenvalues.png" alt="Eigenvalue spectra of learned Koopman operators">
    <figcaption>Eigenvalue spectra show the stability profile of the learned Koopman operators.</figcaption>
  </figure>

  <figure class="paper-figure">
    <img src="/images/publications/koopman_observability.png" alt="Koopman eigenvalue lifetimes versus reservoir memory horizon">
    <figcaption>Reservoir memory determines which Koopman spectral components are observable in the lifted representation.</figcaption>
  </figure>
</div>

## Citation

Gu, Weibin, Chen Yang, and Lu Shi. "Koopman Identification of Nonlinear Systems via Reservoir Liftings." *IEEE Control Systems Letters* (2026).
