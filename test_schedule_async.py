import sys
import os
import asyncio
# 添加项目根目录到sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from playwright.async_api import Playwright, async_playwright
from pages.login_page import LoginPage
from pages.schedule_page import SchedulePage


async def run(playwright: Playwright) -> None:
    # 启动浏览器，Jenkins环境使用headless模式
    import os
    headless = os.getenv('JENKINS_HOME') is not None
    browser = await playwright.chromium.launch(headless=headless, slow_mo=100)
    context = await browser.new_context()
    page = await context.new_page()

    try:
        # 创建页面实例
        login_page = LoginPage(page)
        schedule_page = SchedulePage(page)

        # 执行测试流程
        print("开始测试：登录操作")
        await login_page.navigate()
        await login_page.login("18994057385", "057385")

        print("开始测试：创建日程")
        await schedule_page.navigate_to_schedule()
        await schedule_page.create_schedule("test001", "111")

        print("开始测试：删除日程")
        await schedule_page.delete_schedule("test001")

        print("测试完成：所有操作执行成功！")

    except Exception as e:
        print(f"测试过程中发生错误: {e}")
        # 保存错误截图
        await page.screenshot(path="error_screenshot.png")
        raise
    finally:
        # 等待一下再关闭，确保所有操作完成
        await schedule_page.human_like_delay(1.0, 2.0)
        await context.close()
        await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == "__main__":
    asyncio.run(main())
