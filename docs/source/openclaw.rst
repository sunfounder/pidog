.. _pidog_skill:

.. start_using_pidog

21. Using OpenClaw to Control PiDog
========================================


**What is OpenClaw?**

Think of it as an upgraded version of ChatGPT. While traditional chatbots can only talk (generate text), OpenClaw can take action. It understands your natural language instructions and can actually perform operations on your computer, such as running commands, managing files, and calling various tools.

Here are some fantastic application scenarios:

* **Personal All-around Assistant:** Let it help you manage your schedule, set reminders, and track tasks. You just need to tell it in a chat app (like Telegram, WhatsApp), and it will remember and execute.
* **Automation "Glue":** It can act as a binder for your various services. For example, you can have it monitor a website for price changes. Once a price drop is detected, it can automatically trigger an n8n automation workflow to send you an email notification.
* **Dedicated Development Assistant:** Have it help you manage servers, run scripts, and check logs. You can simply say, "Check the system load for me," and it can SSH into your server, execute the command, and return the results.
* **Hardware "Playmate":** This is a very interesting use case. You can have OpenClaw control hardware connected to a Raspberry Pi. For example, a developer used it to control a robotic vacuum cleaner with a mechanical arm, or even had it help analyze racing simulator data and display it on an LED screen. The official Raspberry Pi team even used it to build an automatic photo booth for a wedding, just through conversation, without writing a single line of code!


Quick Start OpenClaw
------------------------------

If you want to experience the power of OpenClaw as quickly as possible, use this method. It will automatically install and launch an interactive setup wizard.

1.  Open the terminal on your Raspberry Pi and run the following command directly. This command downloads the installation script from the official website and executes it:

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash
   
    .. note:: Because new versions are updated rapidly, it's normal if your installation steps differ slightly.

2.  The script will automatically download and install OpenClaw.

    .. image:: /img/openclaw/install_open_claw.png


3.  You will then see a security prompt asking if you trust OpenClaw. Once you are sure it is safe and reliable, use the arrow keys to navigate to "Yes" and press Enter.

    .. image:: /img/openclaw/security_open_claw.png


4.  Select Quick Start, and then press Enter.

    .. image:: /img/openclaw/quickstart_open_claw.png

5.  Select your Model, and then press Enter. Here we use OpenAI as an example.

    .. image:: /img/openclaw/model_provider_open_claw.png

6.  Select OpenAI API Key.

    .. image:: /img/openclaw/api_key_open_claw.png

7.  Paste API key now.

    .. image:: /img/openclaw/paste_api_key_open_claw.png

.. |link_openai_platform| raw:: html

    <a href="https://platform.openai.com/settings/organization/api-keys" target="_blank">OpenAI Platform</a>

8.  Go to |link_openai_platform| and log in. On the **API keys** page, click **Create new secret key**.

    .. image:: /img/openclaw/llm_openai_create.png

9.  Fill in the details (Owner, Name, Project, and permissions if needed), then click **Create secret key**.

    .. image:: /img/openclaw/llm_openai_create_confirm.png

10. Once the key is created, copy it right away — you won't be able to see it again. If you lose it, you'll need to generate a new one.

    .. image:: /img/openclaw/llm_openai_copy.png

11. Paste the key into the OpenCLaw configuration.

    .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. Select the Model you want to use. In this example, we will use **Keep current**.

    .. image:: /img/openclaw/model_config_open_claw.png

13. Next is the channel selection. Channels refer to the communication services supported by OpenClaw, such as Telegram, WhatsApp, Discord, and more. Use the down arrow key to select the "Skip for now" option, then press Enter.

    .. image:: /img/openclaw/channel_open_claw.png

14. Next, you will be prompted to configure skills immediately. Select "Yes" and press Enter.

    .. image:: /img/openclaw/config_skill_open_claw.png

15. Install the skills you need. In the following example, we select the "Skip for now" option (press the spacebar to select), then press Enter.

    .. image:: /img/openclaw/install_skill_open_claw.png


