---
title: "People"
permalink: /people/
author_profile: true
---

NEAR Lab is a multidisciplinary and multicultural team united by a shared vision for neuro-embodied adaptive robotics and a strong passion for building intelligent physical systems. We believe ambitious research is a team achievement: each of us stands on the shoulders of the group, and great success comes from shared curiosity, trust, rigor, and hands-on work.

<h2>Principal Investigator</h2>

<div class="pi-card">
  <img src="/images/people/Weibin_Gu_Profile.png" alt="PI Photo">
  <div class="pi-info">
    <h3>Dr. Weibin Gu</h3>
    <p class="pi-title">Postdoctoral Researcher<br>Institute for AI Industry Research (AIR), Tsinghua University</p>

    <p class="pi-desc">
      Dr. Weibin Gu is a Postdoctoral Researcher and Shuimu Tsinghua Scholar at the Institute for AI Industry Research (AIR), Tsinghua University, collaborating with <a href="https://air.tsinghua.edu.cn/en/info/1046/1188.htm">Prof. Ya-Qin Zhang</a> and Prof. Chao Gao. His research focuses on nonlinear control, interpretable robot learning, and bio-inspired robotics, with applications in adaptive robotic systems and autonomous industrial inspection. He earned his Ph.D. in Electronics and Communications Engineering <em>cum laude</em> from Politecnico di Torino under the supervision of <a href="https://www.polito.it/en/staff?p=039906">Prof. Alessandro Rizzo</a>, where his doctoral research received funding from the 2021 Amazon Research Award. Dr. Gu has published over 15 papers in leading international journals and conferences, holds 4 Chinese patents, and regularly serves as a reviewer for prominent venues including CDC, ACC, L-CSS, ICRA, RA-L, Automatica, and Nature Portfolio journals. He was selected for the Postdoctoral Overseas Talent Introduction Program and funded by the China Postdoctoral Science Foundation. Moving beyond pure research, he is passionate about translating scientific insights into real-world impact by leading teams, prototyping robotic systems, and developing innovative, market-ready technologies that solve tangible industrial challenges.
    </p>

    <p class="pi-links">
      <a href="https://scholar.google.com/citations?user=PDP31hEAAAAJ&hl=en">Google Scholar</a> ·
      <a href="/cv.pdf">CV</a> ·
      <a href="mailto:guweibin@air.tsinghua.edu">Email</a> ·
      <a href="http://www.linkedin.com/in/wgu938">LinkedIn</a> 
    </p>
  </div>
</div>

<h2>Team</h2>

<div class="people-grid team-grid">

  <!-- Member -->
  <div class="person-card">
    <img src="/images/people/Chenrui_Feng.png" alt="Chenrui Feng">
    <div class="person-card__body">
      <h3>Chenrui Feng</h3>
      <p class="person-role">Research Engineer</p>
      <p class="person-interest">Embedded Systems, Simulator, Dynamics and Control, Hardware</p>
    </div>
  </div>

  <div class="person-card">
    <img src="/images/people/Xingchi_Jiao.jpg" alt="Xingchi Jiao">
    <div class="person-card__body">
      <h3>Xingchi Jiao</h3>
      <p class="person-role">Research Engineer</p>
      <p class="person-interest">Hardware, Embedded Systems, Neuromorphic Computing, Prototyping</p>
    </div>
  </div>

  <div class="person-card">
    <img src="/images/people/Lian_Liu.jpg" alt="Lian Liu">
    <div class="person-card__body">
      <h3>Lian Liu</h3>
      <p class="person-role">Research Intern</p>
      <p class="person-interest">Mechanical Design, CFD Simulation, Prototyping, Drone Piloting</p>
    </div>
  </div>

  <div class="person-card">
    <img src="/images/people/Chen_Yang.png" alt="Chen Yang">
    <div class="person-card__body">
      <h3>Chen Yang</h3>
      <p class="person-role">Research Intern</p>
      <p class="person-interest">Dynamics and Control, Embedded Systems, Machine Learning</p>
    </div>
  </div>

  <div class="person-card">
    <img src="/images/people/Alberto_Bellagamba.png" alt="Alberto Bellagamba">
    <div class="person-card__body">
      <h3>Alberto Bellagamba</h3>
      <p class="person-role">Research Intern</p>
      <p class="person-interest">Reinforcement Learning, Simulator</p>
    </div>
  </div>

  <div class="person-card">
    <img src="/images/people/Yuxuan_Wang.png" alt="Yuxuan Wang">
    <div class="person-card__body">
      <h3>Yuxuan Wang</h3>
      <p class="person-role">Research Intern</p>
      <p class="person-interest">Machine Learning, Prototyping</p>
    </div>
  </div>

