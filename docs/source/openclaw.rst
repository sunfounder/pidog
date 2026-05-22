.. _pidog_skill:

.. start_using_pidog

21. 使用 OpenClaw 控制 PiDog
========================================


**什么是 OpenClaw？**

你可以把它看作 ChatGPT 的升级版。传统聊天机器人只能聊天（生成文本），而 OpenClaw 能够**执行操作**。它能理解你的自然语言指令，并在你的计算机上实际执行操作，例如运行命令、管理文件和调用各种工具。

以下是一些精彩的应用场景：

* **个人全能助手：** 让它帮你管理日程、设置提醒和跟踪任务。你只需在聊天应用（如 Telegram、WhatsApp）中告诉它，它就会记住并执行。
* **自动化"胶水"：** 它可以作为连接各种服务的粘合剂。例如，你可以让它监控某个网站的价格变化。一旦检测到降价，它可以自动触发 n8n 自动化工作流，向你发送邮件通知。
* **专属开发助手：** 让它帮你管理服务器、运行脚本和检查日志。你只需说"帮我检查一下系统负载"，它就能 SSH 到你的服务器，执行命令并返回结果。
* **硬件"玩伴"：** 这是一个非常有趣的用途。你可以让 OpenClaw 控制连接到 Raspberry Pi 的硬件。例如，有开发者用它控制带机械臂的扫地机器人，甚至用它分析赛车模拟器数据并显示在 LED 屏幕上。官方 Raspberry Pi 团队甚至用它为一场婚礼搭建了自动拍照亭，全程只需对话，无需编写一行代码！


.. important::

   Raspberry Pi Zero 2W 只有 512MB 内存，而 OpenClaw 最低需要 1GB。因此，它无法正常运行。建议使用 Raspberry Pi 4/5 或更高版本。

快速开始 OpenClaw
------------------------------

如果你想尽快体验 OpenClaw 的强大功能，请使用此方法。它将自动安装并启动一个交互式设置向导。

1. 打开 Raspberry Pi 的终端，直接运行以下命令。此命令将从官方网站下载安装脚本并执行：

   .. code-block:: bash

      curl -fsSL https://openclaw.ai/install.sh | bash

   .. note:: 由于新版本更新较快，你的安装步骤可能略有不同，这属于正常情况。

2. 脚本将自动下载并安装 OpenClaw。

   .. image:: /img/openclaw/install_open_claw.png


3. 随后你会看到一个安全提示，询问你是否信任 OpenClaw。确认安全可靠后，使用方向键选择"Yes"并按 Enter。

   .. image:: /img/openclaw/security_open_claw.png


4. 选择 Quick Start，然后按 Enter。

   .. image:: /img/openclaw/quickstart_open_claw.png

5. 选择你的 Model，然后按 Enter。这里我们以 OpenAI 为例。

   .. image:: /img/openclaw/model_provider_open_claw.png

6. 选择 OpenAI API Key。

   .. image:: /img/openclaw/api_key_open_claw.png

7. 现在粘贴 API key。

   .. image:: /img/openclaw/paste_api_key_open_claw.png

.. |link_openai_platform| raw:: html

    <a href="https://platform.openai.com/settings/organization/api-keys" target="_blank">OpenAI Platform</a>

8. 前往 |link_openai_platform| 并登录。在 **API keys** 页面，点击 **Create new secret key**。

   .. image:: /img/openclaw/llm_openai_create.png

9. 填写详细信息（Owner、Name、Project 以及权限，如果需要），然后点击 **Create secret key**。

   .. image:: /img/openclaw/llm_openai_create_confirm.png

10. 密钥创建后，请立即复制——你之后将无法再次查看。如果丢失，需要重新生成一个新的。

   .. image:: /img/openclaw/llm_openai_copy.png

11. 将密钥粘贴到 OpenCLaw 的配置中。

   .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. 选择你想要使用的 Model。在此示例中，我们将选择 **Keep current**。

   .. image:: /img/openclaw/model_config_open_claw.png

13. 接下来是渠道选择。渠道指 OpenClaw 支持的通信服务，例如 Telegram、WhatsApp、Discord 等。使用方向键选择"Skip for now"选项，然后按 Enter。

   .. image:: /img/openclaw/channel_open_claw.png

14. 接下来，系统会提示你是否立即配置技能。选择"Yes"并按 Enter。

   .. image:: /img/openclaw/config_skill_open_claw.png

15. 安装你需要的技能。在以下示例中，我们选择"Skip for now"选项（按空格键选择），然后按 Enter。

   .. image:: /img/openclaw/install_skill_open_claw.png


16. 接下来是 Hooks；我们将勾选"command-logger"和"session-memory"。

   .. image:: /img/openclaw/hooks2_open_claw.png


17. 安装现已完成。选择"Hatch in TUI"并按 Enter 即可启动 OpenClaw。

   .. image:: /img/openclaw/hatch_open_claw.png


.. note::

   你可以通过输入以下命令启动 OpenClaw：

   .. code-block:: bash

      openclaw tui

   你可以按两次 ctrl+c 退出 tui 界面。

