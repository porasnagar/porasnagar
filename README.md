<!--
  ══════════════════════════════════════════════════════════════
  porasnagar/porasnagar — profile README
  Every place you need to change something is marked  ✎
  Nothing here needs CSS: all styling lives inside assets/*.svg
  ══════════════════════════════════════════════════════════════
-->

<!-- ✎ HERO — edit the text inside assets/hero.svg AND assets/hero-light.svg -->
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="assets/hero.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
  <img src="assets/hero.svg" alt="Poras Nagar — AI Engineer, Distributed Systems, Full-Stack Developer" width="100%">
</picture>

<!-- ─────────────────────────── NAV ─────────────────────────── -->
<div align="center">

<a href="#systems"><img src="https://img.shields.io/badge/Systems-161b22?style=for-the-badge&labelColor=0d1117&logo=rocket&logoColor=7c5cff" alt="Systems"></a>
<a href="#stack"><img src="https://img.shields.io/badge/Stack-161b22?style=for-the-badge&labelColor=0d1117&logo=stackblitz&logoColor=22d3ee" alt="Stack"></a>
<a href="#signals"><img src="https://img.shields.io/badge/Signals-161b22?style=for-the-badge&labelColor=0d1117&logo=githubactions&logoColor=f59e0b" alt="Signals"></a>
<a href="#contact"><img src="https://img.shields.io/badge/Contact-161b22?style=for-the-badge&labelColor=0d1117&logo=maildotru&logoColor=e6edf3" alt="Contact"></a>

<!-- ✎ your three real links -->
<a href="https://porasnagar.github.io"><img src="https://img.shields.io/badge/Portfolio-porasnagar.github.io-7c5cff?style=for-the-badge&labelColor=0d1117&logo=googlechrome&logoColor=white" alt="Portfolio"></a>
<a href="https://unlistedstox.com"><img src="https://img.shields.io/badge/Live_product-UnlistedStox-22d3ee?style=for-the-badge&labelColor=0d1117&logo=tradingview&logoColor=white" alt="UnlistedStox"></a>
<a href="https://linkedin.com/in/poras-nagar-036886189"><img src="https://img.shields.io/badge/LinkedIn-in%2Fporas--nagar-0A66C2?style=for-the-badge&labelColor=0d1117&logo=linkedin&logoColor=white" alt="LinkedIn"></a>

</div>

<img src="assets/divider.svg" width="100%" alt="">

<!-- ─────────────────────────── ABOUT ─────────────────────────── -->

I build the unglamorous half of AI products: the pricing engines, the queue
workers, the schemas that stop a scraper from lying to a trading screen.
Most of my work lives in Indian pre-IPO and unlisted equity markets, where the
data is messy, thinly traded, and nobody else has cleaned it up yet.

<!-- ✎ swap any of these values -->
```yaml
operator:   Poras Nagar
role:       Full-Stack Developer & Product Manager  # @ EnxtAI / SMC Global Securities
domain:     fintech · unlisted & pre-IPO equities
education:  B.Tech CSE (Hons. AI & ML), Amity University — 2021→2025
timezone:   Asia/Kolkata (UTC+5:30)

currently:
  - shipping valuation + cap-table pipelines on UnlistedStox
  - leading a team of interns across four internal platforms
  - building Hermes, an agent that writes documents so I don't have to

open_to:  [ AI engineering, applied AI, backend-heavy full-stack ]
```

<img src="assets/divider.svg" width="100%" alt="">

<!-- ─────────────────────────── SYSTEMS ─────────────────────────── -->
<a name="systems"></a>
<h3 align="center">Systems in production</h3>
<p align="center"><sub>Four things I'd be happy to be interviewed about line by line.</sub></p>

<!-- ✎ replace cards freely — keep the 2×2 shape, it reads best on mobile -->
<table width="100%">
<tr>
<td width="50%" valign="top">

<h4>UnlistedStox</h4>
<img src="https://img.shields.io/badge/live-in_production-22d3ee?style=flat-square&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/domain-fintech-7c5cff?style=flat-square&labelColor=0d1117" alt="">

<p>An OTC equity pricing and valuation platform. It turns historical
transactions, debt-to-equity metrics and statutory cap-table filings into
a live price for shares that never touch an exchange.</p>

<ul>
<li>Regression workers in Python/TensorFlow re-price on every new filing</li>
<li>B-tree indexed time-series in Postgres, sub-15&nbsp;ms reads</li>
<li>React order book rendering live bid/ask depth</li>
</ul>

<sub><code>Python</code> · <code>TensorFlow</code> · <code>React</code> · <code>Node</code> · <code>PostgreSQL</code></sub><br><br>
<a href="https://unlistedstox.com"><b>Open the platform →</b></a>

</td>
<td width="50%" valign="top">

<h4>Hospital triage over WhatsApp</h4>
<img src="https://img.shields.io/badge/channel-Meta_Cloud_API-25D366?style=flat-square&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/type-triage_bot-f59e0b?style=flat-square&labelColor=0d1117" alt="">

<p>Patients book slots, submit intake and receive pathology reports without
leaving WhatsApp — no app install, which is the whole point in a tier-2
hospital's catchment area.</p>

<ul>
<li>Express webhook verifying HMAC-SHA256 inside a 200&nbsp;ms ack window</li>
<li>Async dispatcher holding multi-turn conversation state in MongoDB</li>
<li>Encrypted, expiring report URLs delivered in-thread</li>
</ul>

<sub><code>Meta WhatsApp API</code> · <code>Node</code> · <code>Express</code> · <code>MongoDB</code></sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

<h4>Market scrapers &amp; queue broker</h4>
<img src="https://img.shields.io/badge/throughput-10k%2B_pages%2Fmin-7c5cff?style=flat-square&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/queue-Redis_%2B_RabbitMQ-FF6600?style=flat-square&labelColor=0d1117" alt="">

<p>The ingestion layer everything else sits on. A distributed extraction
cluster that pulls OTC valuations, filings and registrar data, then
normalises it into one schema before anything downstream sees it.</p>

<ul>
<li>Back-pressured fan-out with per-source rate budgets</li>
<li>Dead-letter replay so a bad parse never loses a day of data</li>
<li>Schema contracts enforced at the queue boundary, not in the consumer</li>
</ul>

<sub><code>Python</code> · <code>RabbitMQ</code> · <code>Redis</code> · <code>Docker</code></sub>

</td>
<td width="50%" valign="top">

<h4>Multi-agent internal tooling</h4>
<img src="https://img.shields.io/badge/scope-internal_platform-22d3ee?style=flat-square&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/CI-GitHub_Actions-2088FF?style=flat-square&labelColor=0d1117" alt="">

<p>Agentic tooling deployed across our repos: it drafts documents, generates
decks and spreadsheets, and takes the repetitive half of engineering
paperwork off the team's plate.</p>

<ul>
<li>Deterministic document pipeline — templates in, DOCX/PPTX/XLSX out</li>
<li>Runs in CI, so artifacts are versioned alongside the code</li>
<li>Tool-calling layer shared across four internal platforms</li>
</ul>

<sub><code>Python</code> · <code>FastAPI</code> · <code>GitHub Actions</code></sub>

</td>
</tr>
</table>

<img src="assets/divider.svg" width="100%" alt="">

<!-- ─────────────────────────── STACK ─────────────────────────── -->
<a name="stack"></a>
<h3 align="center">Stack</h3>
<p align="center"><sub>Grouped by what I reach for, not by what I've read about.</sub></p>

<div align="center">

<!-- ✎ the daily-drivers row stays open; everything else is collapsed -->
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white&labelColor=0d1117" alt="">

</div>

<details>
<summary><b>&nbsp;Everything else, by layer</b></summary>
<br>
<div align="center">

<table width="100%">
<tr>
<td align="right" width="26%"><sub><b>AI / ML</b></sub></td>
<td>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=keras&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white&labelColor=0d1117" alt="">
</td>
</tr>
<tr>
<td align="right"><sub><b>Backend &amp; pipelines</b></sub></td>
<td>
<img src="https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/Redis-FF4438?style=flat-square&logo=redis&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=flat-square&logo=rabbitmq&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/WhatsApp_Cloud_API-25D366?style=flat-square&logo=whatsapp&logoColor=white&labelColor=0d1117" alt="">
</td>
</tr>
<tr>
<td align="right"><sub><b>Frontend</b></sub></td>
<td>
<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white&labelColor=0d1117" alt="">
</td>
</tr>
<tr>
<td align="right"><sub><b>Data</b></sub></td>
<td>
<img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white&labelColor=0d1117" alt="">
</td>
</tr>
<tr>
<td align="right"><sub><b>Infra</b></sub></td>
<td>
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=white&labelColor=0d1117" alt="">
<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white&labelColor=0d1117" alt="">
</td>
</tr>
</table>

</div>
</details>

<img src="assets/divider.svg" width="100%" alt="">

<!-- ─────────────────────────── SIGNALS ─────────────────────────── -->
<a name="signals"></a>
<h3 align="center">Signals</h3>

<div align="center">

<!-- ✎ change username= in all four URLs -->
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="https://github-readme-stats.vercel.app/api?username=porasnagar&show_icons=true&hide_border=true&include_all_commits=true&count_private=true&bg_color=00000000&title_color=7c5cff&icon_color=22d3ee&text_color=8b98ab&ring_color=f59e0b">
  <img src="https://github-readme-stats.vercel.app/api?username=porasnagar&show_icons=true&hide_border=true&include_all_commits=true&count_private=true&bg_color=00000000&title_color=6d28d9&icon_color=0891b2&text_color=4a5565&ring_color=b45309" height="165" alt="GitHub stats">
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=porasnagar&layout=compact&hide_border=true&langs_count=8&bg_color=00000000&title_color=7c5cff&text_color=8b98ab">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=porasnagar&layout=compact&hide_border=true&langs_count=8&bg_color=00000000&title_color=6d28d9&text_color=4a5565" height="165" alt="Top languages">
</picture>

</div>

<details open>
<summary><b>&nbsp;Contribution calendar, in 3D</b></summary>
<br>
<!-- generated nightly by .github/workflows/profile-assets.yml -->
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="profile-3d-contrib/profile-night-rainbow.svg">
  <img src="profile-3d-contrib/profile-green-animate.svg" width="100%" alt="3D contribution calendar">
</picture>
</details>

<details>
<summary><b>&nbsp;The snake eats the graph</b></summary>
<br>
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="https://raw.githubusercontent.com/porasnagar/porasnagar/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/porasnagar/porasnagar/output/github-snake.svg">
  <img src="https://raw.githubusercontent.com/porasnagar/porasnagar/output/github-snake.svg" width="100%" alt="Contribution snake">
</picture>
</details>

<img src="assets/divider.svg" width="100%" alt="">

<!-- ─────────────────────────── CONTACT ─────────────────────────── -->
<a name="contact"></a>
<h3 align="center">Say hello</h3>

<p align="center">
Fastest way to reach me is email. I read everything; I answer anything
with a concrete question in it.
</p>

<div align="center">

<!-- ✎ your handles -->
<a href="mailto:poras9868@gmail.com"><img src="https://img.shields.io/badge/poras9868@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0d1117" alt="Email"></a>
<a href="https://linkedin.com/in/poras-nagar-036886189"><img src="https://img.shields.io/badge/poras--nagar-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0d1117" alt="LinkedIn"></a>
<a href="https://porasnagar.github.io"><img src="https://img.shields.io/badge/porasnagar.github.io-7c5cff?style=for-the-badge&logo=googlechrome&logoColor=white&labelColor=0d1117" alt="Portfolio"></a>

<br><br>
<sub>Hero and dividers are hand-written SVG in <a href="assets/"><code>assets/</code></a> — no template, no generator.</sub>

</div>