16. Next are Hooks; we will check "command-logger" and "session-memory".

    .. image:: /img/openclaw/hooks2_open_claw.png


17. The installation is now complete. You can start OpenClaw by Selecting "Hatch in TUI" and pressing Enter.

   .. image:: /img/openclaw/hatch_open_claw.png


.. note:: 
   
   You can start OpenClaw by entering the following command:

    .. code-block:: bash

       openclaw tui

   And You can press ctrl+c twice to exit the tui interface.

------------------------------------------------------------------------

Making OpenClaw Operate the PiDog
----------------------------------------------

**What is PiDog Skill?**

PiDog Skill is an extension for OpenClaw that allows you to control your SunFounder PiDog V2 robot dog through natural language. Instead of remembering complex command-line parameters, you can simply tell OpenClaw what you want PiDog to do — like "make the dog sit" or "turn the LED lights purple" — and OpenClaw will execute the appropriate commands automatically.

Here are some things you can do with PiDog Skill:

* **Basic Actions:** Make PiDog stand, sit, lie down, wag its tail, bark, walk forward/backward, or turn left/right
* **Pose Holding:** Keep PiDog in a specific pose (like standing) for extended periods
* **LED Light Control:** Change the eye colors with effects like breath, listen, boom, or solid light
* **Color Customization:** Choose from red, green, blue, yellow, purple, pink, cyan, white, orange, or custom hex colors

----------------------------------------------------------------

Prerequisites
------------------------------

Before you can use PiDog Skill with OpenClaw, make sure you have:

1. **PiDog V2** properly assembled and connected to your Raspberry Pi
2. **OpenClaw** installed and running 
3. The following directories exist on your system:

   - ``~/pidog``
   - ``~/robot-hat``
   - ``~/vilib``

You can verify the installation by running:

.. code-block:: bash

   python3 -c "import pidog"

If this command runs without errors, you're ready to proceed.

----------------------------------------------------------------

Installing PiDog Skill
------------------------------

Follow these steps to install the PiDog Skill for OpenClaw:

