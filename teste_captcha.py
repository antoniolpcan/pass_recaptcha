from playwright.async_api import async_playwright
import asyncio
from pass_recaptcha import recaptcha_pass

async def main():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()

    i = 0

    while(i<1000):
        await page.goto('https://patrickhlauke.github.io/recaptcha/')
        await page.click("iframe[title='reCAPTCHA']")
        await recaptcha_pass(page)
        i = i + 1
        print(i)

    browser.close()
    playwright.stop()

asyncio.run(main())