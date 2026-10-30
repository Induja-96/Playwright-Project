import pytest
from playwright.async_api import async_playwright
from playwright.sync_api import expect


# @pytest.mark.asyncio
# async def test_trace():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         context = await browser.new_context()
#         await context.tracing.start(
#             screenshots=True,
#             snapshots=True,
#             sources=True
#         )
#         try:
#             page = await context.new_page()
#             await page.goto("https://parabank.parasoft.com/parabank/register.htm")
#             username = "1213ran1dom123"
#             password = "abc@123"

#             await page.locator(
#                 'input[name="customer.firstName"]'
#             ).fill("abc")

#             await page.locator(
#                 'input[name="customer.lastName"]'
#             ).fill("a")

#             await page.locator(
#                 'input[name="customer.address.street"]'
#             ).fill("10 Test Street")

#             await page.locator(
#                 'input[name="customer.address.city"]'
#             ).fill("Bengaluru")

#             await page.locator(
#                 'input[name="customer.address.state"]'
#             ).fill("Karnataka")

#             await page.locator(
#                 'input[name="customer.address.zipCode"]'
#             ).fill("560001")

#             await page.locator(
#                 'input[name="customer.phoneNumber"]'
#             ).fill("9876543210")

#             await page.locator(
#                 'input[name="customer.ssn"]'
#             ).fill("123456789")

#             await page.locator(
#                 'input[name="customer.username"]'
#             ).fill(username)

#             await page.locator(
#                 'input[name="customer.password"]'
#             ).fill(password)

#             await page.locator(
#                 'input[name="repeatedPassword"]'
#             ).fill(password)

#             # STEP 3: Submit registration
#             await page.locator(
#                 'input[value="Register"]'
#             ).click()

#             # STEP 4: Validate registration result
#             await expect(
#                 page.locator("#rightPanel")
#             ).to_contain_text("Welcome")

#             print("UI registration successful:", username)

           
#         except Exception as e:
#             print(f"error is {e}")
#         finally:
#             await context.tracing.stop(
#                 path="/home/user/Videos/Playwright project/tracing1/trace2.zip"
#             )
#             await context.close()
 
import json
import subprocess
from pathlib import Path

import pytest
from playwright.async_api import async_playwright


# @pytest.mark.asyncio
# async def test_lighthousejson():
#     url = "https://parabank.parasoft.com/parabank/register.htm"

#     # Report directory and JSON file
#     report_dir = Path("/home/user/Videos/Playwright project/lighthouse/light_house")
#     report_dir.mkdir(parents=True, exist_ok=True)
#     report_file = report_dir / "lighthouse.json"

#     username = "1213ran1dom123"
#     password = "abc@123"

#     # STEP 1: Register user using Python Playwright
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)

#         try:
#             page = await browser.new_page()
#             await page.goto(url, wait_until="domcontentloaded")

#             fields = {
#                 'input[name="customer.firstName"]': "abc",
#                 'input[name="customer.lastName"]': "a",
#                 'input[name="customer.address.street"]': "10 Test Street",
#                 'input[name="customer.address.city"]': "Bengaluru",
#                 'input[name="customer.address.state"]': "Karnataka",
#                 'input[name="customer.address.zipCode"]': "560001",
#                 'input[name="customer.phoneNumber"]': "9876543210",
#                 'input[name="customer.ssn"]': "123456789",
#                 'input[name="customer.username"]': username,
#                 'input[name="customer.password"]': password,
#                 'input[name="repeatedPassword"]': password,
#             }

#             for selector, value in fields.items():
#                 await page.locator(selector).fill(value)

#             await page.locator('input[value="Register"]').click()
#             await page.wait_for_load_state("domcontentloaded")

#             print("Registration submitted")
#             print("Current URL:", page.url)

#         finally:
#             await browser.close()

#     # STEP 2: Run Lighthouse audit
#     try:
#         res = subprocess.run(
#             [
#                 "npx",
#                 "--yes",
#                 "lighthouse",
#                 url,
#                 "--chrome-flags=--headless",
#                 "--output=json",
#                 f"--output-path={report_file}",
#             ],
#             cwd=str(report_dir),
#             capture_output=True,
#             text=True,
#             timeout=180,
#             shell=False,
#         )

