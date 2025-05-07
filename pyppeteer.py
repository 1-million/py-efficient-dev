import asyncio
from pyppeteer import connect, launch


async def main():
    # 连接到浏览器
    exe_path = 'C:\Program Files\Google\Chrome\Application/chrome.exe'
    # 设置代理服务器地址和端口
    proxy_server = 'socks5://127.0.0.1:10808'
    browser = await launch({'executablePath': exe_path, 'headless': False, 'slowMo': 30,'dumpio':True, 'autoClose':False,'args': ['--no-sandbox', '--window-size=1366,850', f'--proxy-server={proxy_server}']})
    print("已连接！")

    for i in range(3):
        # 创建一个新页面
        page = await browser.newPage()
        await page.setViewport({'width': 1366, 'height': 768})
        # 访问 youtube
        await page.goto("https://cnys.tv/vodplay-2250-1-9.html",timeout=0,waitUntil='domcontentloaded')
        # 获取页面内容
        content = await page.content()

        await page.close()

asyncio.run(main())