1. **Create the skills directory** (if it doesn't already exist):

   .. code-block:: bash

      mkdir -p ~/.openclaw/workspace/skills/

2. **Copy the PiDog skill files** to the OpenClaw skills directory:

   .. code-block:: bash

      cp -r ~/pidog/pidog-control ~/.openclaw/workspace/skills/pidog-control/

   .. note:: Replace ``~/pidog-skill`` with the actual path where your PiDog skill files are located.

3. **Verify the installation** by checking the skill files:

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/pidog-control/scripts/

   You should see ``pidog_ctl.py`` and ``pidog_rgb_ctl.py`` in the output.

----------------------------------------------------------------

Testing PiDog Skill
------------------------------

Before using the skill with OpenClaw, it's recommended to test the basic functionality directly from the terminal.

**Step 1: Check PiDog Status**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py status

**Step 2: Run a Safe Test**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py safe-test

**Step 3: Test Basic Actions**

Make PiDog sit:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action sit

Make PiDog stand and hold the pose:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action stand --hold

Make PiDog bark:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action bark

**Step 4: Test LED Lights**

Test the boom light effect with purple color:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple

Test other light effects:

.. code-block:: bash

   # Breath effect with red color
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light breath --color red

   # Listen effect with blue color
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light listen --color blue

   # Turn off lights
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light off

----------------------------------------------------------------

Using PiDog Skill in OpenClaw
------------------------------

Once you've verified that PiDog Skill works from the command line, you can start using it within OpenClaw.

1. **Launch OpenClaw TUI**:

   .. code-block:: bash

      openclaw tui

2. **Send natural language commands** to control PiDog. Here are some examples:

   * "Make the dog sit"
   * "Make PiDog stand and stay"
   * "Wag the dog's tail"
   * "Make the dog bark"
   * "Turn the LED lights purple with boom effect"
   * "Set the eye lights to breath effect with red color"
   * "Make PiDog walk forward"

3. **OpenClaw will automatically** translate your request into the appropriate command and execute it on PiDog.

----------------------------------------------------------------

Available Actions and Commands
------------------------------

Here is the complete list of supported actions for PiDog Skill:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Action
     - Description
   * - stand
     - Make PiDog stand up
   * - sit
     - Make PiDog sit down
   * - lie
     - Make PiDog lie down
   * - wag-tail
     - Wag PiDog's tail
   * - bark
     - Make barking sound
   * - forward
     - Walk forward
   * - backward
     - Walk backward


**Pose Holding:**

Add ``--hold`` to any action to keep PiDog in that pose. For example: "stand --hold"

**Light Effects:**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Effect
     - Description
   * - off
     - Turn off all LED lights
   * - breath
     - Gentle breathing/pulsing effect
   * - listen
     - Reactive listening mode
   * - boom
     - Dynamic burst effect (most noticeable)
   * - solid
     - Constant steady light (use boom for better effect)

**Supported Colors:**

red, green, blue, yellow, purple, pink, cyan, white, orange, or hex codes like ``#FF5733``

----------------------------------------------------------------

Troubleshooting
------------------------------

OpenClaw Issues
^^^^^^^^^^^^^^^^^^^^^^^^

Q. During installation, I get the error ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``. What should I do?

   You can ignore this for now, but you might encounter issues in the next steps. Please refer to them one by one at that time.


Q. When I run ``openclaw tui``, I get the error ``-bash: openclaw: command not found``. What should I do?

   Execute the following command:

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   You should now be able to start the tui interface with ``openclaw tui``.



Q. In ``openclaw tui``, I encounter ``not connected to gateway — message not sent`` or the message ``gateway disconnected: closed``.

   This is because your OpenClaw Gateway service is not started. Open another terminal and execute the following command to start the OpenClaw Gateway:

   .. code-block:: bash

      openclaw gateway

   Then restart ``openclaw tui``, and you can use it directly.


Q. I want to set the OpenClaw Gateway service to run in the background / start automatically on boot. How do I do that?

   Normally, your OpenClaw Gateway service should start automatically on boot. If it doesn't, you can manually start it with the following command.

   1. Create the ``~/.config/systemd/user`` directory:

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. Create the ``openclaw-gateway.service`` file:

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


   3. Then reload the systemd configuration:

   .. code-block:: bash

      systemctl --user daemon-reload

   4. Start the service:

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   At this point, restart ``openclaw tui``, and you can use it directly.

   5. Enable it to start on boot:

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


Q. My OpenClaw can not operate the system, what should I do?

   A newly installed OpenClaw may not have permission to operate your Raspberry Pi system by default; it can only chat. We need to manually configure the permissions.

   1.  Open the OpenClaw configuration file:

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  Find the ``tools`` option and change the ``profile`` and ``exec`` as shown.

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
                "secrity": "full"
            }
        },

   3.  Save and exit.

   4.  Enter the following command in the terminal to restart the OpenClaw Gateway:

      .. code-block:: bash

         openclaw gateway restart

   Now, OpenClaw should have read and write permissions and be able to operate your Raspberry Pi system.

PiDog Issues
^^^^^^^^^^^^^^^^^^^^^^^^


Q. PiDog doesn't respond to commands. What should I do?

   First, verify that PiDog is properly connected and powered on. Then test the basic command:

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py status

   If this fails, check that the required directories exist:

      - ``~/pidog``
      - ``~/robot-hat``
      - ``~/vilib``

Q. The ``import pidog`` test fails.

   This means the PiDog Python library is not properly installed. Please refer to the PiDog V2 official installation guide to install the necessary libraries.

Q. LED lights don't work as expected.

   If solid light doesn't show clearly, use the ``boom`` effect instead — it produces the most noticeable results:

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple

Q. OpenClaw doesn't recognize the PiDog skill.

   Remind OpenClaw to sync the skills by saying in the TUI: *"Please rsync my skills"* or restart OpenClaw gateway:

   .. code-block:: bash

      openclaw gateway restart

Q. The bark action doesn't sound right.

   The bark action uses the ``single_bark_1`` sound by default. This is normal behavior for PiDog V2.

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