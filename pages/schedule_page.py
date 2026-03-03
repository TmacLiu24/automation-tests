from playwright.async_api import Page
import re
from pages.base_page import BasePage


class SchedulePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # 日程页面元素定位器
        self.schedule_link = page.get_by_title("日程")
        self.create_button = page.get_by_role("button", name="创建")
        self.title_input = page.get_by_placeholder("请输入").first
        self.type_dropdown = page.locator("div").filter(has_text=re.compile(r"^请选择个人日程会议$"))
        self.type_dropdown_placeholder = self.type_dropdown.get_by_placeholder("请选择")
        self.personal_schedule_option = page.get_by_role("listitem").filter(has_text="个人日程")
        self.start_date_input = page.locator("#startDate")
        self.end_date_input = page.locator("#endDate")
        self.description_input = page.get_by_placeholder("请输入").nth(1)
        self.public_scope_dropdown = page.locator("div").filter(has_text=re.compile(r"^请选择公开私密$"))
        self.public_scope_placeholder = self.public_scope_dropdown.get_by_placeholder("请选择")
        self.public_option = page.get_by_text("公开", exact=True)
        self.confirm_button = page.get_by_role("button", name="确定")
        self.delete_button = page.get_by_title("删除")
        self.confirm_delete_button = page.get_by_role("button", name="确认")

    async def navigate_to_schedule(self) -> None:
        """导航到日程页面"""
        await self.schedule_link.click()
        await self.human_like_delay(1.0, 2.0)  # 等待页面加载

    async def create_schedule(self, title: str, description: str = "") -> None:
        """创建新日程"""
        # 点击创建按钮
        await self.create_button.click()
        await self.human_like_delay(0.8, 1.5)  # 等待弹窗加载
        
        # 填写日程标题
        await self.title_input.click()
        await self.human_like_delay(0.3, 0.8)
        await self.type_like_human(self.title_input, title)
        
        # 选择日程类型为个人日程
        await self.type_dropdown_placeholder.click()
        await self.human_like_delay(0.5, 1.0)
        await self.personal_schedule_option.click()
        await self.human_like_delay(0.3, 0.8)
        
        # 设置开始日期（选择当前月份的18号）
        await self.start_date_input.click()
        await self.human_like_delay(0.5, 1.0)
        start_date_day = self.page.get_by_role("cell", name="18")
        await start_date_day.click()
        start_date_confirm = self.page.locator("#layui-laydate1").get_by_text("确定")
        await start_date_confirm.click()
        await self.human_like_delay(0.3, 0.8)
        
        # 设置结束日期（选择当前月份的20号）
        await self.end_date_input.click()
        await self.human_like_delay(0.5, 1.0)
        end_date_day = self.page.get_by_role("cell", name="20", exact=True)
        await end_date_day.click()
        end_date_confirm = self.page.locator("#layui-laydate2").get_by_text("确定")
        await end_date_confirm.click()
        await self.human_like_delay(0.3, 0.8)
        
        # 填写描述
        if description:
            await self.description_input.click()
            await self.human_like_delay(0.3, 0.8)
            await self.type_like_human(self.description_input, description)
        
        # 设置公开范围为公开
        await self.public_scope_placeholder.click()
        await self.human_like_delay(0.5, 1.0)
        await self.public_option.click()
        await self.human_like_delay(0.3, 0.8)
        
        # 确认创建
        await self.confirm_button.click()
        await self.human_like_delay(1.5, 3.0)  # 等待创建完成

    async def delete_schedule(self, title: str) -> None:
        """删除指定标题的日程"""
        # 点击日程链接
        schedule_link = self.page.locator("a").filter(has_text=title)
        await schedule_link.click()
        await self.human_like_delay(0.8, 1.5)
        
        # 点击删除按钮
        await self.delete_button.click()
        await self.human_like_delay(0.5, 1.0)
        
        # 确认删除
        await self.confirm_delete_button.click()
        await self.human_like_delay(1.0, 2.0)  # 等待删除完成