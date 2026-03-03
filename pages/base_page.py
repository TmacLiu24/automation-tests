from playwright.async_api import Page
import asyncio
import random


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def human_like_delay(self, min_seconds: float = 0.5, max_seconds: float = 2.0) -> None:
        """模拟人类思考的随机延迟"""
        delay = random.uniform(min_seconds, max_seconds)
        await asyncio.sleep(delay)

    async def type_like_human(self, locator, text: str, delay_per_char: float = 0.1) -> None:
        """模拟人类打字效果，每个字符之间有随机延迟"""
        for char in text:
            await locator.type(char, timeout=5000)
            await asyncio.sleep(random.uniform(delay_per_char * 0.5, delay_per_char * 1.5))

    async def click(self, locator, timeout: float = 30000) -> None:
        """封装点击操作，添加延迟"""
        await locator.click(timeout=timeout)
        await self.human_like_delay(0.3, 0.8)

    async def fill(self, locator, text: str, human_like: bool = True) -> None:
        """封装填充操作，支持人类打字效果"""
        if human_like:
            await self.type_like_human(locator, text)
        else:
            await locator.fill(text, timeout=5000)
            await self.human_like_delay(0.3, 0.8)