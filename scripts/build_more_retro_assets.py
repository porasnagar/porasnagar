import os
import xml.etree.ElementTree as ET

ASSETS_DIR = r"C:\Users\poras\.gemini\antigravity-ide\scratch\porasnagar-profile-repo\assets"

def write_svg(filename, content):
    filepath = os.path.join(ASSETS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    # Validate XML
    ET.parse(filepath)
    print(f"Validated XML: {filename} ({os.path.getsize(filepath)} bytes)")

# ==========================================
# 1. WINAMP / CHIPTUNE SYNTH PLAYER (LIGHT)
# ==========================================
player_light_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 148" width="1200" height="148" role="img" aria-label="WinAmp Audio Player">
  <defs>
    <linearGradient id="winampTitle" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#000080"/>
      <stop offset="100%" stop-color="#1084d0"/>
    </linearGradient>
    <clipPath id="eq_clip"><rect x="0" y="0" width="180" height="32"/></clipPath>
  </defs>

  <style>
    .w98 { font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; }
    .mono { font-family: ui-monospace, "Courier New", "Lucida Console", monospace; }
    .lcd { font-family: ui-monospace, "Courier New", monospace; font-size: 11.5px; fill: #00ff00; font-weight: bold; }
    
    /* Equalizer Bar Animations */
    .eq-bar1 { animation: eqJump 0.8s ease-in-out infinite alternate; transform-origin: bottom; }
    .eq-bar2 { animation: eqJump 0.6s ease-in-out infinite alternate-reverse; transform-origin: bottom; }
    .eq-bar3 { animation: eqJump 1.1s ease-in-out infinite alternate; transform-origin: bottom; }
    .eq-bar4 { animation: eqJump 0.7s ease-in-out infinite alternate-reverse; transform-origin: bottom; }
    .eq-bar5 { animation: eqJump 0.9s ease-in-out infinite alternate; transform-origin: bottom; }
    .eq-bar6 { animation: eqJump 0.5s ease-in-out infinite alternate-reverse; transform-origin: bottom; }
    .eq-bar7 { animation: eqJump 1.0s ease-in-out infinite alternate; transform-origin: bottom; }
    .eq-bar8 { animation: eqJump 0.75s ease-in-out infinite alternate-reverse; transform-origin: bottom; }

    @keyframes eqJump {
      0% { transform: scaleY(0.2); }
      50% { transform: scaleY(0.9); }
      100% { transform: scaleY(0.4); }
    }
  </style>

  <!-- Win98 Window Outer Frame -->
  <rect width="1200" height="148" fill="#c0c0c0" stroke="#000000" stroke-width="1.5"/>
  <line x1="1" y1="1" x2="1199" y2="1" stroke="#ffffff" stroke-width="2"/>
  <line x1="1" y1="1" x2="1" y2="147" stroke="#ffffff" stroke-width="2"/>
  <line x1="2" y1="146" x2="1198" y2="146" stroke="#808080" stroke-width="1"/>
  <line x1="1198" y1="2" x2="1198" y2="146" stroke="#808080" stroke-width="1"/>

  <!-- Window Title Bar -->
  <rect x="3" y="3" width="1194" height="24" fill="url(#winampTitle)"/>
  <g transform="translate(8, 7)">
    <rect width="14" height="14" fill="#000000" rx="1"/>
    <polygon points="4,3 11,7 4,11" fill="#ffff00"/>
    <text class="w98" x="22" y="11" font-size="11" font-weight="bold" fill="#ffffff" letter-spacing="0.5">WINAMP 2.91 — PORAS NAGAR AUDIO SYNTHESIZER [LIVE STREAM]</text>
  </g>
  <!-- Window Controls -->
  <g transform="translate(1124, 6)">
    <rect x="0" y="0" width="16" height="14" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
    <text class="w98" x="4" y="11" font-size="11" font-weight="bold" fill="#000000">_</text>
    <rect x="22" y="0" width="16" height="14" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
    <rect x="25" y="3" width="10" height="8" fill="none" stroke="#000000" stroke-width="1.2"/>
    <rect x="44" y="0" width="16" height="14" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
    <text class="w98" x="48" y="11" font-size="11" font-weight="bold" fill="#000000">&#x2715;</text>
  </g>

  <!-- Player Main Body -->
  <g transform="translate(12, 34)">
    <!-- LCD Screen -->
    <rect x="0" y="0" width="480" height="96" fill="#0a140a" stroke="#808080" stroke-width="1"/>
    <line x1="0" y1="0" x2="480" y2="0" stroke="#404040" stroke-width="1"/>
    <line x1="0" y1="0" x2="0" y2="96" stroke="#404040" stroke-width="1"/>

    <!-- Track & Status Inside LCD -->
    <text class="lcd" x="12" y="22">&#x25B6; 01. LUMAVOICE_HINDI_SPEECH_MATRIX.MP3</text>
    <text class="mono" x="12" y="42" font-size="11" fill="#00bb00">KBPS: 320  |  KHZ: 44.1  |  CH: STEREO</text>
    <text class="mono" x="12" y="62" font-size="11" fill="#008800">TIME: 03:42 / 05:18  |  PRESET: DEEP_LEARNING_ACOUSTICS</text>
    <text class="mono" x="12" y="82" font-size="10.5" fill="#ffb000">PLAYLIST: 01. LumaVoice  02. WhatsApp Triage  03. Scrapers  04. Hermes</text>

    <!-- Visualizer / Equalizer Panel -->
    <g transform="translate(496, 0)">
      <rect x="0" y="0" width="220" height="96" fill="#000000" stroke="#808080" stroke-width="1"/>
      <text class="mono" x="8" y="18" font-size="10" fill="#00ff66" font-weight="bold">SPECTRUM EQUALIZER</text>
      <line x1="8" y1="24" x2="212" y2="24" stroke="#1d7734" stroke-width="0.8"/>
      
      <!-- 8-band EQ Bars -->
      <g transform="translate(18, 86) scale(1, -1)">
        <rect class="eq-bar1" x="0" y="0" width="14" height="52" fill="#00ff66"/>
        <rect class="eq-bar2" x="22" y="0" width="14" height="52" fill="#00ff66"/>
        <rect class="eq-bar3" x="44" y="0" width="14" height="52" fill="#33ff33"/>
        <rect class="eq-bar4" x="66" y="0" width="14" height="52" fill="#66ff33"/>
        <rect class="eq-bar5" x="88" y="0" width="14" height="52" fill="#ffff00"/>
        <rect class="eq-bar6" x="110" y="0" width="14" height="52" fill="#ffff00"/>
        <rect class="eq-bar7" x="132" y="0" width="14" height="52" fill="#ff9900"/>
        <rect class="eq-bar8" x="154" y="0" width="14" height="52" fill="#ff3300"/>
      </g>
      <text class="mono" x="16" y="92" font-size="8" fill="#808080">60  170  310  600  1K  3K  6K  14K</text>
    </g>

    <!-- Transport Controls & Sliders -->
    <g transform="translate(732, 0)">
      <rect x="0" y="0" width="444" height="96" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
      <line x1="1" y1="1" x2="443" y2="1" stroke="#ffffff"/>
      <line x1="1" y1="1" x2="1" y2="95" stroke="#ffffff"/>

      <!-- Button Row -->
      <g transform="translate(12, 14)">
        <!-- PREV -->
        <rect x="0" y="0" width="48" height="30" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
        <line x1="1" y1="1" x2="47" y2="1" stroke="#ffffff"/><line x1="1" y1="1" x2="1" y2="29" stroke="#ffffff"/>
        <text class="w98" x="10" y="20" font-size="12" font-weight="bold" fill="#000000">&#x23EE;</text>

        <!-- PLAY -->
        <rect x="56" y="0" width="48" height="30" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
        <line x1="57" y1="1" x2="103" y2="1" stroke="#ffffff"/><line x1="57" y1="1" x2="57" y2="29" stroke="#ffffff"/>
        <polygon points="72,8 86,15 72,22" fill="#008000"/>

        <!-- PAUSE -->
        <rect x="112" y="0" width="48" height="30" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
        <line x1="113" y1="1" x2="159" y2="1" stroke="#ffffff"/><line x1="113" y1="1" x2="113" y2="29" stroke="#ffffff"/>
        <rect x="126" y="8" width="5" height="14" fill="#000000"/><rect x="135" y="8" width="5" height="14" fill="#000000"/>

        <!-- STOP -->
        <rect x="168" y="0" width="48" height="30" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
        <line x1="169" y1="1" x2="215" y2="1" stroke="#ffffff"/><line x1="169" y1="1" x2="169" y2="29" stroke="#ffffff"/>
        <rect x="184" y="8" width="14" height="14" fill="#800000"/>

        <!-- NEXT -->
        <rect x="224" y="0" width="48" height="30" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
        <line x1="225" y1="1" x2="271" y2="1" stroke="#ffffff"/><line x1="225" y1="1" x2="225" y2="29" stroke="#ffffff"/>
        <text class="w98" x="236" y="20" font-size="12" font-weight="bold" fill="#000000">&#x23ED;</text>

        <!-- EJECT -->
        <rect x="280" y="0" width="48" height="30" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
        <line x1="281" y1="1" x2="327" y2="1" stroke="#ffffff"/><line x1="281" y1="1" x2="281" y2="29" stroke="#ffffff"/>
        <polygon points="296,20 312,20 304,10" fill="#000080"/>
        <rect x="296" y="22" width="16" height="2" fill="#000080"/>

        <!-- VOLUME SLIDER -->
        <g transform="translate(340, 4)">
          <text class="w98" x="0" y="10" font-size="9.5" fill="#000000">VOL: 92%</text>
          <rect x="0" y="14" width="76" height="6" fill="#808080"/>
          <rect x="58" y="10" width="12" height="14" fill="#c0c0c0" stroke="#000000"/>
        </g>
      </g>

      <!-- Status Bar Inside Player -->
      <text class="w98" x="14" y="72" font-size="11" fill="#000000">ENGINE STATUS: <tspan font-weight="bold" fill="#008000">SYNCHRONIZED</tspan> • REPETITION: LOOP ALL</text>
      <text class="mono" x="14" y="86" font-size="10" fill="#555555">DSP: STEREO PAN ACTIVE • DIRECTSOUND 3D BUFFER: 0ms LATENCY</text>
    </g>
  </g>
</svg>'''

# ==========================================
# 2. WINAMP / CHIPTUNE SYNTH PLAYER (DARK CRT)
# ==========================================
player_dark_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 148" width="1200" height="148" role="img" aria-label="CRT Audio Streamer">
  <defs>
    <radialGradient id="playerVignette" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#0a180a" stop-opacity="0.1"/>
      <stop offset="90%" stop-color="#050a05" stop-opacity="0.75"/>
      <stop offset="100%" stop-color="#010301" stop-opacity="0.95"/>
    </radialGradient>
    <filter id="pGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="1.8" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <style>
    .crt { font-family: ui-monospace, "Courier New", monospace; font-size: 11.5px; fill: #00ff66; }
    .amber { font-family: ui-monospace, "Courier New", monospace; font-size: 11px; fill: #ffb000; }
    .dim { font-family: ui-monospace, "Courier New", monospace; font-size: 10.5px; fill: #1d7734; }
    .p-eq1 { animation: pEq 0.7s ease-in-out infinite alternate; transform-origin: bottom; }
    .p-eq2 { animation: pEq 0.9s ease-in-out infinite alternate-reverse; transform-origin: bottom; }
    .p-eq3 { animation: pEq 0.5s ease-in-out infinite alternate; transform-origin: bottom; }
    .p-eq4 { animation: pEq 1.1s ease-in-out infinite alternate-reverse; transform-origin: bottom; }
    @keyframes pEq { 0% { transform: scaleY(0.2); } 100% { transform: scaleY(0.85); } }
  </style>

  <rect width="1200" height="148" rx="6" fill="#141714" stroke="#252b25" stroke-width="2"/>
  <rect x="6" y="6" width="1188" height="136" rx="4" fill="#050a05"/>
  <rect x="6" y="6" width="1188" height="136" fill="url(#playerVignette)"/>

  <g filter="url(#pGlow)" transform="translate(24, 28)">
    <text class="dim" x="0" y="0">&#x250C;&#x2500;&#x2500;[ SYNTHESIZER / AUDIO DAEMON: /dev/dsp0 (PCM 44.1kHz) ]&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2510;</text>
    
    <text class="crt" x="18" y="24">&#x25B6; STREAM: [LUMAVOICE_ACOUSTIC_SYNTHESIS.MOD] - 4 CHANNELS / AMIGA TRACKER FORMAT</text>
    <text class="amber" x="18" y="44">BITRATE: 320 KBPS | BUFFER: 1024 FRAMES (0 UNDERFLOWS) | STATUS: STREAMING NOMINAL</text>
    <text class="dim" x="18" y="64">QUEUE: [1] LumaVoice Vision  [2] Triage Cloud API  [3] Distributed Scraper  [4] Hermes Agent</text>
    
    <text class="dim" x="0" y="88">&#x2514;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2518;</text>
  </g>

  <!-- Phosphor Spectrum Bars (Right Side) -->
  <g filter="url(#pGlow)" transform="translate(990, 100) scale(1, -1)">
    <rect class="p-eq1" x="0" y="0" width="12" height="60" fill="#00ff66"/>
    <rect class="p-eq2" x="18" y="0" width="12" height="60" fill="#00ff66"/>
    <rect class="p-eq3" x="36" y="0" width="12" height="60" fill="#00ff66"/>
    <rect class="p-eq4" x="54" y="0" width="12" height="60" fill="#00ff66"/>
    <rect class="p-eq1" x="72" y="0" width="12" height="60" fill="#00ff66"/>
    <rect class="p-eq2" x="90" y="0" width="12" height="60" fill="#00ff66"/>
    <rect class="p-eq3" x="108" y="0" width="12" height="60" fill="#00ff66"/>
    <rect class="p-eq4" x="126" y="0" width="12" height="60" fill="#00ff66"/>
  </g>
</svg>'''

# ==================================================
# 3. SYSTEM PROPERTIES DIALOG (LIGHT MODE)
# ==================================================
sys_prop_light_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 310" width="1200" height="310" role="img" aria-label="System Properties">
  <defs>
    <linearGradient id="spTitle" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#000080"/>
      <stop offset="100%" stop-color="#1084d0"/>
    </linearGradient>
  </defs>

  <style>
    .w98 { font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; }
    .mono { font-family: ui-monospace, "Courier New", "Lucida Console", monospace; }
  </style>

  <!-- Outer Window Frame -->
  <rect width="1200" height="310" fill="#c0c0c0" stroke="#000000" stroke-width="1.5"/>
  <line x1="1" y1="1" x2="1199" y2="1" stroke="#ffffff" stroke-width="2"/>
  <line x1="1" y1="1" x2="1" y2="309" stroke="#ffffff" stroke-width="2"/>
  <line x1="2" y1="308" x2="1198" y2="308" stroke="#808080" stroke-width="1"/>
  <line x1="1198" y1="2" x2="1198" y2="308" stroke="#808080" stroke-width="1"/>

  <!-- Window Title Bar -->
  <rect x="3" y="3" width="1194" height="24" fill="url(#spTitle)"/>
  <text class="w98" x="10" y="19" font-size="11" font-weight="bold" fill="#ffffff">System Properties — PorasOS 98 Second Edition</text>
  <g transform="translate(1172, 6)">
    <rect x="0" y="0" width="16" height="14" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
    <text class="w98" x="4" y="11" font-size="11" font-weight="bold" fill="#000000">&#x2715;</text>
  </g>

  <!-- Property Tabs -->
  <g transform="translate(12, 34)">
    <!-- Active Tab: General -->
    <rect x="0" y="0" width="110" height="24" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
    <line x1="0" y1="0" x2="110" y2="0" stroke="#ffffff" stroke-width="1.5"/>
    <line x1="0" y1="0" x2="0" y2="24" stroke="#ffffff" stroke-width="1.5"/>
    <text class="w98" x="32" y="16" font-size="11" font-weight="bold" fill="#000000">General</text>

    <!-- Tab 2: Architectures -->
    <rect x="114" y="2" width="120" height="22" fill="#d4d0c8" stroke="#808080" stroke-width="1"/>
    <text class="w98" x="134" y="17" font-size="11" fill="#444444">Architectures</text>

    <!-- Tab 3: Hardware -->
    <rect x="238" y="2" width="110" height="22" fill="#d4d0c8" stroke="#808080" stroke-width="1"/>
    <text class="w98" x="264" y="17" font-size="11" fill="#444444">Hardware</text>

    <!-- Tab 4: Performance -->
    <rect x="352" y="2" width="120" height="22" fill="#d4d0c8" stroke="#808080" stroke-width="1"/>
    <text class="w98" x="376" y="17" font-size="11" fill="#444444">Performance</text>

    <!-- Tab Inner Content Box -->
    <rect x="0" y="23" width="1176" height="210" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
    <line x1="0" y1="23" x2="1175" y2="23" stroke="#ffffff"/>
    <line x1="0" y1="23" x2="0" y2="232" stroke="#ffffff"/>

    <!-- Left Column: Retro PC Illustration -->
    <g transform="translate(24, 45)">
      <!-- CRT Monitor Graphic -->
      <rect x="0" y="0" width="96" height="74" rx="4" fill="#e0e0d0" stroke="#808080" stroke-width="1.5"/>
      <rect x="8" y="8" width="80" height="58" rx="2" fill="#000080"/>
      <text class="mono" x="16" y="40" font-size="11" fill="#ffffff" font-weight="bold">PorasOS</text>
      <rect x="32" y="74" width="32" height="14" fill="#c0c0b8" stroke="#808080"/>
      <rect x="20" y="88" width="56" height="8" rx="2" fill="#d0d0c8" stroke="#808080"/>
      <!-- Tower Case -->
      <rect x="108" y="10" width="46" height="86" rx="2" fill="#e0e0d0" stroke="#808080" stroke-width="1.5"/>
      <rect x="114" y="18" width="34" height="6" fill="#808080"/>
      <rect x="114" y="28" width="34" height="6" fill="#808080"/>
      <circle cx="131" cy="74" r="3" fill="#008000"/>
    </g>

    <!-- Right Column: Specs -->
    <g transform="translate(200, 42)">
      <!-- System Specs -->
      <text class="w98" x="0" y="0" font-size="12" font-weight="bold" fill="#000000">System:</text>
      <text class="w98" x="16" y="18" font-size="11.5" fill="#000000">Microsoft Windows 98 / PorasOS Workstation Edition</text>
      <text class="w98" x="16" y="34" font-size="11.5" fill="#000000">4.10.2222 A (Applied AI &amp; Distributed Systems Core)</text>

      <!-- Registered To -->
      <text class="w98" x="0" y="62" font-size="12" font-weight="bold" fill="#000000">Registered to:</text>
      <text class="w98" x="16" y="80" font-size="11.5" font-weight="bold" fill="#000080">Poras Nagar</text>
      <text class="w98" x="16" y="96" font-size="11.5" fill="#000000">Independent AI Engineer &amp; High-Throughput Systems Builder</text>
      <text class="w98" x="16" y="112" font-size="11.5" fill="#555555">B.Tech Computer Science (Honors in AI &amp; ML), Amity University [2021-2025]</text>
      <text class="w98" x="16" y="128" font-size="11.5" fill="#008000">Availability: Open for Global Roles &amp; Full-Time Teams</text>

      <!-- Computer Specs -->
      <text class="w98" x="520" y="0" font-size="12" font-weight="bold" fill="#000000">Computer / Cluster:</text>
      <text class="w98" x="536" y="18" font-size="11.5" fill="#000000">Distributed Ingestion Cluster &amp; Neural Inference Pipeline</text>
      <text class="w98" x="536" y="34" font-size="11.5" fill="#000000">PyTorch 2.x • CUDA 12.1 • RabbitMQ • Docker • Redis</text>
      <text class="w98" x="536" y="50" font-size="11.5" fill="#000000">10,480 pages/min Scraper Cluster Fan-out</text>
      <text class="w98" x="536" y="66" font-size="11.5" fill="#000000">Meta Cloud WhatsApp Webhook (142ms ACK Latency)</text>
      <text class="w98" x="536" y="82" font-size="11.5" fill="#000000">640K Base RAM, 32,768 MB Virtual Neural Memory</text>
    </g>

    <!-- Bottom Buttons: OK, Cancel, Apply -->
    <g transform="translate(840, 242)">
      <rect x="0" y="0" width="76" height="24" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
      <line x1="1" y1="1" x2="75" y2="1" stroke="#ffffff"/><line x1="1" y1="1" x2="1" y2="23" stroke="#ffffff"/>
      <text class="w98" x="28" y="16" font-size="11" font-weight="bold" fill="#000000">OK</text>

      <rect x="86" y="0" width="76" height="24" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
      <line x1="87" y1="1" x2="161" y2="1" stroke="#ffffff"/><line x1="87" y1="1" x2="87" y2="23" stroke="#ffffff"/>
      <text class="w98" x="106" y="16" font-size="11" fill="#000000">Cancel</text>

      <rect x="172" y="0" width="76" height="24" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
      <text class="w98" x="194" y="16" font-size="11" fill="#808080">Apply</text>
    </g>
  </g>
</svg>'''

# ==================================================
# 4. SYSTEM PROPERTIES DIALOG (DARK CRT)
# ==================================================
sys_prop_dark_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 310" width="1200" height="310" role="img" aria-label="CRT System Diagnostics">
  <defs>
    <radialGradient id="spDarkVignette" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#0a180a" stop-opacity="0.1"/>
      <stop offset="90%" stop-color="#050a05" stop-opacity="0.75"/>
      <stop offset="100%" stop-color="#010301" stop-opacity="0.95"/>
    </radialGradient>
    <filter id="spGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <style>
    .crt { font-family: ui-monospace, "Courier New", monospace; font-size: 12px; fill: #00ff66; }
    .amber { font-family: ui-monospace, "Courier New", monospace; font-size: 11.5px; fill: #ffb000; }
    .dim { font-family: ui-monospace, "Courier New", monospace; font-size: 11px; fill: #1d7734; }
  </style>

  <rect width="1200" height="310" rx="8" fill="#141714" stroke="#252b25" stroke-width="2"/>
  <rect x="8" y="8" width="1184" height="294" rx="6" fill="#050e05"/>
  <rect x="8" y="8" width="1184" height="294" fill="url(#spDarkVignette)"/>

  <g filter="url(#spGlow)" transform="translate(36, 36)">
    <text class="dim" x="0" y="0">&#x250C;&#x2500;&#x2500;[ DIAGNOSTIC UTILITY: sys_info --verbose --verified ]&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2510;</text>

    <text class="crt" x="20" y="28" font-weight="bold">SYSTEM HOSTNAME  : PORAS-SYSTEMS-01 [POSIX / LINUX WORKSTATION]</text>
    <text class="crt" x="20" y="48">OPERATOR         : PORAS NAGAR (FULL-STACK DEVELOPER &amp; AI SYSTEMS ENGINEER)</text>
    <text class="crt" x="20" y="68">CREDENTIALS      : B.TECH COMPUTER SCIENCE (HONS. AI &amp; ML), AMITY UNIVERSITY</text>
    <text class="amber" x="20" y="88">CORE ENGINE 01   : LUMAVOICE (HINDI LIP-READING CNN-LSTM PHONEME CLASSIFIER)</text>
    <text class="amber" x="20" y="108">CORE ENGINE 02   : HOSPITAL WHATSAPP TRIAGE WEBHOOK (META CLOUD API / 142ms ACK)</text>
    <text class="amber" x="20" y="128">CORE ENGINE 03   : HIGH-THROUGHPUT SCRAPER BROKER (10,480 PG/MIN / RABBITMQ + REDIS)</text>
    <text class="amber" x="20" y="148">CORE ENGINE 04   : HERMES MULTI-AGENT AUTONOMOUS CI DOCUMENT PIPELINE</text>
    <text class="crt" x="20" y="168">STATUS           : ONLINE [UPTIME: 99.98%] • OPEN FOR FULL-TIME GLOBAL ROLES</text>
    <text class="dim" x="20" y="188">DISPATCH CHANNELS: poras9868@gmail.com | linkedin.com/in/poras-nagar-036886189</text>

    <text class="dim" x="0" y="214">&#x2514;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2518;</text>
    <text class="crt" x="20" y="238">ENTER 'reboot' TO RESET BUFFER • 'connect' TO INITIATE INTERVIEW SEQUENCE</text>
  </g>
</svg>'''

if __name__ == "__main__":
    write_svg("player-light.svg", player_light_svg)
    write_svg("player.svg", player_dark_svg)
    write_svg("sys_prop-light.svg", sys_prop_light_svg)
    write_svg("sys_prop.svg", sys_prop_dark_svg)
    print("All additional retro assets successfully generated and verified!")
