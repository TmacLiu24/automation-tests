from playwright.async_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://wfm-web.warmheart.top/WFM-admin/index.html#/Login"
    
    def __init__(self, page: Page):
        super().__init__(page)
        # 登录页面元素定位器
        self.username_input = page.get_by_placeholder("请输入用户名")
        self.password_input = page.get_by_placeholder("请输入密码")
        self.login_button = page.get_by_role("button", name="登录")

    async def navigate(self) -> None:
        """导航到登录页面"""
        await self.page.goto(self.URL)
        await self.human_like_delay(1.0, 3.0)  # 等待页面加载

    async def login(self, username: str, password: str) -> None:
        """执行登录操作"""
        # 输入用户名
        await self.username_input.click()
        await self.human_like_delay(0.3, 0.8)
        await self.type_like_human(self.username_input, username)
        
        # 输入密码
        await self.password_input.click()
        await self.human_like_delay(0.3, 0.8)
        await self.type_like_human(self.password_input, password)
        
        # 点击登录按钮
        await self.login_button.click()
        await self.human_like_delay(2.0, 4.0)  # 等待登录完成