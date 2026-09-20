import os
import xml.etree.ElementTree as ET

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")

def write_and_verify(filename, content):
    path = os.path.join(ASSETS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    # Verify XML
    try:
        ET.parse(path)
        print(f"VERIFIED XML OK: {filename} ({len(content)} bytes)")
    except Exception as e:
        print(f"ERROR XML INVALID: {filename} -> {e}")
        raise e

# ==============================================================================
# 1. RETRO TASKBAR (WIN98 LIGHT & CRT TMUX DARK)
# ==============================================================================

taskbar_win98 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 42" width="1200" height="42" role="navigation" aria-label="Windows 98 Taskbar">
  <defs>
    <clipPath id="tb_clip"><rect width="1200" height="42" rx="2"/></clipPath>
  </defs>
  <style>
    .w98-btn { font-family: "MS Sans Serif", Tahoma, -apple-system, sans-serif; font-size: 11.5px; font-weight: bold; }
    .w98-tab { font-family: "MS Sans Serif", Tahoma, -apple-system, sans-serif; font-size: 11px; }
    .w98-time { font-family: "MS Sans Serif", Tahoma, -apple-system, sans-serif; font-size: 11px; }
  </style>
  <g clip-path="url(#tb_clip)">
    <!-- Taskbar Body -->
    <rect width="1200" height="42" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
    <!-- Top White Bevel Line -->
    <line x1="0" y1="1" x2="1200" y2="1" stroke="#ffffff" stroke-width="2"/>
    <line x1="0" y1="2" x2="1200" y2="2" stroke="#dfdfdf" stroke-width="1"/>

    <!-- START BUTTON (Raised 3D Bevel) -->
    <g transform="translate(4, 4)">
      <rect width="86" height="32" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
      <line x1="1" y1="1" x2="85" y2="1" stroke="#ffffff" stroke-width="2"/>
      <line x1="1" y1="1" x2="1" y2="31" stroke="#ffffff" stroke-width="2"/>
      <line x1="2" y1="30" x2="84" y2="30" stroke="#808080" stroke-width="2"/>
      <line x1="84" y1="2" x2="84" y2="30" stroke="#808080" stroke-width="2"/>
      
      <!-- Windows 4-Color Flag Icon -->
      <g transform="translate(8, 7)">
        <rect x="0" y="0" width="7" height="7" fill="#e74c3c"/>
        <rect x="9" y="0" width="7" height="7" fill="#2ecc71"/>
        <rect x="0" y="9" width="7" height="7" fill="#3498db"/>
        <rect x="9" y="9" width="7" height="7" fill="#f1c40f"/>
      </g>
      <text class="w98-btn" x="30" y="21" fill="#000000">Start</text>
    </g>

    <!-- Divider Handle -->
    <line x1="96" y1="6" x2="96" y2="36" stroke="#808080" stroke-width="1"/>
    <line x1="97" y1="6" x2="97" y2="36" stroke="#ffffff" stroke-width="1"/>

    <!-- Running Task Tabs -->
    <!-- Tab 1: Profile (Active - Sunken Inset) -->
    <g transform="translate(104, 5)">
      <rect width="180" height="30" fill="#dfdfdf" stroke="#808080" stroke-width="1"/>
      <line x1="0" y1="0" x2="179" y2="0" stroke="#000000"/>
      <line x1="0" y1="0" x2="0" y2="29" stroke="#000000"/>
      <line x1="1" y1="29" x2="179" y2="29" stroke="#ffffff"/>
      <line x1="179" y1="1" x2="179" y2="29" stroke="#ffffff"/>
      <rect x="8" y="7" width="16" height="16" fill="#000080"/>
      <text class="w98-btn" x="30" y="19" fill="#000080">📁 PROFILE.EXE</text>
    </g>

    <!-- Tab 2: Systems (Raised) -->
    <g transform="translate(290, 5)">
      <rect width="180" height="30" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
      <line x1="1" y1="1" x2="179" y2="1" stroke="#ffffff" stroke-width="1.5"/>
      <line x1="1" y1="1" x2="1" y2="29" stroke="#ffffff" stroke-width="1.5"/>
      <line x1="2" y1="28" x2="178" y2="28" stroke="#808080" stroke-width="1.5"/>
      <line x1="178" y1="2" x2="178" y2="28" stroke="#808080" stroke-width="1.5"/>
      <text class="w98-tab" x="12" y="19" fill="#000000">⚡ SYSTEMS (4 PROD)</text>
    </g>

    <!-- Tab 3: Device Manager (Raised) -->
    <g transform="translate(476, 5)">
      <rect width="170" height="30" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
      <line x1="1" y1="1" x2="169" y2="1" stroke="#ffffff" stroke-width="1.5"/>
      <line x1="1" y1="1" x2="1" y2="29" stroke="#ffffff" stroke-width="1.5"/>
      <line x1="2" y1="28" x2="168" y2="28" stroke="#808080" stroke-width="1.5"/>
      <line x1="168" y1="2" x2="168" y2="28" stroke="#808080" stroke-width="1.5"/>
      <text class="w98-tab" x="12" y="19" fill="#000000">🛠️ DEVICE MANAGER</text>
    </g>

    <!-- Tab 4: Telemetry Monitor (Raised) -->
    <g transform="translate(652, 5)">
      <rect width="170" height="30" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
      <line x1="1" y1="1" x2="169" y2="1" stroke="#ffffff" stroke-width="1.5"/>
      <line x1="1" y1="1" x2="1" y2="29" stroke="#ffffff" stroke-width="1.5"/>
      <line x1="2" y1="28" x2="168" y2="28" stroke="#808080" stroke-width="1.5"/>
      <line x1="168" y1="2" x2="168" y2="28" stroke="#808080" stroke-width="1.5"/>
      <text class="w98-tab" x="12" y="19" fill="#000000">📊 SYSTEM MONITOR</text>
    </g>

    <!-- SYSTEM TRAY (Sunken Inset Panel on Right) -->
    <g transform="translate(1008, 5)">
      <rect width="186" height="31" fill="#c0c0c0" stroke="#808080" stroke-width="1"/>
      <line x1="0" y1="0" x2="185" y2="0" stroke="#404040"/>
      <line x1="0" y1="0" x2="0" y2="30" stroke="#404040"/>
      <line x1="1" y1="30" x2="185" y2="30" stroke="#ffffff"/>
      <line x1="185" y1="1" x2="185" y2="30" stroke="#ffffff"/>

      <!-- Speaker / Modem Activity -->
      <polygon points="12,18 16,18 22,23 22,9 16,14 12,14" fill="#000000"/>
      <!-- Flashing Modem LEDs -->
      <circle cx="34" cy="16" r="3" fill="#008000"/>
      <circle cx="43" cy="16" r="3" fill="#00ff00"/>

      <!-- Live Clock -->
      <text class="w98-time" x="62" y="20" fill="#000000">UTC+5:30 (IST)</text>
    </g>
  </g>
</svg>"""

taskbar_crt = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 42" width="1200" height="42" role="navigation" aria-label="CRT Phosphor Status Bar">
  <defs>
    <filter id="tb_glow">
      <feGaussianBlur stdDeviation="1.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <style>
    .crt-tab { font-family: ui-monospace, "Courier New", monospace; font-size: 11.5px; fill: #00ff66; }
    .amber { font-family: ui-monospace, "Courier New", monospace; font-size: 11.5px; fill: #ffb000; }
    .dim { font-family: ui-monospace, "Courier New", monospace; font-size: 11px; fill: #1d7734; }
  </style>
  <rect width="1200" height="42" rx="4" fill="#090d09" stroke="#1f2d1f" stroke-width="2"/>
  <g filter="url(#tb_glow)" transform="translate(18, 25)">
    <text class="amber" x="0" y="0">[TMUX: workstation]</text>
    <text class="crt" x="160" y="0">[0:profile*]</text>
    <text class="crt" x="250" y="0">[1:systems]</text>
    <text class="crt" x="340" y="0">[2:drivers]</text>
    <text class="crt" x="430" y="0">[3:telemetry]</text>
    <text class="crt" x="530" y="0">[4:mail]</text>

    <!-- Right Telemetry Status -->
    <text class="dim" x="840" y="0">CPU: 14% | 10k pg/m | IST 16:20 | ● ONLINE</text>
  </g>
</svg>"""

# ==============================================================================
# 2. RETRO MARQUEE TICKER (WIN98 LIGHT & CRT DARK) - LOOPHOLE #19
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

  <!-- Sunken Inset Panel -->
  <rect width="1200" height="36" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
  <line x1="1" y1="1" x2="1199" y2="1" stroke="#ffffff"/>
  <line x1="1" y1="1" x2="1" y2="35" stroke="#ffffff"/>

  <!-- Inset Ticker Box -->
  <rect x="4" y="4" width="1192" height="28" fill="#ffffea" stroke="#808080" stroke-width="1"/>
  <line x1="4" y1="4" x2="1195" y2="4" stroke="#404040"/>
  <line x1="4" y1="4" x2="4" y2="31" stroke="#404040"/>

  <g clip-path="url(#tk_clip)">
    <g class="ticker-scroll">
      <text class="ticker-font" x="0" y="22">
        📢 [OTC VALUATION ENGINE]: Live price discovery running • [B-TREE TIME-SERIES]: sub-15ms reads • ⚡ [SCRAPER CLUSTER]: 10,480 pages/min fan-out • 💬 [TRIAGE GATEWAY]: Meta WhatsApp Cloud API 142ms ack • 🤖 [HERMES AGENT]: Multi-agent CI document synthesis • 🎓 [EDUCATION]: B.Tech CSE (Hons. AI &amp; ML) Amity University • 💼 [AVAILABILITY]: Open to Global AI &amp; Distributed Backend Roles
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
        &gt;&gt;&gt; [OTC_VALUATION]: STREAMING BID/ASK DEPTH &gt;&gt;&gt; [SCRAPER_QUEUE]: 0 DROPPED RECORDS &gt;&gt;&gt; [TRIAGE_DISPATCH]: MONGO_SESSION_LOCKED &gt;&gt;&gt; [HERMES_CI]: DOCX/PPTX SYNTHESIS OK &gt;&gt;&gt; [COMMITS]: VERIFIED &gt;&gt;&gt; [STATUS]: READY FOR GLOBAL ROLES &gt;&gt;&gt;
      </text>
    </g>
  </g>
</svg>"""

# ==============================================================================
# 3. RETRO CONTACT (WIN98 OUTLOOK EXPRESS 5.0 & CRT SENDMAIL CLIENT)
# ==============================================================================

contact_win98 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 280" width="1200" height="280" role="img" aria-label="Outlook Express 5.0 Contact Form">
  <defs>
    <linearGradient id="oe_tb" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#000080"/><stop offset="100%" stop-color="#1084d0"/>
    </linearGradient>
    <clipPath id="oe_cp"><rect width="1200" height="280" rx="4"/></clipPath>
  </defs>
  <style>
    .w98 { font-family: "MS Sans Serif", Tahoma, -apple-system, sans-serif; font-size: 11.5px; }
    .w98-bold { font-family: "MS Sans Serif", Tahoma, -apple-system, sans-serif; font-size: 11.5px; font-weight: bold; }
    .mono { font-family: ui-monospace, "Courier New", monospace; font-size: 12px; }
  </style>

  <g clip-path="url(#oe_cp)">
    <!-- Main Window Outer Frame -->
    <rect width="1200" height="280" fill="#c0c0c0" stroke="#000000" stroke-width="1"/>
    <line x1="1" y1="1" x2="1199" y2="1" stroke="#ffffff" stroke-width="2"/>
    <line x1="1" y1="1" x2="1" y2="279" stroke="#ffffff" stroke-width="2"/>
    <line x1="2" y1="278" x2="1198" y2="278" stroke="#808080" stroke-width="2"/>
    <line x1="1198" y1="2" x2="1198" y2="278" stroke="#808080" stroke-width="2"/>

    <!-- Title Bar -->
    <g transform="translate(4, 4)">
      <rect width="1192" height="22" fill="url(#oe_tb)"/>
      <text class="w98-bold" x="8" y="15" fill="#ffffff">New Message - [To: Poras Nagar &lt;poras9868@gmail.com&gt;]</text>
      <!-- Buttons -->
      <g transform="translate(1146, 2)">
        <rect x="0" y="0" width="18" height="17" fill="#c0c0c0" stroke="#000000"/>
        <line x1="1" y1="1" x2="17" y2="1" stroke="#ffffff"/><text class="w98-bold" x="5" y="12">_</text>
        <rect x="22" y="0" width="18" height="17" fill="#c0c0c0" stroke="#000000"/>
        <line x1="23" y1="1" x2="39" y2="1" stroke="#ffffff"/><path d="M26 3 L34 12 M34 3 L26 12" stroke="#000000" stroke-width="2"/>
      </g>
    </g>

    <!-- Menu Bar -->
    <g transform="translate(10, 30)">
      <text class="w98" x="0" y="14"><tspan text-decoration="underline">F</tspan>ile</text>
      <text class="w98" x="32" y="14"><tspan text-decoration="underline">E</tspan>dit</text>
      <text class="w98" x="64" y="14"><tspan text-decoration="underline">V</tspan>iew</text>
      <text class="w98" x="100" y="14"><tspan text-decoration="underline">I</tspan>nsert</text>
      <text class="w98" x="144" y="14"><tspan text-decoration="underline">F</tspan>ormat</text>
      <text class="w98" x="194" y="14"><tspan text-decoration="underline">T</tspan>ools</text>
      <text class="w98" x="236" y="14"><tspan text-decoration="underline">M</tspan>essage</text>
      <text class="w98" x="296" y="14"><tspan text-decoration="underline">H</tspan>elp</text>
    </g>
    <line x1="4" y1="48" x2="1196" y2="48" stroke="#808080"/>
    <line x1="4" y1="49" x2="1196" y2="49" stroke="#ffffff"/>

    <!-- Outlook Express Toolbar Buttons -->
    <g transform="translate(10, 54)">
      <!-- Send Button -->
      <rect x="0" y="0" width="70" height="26" fill="#c0c0c0" stroke="#000000"/>
      <line x1="1" y1="1" x2="69" y2="1" stroke="#ffffff"/><text class="w98-bold" x="14" y="17" fill="#000080">✉️ Send</text>

      <!-- Cut -->
      <rect x="76" y="0" width="56" height="26" fill="#c0c0c0" stroke="#000000"/>
      <line x1="77" y1="1" x2="131" y2="1" stroke="#ffffff"/><text class="w98" x="90" y="17">✂️ Cut</text>

      <!-- Copy -->
      <rect x="136" y="0" width="60" height="26" fill="#c0c0c0" stroke="#000000"/>
      <line x1="137" y1="1" x2="195" y2="1" stroke="#ffffff"/><text class="w98" x="148" y="17">📋 Copy</text>

      <!-- Attach -->
      <rect x="200" y="0" width="70" height="26" fill="#c0c0c0" stroke="#000000"/>
      <line x1="201" y1="1" x2="269" y2="1" stroke="#ffffff"/><text class="w98" x="210" y="17">📎 Attach</text>
    </g>
    <line x1="4" y1="86" x2="1196" y2="86" stroke="#808080"/>

    <!-- Header Fields (Sunken Inset Panels) -->
    <g transform="translate(14, 94)">
      <!-- To -->
      <text class="w98-bold" x="0" y="18">To:</text>
      <rect x="64" y="4" width="1108" height="22" fill="#ffffff" stroke="#808080"/>
      <text class="mono" x="72" y="19" fill="#000080" font-weight="bold">poras9868@gmail.com  (Click to compose email)</text>

      <!-- Cc -->
      <text class="w98-bold" x="0" y="44">Cc:</text>
      <rect x="64" y="30" width="1108" height="22" fill="#ffffff" stroke="#808080"/>
      <text class="mono" x="72" y="45" fill="#000000">https://linkedin.com/in/poras-nagar-036886189</text>

      <!-- Subject -->
      <text class="w98-bold" x="0" y="70">Subject:</text>
      <rect x="64" y="56" width="1108" height="22" fill="#ffffff" stroke="#808080"/>
      <text class="mono" x="72" y="71" fill="#404040">Engineering Inquiry / AI &amp; Distributed Backend Collaboration</text>
    </g>

    <!-- Message Body (Sunken White Paper) -->
    <g transform="translate(14, 180)">
      <rect width="1172" height="66" fill="#ffffff" stroke="#808080"/>
      <line x1="1" y1="1" x2="1171" y2="1" stroke="#404040"/>
      <text class="mono" x="16" y="26" fill="#000000">"Fastest way to reach me is email. I read everything; I answer anything with a concrete technical question in it."</text>
      <text class="mono" x="16" y="48" fill="#808080">&gt; Available for applied AI, distributed queue pipelines, and quantitative equity backend roles.</text>
    </g>

    <!-- Status Bar -->
    <g transform="translate(14, 252)">
      <rect width="1172" height="20" fill="#c0c0c0" stroke="#808080"/>
      <text class="w98" x="8" y="14">Dial-Up Networking: Connected at 56,000 bps • SMTP Server Ready (smtp.gmail.com)</text>
    </g>
  </g>
</svg>"""

contact_crt = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 280" width="1200" height="280" role="img" aria-label="CRT Sendmail Console">
  <defs>
    <filter id="mail_glow">
      <feGaussianBlur stdDeviation="1.8" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <style>
    .crt { font-family: ui-monospace, "Courier New", monospace; font-size: 12px; fill: #00ff66; }
    .amber { font-family: ui-monospace, "Courier New", monospace; font-size: 12px; fill: #ffb000; }
    .dim { font-family: ui-monospace, "Courier New", monospace; font-size: 11px; fill: #1d7734; }
  </style>

  <rect width="1200" height="280" rx="8" fill="#141714" stroke="#252b25" stroke-width="3"/>
  <rect x="8" y="8" width="1184" height="264" rx="6" fill="#040804"/>

  <g filter="url(#mail_glow)" transform="translate(36, 36)">
    <text class="amber" x="0" y="0" font-weight="bold">SENDMAIL DAEMON / INTERACTION CONSOLE - PORAS NAGAR</text>
    <text class="dim" x="0" y="18">PROTOCOL: RFC 821 / SMTP ENCRYPTED • PORT: 587 (TLS) • STATUS: LISTENING</text>
    <text class="crt" x="0" y="38">═════════════════════════════════════════════════════════════════════════════════════════════════</text>

    <g transform="translate(0, 60)">
      <text class="crt" x="0" y="0">&gt; RECIPIENT  : <tspan fill="#ffb000" font-weight="bold">poras9868@gmail.com</tspan> (Click to send email)</text>
      <text class="crt" x="0" y="24">&gt; NETWORK    : https://linkedin.com/in/poras-nagar-036886189</text>
      <text class="crt" x="0" y="48">&gt; PORTFOLIO  : https://porasnagar.github.io</text>
      <text class="crt" x="0" y="72">&gt; NOTE       : Fastest way to reach me is email. All technical inquiries answered line-by-line.</text>
      <text class="crt" x="0" y="96">&gt; SCOPE      : Open to AI engineering, distributed queue workers, and quantitative backends.</text>
    </g>

    <text class="dim" x="0" y="196">─────────────────────────────────────────────────────────────────────────────────────────</text>
    <text class="dim" x="0" y="214">[CONNECTION POOL: 200 OK] [DAEMON UPTIME: 300+ DAYS] [ENCRYPTION: VERIFIED]</text>
  </g>
</svg>"""

def main():
    print("Generating comprehensive retro suite...")
    write_and_verify("taskbar-light.svg", taskbar_win98)
    write_and_verify("taskbar.svg", taskbar_crt)
    write_and_verify("ticker-light.svg", ticker_win98)
    write_and_verify("ticker.svg", ticker_crt)
    write_and_verify("contact-light.svg", contact_win98)
    write_and_verify("contact.svg", contact_crt)
    print("Retro suite generated and verified successfully!")

if __name__ == "__main__":
    main()
