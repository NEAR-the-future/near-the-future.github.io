---
permalink: /
title: "Welcome to the NEAR Lab website!"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Intelligence does not live in algorithms alone. It emerges from **bodies, brains, and interaction with the physical world**.

At the NEAR Lab, we study how intelligent behavior arises from the tight coupling of neural systems, data-driven control, and physical embodiment in robotic systems. By integrating bio-inspired morphology, neurorobotics, and lifelong learning, we aim to build robots that learn, adapt, and evolve through real physical interaction.

<div class="homepage-buttons">
  <a href="https://near-the-future.github.io/research/" class="btn btn-primary">Explore Research</a>
  <a href="https://near-the-future.github.io/people/" class="btn btn-secondary">Meet the Team</a>
  <a href="#" onclick="navigator.clipboard.writeText(window.location.href); alert('Page URL copied!');" class="btn btn-tertiary">Share This Page</a>
</div>

---

# Our Approach

Rather than treating perception, learning, and control as separate modules, NEAR takes an embodied perspective on intelligence. We design robotic systems in which **the body shapes computation**, **learning unfolds over time**, and **behavior emerges through interaction with the environment**.

Our work spans **robot design, modeling, control, and learning**, with a particular emphasis on **dynamic and underactuated systems**, such as flapping-wing robots. We believe that understanding how animals fly, sense, learn, and adapt offers essential principles for the next generation of autonomous robots.

---

# Research
Our research focuses on **bio-inspired robotics and embodied intelligence**, including:
- flapping-wing and morphologically adaptive robots  
- neuro-embodied and neuromorphic systems  
- adaptation and lifelong learning in physical agents  
- modeling, dynamics, and control of complex robotic systems 

See the [**Research**](https://near-the-future.github.io/research/) page for details.

---

<!-- # News & Updates

<div class="news-list">

  <div class="news-item">
    <span class="news-date">2026 · Jan</span>
    <p class="news-text">
      <strong>Paper accepted</strong> to <em>IEEE CDC 2026</em> on neuro-embodied control of flapping-wing robots.
    </p>
  </div>

  <div class="news-item">
    <span class="news-date">2025 · Dec</span>
    <p class="news-text">
      <strong>Invited talk</strong> at Tsinghua AIR seminar on neuromorphic embodied intelligence.
    </p>
  </div>

  <div class="news-item">
    <span class="news-date">2025 · Nov</span>
    <p class="news-text">
      Released <strong>NEAR-Control</strong>, an open-source toolkit for adaptive control in underactuated robots.
      <a href="#" class="news-link">[code]</a>
    </p>
  </div>

</div> -->

<!-- # News & Updates

<div class="news-list">
{% assign latest_news = site.news | sort: "date" | reverse | slice: 0,5 %}
{% for item in latest_news %}
  <div class="news-item">
    <span class="news-date">
      {{ item.date | date: "%Y · %b" }}
    </span>
    <p class="news-text">
      <strong>{{ item.title }}</strong>
    </p>
  </div>
{% endfor %}
</div>

<p style="text-align: right; margin-top: 0.5rem;">
  <a href="/news/">View all updates →</a>
</p> -->

---

# Join Us

We welcome students and collaborators interested in bio-inspired robots that learn and adapt through real-world interaction. For more information and contact details, please visit our [**People**](https://near-the-future.github.io/people/) page — we’d be happy to hear from you.

---

**NEAR Lab**  
*Where intelligence takes physical form.*

<!-- 
Why NEAR?
- Neuro-Embodied: neural principles grounded in real physical systems
- Adaptive: learning and change across time, not fixed behaviors
- Robotics: intelligence tested in the real world, not simulations alone

If you are excited about building robots that learn through their bodies, we would love to hear from you. Together, we are NEAR the future where robots learn like living systems. -->