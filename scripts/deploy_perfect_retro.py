import os
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
README_PATH = os.path.join(BASE_DIR, "README.md")

def write_and_verify(filename, content):
    path = os.path.join(ASSETS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    try:
        ET.parse(path)
        print(f"VERIFIED XML OK: {filename} ({len(content)} bytes)")
    except Exception as e:
        print(f"ERROR XML INVALID: {filename} -> {e}")
        raise e

# ==============================================================================
# 1. HERO CONSOLE (NO UNLISTEDSTOX/ENXTAI CURRENT EMPLOYMENT)
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
  </style>

  <g clip-path="url(#frame)">
    <rect width="1200" height="370" fill="#008080"/>
    <rect width="1200" height="370" fill="url(#scanlines)"/>

    <!-- Main Window Outer Frame -->
    <g transform="translate(20, 16)">
      <rect width="1160" height="338" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
      <line x1="1" y1="1" x2="1159" y2="1" stroke="#ffffff" stroke-width="2"/>
      <line x1="1" y1="1" x2="1" y2="337" stroke="#ffffff" stroke-width="2"/>
      <line x1="2" y1="336" x2="1158" y2="336" stroke="#808080" stroke-width="2"/>
      <line x1="1158" y1="2" x2="1158" y2="336" stroke="#808080" stroke-width="2"/>

      <!-- Title Bar -->
      <g transform="translate(4, 4)">
        <rect width="1152" height="24" fill="url(#w98title)"/>
        <rect x="5" y="4" width="16" height="16" fill="#ffff00" stroke="#000000" stroke-width="1"/>
        <rect x="8" y="7" width="10" height="10" fill="#000080"/>
        <text class="w98-font" x="27" y="17" font-size="12" font-weight="bold" fill="#ffffff" letter-spacing="0.02em">C:\\PORAS\\PROFILE.EXE - [Poras Nagar: AI Engineer &amp; Distributed Systems Builder]</text>
        
        <g transform="translate(1088, 3)">
          <rect x="0" y="0" width="18" height="18" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
          <line x1="1" y1="1" x2="17" y2="1" stroke="#ffffff"/><line x1="4" y1="13" x2="12" y2="13" stroke="#000000" stroke-width="2"/>
          <rect x="20" y="0" width="18" height="18" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
          <line x1="21" y1="1" x2="37" y2="1" stroke="#ffffff"/><rect x="24" y="4" width="10" height="9" fill="none" stroke="#000000" stroke-width="2"/>
          <rect x="40" y="0" width="18" height="18" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
          <line x1="41" y1="1" x2="57" y2="1" stroke="#ffffff"/><path d="M44 4 L53 13 M53 4 L44 13" stroke="#000000" stroke-width="2"/>
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
            <text class="mono" x="0" y="46" font-size="13" font-weight="bold" fill="#008000">&gt; AI Engineer &amp; Distributed Systems Developer</text>
            <text class="w98-font" x="0" y="68" font-size="12" fill="#404040">Specializing in high-throughput scrapers, vision/audio models &amp; multi-agent autonomous CI tooling.</text>
          </g>

          <!-- Bio / Details Inset Box -->
          <g transform="translate(0, 96)">
            <rect width="640" height="106" fill="#f0f0f0" stroke="#808080" stroke-width="1"/>
            <line x1="1" y1="1" x2="639" y2="1" stroke="#000000" stroke-width="1"/>
            <line x1="1" y1="1" x2="1" y2="105" stroke="#000000" stroke-width="1"/>

            <text class="mono" x="16" y="24" font-size="11.5" fill="#000080">OPERATOR   : Poras Nagar</text>
            <text class="mono" x="16" y="44" font-size="11.5" fill="#000000">EDUCATION  : B.Tech CSE (Hons. AI &amp; ML), Amity University [2021-2025]</text>
            <text class="mono" x="16" y="64" font-size="11.5" fill="#000000">LOCATION   : Noida, India (UTC+5:30) • Open to Global AI &amp; Backend Roles</text>
            <text class="mono" x="16" y="84" font-size="11.5" fill="#800000">BUILDING   : LumaVoice (Lip-Reading AI), Scraper Clusters &amp; Hermes Agent</text>
          </g>
        </g>

        <!-- Right Column: System Resource Inset Box -->
        <g transform="translate(700, 20)">
          <rect width="410" height="182" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
          <line x1="0" y1="0" x2="409" y2="0" stroke="#404040" stroke-width="1"/>
          <line x1="0" y1="0" x2="0" y2="181" stroke="#404040" stroke-width="1"/>

          <rect x="8" y="6" width="394" height="20" fill="#000080"/>
          <text class="w98-font" x="14" y="20" font-size="11" font-weight="bold" fill="#ffffff">SYSTEM ARCHITECTURE &amp; OPERATIONAL STATUS</text>

          <g transform="translate(16, 40)">
            <text class="mono" x="0" y="12" font-size="11" fill="#000000">LumaVoice Vision Inference :</text>
            <text class="mono" x="220" y="12" font-size="11" font-weight="bold" fill="#000080">[30 FPS STREAM] OK</text>

            <text class="mono" x="0" y="36" font-size="11" fill="#000000">Scraper Ingestion Rate     :</text>
            <text class="mono" x="220" y="36" font-size="11" font-weight="bold" fill="#008000">[10k+ pg/m] OK</text>

            <text class="mono" x="0" y="60" font-size="11" fill="#000000">WhatsApp Webhook ACK Window :</text>
            <text class="mono" x="220" y="60" font-size="11" font-weight="bold" fill="#800080">[&lt; 200ms] OK</text>

            <text class="mono" x="0" y="84" font-size="11" fill="#000000">Hermes Multi-Agent CI      :</text>
            <text class="mono" x="220" y="84" font-size="11" font-weight="bold" fill="#000080">[AUTONOMOUS] DOCS</text>

            <text class="mono" x="0" y="108" font-size="11" fill="#000000">Availability For Hire      :</text>
            <text class="mono" x="220" y="108" font-size="11" font-weight="bold" fill="#008000">[OPEN GLOBALLY]</text>
          </g>
        </g>
      </g>

      <!-- Status Bar -->
      <g transform="translate(12, 304)">
        <rect x="0" y="0" width="460" height="22" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
        <text class="w98-font" x="8" y="15" font-size="11" fill="#000000">Ready</text>

        <rect x="466" y="0" width="340" height="22" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
        <text class="w98-font" x="474" y="15" font-size="11" fill="#000000">4 Architecture Engines in Production</text>

        <rect x="812" y="0" width="324" height="22" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
        <text class="w98-font" x="820" y="15" font-size="11" fill="#000080">● MS-DOS Prompt Connected (COM1)</text>
      </g>
    </g>
  </g>
</svg>"""

hero_crt = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-label="Poras Nagar — 90s CRT Terminal Boot Console">
  <defs>
    <radialGradient id="crtVignette" cx="50%" cy="50%" r="65%">
      <stop offset="0%" stop-color="#0a180a" stop-opacity="0.2"/>
      <stop offset="85%" stop-color="#050a05" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#010301" stop-opacity="0.98"/>
    </radialGradient>
    <pattern id="crtScanlines" width="100" height="3" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="100" y2="0" stroke="#000000" stroke-width="1.2" opacity="0.45"/>
    </pattern>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.2" result="coloredBlur"/>
      <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="screen"><rect x="18" y="16" width="1164" height="338" rx="14"/></clipPath>
  </defs>

  <style>
    .crt-font { font-family: ui-monospace, "Courier New", "Lucida Console", monospace; font-size: 13px; fill: #00ff66; }
    .amber-font { font-family: ui-monospace, "Courier New", "Lucida Console", monospace; font-size: 13px; fill: #ffb000; }
    .dim-font { font-family: ui-monospace, "Courier New", "Lucida Console", monospace; font-size: 12px; fill: #1d7734; }
    .blink { animation: crtBlink 0.9s step-end infinite; }
    @keyframes crtBlink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
  </style>

  <rect width="1200" height="370" rx="8" fill="#141714" stroke="#252b25" stroke-width="3"/>
  <rect x="8" y="8" width="1184" height="354" rx="6" fill="#0d100d"/>
  <circle cx="1150" cy="354" r="3.5" fill="#00ff66" filter="url(#glow)"/>
  <text class="dim-font" x="1080" y="357" font-size="9.5">POWER / CRT</text>

  <g clip-path="url(#screen)">
    <rect x="18" y="16" width="1164" height="338" fill="#050e05"/>
    <rect x="18" y="16" width="1164" height="338" fill="url(#crtVignette)"/>
    <rect x="18" y="16" width="1164" height="338" fill="url(#crtScanlines)"/>

    <g filter="url(#glow)" transform="translate(42, 44)">
      <text class="dim-font" x="0" y="0">PHOSPHOR-BIOS v4.02 (C) 1998 PORAS NAGAR SYSTEMS INC.</text>
      <text class="dim-font" x="0" y="18">CPU: DISTRIBUTED QUANT ENGINE @ 10,000 PAGES/MIN • MEMORY: 640KB ALLOCATED</text>
      
      <text class="crt-font" x="0" y="44" font-weight="bold">╔═════════════════════════════════════════════════════════════════════════════════════════════╗</text>
      <text class="crt-font" x="0" y="62" font-weight="bold">║  OPERATOR: PORAS NAGAR  |  ROLE: AI ENGINEER &amp; DISTRIBUTED SYSTEMS  |  LOCATION: NOIDA, IN  ║</text>
      <text class="crt-font" x="0" y="80" font-weight="bold">╚═════════════════════════════════════════════════════════════════════════════════════════════╝</text>

      <g transform="translate(0, 108)">
        <text class="amber-font" x="0" y="0">&gt; CURRENTLY ACTIVE CORE ENGINES &amp; RESEARCH PIPELINES:</text>

        <text class="crt-font" x="18" y="24">[DAEMON 01] lumavoice-vision       : Hindi Lip-Reading Computer Vision Model (PyTorch / CNN-LSTM)</text>
        <text class="crt-font" x="18" y="44">[DAEMON 02] triage-gateway         : Hospital Intake via Meta WhatsApp Cloud API - 200ms ACK</text>
        <text class="crt-font" x="18" y="64">[DAEMON 03] scraper-cluster        : RabbitMQ Queue Fan-out + Redis Deduplication (10k+ pg/m)</text>
        <text class="crt-font" x="18" y="84">[DAEMON 04] hermes-agent           : Multi-Agent Autonomous Document Synthesis Pipeline</text>

        <text class="dim-font" x="0" y="116">---------------------------------------------------------------------------------------------</text>
        <text class="amber-font" x="0" y="136">C:\PORAS\SYSTEM&gt; exec --status=ONLINE --open_for_hire=TRUE</text>
        <text class="crt-font" x="0" y="156">TELEMETRY STREAM: SYNCHRONIZED [99.9% UPTIME] <tspan class="blink">█</tspan></text>
      </g>
    </g>
  </g>
</svg>"""

# ==============================================================================
# 2. TICKER (CLEANED UP TO AVOID UNLISTEDSTOX SPAM)
# ==============================================================================

ticker_win98 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 36" width="1200" height="36" role="marquee" aria-label="Live Retro Ticker">
  <defs>
    <clipPath id="tk_clip"><rect x="6" y="4" width="1188" height="28" rx="2"/></clipPath>
  </defs>
  <style>
    .ticker-font { font-family: "MS Sans Serif", Tahoma, ui-monospace, sans-serif; font-size: 11.5px; font-weight: bold; fill: #000080; }
    .ticker-scroll { animation: scrollLeft 32s linear infinite; }
    @keyframes scrollLeft {
      0%   { transform: translateX(1180px); }
      100% { transform: translateX(-2400px); }
    }
  </style>

  <rect width="1200" height="36" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
  <line x1="1" y1="1" x2="1199" y2="1" stroke="#ffffff"/>
  <line x1="1" y1="1" x2="1" y2="35" stroke="#ffffff"/>

  <rect x="4" y="4" width="1192" height="28" fill="#ffffea" stroke="#808080" stroke-width="1"/>
  <line x1="4" y1="4" x2="1195" y2="4" stroke="#404040"/>
  <line x1="4" y1="4" x2="4" y2="31" stroke="#404040"/>

  <g clip-path="url(#tk_clip)">
    <g class="ticker-scroll">
      <text class="ticker-font" x="0" y="22">
        📢 [OPERATOR]: Poras Nagar • Independent AI Engineer &amp; Distributed Systems Builder • 🧠 [LUMAVOICE]: Lip-reading deep learning model (Hindi phoneme extraction) • ⚡ [SCRAPER CLUSTER]: 10,480 pages/min fan-out • 💬 [TRIAGE GATEWAY]: Meta WhatsApp Cloud API 142ms ack • 🤖 [HERMES AGENT]: Multi-agent CI document synthesis • 🎓 [EDUCATION]: B.Tech CSE (Hons. AI &amp; ML) Amity University • 💼 [AVAILABILITY]: Open to Global AI &amp; Distributed Backend Roles
      </text>
    </g>
  </g>
</svg>"""

ticker_crt = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 36" width="1200" height="36" role="marquee" aria-label="CRT Stream Ticker">
  <defs>
    <filter id="crt_tk_glow">
      <feGaussianBlur stdDeviation="1.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="crt_tk_clip"><rect x="8" y="4" width="1184" height="28" rx="2"/></clipPath>
  </defs>
  <style>
    .crt-tk { font-family: ui-monospace, "Courier New", monospace; font-size: 12px; fill: #00ff66; }
    .scroll-crt { animation: scrollCrt 32s linear infinite; }
    @keyframes scrollCrt {
      0%   { transform: translateX(1180px); }
      100% { transform: translateX(-2400px); }
    }
  </style>

  <rect width="1200" height="36" rx="4" fill="#070b07" stroke="#1a2b1a" stroke-width="1.5"/>
  <g clip-path="url(#crt_tk_clip)">
    <g filter="url(#crt_tk_glow)" class="scroll-crt">
      <text class="crt-tk" x="0" y="22">
        &gt;&gt;&gt; [OPERATOR]: PORAS NAGAR &gt;&gt;&gt; [LUMAVOICE]: COMPUTER VISION INFERENCE STREAMING &gt;&gt;&gt; [SCRAPER_QUEUE]: 10,480 PG/MIN OK &gt;&gt;&gt; [TRIAGE_DISPATCH]: HMAC-SHA256 VERIFIED &gt;&gt;&gt; [HERMES_CI]: MULTI-AGENT PIPELINE NOMINAL &gt;&gt;&gt; [STATUS]: READY FOR INTERVIEWS &gt;&gt;&gt;
      </text>
    </g>
  </g>
</svg>"""

# ==============================================================================
# 3. CARD 1: LUMAVOICE (HINDI LIP-READING AI / COMPUTER VISION)
# ==============================================================================

def make_lumavoice_card(dark=False):
    if not dark:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 176" width="580" height="176" role="img" aria-label="LumaVoice AI">
  <defs>
    <linearGradient id="tb_lv" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#000080"/><stop offset="100%" stop-color="#1084d0"/>
    </linearGradient>
    <clipPath id="cp_lv"><rect width="580" height="176" rx="2"/></clipPath>
  </defs>
  <style>
    .w98 { font-family: "MS Sans Serif", Tahoma, -apple-system, sans-serif; font-size: 11px; }
    .mono { font-family: ui-monospace, "Courier New", monospace; font-size: 11px; }
  </style>
  <g clip-path="url(#cp_lv)">
    <rect width="580" height="176" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
    <line x1="1" y1="1" x2="579" y2="1" stroke="#ffffff" stroke-width="2"/>
    <line x1="1" y1="1" x2="1" y2="175" stroke="#ffffff" stroke-width="2"/>
    <line x1="2" y1="174" x2="578" y2="174" stroke="#808080" stroke-width="2"/>
    <line x1="578" y1="2" x2="578" y2="174" stroke="#808080" stroke-width="2"/>

    <rect x="4" y="4" width="572" height="20" fill="url(#tb_lv)"/>
    <text class="w98" x="10" y="18" font-weight="bold" fill="#ffffff">LUMAVOICE_AI.EXE - [Lip-Reading Computer Vision Model]</text>
    <g transform="translate(528, 5)">
      <rect x="0" y="0" width="14" height="14" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
      <line x1="1" y1="1" x2="13" y2="1" stroke="#ffffff"/><line x1="3" y1="10" x2="10" y2="10" stroke="#000000" stroke-width="2"/>
      <rect x="18" y="0" width="14" height="14" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
      <line x1="19" y1="1" x2="31" y2="1" stroke="#ffffff"/><path d="M22 3 L29 10 M29 3 L22 10" stroke="#000000" stroke-width="1.5"/>
    </g>

    <g transform="translate(8, 28)">
      <rect width="564" height="118" fill="#ffffff" stroke="#808080" stroke-width="1"/>
      <line x1="1" y1="1" x2="563" y2="1" stroke="#404040"/>
      <line x1="1" y1="1" x2="1" y2="117" stroke="#404040"/>
      
      <g transform="translate(14, 12)">
        <rect width="256" height="52" fill="#f0f0f0" stroke="#808080" stroke-width="1"/>
        <text class="w98" x="8" y="16" fill="#000080" font-weight="bold">LIP-READING INFERENCE</text>
        <text class="mono" x="8" y="38" font-size="16" font-weight="bold" fill="#008000">30 FPS Stream</text>
      </g>
      <g transform="translate(284, 12)">
        <rect width="266" height="52" fill="#f0f0f0" stroke="#808080" stroke-width="1"/>
        <text class="w98" x="8" y="16" fill="#000080" font-weight="bold">TARGET DIALECT</text>
        <text class="mono" x="8" y="38" font-size="16" font-weight="bold" fill="#800080">Hindi Phonemes (CNN-LSTM)</text>
      </g>

      <text class="w98" x="16" y="86" fill="#000000">Spatio-temporal neural network extracts phonemes from silent mouth ROI crops.</text>
      <text class="mono" x="16" y="104" fill="#808080">PyTorch • OpenCV • Lip ROI Cropper • Real-Time Audio-Visual Synth</text>
    </g>

    <rect x="8" y="150" width="564" height="18" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
    <text class="w98" x="14" y="163" fill="#000000">Model Weights Loaded • CUDA Stream Synchronized</text>
  </g>
</svg>"""
    else:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 176" width="580" height="176" role="img" aria-label="LumaVoice AI">
  <defs>
    <filter id="cglow_lv">
      <feGaussianBlur stdDeviation="1.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <style>
    .crt { font-family: ui-monospace, "Courier New", monospace; font-size: 11.5px; fill: #00ff66; }
    .amber { font-family: ui-monospace, "Courier New", monospace; font-size: 11.5px; fill: #ffb000; }
    .dim { font-family: ui-monospace, "Courier New", monospace; font-size: 10px; fill: #1d7734; }
  </style>
  <rect width="580" height="176" rx="6" fill="#080e08" stroke="#223322" stroke-width="2"/>
  <rect x="6" y="6" width="568" height="164" rx="4" fill="#030803"/>

  <g filter="url(#cglow_lv)" transform="translate(18, 24)">
    <text class="dim" x="0" y="0">┌──[ MODEL: lumavoice_hindi_lipreading.py ]──────────────────┐</text>
    <text class="amber" x="12" y="24">&gt; INFERENCE RATE: <tspan fill="#00ff66" font-weight="bold">30 FPS Live Stream</tspan></text>
    <text class="amber" x="12" y="44">&gt; ARCHITECTURE  : <tspan fill="#00ff66" font-weight="bold">CNN-LSTM + Lip Spatio-Temporal ROI</tspan></text>
    <text class="crt" x="12" y="70">Spatio-temporal network extracts visual phonemes from silent video crops.</text>
    <text class="dim" x="12" y="94">[STACK: PyTorch / OpenCV / NumPy] [STATUS: INFERENCE_ACTIVE]</text>
    <text class="dim" x="0" y="120">└─────────────────────────────────────────────────────────────┘</text>
  </g>
</svg>"""

def main():
    print("Writing updated retro assets without former employer/UnlistedStox current text...")
    write_and_verify("hero-light.svg", hero_win98)
    write_and_verify("hero.svg", hero_crt)
    write_and_verify("ticker-light.svg", ticker_win98)
    write_and_verify("ticker.svg", ticker_crt)
    write_and_verify("card-lumavoice-light.svg", make_lumavoice_card(False))
    write_and_verify("card-lumavoice.svg", make_lumavoice_card(True))
    print("Asset updates complete.")

if __name__ == "__main__":
    main()
