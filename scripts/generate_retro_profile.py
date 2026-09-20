import os

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")

def write_asset(filename, content):
    path = os.path.join(ASSETS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated: {filename} ({len(content)} bytes)")

# ==============================================================================
# 1. HERO - WINDOWS 98 LIGHT & CRT DARK
# ==============================================================================

hero_win98 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-label="Poras Nagar — Windows 98 Profile Console">
  <defs>
    <linearGradient id="w98title" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#000080"/>
      <stop offset="100%" stop-color="#1084d0"/>
    </linearGradient>
    <pattern id="scanlines" width="100" height="2" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="100" y2="0" stroke="#000000" stroke-width="0.5" opacity="0.06"/>
    </pattern>
    <clipPath id="frame"><rect width="1200" height="370" rx="4"/></clipPath>
  </defs>

  <style>
    .w98-font { font-family: "MS Sans Serif", Tahoma, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    .mono { font-family: ui-monospace, "Courier New", monospace; }
    .blink { animation: cursorBlink 1s step-end infinite; }
    @keyframes cursorBlink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
  </style>

  <g clip-path="url(#frame)">
    <!-- Desktop Background (Classic Win98 Teal) -->
    <rect width="1200" height="370" fill="#008080"/>
    <rect width="1200" height="370" fill="url(#scanlines)"/>

    <!-- Main Window Outer Frame (Classic Bevel) -->
    <g transform="translate(20, 16)">
      <!-- Outer drop shadow/black border -->
      <rect width="1160" height="338" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
      <!-- Top/Left White Bevel Highlight -->
      <line x1="1" y1="1" x2="1159" y2="1" stroke="#ffffff" stroke-width="2"/>
      <line x1="1" y1="1" x2="1" y2="337" stroke="#ffffff" stroke-width="2"/>
      <!-- Bottom/Right Dark Grey Shadow -->
      <line x1="2" y1="336" x2="1158" y2="336" stroke="#808080" stroke-width="2"/>
      <line x1="1158" y1="2" x2="1158" y2="336" stroke="#808080" stroke-width="2"/>

      <!-- Title Bar -->
      <g transform="translate(4, 4)">
        <rect width="1152" height="24" fill="url(#w98title)"/>
        <!-- 16x16 Pixel Icon Placeholder -->
        <rect x="5" y="4" width="16" height="16" fill="#ffff00" stroke="#000000" stroke-width="1"/>
        <rect x="8" y="7" width="10" height="10" fill="#000080"/>
        <text class="w98-font" x="27" y="17" font-size="12" font-weight="bold" fill="#ffffff" letter-spacing="0.02em">C:\\PORAS\\PROFILE.EXE - [Poras Nagar: AI Engineer &amp; Distributed Systems]</text>
        
        <!-- Win98 Buttons [_] [?] [X] -->
        <g transform="translate(1088, 3)">
          <!-- Minimize -->
          <rect x="0" y="0" width="18" height="18" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
          <line x1="1" y1="1" x2="17" y2="1" stroke="#ffffff"/>
          <line x1="1" y1="1" x2="1" y2="17" stroke="#ffffff"/>
          <line x1="4" y1="13" x2="12" y2="13" stroke="#000000" stroke-width="2"/>

          <!-- Maximize -->
          <rect x="20" y="0" width="18" height="18" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
          <line x1="21" y1="1" x2="37" y2="1" stroke="#ffffff"/>
          <line x1="21" y1="1" x2="21" y2="17" stroke="#ffffff"/>
          <rect x="24" y="4" width="10" height="9" fill="none" stroke="#000000" stroke-width="2"/>

          <!-- Close -->
          <rect x="40" y="0" width="18" height="18" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
          <line x1="41" y1="1" x2="57" y2="1" stroke="#ffffff"/>
          <line x1="41" y1="1" x2="41" y2="17" stroke="#ffffff"/>
          <path d="M44 4 L53 13 M53 4 L44 13" stroke="#000000" stroke-width="2"/>
        </g>
      </g>

      <!-- Menu Bar -->
      <g transform="translate(8, 32)">
        <text class="w98-font" x="8" y="14" font-size="12" fill="#000000"><tspan text-decoration="underline">F</tspan>ile</text>
        <text class="w98-font" x="42" y="14" font-size="12" fill="#000000"><tspan text-decoration="underline">E</tspan>dit</text>
        <text class="w98-font" x="76" y="14" font-size="12" fill="#000000"><tspan text-decoration="underline">V</tspan>iew</text>
        <text class="w98-font" x="115" y="14" font-size="12" fill="#000000"><tspan text-decoration="underline">S</tspan>ystems</text>
        <text class="w98-font" x="175" y="14" font-size="12" fill="#000000"><tspan text-decoration="underline">H</tspan>elp</text>
      </g>
      <line x1="4" y1="52" x2="1156" y2="52" stroke="#808080" stroke-width="1"/>
      <line x1="4" y1="53" x2="1156" y2="53" stroke="#ffffff" stroke-width="1"/>

      <!-- Window Content Area (Sunken Inset Panel) -->
      <g transform="translate(12, 60)">
        <rect width="1136" height="236" fill="#ffffff" stroke="#808080" stroke-width="1"/>
        <line x1="1" y1="1" x2="1135" y2="1" stroke="#404040" stroke-width="1"/>
        <line x1="1" y1="1" x2="1" y2="235" stroke="#404040" stroke-width="1"/>
        <line x1="1" y1="235" x2="1135" y2="235" stroke="#ffffff" stroke-width="1"/>
        <line x1="1135" y1="1" x2="1135" y2="235" stroke="#ffffff" stroke-width="1"/>

        <!-- Left Column: User Card & Bio -->
        <g transform="translate(24, 20)">
          <!-- Pixel Avatar / Retro Computer Icon -->
          <g transform="translate(0, 4)">
            <rect width="72" height="72" fill="#008080" stroke="#000000" stroke-width="2"/>
            <rect x="8" y="8" width="56" height="42" fill="#c0c0c0" stroke="#000000" stroke-width="2"/>
            <rect x="14" y="14" width="44" height="30" fill="#000080"/>
            <text class="mono" x="18" y="32" font-size="11" fill="#00ff66">C:\&gt;_</text>
            <rect x="24" y="52" width="24" height="6" fill="#808080"/>
            <rect x="18" y="58" width="36" height="6" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
          </g>

          <g transform="translate(92, 4)">
            <text class="w98-font" x="0" y="24" font-size="26" font-weight="bold" fill="#000080">Poras Nagar</text>
            <text class="mono" x="0" y="46" font-size="13" font-weight="bold" fill="#008000">&gt; Full-Stack Developer &amp; AI Engineer @ EnxtAI</text>
            <text class="w98-font" x="0" y="68" font-size="12" fill="#404040">Specializing in OTC equity pricing engines, queue brokers &amp; distributed valuation pipelines.</text>
          </g>

          <!-- Bio / Details Inset Box -->
          <g transform="translate(0, 96)">
            <rect width="640" height="106" fill="#f0f0f0" stroke="#808080" stroke-width="1"/>
            <line x1="1" y1="1" x2="639" y2="1" stroke="#000000" stroke-width="1"/>
            <line x1="1" y1="1" x2="1" y2="105" stroke="#000000" stroke-width="1"/>

            <text class="mono" x="16" y="24" font-size="11.5" fill="#000080">OPERATOR   : Poras Nagar</text>
            <text class="mono" x="16" y="44" font-size="11.5" fill="#000000">EDUCATION  : B.Tech CSE (Hons. AI &amp; ML), Amity University [2021-2025]</text>
            <text class="mono" x="16" y="64" font-size="11.5" fill="#000000">LOCATION   : Noida, India (UTC+5:30) • Open to Global AI &amp; Backend Roles</text>
            <text class="mono" x="16" y="84" font-size="11.5" fill="#800000">CURRENTLY  : Shipping valuation pipelines on UnlistedStox &amp; Hermes Agent</text>
          </g>
        </g>

        <!-- Right Column: System Resource Inset Box -->
        <g transform="translate(700, 20)">
          <rect width="410" height="182" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
          <!-- 3D Sunken -->
          <line x1="0" y1="0" x2="409" y2="0" stroke="#404040" stroke-width="1"/>
          <line x1="0" y1="0" x2="0" y2="181" stroke="#404040" stroke-width="1"/>
          <line x1="0" y1="181" x2="410" y2="181" stroke="#ffffff" stroke-width="1"/>
          <line x1="409" y1="0" x2="409" y2="181" stroke="#ffffff" stroke-width="1"/>

          <rect x="8" y="6" width="394" height="20" fill="#000080"/>
          <text class="w98-font" x="14" y="20" font-size="11" font-weight="bold" fill="#ffffff">SYSTEM HARDWARE &amp; RUNTIME STATUS</text>

          <g transform="translate(16, 40)">
            <text class="mono" x="0" y="12" font-size="11" fill="#000000">UnlistedStox B-Tree Reads :</text>
            <text class="mono" x="220" y="12" font-size="11" font-weight="bold" fill="#000080">[SUB-15ms] OK</text>

            <text class="mono" x="0" y="36" font-size="11" fill="#000000">Scraper Ingestion Rate    :</text>
            <text class="mono" x="220" y="36" font-size="11" font-weight="bold" fill="#008000">[10k+ pg/m] OK</text>

            <text class="mono" x="0" y="60" font-size="11" fill="#000000">WhatsApp Webhook ACK Window:</text>
            <text class="mono" x="220" y="60" font-size="11" font-weight="bold" fill="#800080">[&lt; 200ms] OK</text>

            <text class="mono" x="0" y="84" font-size="11" fill="#000000">Hermes Multi-Agent CI     :</text>
            <text class="mono" x="220" y="84" font-size="11" font-weight="bold" fill="#000080">[ACTIVE] DOCS</text>

            <text class="mono" x="0" y="108" font-size="11" fill="#000000">Memory Integrity Check    :</text>
            <text class="mono" x="220" y="108" font-size="11" font-weight="bold" fill="#008000">[640K ALLOCATED]</text>
          </g>
        </g>
      </g>

      <!-- Status Bar (Beveled Sunken Panels) -->
      <g transform="translate(12, 304)">
        <!-- Panel 1 -->
        <rect x="0" y="0" width="460" height="22" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
        <line x1="0" y1="21" x2="460" y2="21" stroke="#ffffff"/>
        <line x1="459" y1="0" x2="459" y2="21" stroke="#ffffff"/>
        <text class="w98-font" x="8" y="15" font-size="11" fill="#000000">Ready</text>

        <!-- Panel 2 -->
        <rect x="466" y="0" width="340" height="22" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
        <line x1="466" y1="21" x2="806" y2="21" stroke="#ffffff"/>
        <line x1="805" y1="0" x2="805" y2="21" stroke="#ffffff"/>
        <text class="w98-font" x="474" y="15" font-size="11" fill="#000000">4 Platform(s) in Production</text>

        <!-- Panel 3 -->
        <rect x="812" y="0" width="324" height="22" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
        <line x1="812" y1="21" x2="1136" y2="21" stroke="#ffffff"/>
        <line x1="1135" y1="0" x2="1135" y2="21" stroke="#ffffff"/>
        <text class="w98-font" x="820" y="15" font-size="11" fill="#000080">● MS-DOS Prompt Connected (COM1)</text>
      </g>
    </g>
  </g>
</svg>"""

hero_crt = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-label="Poras Nagar — 90s CRT Terminal Boot Console">
  <defs>
    <!-- CRT Screen Vignette -->
    <radialGradient id="crtVignette" cx="50%" cy="50%" r="65%">
      <stop offset="0%" stop-color="#0a180a" stop-opacity="0.2"/>
      <stop offset="85%" stop-color="#050a05" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#010301" stop-opacity="0.98"/>
    </radialGradient>

    <!-- Scanline Pattern -->
    <pattern id="crtScanlines" width="100" height="3" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="100" y2="0" stroke="#000000" stroke-width="1.2" opacity="0.45"/>
    </pattern>

    <!-- Green Phosphor Glow Filter -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.2" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <clipPath id="screen"><rect x="18" y="16" width="1164" height="338" rx="14"/></clipPath>
  </defs>

  <style>
    .crt-font { font-family: ui-monospace, "Courier New", "Lucida Console", monospace; font-size: 13px; fill: #00ff66; }
    .amber-font { font-family: ui-monospace, "Courier New", "Lucida Console", monospace; font-size: 13px; fill: #ffb000; }
    .dim-font { font-family: ui-monospace, "Courier New", "Lucida Console", monospace; font-size: 12px; fill: #1d7734; }
    .blink { animation: crtBlink 0.9s step-end infinite; }
    @keyframes crtBlink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    .sweep { animation: crtScan 12s linear infinite; }
    @keyframes crtScan { 0% { transform: translateY(-100px); } 100% { transform: translateY(400px); } }
  </style>

  <!-- Monitor Chassis (90s Industrial Workstation Bezel) -->
  <rect width="1200" height="370" rx="8" fill="#141714" stroke="#252b25" stroke-width="3"/>
  <rect x="8" y="8" width="1184" height="354" rx="6" fill="#0d100d"/>

  <!-- Power LED Badge on Bezel -->
  <circle cx="1150" cy="354" r="3.5" fill="#00ff66" filter="url(#glow)"/>
  <text class="dim-font" x="1080" y="357" font-size="9.5">POWER / CRT</text>

  <!-- CRT Screen Surface -->
  <g clip-path="url(#screen)">
    <rect x="18" y="16" width="1164" height="338" fill="#050e05"/>
    <rect x="18" y="16" width="1164" height="338" fill="url(#crtVignette)"/>
    <rect x="18" y="16" width="1164" height="338" fill="url(#crtScanlines)"/>

    <!-- Sweep Beam -->
    <g class="sweep">
      <rect x="18" y="0" width="1164" height="60" fill="#00ff66" opacity="0.04"/>
    </g>

    <!-- Terminal Content with Phosphor Glow -->
    <g filter="url(#glow)" transform="translate(42, 44)">
      <!-- BIOS / Boot Sequence -->
      <text class="dim-font" x="0" y="0">PHOSPHOR-BIOS v4.02 (C) 1998 PORAS NAGAR SYSTEMS INC.</text>
      <text class="dim-font" x="0" y="18">CPU: DISTRIBUTED QUANT ENGINE @ 10,000 PAGES/MIN • MEMORY: 640KB ALLOCATED</text>
      
      <!-- ASCII Header Divider -->
      <text class="crt-font" x="0" y="44" font-weight="bold">╔═════════════════════════════════════════════════════════════════════════════════════════════╗</text>
      <text class="crt-font" x="0" y="62" font-weight="bold">║  OPERATOR: PORAS NAGAR  |  ROLE: FULL-STACK DEVELOPER &amp; AI ENGINEER  |  LOCATION: NOIDA, IN  ║</text>
      <text class="crt-font" x="0" y="80" font-weight="bold">╚═════════════════════════════════════════════════════════════════════════════════════════════╝</text>

      <!-- System Diagnostic Readout -->
      <g transform="translate(0, 108)">
        <text class="amber-font" x="0" y="0">&gt; CURRENTLY ACTIVE PRODUCTION DAEMONS:</text>

        <text class="crt-font" x="18" y="24">[DAEMON 01] unlistedstox.com       : OTC Valuation Engine (Python / TensorFlow) - sub-15ms</text>
        <text class="crt-font" x="18" y="44">[DAEMON 02] triage-gateway         : Hospital Intake via Meta WhatsApp Cloud API - 200ms ACK</text>
        <text class="crt-font" x="18" y="64">[DAEMON 03] scraper-cluster        : RabbitMQ Queue Fan-out + Redis Dead-Letter Replay</text>
        <text class="crt-font" x="18" y="84">[DAEMON 04] hermes-agent           : Multi-Agent Autonomous Document Synthesis Pipeline</text>

        <text class="dim-font" x="0" y="116">---------------------------------------------------------------------------------------------</text>
        <text class="amber-font" x="0" y="136">C:\PORAS\SYSTEM&gt; exec --status=ONLINE --open_for_hire=TRUE</text>
        <text class="crt-font" x="0" y="156">TELEMETRY STREAM: CONNECTED [99.9% UPTIME] <tspan class="blink">█</tspan></text>
      </g>
    </g>
  </g>
</svg>"""

# ==============================================================================
# 2. DIVIDER (WIN98 SUNKEN GROOVE LIGHT / CRT PHOSPHOR WIRE DARK)
# ==============================================================================

divider_dual = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 16" width="1200" height="16" role="separator">
  <style>
    .light-bar { display: block; }
    .dark-bar  { display: none; }
    @media (prefers-color-scheme: dark) {
      .light-bar { display: none; }
      .dark-bar  { display: block; }
    }
  </style>

  <!-- Light Mode: Authentic Win98 Sunken 3D Groove -->
  <g class="light-bar">
    <line x1="0" y1="7" x2="1200" y2="7" stroke="#808080" stroke-width="1"/>
    <line x1="0" y1="8" x2="1200" y2="8" stroke="#ffffff" stroke-width="1"/>
  </g>

  <!-- Dark Mode: CRT Phosphor Scanline Beam -->
  <g class="dark-bar">
    <line x1="0" y1="8" x2="1200" y2="8" stroke="#00ff66" stroke-width="1" opacity="0.65"/>
    <circle cx="600" cy="8" r="3" fill="#00ff66" opacity="0.85"/>
  </g>
</svg>"""

# ==============================================================================
# 3. FOUR SYSTEM PREVIEW CONSOLES (WIN98 LIGHT & CRT DARK)
# ==============================================================================

def make_retro_card(title, daemon, metric1_label, metric1_val, metric2_label, metric2_val, detail, dark=False):
    if not dark:
        # Windows 98 Light Window
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 176" width="580" height="176" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="tb_{title[:3]}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#000080"/><stop offset="100%" stop-color="#1084d0"/>
    </linearGradient>
    <clipPath id="cp_{title[:3]}"><rect width="580" height="176" rx="2"/></clipPath>
  </defs>
  <style>
    .w98 {{ font-family: "MS Sans Serif", Tahoma, -apple-system, sans-serif; font-size: 11px; }}
    .mono {{ font-family: ui-monospace, "Courier New", monospace; font-size: 11px; }}
  </style>
  <g clip-path="url(#cp_{title[:3]})">
    <!-- Body -->
    <rect width="580" height="176" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
    <line x1="1" y1="1" x2="579" y2="1" stroke="#ffffff" stroke-width="2"/>
    <line x1="1" y1="1" x2="1" y2="175" stroke="#ffffff" stroke-width="2"/>
    <line x1="2" y1="174" x2="578" y2="174" stroke="#808080" stroke-width="2"/>
    <line x1="578" y1="2" x2="578" y2="174" stroke="#808080" stroke-width="2"/>

    <!-- Title bar -->
    <rect x="4" y="4" width="572" height="20" fill="url(#tb_{title[:3]})"/>
    <text class="w98" x="10" y="18" font-weight="bold" fill="#ffffff">{title}.EXE</text>
    <!-- Buttons -->
    <g transform="translate(528, 5)">
      <rect x="0" y="0" width="14" height="14" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
      <line x1="1" y1="1" x2="13" y2="1" stroke="#ffffff"/><line x1="3" y1="10" x2="10" y2="10" stroke="#000000" stroke-width="2"/>
      <rect x="18" y="0" width="14" height="14" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
      <line x1="19" y1="1" x2="31" y2="1" stroke="#ffffff"/><path d="M22 3 L29 10 M29 3 L22 10" stroke="#000000" stroke-width="1.5"/>
    </g>

    <!-- Content Area (Sunken Inset) -->
    <g transform="translate(8, 28)">
      <rect width="564" height="118" fill="#ffffff" stroke="#808080" stroke-width="1"/>
      <line x1="1" y1="1" x2="563" y2="1" stroke="#404040"/>
      <line x1="1" y1="1" x2="1" y2="117" stroke="#404040"/>
      
      <!-- Metrics Boxes inside -->
      <g transform="translate(14, 12)">
        <rect width="256" height="52" fill="#f0f0f0" stroke="#808080" stroke-width="1"/>
        <text class="w98" x="8" y="16" fill="#000080" font-weight="bold">{metric1_label}</text>
        <text class="mono" x="8" y="38" font-size="16" font-weight="bold" fill="#008000">{metric1_val}</text>
      </g>
      <g transform="translate(284, 12)">
        <rect width="266" height="52" fill="#f0f0f0" stroke="#808080" stroke-width="1"/>
        <text class="w98" x="8" y="16" fill="#000080" font-weight="bold">{metric2_label}</text>
        <text class="mono" x="8" y="38" font-size="16" font-weight="bold" fill="#800080">{metric2_val}</text>
      </g>

      <text class="w98" x="16" y="86" fill="#000000">{detail}</text>
      <text class="mono" x="16" y="104" fill="#808080">STATUS: PROD DAEMON EXECUTION VERIFIED</text>
    </g>

    <!-- Bottom Status Bar -->
    <rect x="8" y="150" width="564" height="18" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
    <text class="w98" x="14" y="163" fill="#000000">100% Task Complete • 0 Faults</text>
  </g>
</svg>"""
    else:
        # CRT Terminal Dark Window
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 176" width="580" height="176" role="img" aria-label="{title}">
  <defs>
    <filter id="cglow_{title[:3]}">
      <feGaussianBlur stdDeviation="1.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <style>
    .crt {{ font-family: ui-monospace, "Courier New", monospace; font-size: 11.5px; fill: #00ff66; }}
    .amber {{ font-family: ui-monospace, "Courier New", monospace; font-size: 11.5px; fill: #ffb000; }}
    .dim {{ font-family: ui-monospace, "Courier New", monospace; font-size: 10px; fill: #1d7734; }}
  </style>
  <rect width="580" height="176" rx="6" fill="#080e08" stroke="#223322" stroke-width="2"/>
  <rect x="6" y="6" width="568" height="164" rx="4" fill="#030803"/>

  <g filter="url(#cglow_{title[:3]})" transform="translate(18, 24)">
    <text class="dim" x="0" y="0">┌──[ DAEMON: {daemon} ]──────────────────────────────┐</text>
    <text class="amber" x="12" y="24">&gt; {metric1_label}: <tspan fill="#00ff66" font-weight="bold">{metric1_val}</tspan></text>
    <text class="amber" x="12" y="44">&gt; {metric2_label}: <tspan fill="#00ff66" font-weight="bold">{metric2_val}</tspan></text>
    <text class="crt" x="12" y="70">{detail}</text>
    <text class="dim" x="12" y="94">[SYS_STATUS: RUNNING] [LOG_PIPE: VERIFIED] [PID: 4096]</text>
    <text class="dim" x="0" y="120">└─────────────────────────────────────────────────────────────┘</text>
  </g>
</svg>"""

# ==============================================================================
# 4. RUNTIME STACK (WIN98 DEVICE MANAGER LIGHT & CRT HTOP PROCESS MONITOR DARK)
# ==============================================================================

stack_win98 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-label="Windows 98 Device Manager Tech Stack">
  <defs>
    <linearGradient id="stk_w98title" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#000080"/><stop offset="100%" stop-color="#1084d0"/>
    </linearGradient>
    <clipPath id="stk_cp"><rect width="1200" height="370" rx="4"/></clipPath>
  </defs>

  <style>
    .w98 { font-family: "MS Sans Serif", Tahoma, -apple-system, sans-serif; font-size: 11.5px; }
    .w98-bold { font-family: "MS Sans Serif", Tahoma, -apple-system, sans-serif; font-size: 11.5px; font-weight: bold; }
    .mono { font-family: ui-monospace, "Courier New", monospace; font-size: 11px; }
  </style>

  <g clip-path="url(#stk_cp)">
    <!-- Main Window Outer Frame -->
    <rect width="1200" height="370" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
    <line x1="1" y1="1" x2="1199" y2="1" stroke="#ffffff" stroke-width="2"/>
    <line x1="1" y1="1" x2="1" y2="369" stroke="#ffffff" stroke-width="2"/>
    <line x1="2" y1="368" x2="1198" y2="368" stroke="#808080" stroke-width="2"/>
    <line x1="1198" y1="2" x2="1198" y2="368" stroke="#808080" stroke-width="2"/>

    <!-- Title Bar -->
    <g transform="translate(4, 4)">
      <rect width="1192" height="24" fill="url(#stk_w98title)"/>
      <text class="w98" x="10" y="17" font-size="12" font-weight="bold" fill="#ffffff">System Properties - [Device Manager: Engineering Tech Stack Drivers]</text>
      <!-- Buttons -->
      <g transform="translate(1148, 3)">
        <rect x="0" y="0" width="18" height="18" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
        <line x1="1" y1="1" x2="17" y2="1" stroke="#ffffff"/><text class="w98" x="5" y="13" font-weight="bold">?</text>
        <rect x="22" y="0" width="18" height="18" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
        <line x1="23" y1="1" x2="39" y2="1" stroke="#ffffff"/><path d="M26 4 L35 13 M35 4 L26 13" stroke="#000000" stroke-width="2"/>
      </g>
    </g>

    <!-- Tabs: [General] [Device Manager (Active)] [Hardware Profiles] [Performance] -->
    <g transform="translate(12, 34)">
      <!-- Inactive Tab 1 -->
      <rect x="0" y="4" width="70" height="20" rx="2" fill="#c0c0c0" stroke="#808080"/>
      <text class="w98" x="12" y="18" fill="#404040">General</text>

      <!-- Active Tab: Device Manager -->
      <rect x="74" y="0" width="130" height="25" rx="3" fill="#c0c0c0" stroke="#808080"/>
      <line x1="75" y1="1" x2="203" y2="1" stroke="#ffffff"/>
      <line x1="75" y1="1" x2="75" y2="24" stroke="#ffffff"/>
      <text class="w98-bold" x="84" y="17" fill="#000000">Device Manager</text>

      <!-- Inactive Tab 3 -->
      <rect x="208" y="4" width="120" height="20" rx="2" fill="#c0c0c0" stroke="#808080"/>
      <text class="w98" x="216" y="18" fill="#404040">Hardware Profiles</text>

      <!-- Inactive Tab 4 -->
      <rect x="332" y="4" width="90" height="20" rx="2" fill="#c0c0c0" stroke="#808080"/>
      <text class="w98" x="342" y="18" fill="#404040">Performance</text>
    </g>

    <!-- Tab Sunken Panel Surface -->
    <g transform="translate(12, 58)">
      <rect width="1176" height="268" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
      <line x1="1" y1="1" x2="1175" y2="1" stroke="#ffffff"/>
      <line x1="1" y1="1" x2="1" y2="267" stroke="#ffffff"/>

      <!-- View by type radio buttons -->
      <g transform="translate(16, 12)">
        <circle cx="6" cy="6" r="5" fill="#ffffff" stroke="#000000"/>
        <circle cx="6" cy="6" r="2.5" fill="#000000"/>
        <text class="w98" x="18" y="10">View devices by connection &amp; system architecture</text>
      </g>

      <!-- Tree View White Box (Device Tree) -->
      <g transform="translate(16, 32)">
        <rect width="960" height="220" fill="#ffffff" stroke="#808080" stroke-width="1"/>
        <line x1="1" y1="1" x2="959" y2="1" stroke="#404040"/>
        <line x1="1" y1="1" x2="1" y2="219" stroke="#404040"/>

        <!-- Computer Root Node -->
        <g transform="translate(16, 20)">
          <text class="mono" x="0" y="0" font-weight="bold" fill="#000080">[-] Computer (PORAS_NAGAR_RUNTIME_SYSTEM)</text>
          
          <!-- Category 1: Systems & Backend -->
          <text class="mono" x="20" y="22" font-weight="bold" fill="#000000">├── [+] Systems &amp; Distributed Backend</text>
          <text class="mono" x="50" y="38" fill="#404040">│   ├── Python 3.12 (Primary API Engine)</text>
          <text class="mono" x="50" y="52" fill="#404040">│   ├── FastAPI / Express / Node.js (High-Throughput Services)</text>
          <text class="mono" x="50" y="66" fill="#404040">│   └── RabbitMQ / Celery (Back-Pressured Message Broker)</text>

          <!-- Category 2: AI & ML -->
          <text class="mono" x="20" y="86" font-weight="bold" fill="#000000">├── [+] AI &amp; Quantitative Modeling</text>
          <text class="mono" x="50" y="102" fill="#404040">│   ├── TensorFlow / PyTorch (Valuation &amp; Regression Models)</text>
          <text class="mono" x="50" y="116" fill="#404040">│   └── OpenCV / scikit-learn / Pandas / NumPy</text>

          <!-- Category 3: Databases -->
          <text class="mono" x="20" y="136" font-weight="bold" fill="#000000">├── [+] Data Storage &amp; Cache Layers</text>
          <text class="mono" x="50" y="152" fill="#404040">│   ├── PostgreSQL (B-Tree Partitioned Time-Series)</text>
          <text class="mono" x="50" y="166" fill="#404040">│   └── Redis / MongoDB / MySQL</text>

          <!-- Category 4: Platforms -->
          <text class="mono" x="20" y="186" font-weight="bold" fill="#000000">└── [+] Frontend &amp; Cloud Infrastructure</text>
          <text class="mono" x="50" y="200" fill="#404040">    └── TypeScript • React 18 • Docker • Linux (POSIX) • GitHub Actions</text>
        </g>
      </g>

      <!-- Right Action Push Buttons -->
      <g transform="translate(994, 32)">
        <g transform="translate(0, 0)">
          <rect width="164" height="26" fill="#c0c0c0" stroke="#000000"/>
          <line x1="1" y1="1" x2="163" y2="1" stroke="#ffffff"/><text class="w98" x="48" y="17">Properties</text>
        </g>
        <g transform="translate(0, 36)">
          <rect width="164" height="26" fill="#c0c0c0" stroke="#000000"/>
          <line x1="1" y1="1" x2="163" y2="1" stroke="#ffffff"/><text class="w98" x="54" y="17">Refresh</text>
        </g>
        <g transform="translate(0, 72)">
          <rect width="164" height="26" fill="#c0c0c0" stroke="#000000"/>
          <line x1="1" y1="1" x2="163" y2="1" stroke="#ffffff"/><text class="w98" x="62" y="17">Print...</text>
        </g>
      </g>
    </g>

    <!-- Bottom Buttons: [OK] [Cancel] -->
    <g transform="translate(1006, 334)">
      <rect width="84" height="24" fill="#c0c0c0" stroke="#000000"/>
      <line x1="1" y1="1" x2="83" y2="1" stroke="#ffffff"/><text class="w98-bold" x="32" y="16">OK</text>

      <rect x="94" width="84" height="24" fill="#c0c0c0" stroke="#000000"/>
      <line x1="95" y1="1" x2="177" y2="1" stroke="#ffffff"/><text class="w98" x="116" y="16">Cancel</text>
    </g>
  </g>
</svg>"""

stack_crt = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-label="CRT Process Monitor Tech Stack">
  <defs>
    <filter id="stack_glow">
      <feGaussianBlur stdDeviation="1.8" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <style>
    .crt { font-family: ui-monospace, "Courier New", monospace; font-size: 12px; fill: #00ff66; }
    .amber { font-family: ui-monospace, "Courier New", monospace; font-size: 12px; fill: #ffb000; }
    .dim { font-family: ui-monospace, "Courier New", monospace; font-size: 11px; fill: #1d7734; }
  </style>

  <rect width="1200" height="370" rx="8" fill="#141714" stroke="#252b25" stroke-width="3"/>
  <rect x="8" y="8" width="1184" height="354" rx="6" fill="#050a05"/>

  <g filter="url(#stack_glow)" transform="translate(36, 36)">
    <!-- HTOP / PS Readout -->
    <text class="amber" x="0" y="0" font-weight="bold">TOP - PORAS_NAGAR_OS: 18 PROCESSES ACTIVE, 0 FAILED, LOAD AVERAGE: 0.08, 0.05, 0.01</text>
    <text class="dim" x="0" y="18">Tasks: 18 total, 4 running, 14 sleeping | Mem: 640K total, 142K free | Swap: 0K</text>
    
    <text class="crt" x="0" y="44" font-weight="bold">PID   USER     PR  NI  VIRT   RES   SHR S %CPU %MEM   TIME+  COMMAND</text>
    <text class="dim" x="0" y="58">─────────────────────────────────────────────────────────────────────────────────────────────</text>
    
    <text class="crt" x="0" y="78">101   poras    20   0  14.2M  8.4M  2.1M S  44.2 12.4  142:01  python3 -m uvicorn.api.unlistedstox</text>
    <text class="crt" x="0" y="98">102   poras    20   0  18.6M 11.2M  3.4M S  31.8 15.2   88:14  node --max-old-space=4096 triage.js</text>
    <text class="crt" x="0" y="118">103   poras    20   0  22.1M 14.8M  4.2M S  14.5 18.0  210:45  celery -A scraper_cluster worker -l info</text>
    <text class="crt" x="0" y="138">104   poras    20   0  32.4M 24.1M  8.5M S   8.2 22.4   44:20  python3 hermes_agentic_pipeline.py</text>
    <text class="crt" x="0" y="158">105   postgres 20   0  48.0M 32.0M 12.0M S   4.1 28.5  512:30  postgres: btree_partition_idx_worker</text>
    <text class="crt" x="0" y="178">106   redis    20   0   8.2M  4.1M  1.8M S   2.0  4.2   98:12  redis-server *:6379 [dead_letter_replay]</text>
    <text class="crt" x="0" y="198">107   docker   20   0  12.8M  6.4M  2.2M S   1.4  6.0   34:02  dockerd --dns 1.1.1.1 [production_suite]</text>
    <text class="crt" x="0" y="218">108   poras    20   0   9.4M  5.2M  1.9M S   0.9  4.8   12:10  next-server (React 18 / TypeScript)</text>

    <text class="dim" x="0" y="248">─────────────────────────────────────────────────────────────────────────────────────────────</text>
    <text class="amber" x="0" y="272">&gt; ACTIVE PROCESS INTERFACE: ALL SERVICES RESPONDING WITHIN NORMAL OPERATING PARAMETERS</text>
    <text class="crt" x="0" y="294">PRESS &lt;F1&gt; FOR SYSTEM ARCHITECTURE • &lt;F10&gt; TO QUIT WORKSTATION</text>
  </g>
</svg>"""

# ==============================================================================
# 5. SIGNALS & TELEMETRY (WIN98 SYSTEM MONITOR LIGHT & CRT TELEMETRY STREAM DARK)
# ==============================================================================

def make_signals(commits="1,200+", repos="18", py_pct="46%", ts_pct="32%", sql_pct="15%", ops_pct="7%", dark=False):
    if not dark:
        # Windows 98 Light System Monitor
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 350" width="1200" height="350" role="img" aria-label="Windows 98 System Monitor Live Telemetry">
  <defs>
    <linearGradient id="sig_w98title" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#000080"/><stop offset="100%" stop-color="#1084d0"/>
    </linearGradient>
    <pattern id="cpu_grid" width="16" height="16" patternUnits="userSpaceOnUse">
      <path d="M 16 0 L 0 0 0 16" fill="none" stroke="#004400" stroke-width="1"/>
    </pattern>
    <clipPath id="sig_cp"><rect width="1200" height="350" rx="4"/></clipPath>
  </defs>

  <style>
    .w98 {{ font-family: "MS Sans Serif", Tahoma, -apple-system, sans-serif; font-size: 11.5px; }}
    .w98-bold {{ font-family: "MS Sans Serif", Tahoma, -apple-system, sans-serif; font-size: 11.5px; font-weight: bold; }}
    .mono {{ font-family: ui-monospace, "Courier New", monospace; font-size: 11px; }}
  </style>

  <g clip-path="url(#sig_cp)">
    <rect width="1200" height="350" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
    <line x1="1" y1="1" x2="1199" y2="1" stroke="#ffffff" stroke-width="2"/>
    <line x1="1" y1="1" x2="1" y2="349" stroke="#ffffff" stroke-width="2"/>
    <line x1="2" y1="348" x2="1198" y2="348" stroke="#808080" stroke-width="2"/>
    <line x1="1198" y1="2" x2="1198" y2="348" stroke="#808080" stroke-width="2"/>

    <!-- Title Bar -->
    <g transform="translate(4, 4)">
      <rect width="1192" height="24" fill="url(#sig_w98title)"/>
      <text class="w98" x="10" y="17" font-size="12" font-weight="bold" fill="#ffffff">System Monitor - [Telemetry: Real-Time Engine Metrics &amp; Language Distribution]</text>
      <!-- Buttons -->
      <g transform="translate(1148, 3)">
        <rect x="0" y="0" width="18" height="18" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
        <line x1="1" y1="1" x2="17" y2="1" stroke="#ffffff"/><text class="w98" x="5" y="13" font-weight="bold">_</text>
        <rect x="22" y="0" width="18" height="18" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
        <line x1="23" y1="1" x2="39" y2="1" stroke="#ffffff"/><path d="M26 4 L35 13 M35 4 L26 13" stroke="#000000" stroke-width="2"/>
      </g>
    </g>

    <!-- Menu Bar -->
    <g transform="translate(12, 32)">
      <text class="w98" x="0" y="14"><tspan text-decoration="underline">F</tspan>ile</text>
      <text class="w98" x="34" y="14"><tspan text-decoration="underline">E</tspan>dit</text>
      <text class="w98" x="68" y="14"><tspan text-decoration="underline">V</tspan>iew</text>
      <text class="w98" x="106" y="14"><tspan text-decoration="underline">O</tspan>ptions</text>
      <text class="w98" x="156" y="14"><tspan text-decoration="underline">H</tspan>elp</text>
    </g>
    <line x1="4" y1="52" x2="1196" y2="52" stroke="#808080" stroke-width="1"/>
    <line x1="4" y1="53" x2="1196" y2="53" stroke="#ffffff" stroke-width="1"/>

    <!-- Left Box: Retro CRT CPU Usage History Graph -->
    <g transform="translate(16, 64)">
      <rect width="560" height="236" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
      <rect x="8" y="6" width="544" height="18" fill="#000080"/>
      <text class="w98" x="14" y="19" font-weight="bold" fill="#ffffff">CPU &amp; TELEMETRY VOLUME HISTORY (LAST 24 HOURS)</text>

      <!-- Graph Surface (Classic Green on Black Grid) -->
      <g transform="translate(8, 28)">
        <rect width="544" height="196" fill="#001100" stroke="#404040" stroke-width="1"/>
        <rect width="544" height="196" fill="url(#cpu_grid)"/>

        <!-- Simulated Pulse line in bright green -->
        <path d="M0 160 L40 150 L80 165 L120 130 L160 145 L200 90 L240 110 L280 60 L320 85 L360 40 L400 65 L440 30 L480 50 L520 20 L544 35" fill="none" stroke="#00ff00" stroke-width="2"/>
        
        <text class="mono" x="12" y="24" fill="#00ff00" font-weight="bold">THROUGHPUT: 10,480 PAGES/MIN</text>
        <text class="mono" x="12" y="42" fill="#00ff00">QUERY LATENCY: &lt; 15ms (B-TREE OPTIMIZED)</text>
        <text class="mono" x="380" y="24" fill="#00ff00">TOTAL COMMITS: {commits}</text>
        <text class="mono" x="380" y="42" fill="#00ff00">REPOSITORIES: {repos} ACTIVE</text>
      </g>
    </g>

    <!-- Right Box: Language Distribution & Resource Chunks -->
    <g transform="translate(600, 64)">
      <rect width="584" height="236" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
      <rect x="8" y="6" width="568" height="18" fill="#000080"/>
      <text class="w98" x="14" y="19" font-weight="bold" fill="#ffffff">CODEBASE COMPOSITION &amp; STACK ALLOCATION</text>

      <g transform="translate(18, 38)">
        <!-- Python -->
        <text class="w98-bold" x="0" y="14">Python (Backend, ML &amp; Quant Pipelines): {py_pct}</text>
        <!-- Segmented Royal Blue Progress Bar Chunks -->
        <g transform="translate(0, 22)">
          <rect width="548" height="20" fill="#ffffff" stroke="#808080"/>
          <!-- Chunky blocks -->
          <rect x="3" y="3" width="16" height="14" fill="#000080"/><rect x="22" y="3" width="16" height="14" fill="#000080"/>
          <rect x="41" y="3" width="16" height="14" fill="#000080"/><rect x="60" y="3" width="16" height="14" fill="#000080"/>
          <rect x="79" y="3" width="16" height="14" fill="#000080"/><rect x="98" y="3" width="16" height="14" fill="#000080"/>
          <rect x="117" y="3" width="16" height="14" fill="#000080"/><rect x="136" y="3" width="16" height="14" fill="#000080"/>
          <rect x="155" y="3" width="16" height="14" fill="#000080"/><rect x="174" y="3" width="16" height="14" fill="#000080"/>
          <rect x="193" y="3" width="16" height="14" fill="#000080"/><rect x="212" y="3" width="16" height="14" fill="#000080"/>
        </g>

        <!-- TypeScript & Node -->
        <text class="w98-bold" x="0" y="66">TypeScript &amp; JavaScript (React, Next.js, Express): {ts_pct}</text>
        <g transform="translate(0, 74)">
          <rect width="548" height="20" fill="#ffffff" stroke="#808080"/>
          <rect x="3" y="3" width="16" height="14" fill="#1084d0"/><rect x="22" y="3" width="16" height="14" fill="#1084d0"/>
          <rect x="41" y="3" width="16" height="14" fill="#1084d0"/><rect x="60" y="3" width="16" height="14" fill="#1084d0"/>
          <rect x="79" y="3" width="16" height="14" fill="#1084d0"/><rect x="98" y="3" width="16" height="14" fill="#1084d0"/>
          <rect x="117" y="3" width="16" height="14" fill="#1084d0"/><rect x="136" y="3" width="16" height="14" fill="#1084d0"/>
        </g>

        <!-- SQL & Messaging -->
        <text class="w98-bold" x="0" y="118">SQL, Redis &amp; RabbitMQ Ingestion Queues: {sql_pct}</text>
        <g transform="translate(0, 126)">
          <rect width="548" height="20" fill="#ffffff" stroke="#808080"/>
          <rect x="3" y="3" width="16" height="14" fill="#800080"/><rect x="22" y="3" width="16" height="14" fill="#800080"/>
          <rect x="41" y="3" width="16" height="14" fill="#800080"/><rect x="60" y="3" width="16" height="14" fill="#800080"/>
        </g>

        <!-- Infrastructure & CI -->
        <text class="w98-bold" x="0" y="170">Docker, Linux &amp; GitHub Actions CI Pipelines: {ops_pct}</text>
        <g transform="translate(0, 178)">
          <rect width="548" height="16" fill="#ffffff" stroke="#808080"/>
          <rect x="3" y="2" width="16" height="12" fill="#008000"/><rect x="22" y="2" width="16" height="12" fill="#008000"/>
        </g>
      </g>
    </g>

    <!-- Bottom Status Bar -->
    <g transform="translate(16, 312)">
      <rect width="1168" height="24" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
      <text class="w98" x="10" y="16">Updated by GitHub Actions Cron • Next refresh scheduled at 00:00 IST • COM1 9600-8-N-1</text>
    </g>
  </g>
</svg>"""
    else:
        # CRT Terminal Dark Telemetry Monitor
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 350" width="1200" height="350" role="img" aria-label="CRT Phosphor Live Telemetry Monitor">
  <defs>
    <filter id="sig_glow">
      <feGaussianBlur stdDeviation="1.8" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <style>
    .crt {{ font-family: ui-monospace, "Courier New", monospace; font-size: 12px; fill: #00ff66; }}
    .amber {{ font-family: ui-monospace, "Courier New", monospace; font-size: 12px; fill: #ffb000; }}
    .dim {{ font-family: ui-monospace, "Courier New", monospace; font-size: 11px; fill: #1d7734; }}
  </style>

  <rect width="1200" height="350" rx="8" fill="#141714" stroke="#252b25" stroke-width="3"/>
  <rect x="8" y="8" width="1184" height="334" rx="6" fill="#040804"/>

  <g filter="url(#sig_glow)" transform="translate(36, 34)">
    <text class="amber" x="0" y="0" font-weight="bold">NETSTAT / REAL-TIME PRODUCTION TELEMETRY &amp; GITHUB TELEMETRY</text>
    <text class="dim" x="0" y="18">SOURCE: api.github.com/users/porasnagar • VERIFIED ENCRYPTION: SHA-256 • POLLING: AUTOMATED</text>
    <text class="crt" x="0" y="38">═════════════════════════════════════════════════════════════════════════════════════════════════</text>

    <!-- 2 Columns in ASCII -->
    <!-- Left Column: Metrics -->
    <g transform="translate(0, 60)">
      <text class="amber" x="0" y="0">[ ENGINE TELEMETRY ]</text>
      <text class="crt" x="0" y="24">┌────────────────────────────────────────────────────────┐</text>
      <text class="crt" x="0" y="44">│ OTC Valuation Latency : &lt; 15 ms  (B-tree index query)  │</text>
      <text class="crt" x="0" y="64">│ Distributed Scrapers  : 10k+ pages/min (Backpressure)  │</text>
      <text class="crt" x="0" y="84">│ WhatsApp Webhook Ack  : &lt; 200 ms (HMAC-SHA256 verified)│</text>
      <text class="crt" x="0" y="104">│ Total GitHub Commits  : {commits} across repositories    │</text>
      <text class="crt" x="0" y="124">│ Public Repositories   : {repos} active repositories      │</text>
      <text class="crt" x="0" y="144">│ Multi-Agent CI Tools  : Hermes Autonomous Doc Pipeline │</text>
      <text class="crt" x="0" y="164">└────────────────────────────────────────────────────────┘</text>
    </g>

    <!-- Right Column: Language Distribution Bars in ASCII -->
    <g transform="translate(560, 60)">
      <text class="amber" x="0" y="0">[ CODEBASE COMPOSITION &amp; BYTE DISTRIBUTION ]</text>
      <text class="crt" x="0" y="24">Python (Backend, ML, Models)   [{py_pct}]</text>
      <text class="crt" x="0" y="40">████████████████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒</text>

      <text class="crt" x="0" y="70">TypeScript &amp; Node (React/APIs)  [{ts_pct}]</text>
      <text class="crt" x="0" y="86">██████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒</text>

      <text class="crt" x="0" y="116">SQL, Redis &amp; Queue Ingestion    [{sql_pct}]</text>
      <text class="crt" x="0" y="132">████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒</text>

      <text class="crt" x="0" y="162">Infra, Docker &amp; CI Workflows    [{ops_pct}]</text>
      <text class="crt" x="0" y="178">██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒</text>
    </g>

    <text class="dim" x="0" y="260">─────────────────────────────────────────────────────────────────────────────────────────</text>
    <text class="dim" x="0" y="278">[TELEMETRY STREAM: SYNCHRONIZED] [CRON_DAEMON: 18:30 UTC / 00:00 IST] [STATUS: NORMAL]</text>
  </g>
</svg>"""

def main():
    print("Generating dual-theme retro OS assets...")
    write_asset("hero-light.svg", hero_win98)
    write_asset("hero.svg", hero_crt)
    write_asset("divider.svg", divider_dual)

    # 4 System Cards
    write_asset("card-unlistedstox-light.svg", make_retro_card(
        "UNLISTEDSTOX", "unlistedstox_pipeline.py",
        "OTC Valuation Engine", "Sub-15ms Reads",
        "Cap-Table Pipeline", "TF Regression",
        "Turns statutory filings &amp; debt metrics into live OTC prices.", False
    ))
    write_asset("card-unlistedstox.svg", make_retro_card(
        "UNLISTEDSTOX", "unlistedstox_pipeline.py",
        "OTC Valuation Engine", "Sub-15ms Reads",
        "Cap-Table Pipeline", "TF Regression",
        "Turns statutory filings &amp; debt metrics into live OTC prices.", True
    ))

    write_asset("card-triage-light.svg", make_retro_card(
        "TRIAGE_GATEWAY", "whatsapp_dispatcher.js",
        "Webhook Ack Window", "142ms (&lt; 200ms)",
        "Intake Authentication", "HMAC-SHA256 OK",
        "WhatsApp booking, triage intake &amp; expiring reports without app install.", False
    ))
    write_asset("card-triage.svg", make_retro_card(
        "TRIAGE_GATEWAY", "whatsapp_dispatcher.js",
        "Webhook Ack Window", "142ms (&lt; 200ms)",
        "Intake Authentication", "HMAC-SHA256 OK",
        "WhatsApp booking, triage intake &amp; expiring reports without app install.", True
    ))

    write_asset("card-scrapers-light.svg", make_retro_card(
        "SCRAPER_CLUSTER", "rabbitmq_redis_broker.py",
        "Ingestion Throughput", "10,480 pg/min",
        "Queue Resilience", "0 Dropped Records",
        "Distributed extraction cluster pulling OTC filings &amp; registrar data.", False
    ))
    write_asset("card-scrapers.svg", make_retro_card(
        "SCRAPER_CLUSTER", "rabbitmq_redis_broker.py",
        "Ingestion Throughput", "10,480 pg/min",
        "Queue Resilience", "0 Dropped Records",
        "Distributed extraction cluster pulling OTC filings &amp; registrar data.", True
    ))

    write_asset("card-agents-light.svg", make_retro_card(
        "HERMES_AGENT", "hermes_document_ci.py",
        "Document Synthesis", "DOCX/PPTX/XLSX",
        "CI Tool-Calling", "4 Repositories",
        "Autonomous agent drafts engineering paperwork &amp; decks inside CI.", False
    ))
    write_asset("card-agents.svg", make_retro_card(
        "HERMES_AGENT", "hermes_document_ci.py",
        "Document Synthesis", "DOCX/PPTX/XLSX",
        "CI Tool-Calling", "4 Repositories",
        "Autonomous agent drafts engineering paperwork &amp; decks inside CI.", True
    ))

    # Tech Stack
    write_asset("stack-light.svg", stack_win98)
    write_asset("stack.svg", stack_crt)

    # Telemetry
    write_asset("signals-light.svg", make_signals(dark=False))
    write_asset("signals.svg", make_signals(dark=True))

    print("All retro assets generated successfully!")

if __name__ == "__main__":
    main()
