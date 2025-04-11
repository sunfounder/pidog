.. _filezilla:

Filezilla 软件
==========================

.. image:: img/filezilla_icon.png

文件传输协议（FTP）是一种标准的通讯协议，用于在计算机网络上从服务器传输计算机文件至客户端。

Filezilla 是一款开源软件，不仅支持 FTP，还支持通过 TLS 的 FTP（FTPS）和 SFTP。我们可以使用 Filezilla 上传本地文件（如图片和音频等）到 Raspberry Pi，或者从 Raspberry Pi 下载文件到本地。

**Step 1**: 下载 Filezilla。

从 `Filezilla 官方网站 <https://filezilla-project.org/>`_ 下载客户端，Filezilla 提供了非常好的教程，请参考： `Documentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_。

**Step 2**: 连接到 Raspberry Pi

安装完毕后打开程序，现在可以 `连接到一个 FTP 服务器 <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_。它提供了三种连接方式，这里我们使用 **Quick Connect** 栏。输入 **hostname/IP** 、 **username** 、 **password** 和 **port (22)**，然后点击 **Quick Connect** 或按 **Enter** 连接到服务器。

.. image:: img/filezilla_connect.png

.. note::

    Quick Connect 是测试登录信息的好方法。如果您想创建一个永久条目，可以在成功的 Quick Connect 后选择 **File**-> **Copy Current Connection to Site Manager**，输入名称并点击 **OK**。下次可以通过选择 **File** -> **Site Manager** 中之前保存的站点来连接。
    
    .. image:: img/ftp_site.png

**Step 3**: 上传/下载文件。

您可以通过拖放的方式上传本地文件到 Raspberry Pi，或者下载 Raspberry Pi 中的文件到本地。

.. image:: img/upload_ftp.png
