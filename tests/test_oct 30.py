from pathlib import Path
from PIL import Image, ImageChops
import pytest
from playwright.async_api import async_playwright


BASELINE = Path("screenshots/baseline.png")
ACTUAL = Path("screenshots/actual.png")
DIFF = Path("screenshots/diff.png")


@pytest.mark.asyncio
async def test_visual_regression():
   BASELINE.parent.mkdir(parents=True, exist_ok=True)
   async with async_playwright() as p:
       browser = await p.chromium.launch()
       page = await browser.new_page(
           viewport={"width": 1366, "height": 768},
           device_scale_factor=1
       )
       await page.goto(
           "https://www.amazon.in/",
           wait_until="load"
       )
       await page.screenshot(path=str(ACTUAL), full_page=True)
       await browser.close()


   assert BASELINE.exists(), (
       "Baseline missing. Capture and approve a reference image first."
   )


   with Image.open(BASELINE) as img1, Image.open(ACTUAL) as img2:
       baseline = img1.convert("RGB")
       actual = img2.convert("RGB")


       if baseline.size != actual.size:
           pytest.fail(
               f"Image dimensions differ: "
               f"{baseline.size} vs {actual.size}"
           )


       diff = ImageChops.difference(baseline, actual)
       changed_pixels = sum(
           1 for pixel in diff.getdata() if pixel != (0, 0, 0)
       )
       total_pixels = baseline.width * baseline.height
       difference_ratio = changed_pixels / total_pixels


       diff.save(DIFF)


       print(f"Changed pixels: {changed_pixels}")
       print(f"Difference ratio: {difference_ratio:.4%}")


       assert difference_ratio <= 0.01, (
           f"Visual difference exceeds 1%: "
           f"{difference_ratio:.4%}"
       )