------------------------------------------------------------------------

让 OpenClaw 操控 PiDog
----------------------------------------------

**什么是 PiDog Skill？**

PiDog Skill 是 OpenClaw 的一个扩展，让你可以通过自然语言控制 SunFounder PiDog V2 机器狗。无需记住复杂的命令行参数，只需告诉 OpenClaw 你希望 PiDog 做什么——例如"让狗坐下"或"把 LED 灯变成紫色"——OpenClaw 就会自动执行相应的命令。

以下是 PiDog Skill 可以实现的功能：

* **基础动作：** 让 PiDog 站立、坐下、躺下、摇尾巴、吠叫、向前/向后走或左转/右转
* **姿态保持：** 让 PiDog 长时间保持特定姿态（如站立）
* **LED 灯光控制：** 改变眼睛颜色，支持呼吸、聆听、爆闪或常亮等效果
* **颜色定制：** 可选择红、绿、蓝、黄、紫、粉、青、白、橙，或自定义十六进制颜色

----------------------------------------------------------------

先决条件
------------------------------

在将 PiDog Skill 与 OpenClaw 结合使用之前，请确保你已具备以下条件：

1. 已正确组装 **PiDog V2** 并连接到 Raspberry Pi
2. 已安装并正在运行 **OpenClaw**
3. 你的系统中存在以下目录：

   - ``~/pidog``
   - ``~/robot-hat``
   - ``~/vilib``

你可以通过运行以下命令来验证安装：

.. code-block:: bash

   python3 -c "import pidog"

如果该命令运行无错误，说明已准备就绪。

----------------------------------------------------------------

安装 PiDog Skill
------------------------------

按照以下步骤为 OpenClaw 安装 PiDog Skill：

1. **创建技能目录**\ （如果尚不存在）：

   .. code-block:: bash

      mkdir -p ~/.openclaw/workspace/skills/

2. **将 PiDog 技能文件复制**\ 到 OpenClaw 技能目录：

   .. code-block:: bash

      cp -r ~/pidog/pidog-control ~/.openclaw/workspace/skills/pidog-control/

   .. note:: 请将 ``~/pidog-skill`` 替换为你的 PiDog 技能文件所在的实际路径。

3. **验证安装**，检查技能文件：

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/pidog-control/scripts/

   你应当能在输出中看到 ``pidog_ctl.py`` 和 ``pidog_rgb_ctl.py``。

----------------------------------------------------------------

测试 PiDog Skill
------------------------------

在 OpenClaw 中使用该技能之前，建议先在终端中测试基本功能。

**第 1 步：检查 PiDog 状态**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py status

**第 2 步：运行安全测试**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py safe-test

**第 3 步：测试基础动作**

让 PiDog 坐下：

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action sit

让 PiDog 站立并保持姿态：

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action stand --hold

让 PiDog 吠叫：

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action bark

**第 4 步：测试 LED 灯光**

使用紫色测试爆闪灯效：

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple

测试其他灯效：

.. code-block:: bash

   # 红色呼吸效果
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light breath --color red

   # 蓝色聆听效果
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light listen --color blue

   # 关闭灯光
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light off

----------------------------------------------------------------

在 OpenClaw 中使用 PiDog Skill
------------------------------

确认 PiDog Skill 可以在命令行正常工作后，即可开始在 OpenClaw 中使用它。

1. **启动 OpenClaw TUI**：

   .. code-block:: bash

      openclaw tui

2. **发送自然语言命令**\ 来控制 PiDog。以下是一些示例：

   * "让狗坐下"
   * "让 PiDog 站着别动"
   * "摇摇狗的尾巴"
   * "让狗叫一声"
   * "把 LED 灯变成紫色爆闪效果"
   * "把眼睛灯设为红色呼吸效果"
   * "让 PiDog 向前走"

3. **OpenClaw 将自动**\ 把你的请求转换为相应的命令并在 PiDog 上执行。

----------------------------------------------------------------

可用动作与命令
------------------------------

以下是 PiDog Skill 支持的动作完整列表：

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 动作
     - 描述
   * - stand
     - 让 PiDog 站立
   * - sit
     - 让 PiDog 坐下
   * - lie
     - 让 PiDog 躺下
   * - wag-tail
     - 摇动 PiDog 的尾巴
   * - bark
     - 发出吠叫声
   * - forward
     - 向前行走
   * - backward
     - 向后行走


**姿态保持：**

在任何动作后添加 ``--hold`` 可让 PiDog 保持该姿态。例如："stand --hold"

**灯光效果：**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 效果
     - 描述
   * - off
     - 关闭所有 LED 灯
   * - breath
     - 温和的呼吸/脉冲效果
   * - listen
     - 响应式聆听模式
   * - boom
     - 动态爆闪效果（最明显）
   * - solid
     - 恒定常亮（建议使用 boom 效果更佳）

**支持的颜色：**

red、green、blue、yellow、purple、pink、cyan、white、orange 或十六进制颜色代码如 ``#FF5733``

----------------------------------------------------------------

故障排除
------------------------------

