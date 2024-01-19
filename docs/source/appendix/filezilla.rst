.. _filezilla:

Filezillaソフトウェア
==========================

.. image:: img/filezilla_icon.png

ファイル転送プロトコル（FTP）は、コンピュータネットワーク上のサーバーからクライアントへのコンピュータファイルの転送に使用される標準通信プロトコルです。

Filezillaはオープンソースのソフトウェアで、FTPだけでなくFTP over TLS（FTPS）およびSFTPもサポートしています。Filezillaを使用して、ローカルファイル（写真や音声など）をRaspberry Piにアップロードしたり、Raspberry Piからローカルにファイルをダウンロードしたりすることができます。

**ステップ1**: Filezillaのダウンロード

Filezillaのクライアントを `Filezillaの公式ウェブサイト <https://filezilla-project.org/>`_ からダウンロードします。Filezillaには非常に良いチュートリアルがありますので、 `ドキュメンテーション - Filezilla <https://wiki.filezilla-project.org/Documentation>`_ を参照してください。

**ステップ2**: Raspberry Piに接続

クイックインストールの後、Filezillaを開いて `FTPサーバーに接続 <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_ します。接続する方法は3つありますが、ここでは **クイック接続** バーを使用します。 **ホスト名/IP** 、 **ユーザー名** 、 **パスワード** 、 **ポート（22）** を入力し、 **クイック接続** をクリックするか、 **Enter** キーを押してサーバーに接続します。

.. image:: img/filezilla_connect.png

.. note::

    クイック接続はログイン情報をテストする良い方法です。永続的なエントリを作成したい場合は、クイック接続に成功した後に **ファイル** -> **現在の接続をサイトマネージャーにコピー** を選択し、名前を入力して **OK** をクリックします。次回から、以前保存したサイトを選択して **ファイル** -> **サイトマネージャー** 内で接続できます。
    
    .. image:: img/ftp_site.png

**ステップ3**: ファイルのアップロード/ダウンロード

ファイルをアップロードするには、ローカルファイルをRaspberry Piにドラッグアンドドロップするか、Raspberry Pi内のファイルをローカルにダウンロードすることができます。

.. image:: img/upload_ftp.png
