# 从这里开始 — v1.1.0

本项目是跨平台命题协议、空白状态模板和离线检查工具，不包含模型、历次试卷、答案或原作者个人记录。仅限个人、非商业学习使用，见 [LICENSE.md](LICENSE.md)。

## 普通聊天平台

先确认当前会话能实际创建并提供可下载PDF，而不只是阅读PDF或描述制作步骤。若你要直接获取可打印文件，应先完成一页中英文和简单图形的测试PDF生成、下载、打开验证；之后再开始整套命题。没有此能力时，请换到支持文件生成的环境，或明确接受文字稿/HTML及手动导出的额外步骤。

上传 [UNIVERSAL_PROMPT.md](UNIVERSAL_PROMPT.md)，发送：

> 我需要最终可下载的试卷PDF和答案解析PDF。先不要出整卷：请实际创建一页含中文、英文和简单图形的测试PDF并提供附件，确认你能生成真实文件，而不是只给代码、HTML或虚构下载链接。另行报告作文图片制作、PDF逐页渲染查看和独立盲审能力。PDF生成不可用时先明确说明，不要直接开始整卷。预检通过后，按这份1.1规则建立我的独立学习系列，进行双向钢人审视及整卷设计；不虚构检查或真题等值。

每轮保存自己的状态，换会话时重新提供。使用联网AI服务时，自行确认数据处理条款，不提交个人敏感资料。

## 原生 Skill 平台

下载完整仓库，使用根目录 [SKILL.md](SKILL.md)，不要只复制入口文件。将 `state/STARTER_STATE.json` 复制到自己的工作目录；接续时加载自己保存的状态。

## 可选本地检查

Python 3.10+，只使用标准库，无需安装依赖：

```text
python scripts/preflight.py
python scripts/migrate_state.py state/STARTER_STATE.json ../my-work/CURRENT_STATE.json
python scripts/validate_paper.py ../my-work/paper.json
python scripts/render_print.py ../my-work/paper.json --output-dir ../my-print
python scripts/test_public_package.py
```

验证和渲染命令需要先生成自己的 `paper.json`。渲染脚本输出 HTML，不自动完成 PDF；浏览器导出后须逐页检查。公共包不带含答案的历史测试卷。

脚本通过不证明答案唯一、来源真实或难度等值。没有独立/隔离上下文盲审时，最多声明结构检查通过。尚未完成所有AI平台端到端测试。