#         if res.stdout:
#             print("Lighthouse output:", res.stdout)

#         if res.returncode != 0:
#             print("Lighthouse error:")
#             print(res.stderr)
#             pytest.fail("Lighthouse audit failed")

#         # STEP 3: Read Lighthouse JSON report
#         with report_file.open(encoding="utf-8") as f:
#             json_data = json.load(f)

#         # STEP 4: Print audit scores
#         for name in (
#             "performance",
#             "accessibility",
#             "best-practices",
#             "seo",
#         ):
#             score = json_data["categories"][name]["score"]

#             if score is not None:
#                 print(f"{name}: {score * 100:.0f} / 100")
#             else:
#                 print(f"{name}: Score unavailable")

#         print("JSON report saved to:", report_file)

#     except subprocess.TimeoutExpired:
#         pytest.fail("Lighthouse timed out after 180 seconds")
        
# from pytest_check import check

# @pytest.mark.asyncio
# async def test_sanity_dom_check():
#     url = "https://parabank.parasoft.com/parabank/register.htm"
#     async with (async_playwright() as p):
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#         await page.goto(url)
#         title =await page.title()
#         print("title is not missing") if bool(title.strip()) else print("title is missing") #  bool("") False bool("sddd") true
#         check.is_true(bool(title.strip()),"title is missing")

#         # alt :-->
#         missing_alt = await page.locator("img:not([alt])").count()
#         print(missing_alt)
#         check.equal(missing_alt,0,f"{missing_alt} num of img missing alt attribute")

#         main_count = await page.locator("main").count()
#         print(main_count)
#         check.equal(main_count, 0, f"{main_count} main landlandmarks missing")    
        
# from pytest_check import check

# @pytest.mark.asyncio
# async def test_sanity_dom_check():
#     url = "https://demowebshop.tricentis.com/"
#     async with (async_playwright() as p):
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#         await page.goto(url)
#         title =await page.title()
#         print("title is not missing") if bool(title.strip()) else print("title is missing") #  bool("") False bool("sddd") true
#         check.is_true(bool(title.strip()),"title is missing") # stop

#         # alt :-->
#         missing_alt = await page.locator("img:not([alt])").count()
#         print(missing_alt)
#         check.equal(missing_alt,0,f"{missing_alt} num of img missing alt attribute")

#         main_count = await page.locator("main").count()
#         print(main_count)
#         check.equal(main_count>1, f"{main_count} main land landmarks missing")

#         # load axe-core js
#         axe_path = Path("node_modules/axe-core/axe.min.js")
#         check.is_true(
#             axe_path.exists(),
#             "Install axe-core using npm"
#         )
#         # stop the accessiblity
#         if not axe_path.exists():
#             return
#         await page.add_script_tag(path=str(axe_path))

#         # run axe-core accessablity scan
#         resu = await page.evaluate(
#             """
#             async ()=> {
#               return await axe.run(document);
#             }
#             """
#         )
#         violations = resu["violations"]

#         for i in violations:
#             print(
#                 f"Rule : {i['id']} "
#                 f"Impact :  {i['impact']}"
#                 f"Description:{i['description']}"
#             )

#             for j in i["nodes"]:
#                 print("ele affected : {j['target']}")
#                 print("Details: {j['failureSummary']}" )

#         check.equal(
#             len(violations),0,f"Accessibility violations : {len(violations)}"
#         )

#     await browser.close()    
    
# @pytest.mark.asyncio
# async def test_screenshots_full_page():
#     url = "https://demowebshop.tricentis.com/"
#     async with (async_playwright() as p):
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#         await page.goto(url)
#         title =await page.title()
#         print(title)
#         await page.screenshot(path= "/home/user/Videos/Playwright project/photos1/demo.png",full_page=True)     
@pytest.mark.asyncio
async def test_screenshots_full_page():
    url = "https://demowebshop.tricentis.com/"
    async with (async_playwright() as p):
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        title =await page.title()
        print(title)
        # await page.screenshot(path= "D:/AI/Python_playwright/photos/demo1.png")
        ele = page.locator("input#small-searchterms")
        await ele.screenshot(path="/home/user/Videos/Playwright project/photos1/ele1.png")   