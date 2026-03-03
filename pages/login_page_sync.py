from playwright.sync_api import Page
import random


class LoginPage:
    """登录页面 - 同步版本"""

    URL = "https://wfm-web.warmheart.top/WFM-admin/index.html#/Login"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder("请输入用户名")
        self.password_input = page.get_by_placeholder("请输入密码")
        self.login_button = page.get_by_role("button", name="登录")

    def human_delay(self, min_sec: float = 0.5, max_sec: float = 2.0) -> None:
        """模拟人类延迟"""
        delay = random.uniform(min_sec, max_sec)
        self.page.wait_for_timeout(int(delay * 1000))

    def navigate(self) -> None:
        """导航到登录页面"""
        self.page.goto(self.URL)
        self.page.wait_for_load_state("networkidle")
        self.human_delay(1.0, 3.0)

    def login(self, username: str, password: str) -> None:
        """执行登录操作"""
        # 输入用户名
        self.username_input.click()
        self.human_delay(0.3, 0.8)
        self.username_input.fill(username)

        # 输入密码
        self.password_input.click()
        self.human_delay(0.3, 0.8)
        self.password_input.fill(password)

        # 点击登录按钮
        self.login_button.click()
        self.human_delay(2.0, 4.0)
