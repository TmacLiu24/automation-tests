# 自动化测试Jenkins集成指南

## 项目介绍
这是一个使用Playwright编写的自动化测试项目，用于测试日程管理功能，包括登录、创建日程和删除日程操作。

## 环境准备

### 1. 安装Python
确保Jenkins服务器上安装了Python 3.7或更高版本。

### 2. 安装Playwright依赖
```bash
# 安装Playwright
pip install playwright

# 安装浏览器
playwright install chromium
```

## Jenkins集成步骤

### 1. 创建Jenkins任务
- 登录Jenkins控制台
- 点击"新建任务"
- 输入任务名称，选择"流水线"
- 点击"确定"

### 2. 配置流水线
- 在"流水线"部分，选择"Pipeline script from SCM"
- 选择Git作为SCM（如果项目已托管在Git仓库）
- 输入仓库URL和凭据
- 选择分支（如main/master）
- 在"脚本路径"中输入`Jenkinsfile`

### 3. 保存并构建
- 点击"保存"
- 点击"立即构建"开始执行测试

## 项目结构

```
├── Jenkinsfile           # Jenkins流水线配置文件
├── requirements.txt      # 项目依赖
├── pages/               # Page Object Model页面类
│   ├── base_page.py     # 基础页面类
│   ├── login_page.py    # 登录页面类
│   └── schedule_page.py # 日程页面类
└── tests/               # 测试脚本
    └── test_schedule_async.py # 异步测试脚本
```

## 测试流程

1. 启动浏览器
2. 导航到登录页面
3. 执行登录操作
4. 导航到日程页面
5. 创建新日程
6. 删除创建的日程
7. 关闭浏览器

## 错误处理

- 测试过程中如发生错误，会自动保存截图到`error_screenshot.png`
- Jenkins会自动归档错误截图

## 注意事项

1. 确保Jenkins服务器有足够的权限执行浏览器操作
2. 如果在Docker环境中运行，可能需要使用无界面模式（headless=True）
3. 定期更新Playwright依赖以确保兼容性
