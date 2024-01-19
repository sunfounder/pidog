.. _openssh_powershell:

Powershellを使用してOpenSSHをインストール
-----------------------------------------------

``ssh <username>@<hostname>.local`` （または ``ssh <username>@<IPアドレス>`` ）を使用してRaspberry Piに接続しようとすると、次のエラーメッセージが表示される場合があります。

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


これは、コンピューターシステムが古すぎて `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ が事前にインストールされていないことを意味します。以下のチュートリアルに従って、手動でインストールする必要があります。

#. Windowsデスクトップの検索ボックスに ``powershell`` と入力し、 ``Windows PowerShell`` を右クリックし、表示されるメニューから ``管理者として実行`` を選択します。

    .. image:: img/powershell_ssh.png
        :align: center

#. 以下のコマンドを使用して ``OpenSSH.Client`` をインストールします。

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. インストール後、以下の出力が返されます。

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 次のコマンドを使用してインストールを確認します。

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. これにより、 ``OpenSSH.Client`` が正常にインストールされたことがわかります。

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        上記のプロンプトが表示されない場合、Windowsシステムがまだ古い可能性があり、 :ref:`login_windows` のようなサードパーティのSSHツールをインストールすることをお勧めします。

#. 今、PowerShellを再起動し、管理者として実行し続けます。この時点で、 ``ssh`` コマンドを使用してRaspberry Piにログインできるようになり、以前に設定したパスワードを入力するように求められます。

    .. image:: img/powershell_login.png
