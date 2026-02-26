import sys
from playwright.sync_api import sync_playwright, Page

# Fix encoding for Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# 配置
BASE_URL = "https://wfm-web.warmheart.top/WFM-admin/index.html"
LOGIN_URL = f"{BASE_URL}#/Login"
USERNAME = "18994057385"
PASSWORD = "057385"


def human_delay(page: Page, min_sec: float = 0.5, max_sec: float = 2.0) -> None:
    """模拟人类延迟"""
    import random
    delay = random.uniform(min_sec, max_sec)
    page.wait_for_timeout(int(delay * 1000))


def  test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()

        try:
            # ===== 1. 登录 =====
            print("[1/5] 导航到登录页面...")
            page.goto(LOGIN_URL)
            page.wait_for_load_state("networkidle")
            human_delay(page, 1.0, 2.0)

            # 输入用户名
            print("[2/5] 输入用户名...")
            username_input = page.get_by_placeholder("请输入用户名")
            username_input.click()
            human_delay(page, 0.3, 0.8)
            username_input.fill(USERNAME)

            # 输入密码
            print("[3/5] 输入密码...")
            password_input = page.get_by_placeholder("请输入密码")
            password_input.click()
            human_delay(page, 0.3, 0.8)
            password_input.fill(PASSWORD)

            # 点击登录按钮
            print("[4/5] 点击登录按钮...")
            page.get_by_role("button", name="登录").click()

            # 等待登录完成，验证跳转
            page.wait_for_load_state("networkidle")
            page.wait_for_url(lambda url: "#/Login" not in url, timeout=10000)
            print(f"登录成功，当前URL: {page.url}")

            # 验证登录成功 - 检查是否包含首页元素
            page.wait_for_selector(".el-container, .el-header, .el-main", timeout=10000)
            print("[OK] 已进入WFM首页")

            # ===== 2. 点击任务项 =====
            print("[5/5] 点击任务项目...")
            # 使用 class="td-hover" 和 title 属性定位
            task_item = page.locator('.td-hover[title*="【测试部门-2月第2周-项目汇总】功能优化点测试"]')
            # 如果找不到，尝试使用 get_by_text
            if not task_item.count():
                task_item = page.get_by_text("【测试部门-2月第2周-项目汇总】功能优化点测试")
            task_item.first.scroll_into_view_if_needed()
            human_delay(page, 0.3, 0.8)
            task_item.first.click()
            page.wait_for_load_state("networkidle")
            print("[OK] 已打开任务详情")

            # ===== 3. 点击返回按钮 =====
            print("点击返回按钮...")
            page.get_by_role("button", name="返回").click()
            page.wait_for_load_state("networkidle")

            # 处理离开弹窗
            if page.get_by_text("离开").is_visible():
                page.get_by_text("离开").click()
                page.wait_for_load_state("networkidle")

            # ===== 4. 点击前往查看 =====
            print("点击前往查看...")
            page.get_by_text("前往查看 >").click()
            page.wait_for_load_state("networkidle")

            # ===== 5. 点击修改任务 =====
            print("点击修改任务...")
            page.get_by_role("button", name="修改任务").click()
            page.wait_for_load_state("networkidle")

            # ===== 6. 返回 =====
            page.get_by_role("button", name="返回").click()
            page.wait_for_load_state("networkidle")
            if page.get_by_text("离开").is_visible():
                page.get_by_text("离开").click()
                page.wait_for_load_state("networkidle")

            # ===== 7. 点击TALK =====
            print("点击TALK...")
            page.get_by_text("TALK").first.click()
            page.wait_for_load_state("networkidle")

            # 再次点击TALK（可能需要展开）
            page.get_by_text("TALK").click()
            page.wait_for_load_state("networkidle")

            # ===== 8. 点击性能测试任务 =====
            print("点击性能测试任务...")
            page.get_by_text("性能测试-压力测试").click()
            page.wait_for_load_state("networkidle")

            # ===== 9. 点击评论 =====
            print("点击评论...")
            page.get_by_text("评论 1").click()
            page.wait_for_load_state("networkidle")

            # ===== 10. 点击修改按钮 =====
            print("点击修改按钮...")
            page.get_by_role("button", name="修改").click()
            page.wait_for_load_state("networkidle")

            # 点击标题输入框再取消
            page.get_by_placeholder("请输入标题").click()
            human_delay(page, 0.5, 1.0)

            # 点击取消
            page.get_by_role("button", name="取消").click()
            page.wait_for_load_state("networkidle")

            # 返回
            page.get_by_role("button", name="返回").click()
            page.wait_for_load_state("networkidle")

            print("\n[SUCCESS] 所有测试步骤执行完成！")

        except Exception as e:
            print(f"\n[ERROR] 测试失败: {e}")
            page.screenshot(path="error_screenshot.png")
            print("已保存错误截图: error_screenshot.png")
            raise
        finally:
            human_delay(page, 2, 3)
            context.close()
            browser.close()


if __name__ == "__main__":
    # 调用重命名后的函数
    test_login()
