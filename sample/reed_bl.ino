#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

//変数宣言
String MACadd = "E4:5F:01:40:D4:D1";  //ラズパイのMACアドレス
String name = "raspberrypi";          //ラズパイのBluetooth接続名
bool connected;                       //Bluetooth接続結果
int pin = 15;                         //使用するPIN

void setup() {
  //PINのセットアップ
  pinMode(pin, INPUT);
  
  //シリアルモニタへの書込速度
  Serial.begin(115200);
  SerialBT.begin("ESP32test", true); 

  Serial.println("The device started in master mode, make sure remote BT device is on!");

  //Bluetooth接続
  connected = SerialBT.connect(name);
  //connected = SerialBT.connect(address);

  //成功した場合
  if(connected) {
    Serial.println("Connected Succesfully!");
  //失敗した場合
  } else {
    while(!SerialBT.connected(10000)) {
      Serial.println("Failed to connect. Make sure remote device is available and in range, then restart app."); 
    }
  }
  //もう一度接続？？？
  SerialBT.connect();
}

void loop() {
  
  //リードスイッチに磁石がついたらシリアルボードにOKを出力
  if ( digitalRead(15) == 1) {
    //文字列送信
    SerialBT.print("xxxxxxxxxxxx");
    Serial.println("Send OK");
  }
  
  delay(1000);
}