</div>

<h2>Alumni & Visitors</h2>

<ul class="alumni-list">
  <li><strong>Rim El Filali</strong> — Previous Master's Student; Machine Learning, Neuromorphic Computing, Dynamics and Control</li>
  <li><strong>Chaolai Da</strong> — Previous Research Intern; Hardware, FPGA Simulation</li>
  <li><strong>Chun Zhang</strong> — Previous Research Intern; Neuromorphic Computing</li>
  <li><strong>Hengyang Li</strong> — Previous Research Intern; CFD/FSI Simulation, Prototyping</li>
  <!-- <li><strong>Xinge Huang</strong> — Previous Research Intern; Simulator</li> -->
  <li><strong>Yuhe Ding</strong> — Previous Research Intern; Embedded Systems, Dynamics and Control, Prototyping</li>
  <li><strong>Xiaofei Shi</strong> — Previous Research Intern; Mechanical Design, Prototyping, Drone Piloting</li>
</ul>

<h2>Gallery</h2>

<section class="people-gallery" aria-label="NEAR Lab dinner gathering photo gallery">
  <div class="people-gallery__track">
    <img class="people-gallery__slide is-active" src="/images/people/dinner_gathering/735.jpg" alt="NEAR Lab dinner gathering photo 1">
    <img class="people-gallery__slide" src="/images/people/dinner_gathering/IMG_0566.jpg" alt="NEAR Lab dinner gathering photo 2">
    <img class="people-gallery__slide" src="/images/people/dinner_gathering/IMG_2760.jpg" alt="NEAR Lab dinner gathering photo 3">
  </div>
  <div class="people-gallery__dots" aria-label="Choose dinner gathering photo">
    <button class="is-active" type="button" aria-label="Show photo 1"></button>
    <button type="button" aria-label="Show photo 2"></button>
    <button type="button" aria-label="Show photo 3"></button>
  </div>
</section>

<script>
document.addEventListener("DOMContentLoaded", function () {
  var gallery = document.querySelector(".people-gallery");
  if (!gallery) return;

  var slides = gallery.querySelectorAll(".people-gallery__slide");
  var dots = gallery.querySelectorAll(".people-gallery__dots button");
  var activeIndex = 0;

  function showSlide(index) {
    activeIndex = (index + slides.length) % slides.length;
    slides.forEach(function (slide, i) {
      slide.classList.toggle("is-active", i === activeIndex);
    });
    dots.forEach(function (dot, i) {
      dot.classList.toggle("is-active", i === activeIndex);
    });
  }

  dots.forEach(function (dot, i) {
    dot.addEventListener("click", function () {
      showSlide(i);
    });
  });

  setInterval(function () {
    showSlide(activeIndex + 1);
  }, 4500);
});
</script>

<hr>

<section class="join-near">
  <h2>Join NEAR Lab</h2>

  <p>
    We welcome students and collaborators with strong curiosity about our work
    and a willingness to build, test, and iterate on real systems.
  </p>

  <p>
    Students interested in joining the lab are expected to have a good academic
    record and skill sets that match our research directions. Please send a resume and a brief introduction of your background, interests,
    and goals to <strong>guweibin@air.tsinghua.edu</strong>.
  </p>

  <!-- <p>
    
  </p> -->

  <!-- <p class="join-note">
    We welcome Ph.D., Master’s, undergraduate researchers, and visiting students.
  </p> -->
</section>