OpenClaw 问题
^^^^^^^^^^^^^^^^^^^^^^^^

问：安装过程中出现错误 ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``，该怎么办？

   你可以暂时忽略此错误，但后续步骤可能会遇到问题。届时请逐一排查。


问：运行 ``openclaw tui`` 时出现错误 ``-bash: openclaw: command not found``，该怎么办？

   执行以下命令：

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   现在你应该可以用 ``openclaw tui`` 启动 tui 界面了。



问：在 ``openclaw tui`` 中遇到 ``not connected to gateway — message not sent`` 或 ``gateway disconnected: closed`` 消息。

   这是因为你的 OpenClaw Gateway 服务未启动。打开另一个终端，执行以下命令启动 OpenClaw Gateway：

   .. code-block:: bash

      openclaw gateway

   然后重启 ``openclaw tui``，即可正常使用。


问：我想让 OpenClaw Gateway 服务在后台运行 / 开机自启动，该怎么做？

   通常情况下，OpenClaw Gateway 服务应在开机时自动启动。如果没有自动启动，你可以通过以下命令手动启动。

   1. 创建 ``~/.config/systemd/user`` 目录：

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. 创建 ``openclaw-gateway.service`` 文件：

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF


   3. 然后重新加载 systemd 配置：

   .. code-block:: bash

      systemctl --user daemon-reload

   4. 启动服务：

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   此时，重启 ``openclaw tui``，即可正常使用。

   5. 启用开机自启动：

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


问：我的 OpenClaw 无法操作系统，该怎么办？

   新安装的 OpenClaw 默认可能没有操作 Raspberry Pi 系统的权限，只能进行对话。我们需要手动配置权限。

   1. 打开 OpenClaw 配置文件：

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2. 找到 ``tools`` 选项，按照下方所示修改 ``profile`` 和 ``exec``：

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
                "secrity": "full"
            }
        },

   3. 保存并退出。

   4. 在终端中输入以下命令重启 OpenClaw Gateway：

      .. code-block:: bash

         openclaw gateway restart

   现在，OpenClaw 应该拥有读写权限，能够操作你的 Raspberry Pi 系统了。

PiDog 问题
^^^^^^^^^^^^^^^^^^^^^^^^


问：PiDog 对命令无响应，该怎么办？

   首先确认 PiDog 已正确连接并开机。然后测试基本命令：

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py status

   如果此命令失败，请检查所需目录是否存在：

      - ``~/pidog``
      - ``~/robot-hat``
      - ``~/vilib``

问：``import pidog`` 测试失败。

   这意味着 PiDog Python 库未正确安装。请参考 PiDog V2 官方安装指南安装必要的库。

问：LED 灯工作不正常。

   如果常亮效果不明显，请改用 ``boom`` 效果——它的显示效果最突出：

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple

问：OpenClaw 无法识别 PiDog 技能。

   在 TUI 中对 OpenClaw 说：*"Please rsync my skills"* 来提醒它同步技能，或重启 OpenClaw gateway：

   .. code-block:: bash

      openclaw gateway restart

问：bark 动作的声音不对劲。

   bark 动作默认使用 ``single_bark_1`` 声音。这是 PiDog V2 的正常行为。

----------------------------------------------------------------

.. end_using_pidog



..  PiDog skill 短说明

..  把整个目录放到：
..  ~/.openclaw/workspace/skills/pidog-control/

..  这套 skill 适用于按官方教程安装的 SunFounder PiDog V2，默认依赖这些目录存在：
..  - ~/pidog
..  - ~/robot-hat
..  - ~/vilib

..  并且这句要能通过：

..  ```bash
..    python3 -c "import pidog"
..  ```

..  目前支持
..  - 动作：stand sit lie wag-tail bark forward backward turn-left turn-right
..  - 姿态保持：--hold
..  - 灯光：off breath listen boom solid
..  - 颜色：red green blue yellow purple pink cyan white orange 或 #RRGGBB

..  推荐首次测试

..  ```bash
..    python3 skills/pidog-control/scripts/pidog_ctl.py status
..    python3 skills/pidog-control/scripts/pidog_ctl.py safe-test
..    python3 skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple
..  ```

..  常用例子

..  ```bash
..    python3 skills/pidog-control/scripts/pidog_ctl.py action sit
..    python3 skills/pidog-control/scripts/pidog_ctl.py action stand --hold
..    python3 skills/pidog-control/scripts/pidog_ctl.py action bark
..    python3 skills/pidog-control/scripts/pidog_ctl.py light boom --color red
..    python3 skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple
..  ```

..  这台机器上已验证
..  - 动作：stand / sit / lie / wag-tail / bark
..  - 灯光：boom / listen / breath / off
..  - 已现场看到：红、黄、紫 灯效

..  建议默认用法
..  - 动作演示：sit
..  - 灯光演示：boom --color purple
..  - 灯光排障优先用：pidog_rgb_ctl.py

..  注意
..  - bark 实际走的是 single_bark_1
..  - solid 不保证是真正稳定常亮，想要明显效果优先用 boom
