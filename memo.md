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

4月20日(水)  
- ESP32からBluetooth接続でRasPiにシグナル送信の方法  
  ESP側のソースはArudino IDEにサンプルソースがある。
  
4月21日(木)  
 実装整理  
 期限→14人日 ～5月19日(木)  
 5月16日は研修（1日中）

 - 1 raspi⇔espの通信　3人日（＋バッファ1人日）～4月26日(火)  
   - 1-1 espのBluetooth送信  
     - シリアルボードの入力を受信側で受け取る  
   - 1-2 raspiのBluetooth受信  
     - pythonのプログラムで、受信した文字列を表示してみる。  
   - 1-3 esp⇔raspiの自動ペアリング  
     - ESP32とラズパイが接続していない状態から、接続～受信まで、プログラムで行う実装  
<br> 

 - 2 リードスイッチ設定  2人日（＋バッファ1人日）～5月9日(月)  
   - 2-1 回路作成  
     - リードスイッチが離れたら、シリアルボードに文字を表示する実装を
       ESP32に実装
     - リードスイッチが離れたら、送信を行うプログラムを  
       ESP32に実装  
<br>

 - 3 esp32のスリープモード設定  2人日（＋バッファ1人日）～5月12日(木)  
   - 3-1「EN」ピンに信号を送ると再起動するプログラム調査＋作成  
   - 3-2 1での実装を加えて、ESPが再起動したら、接続から受信まで行う実装をする    
<br>

 - 4 raspiでデータ受信したら、現在時刻をDynamoDBへ登録する実装を行う 1人日 ～5月13日(金)  
   - AWSの設定  
   - MQTT送信の実装  
<br>

 - 5 取付作業  1人日　～5月17日(火)  
   - 不具合の修正  
   - 課題調査  
<br>

 - 6 手順書作成  2人日　～5月19日(木)  

 4月25日(月)  
 bluezのインストールをやり直す。  
 参考サイト1  
 https://blog.kakakikikeke.com/2015/10/raspberrypi-bluez-ble.html  
 →このサイトはだめだった（make部分でエラーになる）  

参考サイト2  
https://qiita.com/azarashin/items/9fcd18174c199c62b679  
→このサイトに「環境のインストール」とあるが、そこが参照している  
 環境設定方法もある。今回は下のpythonのソースも利用するため、このページに限って行ってみる  
ラズパイのMACアドレス→E4:5F:01:40:D4:D2  
未使用チャンネルを調べる→どこも使ってない  
手順の中にSDPを使用するところがあるが、エラーが出るため（Failed to connect to SDP server on～～～）  
以下のサイトを参考に、SDPの変更を行う。  
https://raspberrypi.stackexchange.com/questions/41776/failed-to-connect-to-sdp-server-on-ffffff000000-no-such-file-or-directory  
再び未使用チャンネルを調べる→3と12が使われている  
サイトにある通りに22を使用  

参考サイトの「ペアリングする」というところまで成功  
「python&bluezで受信してみる」のところまでできた  

参考サイト2を使えば、RaspberryPiで受信までできた。  
→このサイトで行っていることが具体的に何なのかを調べる必要がある。  
「環境のインストール」  
- pybluezの依存パッケージとpybluezのインストールを行う  
- ラズパイのSDPの変更  
  SDP(Service Discovery Protocol)...Bluetoothで利用できるサービスを通知するためのプロトコル  
    Bluetoothで利用できるサービス  
    - PCとRaspberrypiをBluetooth接続した状態で  
      コントロールパネル>ハードウェアとサウンド>デバイスとプリンター  
      でRaspberrypiのプロパティからサービスを選択し出てくる一覧  
    Bluetoothでは必須のプロトコル  
    参考サイト→https://www.wdic.org/w/WDIC/SDP%20(Bluetooth)  
  sdptoolなどは、シリアルポートの設定を行っている。  
- Bluetoothctlのコマンド一覧  
  https://qiita.com/noraworld/items/55c0cb1eb52cf8dccc12  

4月26日(火)  
ESP32のMACアドレス → 78:21:84:80:29:0E  
ラズパイのUUID？ → 516825d8-c508-11ec-beba-ff7091cc9b2a  

ラズパイにUSB接続でデータを受信する参考サイト  
→ https://qiita.com/zakkied/items/5d01c0b42e3476cf449a  
WiFiでPCとESP32のデータ送信を行う参考サイト  
→ https://qiita.com/GANTZ/items/5be4ccd2f2d45d6bd36d  
Bluetoothの自動接続が可能なコマンドがある参考サイト  
→ https://nwpct1.hatenablog.com/entry/2013/10/19/190029  
