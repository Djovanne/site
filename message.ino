#include <WiFi.h>
#include <Arduino.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,20,4);

const char* ssid = "Galaxy Note96143";
const char* password = "xbjj8897";
IPAddress server(143,198,186,226);
const int port = 8080;

WiFiClient client;

void setup() 
{
  lcd.init();
  lcd.backlight();
  lcd.clear();

  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) 
  {
    delay(1000);
    lcd.setCursor(1,0);
    lcd.print("Conectando ao WiFi...");
    Serial.println("Conectando ao WiFi...");
  }
  lcd.clear();
  lcd.setCursor(1,0);
  lcd.print("Conectado ao WiFi");
  Serial.println("Conectado ao WiFi");
  Serial.println(WiFi.localIP() );
}

void loop() 
{
  if (Serial.available() >= sizeof(int)) 
  {
    int dado;
    lcd.clear();
    Serial.readBytes((byte*)&dado, sizeof(dado));
    Serial.println(dado);

    lcd.setCursor(1,2);
    lcd.print("dado recebido:");
    lcd.setCursor(1,3);
    lcd.print(dado);

    if (client.connect(server, port)) 
    {
      lcd.setCursor(1,0);
      Serial.println("Conectado ao servidor");

      client.print("GET /api/log/");
      client.print(dado);
      client.println(" HTTP/1.1");
      client.print("Host: ");
      client.println(server);
      client.println("Connection: close");
      client.println();

      while (client.available() )
      {
        char c = client.read();
        Serial.print(c);
      }
      client.stop();
      lcd.clear();
      lcd.setCursor(1,0);
      lcd.print("Coneccao fechada");
      lcd.setCursor(1,2);
      lcd.print("dado recebido:");
      lcd.setCursor(1,3);
      lcd.print(dado);
      Serial.println("\n Coneccao fechada");
    } 
    else 
    {
      lcd.setCursor(1,0);
      lcd.print("Coneccao falhou");
      Serial.println("Coneccao falhou");
    }
  }
  delay(5000);
}