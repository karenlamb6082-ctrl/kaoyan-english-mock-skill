# 从这里开始 — v1.1.0

本项目是跨平台命题协议、空白状态模板和离线检查工具，不包含模型、历次试卷、答案或原作者个人记录。仅限个人、非商业学习使用，见 [LICENSE.md](LICENSE.md)。

## 普通聊天平台

上传 [UNIVERSAL_PROMPT.md](UNIVERSAL_PROMPT.md)，发送：

> 按这份1.1规则建立我自己的考研英语一训练系列。先报告实际具备的联网、文件、代码、图像、PDF和独立审查能力，再做双向钢人审视及整卷设计。不虚构来源核验、盲审、脚本执行、PDF检查或真题等值。

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
