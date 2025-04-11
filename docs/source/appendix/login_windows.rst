
.. _login_windows:

PuTTY
=========================

如果您是 Windows 用户，可以使用几种 SSH 应用程序。这里，我们推荐使用 `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_。

**Step 1**

下载 PuTTY。

**Step 2**

打开 PuTTY，点击左侧树状结构中的 **Session** 。在 **Host Name (or IP address)** 下输入 RPi 的 IP 地址，在 **Port** 下输入 **22** （默认为22）。

.. image:: img/image25.png
    :align: center

**Step 3**

点击 **Open**。请注意，当您第一次使用 IP 地址登录 Raspberry Pi 时，会出现安全提示。只需点击 **Yes**。


**Step 4**

当 PuTTY 窗口提示 \"**login as:**\" 时，输入
\"**pi**\"（RPi 的用户名），和 **password**: \"raspberry\"
（默认密码，如果您未进行更改）。

.. note::

    输入密码时，窗口不会显示字符，这是正常的。您需要做的是输入正确的密码。
    
    如果 PuTTY 旁边显示不活跃，说明连接已断开，需要重新连接。
    
.. image:: img/image26.png
    :align: center

**Step 5**

此时，我们已成功连接到 Raspberry Pi，可以进行下一步操作。