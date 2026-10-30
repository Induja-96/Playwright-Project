from playwright.async_api import async_playwright
import pytest
import asyncio
# @pytest.mark.asyncio
# async def test_slow_network():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#         # slow
#         async def slowapi(route):
#             print(route.request.url)
#             await asyncio.sleep(3)
#             await route.continue_()
#         await page.route(
#             "**/api/**",slowapi
#         )

#         await page.goto("https://demowebshop.tricentis.com/")
#         await page.wait_for_timeout(5000)
#         await browser.close()
# @pytest.mark.asyncio
# async def test_slow_network():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#         # slow
#         async def modify_req(route):
#             print(route.request.url)
#             req = route.request
#             header = await req.all_headers()
#             # custom herder
#             header["x-test-client"] = "playwright-Async"
#             # post with playload
#             if req.method == "POST" and req.post_data:
#                 try:
#                     payload =json.load(req.post_data)
#                     if isinstance(payload, dict):
#                         print(payload)
#                         if "quantity" in payload:
#                             payload["quantity"] = 5

#                             update_playload = json.dumps(payload)
#                             print(update_playload)
#                             await route.continue_(
#                                 headers=header,
#                                 post_data=update_playload
#                             )
#                             return
#                 except json.JSONDecodeError:
#                     print("req body not json")

#             await route.continue_(headers=header)
#                     # {"key" : "value }
#         await page.route(
#             "**/api/**",modify_req
#         )
# # api :-->
#         await page.goto("https://demowebshop.tricentis.com/")
#         await page.wait_for_timeout(5000)
#         await browser.close()       
        
        
  #step 6 .Capture network traffic for performance analysis(har)
# @pytest.mark.asyncio
# async def test_slow_network():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         context = await browser.new_context(
#             record_har_path= "network_traffic.har"
#         )
#         page = await context.new_page()
#         async def log_res(response):
#            req =  response.request
#            timings = req.timing

#            st =  timings.get("startTime" , 0)
#            et = timings.get("endTime" , -1)

#            if et >= 0:
#                 duration = et - st
#                 print(
#                     f"status : {response.status}",
#                     f"Time : {duration:.2f} ms ",
#                     f"url : {req.url}"
#                 )

#         page.on("response" ,
#                 lambda  response : asyncio.create_task(log_res(response)))
#         await page.goto("https://demowebshop.tricentis.com/")
#         await page.wait_for_timeout(5000)
#         await context.close()
#         await browser.close()      

#1. Measuring page performance metrics
@pytest.mark.asyncio
async def test_slow_network():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        response = await page.goto("https://demowebshop.tricentis.com/")
        await page.wait_for_timeout(5000)
        assert response is not None
        assert response.status < 400
        metrics = await page.evaluate("""() => {
            const timing = performance.getEntriesByType(
                'navigation'
            )[0];

            return {
                domContentLoaded:
                    timing.domContentLoadedEventEnd -
                    timing.startTime,
                loadEvent:
                    timing.loadEventEnd - timing.startTime,
                responseTime:
                    timing.responseEnd - timing.requestStart,
                resourceCount:
                performance.getEntriesByType('resource').length
            };
        }""")

        print("http status" , response.status)
        print(metrics)