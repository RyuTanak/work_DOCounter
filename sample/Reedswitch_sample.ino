void setup() {
  pinMode(15, INPUT);
  Serial.begin(115200);
}

void loop() {
  
  //リードスイッチに磁石がついたらシリアルボードにOKを出力
  if  ( digitalRead(15) == 0) {s
    Serial.println("OK");
  }
  //1秒毎に行う
  delay(1000);
}
