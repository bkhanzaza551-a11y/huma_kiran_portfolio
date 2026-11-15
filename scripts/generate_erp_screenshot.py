import os
from playwright.sync_api import sync_playwright

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Central ERP Mobile</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    body { background: #0f172a; color: #f8fafc; padding: 16px; padding-top: 24px; min-height: 100vh; }
    .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
    .badge { background: #2563eb; color: #fff; padding: 4px 10px; border-radius: 99px; font-size: 11px; font-weight: 600; letter-spacing: 0.05em; }
    .title { font-size: 22px; font-weight: 700; color: #fff; margin-top: 4px; }
    .sub { font-size: 12px; color: #94a3b8; }
    .metrics { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 20px; }
    .card { background: #1e293b; border: 1px solid #334155; border-radius: 14px; padding: 14px; }
    .card-label { font-size: 11px; color: #94a3b8; text-transform: uppercase; font-weight: 600; }
    .card-val { font-size: 20px; font-weight: 700; color: #fff; margin: 4px 0; }
    .card-trend { font-size: 11px; color: #10b981; font-weight: 600; }
    .chart-box { background: #1e293b; border: 1px solid #334155; border-radius: 14px; padding: 16px; margin-bottom: 20px; }
    .chart-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; }
    .chart-title { font-size: 14px; font-weight: 600; color: #f1f5f9; }
    .modules { display: flex; flex-direction: column; gap: 10px; }
    .mod-item { display: flex; align-items: center; justify-content: space-between; background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 12px 14px; }
    .mod-icon { width: 36px; height: 36px; border-radius: 10px; background: #2563eb; display: grid; place-items: center; font-size: 16px; margin-right: 12px; flex-shrink: 0; }
    .mod-info { flex: 1; }
    .mod-name { font-size: 14px; font-weight: 600; color: #fff; }
    .mod-sub { font-size: 11px; color: #94a3b8; }
    .status-dot { width: 8px; height: 8px; border-radius: 50%; background: #10b981; }
  </style>
</head>
<body>
  <div class="header">
    <div>
      <span class="badge">CENTRAL ERP v2.4</span>
      <div class="title">Enterprise Ops</div>
      <div class="sub">Centralized System Architecture</div>
    </div>
    <div style="width: 40px; height: 40px; border-radius: 50%; background: #3b82f6; display: grid; place-items: center; font-weight: 700; color: #fff;">HK</div>
  </div>

  <div class="metrics">
    <div class="card">
      <div class="card-label">Daily Workflows</div>
      <div class="card-val">12,480</div>
      <div class="card-trend">↑ 99.8% Sync Rate</div>
    </div>
    <div class="card">
      <div class="card-label">Inventory Balance</div>
      <div class="card-val">98.4%</div>
      <div class="card-trend">↑ Automated</div>
    </div>
  </div>

  <div class="chart-box">
    <div class="chart-head">
      <div class="chart-title">System Performance & Inflow</div>
      <span style="font-size: 11px; color: #38bdf8;">Real-Time</span>
    </div>
    <svg viewBox="0 0 320 90" style="width: 100%; height: 80px;">
      <defs>
        <linearGradient id="grad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.5"/>
          <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.0"/>
        </linearGradient>
      </defs>
      <path d="M0,70 Q40,30 80,45 T160,25 T240,40 T320,15 L320,90 L0,90 Z" fill="url(#grad)" />
      <path d="M0,70 Q40,30 80,45 T160,25 T240,40 T320,15" fill="none" stroke="#3b82f6" stroke-width="3" />
    </svg>
  </div>

  <div style="font-size: 12px; font-weight: 600; color: #94a3b8; text-transform: uppercase; margin-bottom: 10px; letter-spacing: 0.05em;">Integrated Core Modules</div>
  <div class="modules">
    <div class="mod-item">
      <div class="mod-icon">📊</div>
      <div class="mod-info">
        <div class="mod-name">Finance & Automated Ledger</div>
        <div class="mod-sub">Multi-Entity Balancing · Real-time</div>
      </div>
      <div class="status-dot"></div>
    </div>
    <div class="mod-item">
      <div class="mod-icon" style="background: #7c3aed;">📦</div>
      <div class="mod-info">
        <div class="mod-name">Inventory & Warehouse SCM</div>
        <div class="mod-sub">Barcode Tracking & Auto Restock</div>
      </div>
      <div class="status-dot"></div>
    </div>
    <div class="mod-item">
      <div class="mod-icon" style="background: #0d9488;">👥</div>
      <div class="mod-info">
        <div class="mod-name">HR & Operational Workforce</div>
        <div class="mod-sub">Shift Scheduling & Attendance</div>
      </div>
      <div class="status-dot"></div>
    </div>
    <div class="mod-item">
      <div class="mod-icon" style="background: #e11d48;">⚡</div>
      <div class="mod-info">
        <div class="mod-name">ERP Pipeline Automation</div>
        <div class="mod-sub">REST / Webhook Orchestration</div>
      </div>
      <div class="status-dot"></div>
    </div>
  </div>
</body>
</html>
"""

with open("public/projects/erp.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=True)
    page = browser.new_page(
        viewport={"width": 393, "height": 852},
        device_scale_factor=2
    )
    abs_path = os.path.abspath("public/projects/erp.html")
    page.goto(f"file:///{abs_path}")
    page.screenshot(path="public/projects/centralerp.jpg", type="jpeg", quality=92)
    browser.close()

print("Central ERP mobile screenshot generated successfully!")
