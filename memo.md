～Bluetooth用語～
バインド→ペアリングのこと
<br>
<br>
ラズパイで接続待ち状態にすることに成功  
(アドバタイズ状態)  
uuid →sudo blkidでわかる  
no advertisable device →　https://www.bing.com/videos/search?q=no+advertisable+device&view=detail&mid=F91E5AC10F12472BAEBEF91E5AC10F12472BAEBE&FORM=VIRE
この動画を参考に
実行ソース→BLtest.py  
参考サイト→https://github.com/pybluez/pybluez/blob/master/examples/simple/rfcomm-server.py  

<br>
<br>

接続できたけど
→ラズパイのほうで、OKを押さないといけない
→時間が多少かかってる

一旦、ラズパイ側の設定
Bluetoothの互換モードを有効にする。
→terminalで
 cd /etc/systemd/system/bluetooth.target.wants
 sudo nano bluetooth.services

 ExecStart = .... の後ろに、スペースを入れて-Cを入れる

 sudo reboot

 sudo sdptool add SP

 どの hciX が BL アダプタであるかを確認
 sudo hcitool dev

 sudo hciconfig hci0 piscan

 raspiのBluetooth Macアドレス  
 E4:5F:01:40:D4:D2  