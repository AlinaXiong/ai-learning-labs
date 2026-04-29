# AI 系统化学习实战仓库

这个仓库用来记录我系统学习 AI 的实战案例。

它不是某一个模型或某一家平台的专用项目。第一个案例会先使用 DashScope
调用 Qwen 模型完成情感分析，后续可以继续加入 OpenAI、Claude、Gemini、
本地大模型、RAG、Agent、多模态等方向的实验。

## 当前案例

### 01. 情感分析：判断评论正向还是负向

目标：把一段商品评论发送给大语言模型，让模型判断这条评论是 `正向` 还是 `负向`。

当前文件：

- `01_sentiment_analysis_qwen.py`：按课程截图整理的原样版代码
- `main.py`：情感分析主程序
- `requirements.txt`：Python 依赖
- `.env.example`：环境变量示例

## 环境准备

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 DashScope API Key

Windows PowerShell 临时配置：

```powershell
$env:DASHSCOPE_API_KEY="sk-你的真实密钥"
```

也可以在项目根目录创建 `.env` 文件：

```text
DASHSCOPE_API_KEY=sk-你的真实密钥
```

如果希望长期生效，可以在 Windows 系统环境变量中新增：

```text
DASHSCOPE_API_KEY=sk-你的真实密钥
```

## 运行案例

运行默认示例：

```bash
python main.py
```

运行课程截图对应的 Qwen 情感分析案例：

```bash
python 01_sentiment_analysis_qwen.py
```

输入自己的评论：

```bash
python main.py --review "这个耳机太差了，声音发闷，而且续航很短。"
```

查看模型原始输出：

```bash
python main.py --review "这家店服务很好，下次还会再来。" --show-raw
```

## 示例输出

```text
评论: 这款音效特别好，给你意想不到的音质。
情感结果: 正向
```

## 这个案例在学什么

1. 如何使用 Python 调用大语言模型
2. 如何配置 API Key
3. 如何组织 `system` 和 `user` 消息
4. 如何通过提示词约束模型输出
5. 如何把大模型用于一个简单的文本分类任务

## 后续学习路线

1. Prompt 基础：角色设定、任务描述、输出约束
2. 文本分类：情感分析、主题分类、意图识别
3. 结构化输出：JSON 输出、Schema 校验
4. Embedding：语义搜索、相似度匹配
5. RAG：基于本地文档的问答系统
6. Agent：工具调用、任务规划、记忆与自动化
7. 模型评估：测试集、评分、回归检查、错误分析
8. 多模态：图片理解、文档理解、语音相关任务

## 说明

当前第一个案例默认使用 `qwen-plus`。以后可以把模型调用部分抽象出来，
让同一个案例支持不同模型供应商，这样更适合长期学习和对比实验。
