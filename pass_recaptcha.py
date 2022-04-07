from bs4 import BeautifulSoup as bs
import requests
from io import BytesIO
from .transcript import *

#captcha
link_audio_type = 'href'
parser_bs = 'lxml'
iframe_title = 'iframe[title="o desafio reCAPTCHA expira em dois minutos"]'
captcha_audio_option = 'button[id="recaptcha-audio-button"]'
download_audio_class = 'rc-audiochallenge-tdownload-link'
input_captcha = 'input[id="audio-response"]'
verify_bcaptcha = 'button[id="recaptcha-verify-button"]'
audio_wait = "[class='rc-audiochallenge-control']"


async def recaptcha_pass(page):
    """
    Realiza o recaptcha, pela opção de audio.
    """
    print("recaptcha")

    iframe = await page.locator(iframe_title).get_attribute('name')
    print(iframe)
    frame = page.frame(iframe)
    print(frame)
    await frame.click(captcha_audio_option)
    await page.wait_for_timeout(5000)

    page_content = await frame.content()
    soup = bs(page_content,parser_bs)

    link_content = soup.find(class_=download_audio_class, href = True)
    link = link_content.get(link_audio_type)

    r = requests.get(link)
    download_audio=BytesIO(r.content)
    transcr = transcription(download_audio)
    print(f"Transcription: {transcr}")

    await frame.fill(input_captcha, value = transcr)
    await frame.click(verify_bcaptcha)
    await frame.wait_for_load_state()
    await page.wait_for_timeout(3000)