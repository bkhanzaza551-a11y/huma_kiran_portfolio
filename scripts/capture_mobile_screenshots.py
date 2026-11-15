import os
import time
from playwright.sync_api import sync_playwright

os.makedirs("public/projects", exist_ok=True)

targets = [
    {
        "id": "salonnest",
        "url": "http://salonnest.in/",
    },
    {
        "id": "noamskin",
        "url": "https://noamskin.com/",
    },
    {
        "id": "forextutor",
        "url": "https://www.forextutoracademy.com/",
    },
    {
        "id": "raysbus",
        "url": "https://rays-international-bus-frontend.vercel.app/",
    },
    {
        "id": "wellnexpk",
        "url": "https://wellnexpk.com/",
    },
    {
        "id": "khadlaj",
        "url": "https://khadlaj-perfumes.com/",
    },
]

# We map hosts explicitly so any local DNS issue never fails navigation
host_rules = (
    "MAP noamskin.com 217.21.91.178, "
    "MAP khadlaj-perfumes.com 23.227.38.32, "
    "MAP www.khadlaj-perfumes.com 23.227.38.32, "
    "MAP forextutoracademy.com 185.16.39.50, "
    "MAP www.forextutoracademy.com 185.16.39.50, "
    "MAP wellnexpk.com 185.16.39.50, "
    "MAP www.wellnexpk.com 185.16.39.50"
)

with sync_playwright() as p:
    browser = p.chromium.launch(
        channel="chrome",
        headless=True,
        args=[
            f"--host-rules={host_rules}",
            "--ignore-certificate-errors",
            "--no-sandbox"
        ]
    )
    context = browser.new_context(
        viewport={"width": 393, "height": 852},
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
        is_mobile=True,
        has_touch=True,
        device_scale_factor=2
    )

    for target in targets:
        tid = target["id"]
        url = target["url"]
        out_path = f"public/projects/{tid}.jpg"
        print(f"Capturing {tid} from {url}...")
        try:
            page = context.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=25000)
            page.wait_for_timeout(4000)
            page.screenshot(path=out_path, type="jpeg", quality=92)
            print(f"Successfully saved {out_path} ({os.path.getsize(out_path)} bytes)")
            page.close()
        except Exception as e:
            print(f"Error capturing {tid}: {e}")

    browser.close()
print("All done!")
