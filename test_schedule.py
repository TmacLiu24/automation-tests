import sys
import os
# 添加项目根目录到sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from playwright.sync_api import Playwright, sync_playwright
from pages.login_page import LoginPage
from pages.schedule_page import SchedulePage


def run(playwright: Playwright) -> None:
    # 启动浏览器，添加slow_mo使所有操作变慢
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context()
    page = context.new_page()

    try:
        # 创建页面实例
        login_page = LoginPage(page)
        schedule_page = SchedulePage(page)

        # 执行测试流程
        print("开始测试：登录操作")
        login_page.navigate()
        login_page.login("18994057385", "057385")

        print("开始测试：创建日程")
        schedule_page.navigate_to_schedule()
        schedule_page.create_schedule("test001", "111")

        print("开始测试：删除日程")
        schedule_page.delete_schedule("test001")

        print("测试完成：所有操作执行成功！")

    except Exception as e:
        print(f"测试过程中发生错误: {e}")
        # 保存错误截图
        page.screenshot(path="error_screenshot.png")
        raise
    finally:
        # 等待一下再关闭，确保所有操作完成
        schedule_page.human_like_delay(1.0, 2.0)
        context.close()
        browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)