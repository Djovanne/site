#include <BLEDevice.h>
#include <BLEScan.h>
#include <Arduino.h>

BLEScan* pBLEScan;

void setup() 
{
  Serial.begin(115200);
  BLEDevice::init("ESP32");
  pBLEScan = BLEDevice::getScan();
}

void loop() 
{
  BLEScanResults foundDevices = pBLEScan->start(15);

  //Serial.println("Dispositivos encontrados:");
  for (int i = 0; i < foundDevices.getCount(); i++) 
  {
    BLEAdvertisedDevice device = foundDevices.getDevice(i);
    //Serial.printf("[%d] Endereço: %s\n", i, device.getAddress().toString().c_str());

    // Tenta obter o nome do dispositivo
    //if (device.haveName()) 
      //Serial.printf("    Nome: %s\n", device.getName().c_str());

    // Tenta obter informações adicionais
    if (device.haveServiceData()) 
    {
      //Serial.println("    Informações adicionais:");
      for (int i = 0; i < device.getServiceDataCount(); i++) 
      {
        //Serial.printf("        UUID: %s, Dados: %s\n", device.getServiceDataUUID(i).toString().c_str(), device.getServiceData(i).c_str());
      }
    }
  }
  /*
  int meuInteiro = 123; // Seu inteiro a ser transmitido

  Serial.write((uint8_t*)&meuInteiro, sizeof(meuInteiro));
  */
  int dado = foundDevices.getCount(); // Seu dado do tipo int
  Serial.write((uint8_t*)&dado, sizeof(dado));
  /*
  Serial.println();
  Serial.println(dado);
  Serial.println(*(uint8_t*)& dado);
  */
  delay(2000);
}