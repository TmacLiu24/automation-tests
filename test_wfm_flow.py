"""
WFM 自动化测试 - 使用 Page Object Model 模式
"""
import sys
import os

# 添加项目根目录到 sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import io
from playwright.sync_api import sync_playwright
from pages.login_page_sync import LoginPage
#from pages.wfm_home_page import WFMHomePage

# Fix encoding for Windows
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 配置
BASE_URL = "https://wfm-web.warmheart.top/WFM-admin"
LOGIN_URL = f"{BASE_URL}/index.html#/Login"
USERNAME = "18994057385"
PASSWORD = "057385"


def run():
    """执行 WFM 自动化测试"""
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()

        try:
            # ===== 初始化页面对象 =====
            login_page = LoginPage(page)
            wfm_home = WFMHomePage(page)

            # ===== 1. 登录 =====
            print("[Step 1/10] 登录...")
            login_page.navigate()
            login_page.login(USERNAME, PASSWORD)

            # 验证登录成功
            wfm_home.verify_login_success()
            print(f"[OK] 登录成功，当前URL: {page.url}")

            # ===== 2. 点击任务项目 =====
            print("[Step 2/10] 点击任务项目...")
            wfm_home.click_task_item("【测试部门-2月第2周-项目汇总】功能优化点测试")

            # ===== 3. 点击返回按钮 =====
            print("[Step 3/10] 点击返回按钮...")
            wfm_home.click_back_button()

            # 处理离开弹窗
            wfm_home.handle_leave_popup()

            # ===== 4. 点击前往查看 =====
            print("[Step 4/10] 点击前往查看...")
            wfm_home.click_view_more()

            # ===== 5. 点击修改任务 =====
            print("[Step 5/10] 点击修改任务...")
            wfm_home.click_edit_task()

            # ===== 6. 返回 =====
            print("[Step 6/10] 返回...")
            wfm_home.click_back_button()
            wfm_home.handle_leave_popup()

            # ===== 7. 点击TALK =====
            print("[Step 7/10] 点击TALK...")
            wfm_home.click_talk_tab(times=2)

            # ===== 8. 点击性能测试任务 =====
            print("[Step 8/10] 点击性能测试任务...")
            wfm_home.click_task_by_name("性能测试-压力测试")

            # ===== 9. 点击评论 =====
            print("[Step 9/10] 点击评论...")
            wfm_home.click_comment("评论 1")

            # ===== 10. 点击修改按钮 =====
            print("[Step 10/10] 点击修改按钮...")
            wfm_home.click_edit_button()
            wfm_home.click_title_input()
            wfm_home.click_cancel()

            # 返回
            wfm_home.click_back_button()

            print("\n[SUCCESS] 所有测试步骤执行完成！")

        except Exception as e:
            print(f"\n[ERROR] 测试失败: {e}")
            page.screenshot(path="error_screenshot.png")
            print("已保存错误截图: error_screenshot.png")
            raise
        finally:
            # 等待一下再关闭
            page.wait_for_timeout(2000)
            context.close()
            browser.close()


if __name__ == "__main__":
    run()
