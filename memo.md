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

4月28日(木)  
enピンの動作確認  
- まず、電気信号が送れていること→送れている  
- High→LOWなのか、LOW→Highなのかどちらかわからないので、どちらも試す。  
  →プルアップ回路を作成した時に成功した。  
  　Low→Highの時にENピンが起動する？  
  　具体的には磁石をつけて、離した瞬間にリセットがかかる。  
- deep_sleepの処理は今は必要なので、省略する。  

enピンの動作がうまくいったので、deep_sleepがされていることを確認する。  
→loop処理でLEDを光らせて、deepsleepが動いていたらLEDは止まるはず。  
 →esp_deep_sleep_start();でloop処理に入らないことを確認した。  

5月9日（月）  
・チームズの記事を参考にbleakを使った実装を行う。  
・チームズのソース通りに通信は成功したが、問題がありそう。  
　→どこかの記事でみたが、Ctrl＋Cで処理を止めた場合、スレッドが残って？  
   次の接続ができなくなる。 
  →ラズパイはつけっぱで、ESPの電源を抜いたり、つけたりしてみる。 

5月10日（火）  
・今あるソースを参考に、deep_sleepの実装を行う。  
　→deep_sleepの実装はできた。  
リードスイッチさえ、正確にON/OFFできればとりあえず動く  
・今温湿度センサーで使っているラズパイを利用して行う予定なので  
  マルチスレッドで実行する方法を調べて行う。  

5月11日（水）  
・マルチプロセスで行う場合は、単純に別ターミナルで実行するだけ  
・MQTT通信はできたが、1発目はConnect→パブリッシュの時間を3秒開けなとできない  
  また、パブリッシュの処理をループ処理に入れないと実行できない  
・DynamoDBへ登録をテスト的に確認できたので、実際に組み込んで試してみる。  
・組み込んでDynamoDBへ登録まで行うことはできたが、課題が多い  
  →リードスイッチの反応が悪い→ESP側の接続が確認できない。
・ESP32から接続ができた時、raspi側で接続できているはずだが、3割くらいでしか成功しない。  
　問題は2段階で存在する  
  1,ESP32でリードスイッチが離れた時にRaspiとの接続に成功しない  
  2,1が成功してもラズパイの方が、接続したことを認識しない。

・deep_sleepのタイミングを1秒後にしたら成功した。  

〇残り残件  
 ・ソース整理(いらない部分の削除・コメント付与・ファイル名の決定)  
 ・温湿度で使っているRaspiを利用して運用  
 ・ESP32を電池で運用  
   問題は3点
   ・3.3V以上の電圧が必要→高い電圧を3.3V降圧する必要がある。それをするのがレギュレーター  
   ・一時的に高い電圧が必要、コンデンサを置いてそこから借りる  
   ・電池減る、底辺部分で高速でリセットされ、壊れる可能性、リセットICという部品

 ・取付作業  
   1,リードスイッチを取り付けて、簡単なソースを利用して、リードスイッチが正常に動いていることの確認  
   2,実際のソースを動かす  
 ・手順書の作成  

 〇残課題  
 ・DoorOpenerの残課題  
   →自動起動  
   →LED点灯変更  
 ・RaspiOSのインストール方法の変更に伴った、手順書の変更  
