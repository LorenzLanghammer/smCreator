from camoufox.sync_api import Camoufox
import time

with Camoufox(
    geoip=True,
    block_webrtc=True
) as browser:
    page = browser.new_page()
    page.goto("https://example.com")

    



    while(True):
        time.sleep(1)
