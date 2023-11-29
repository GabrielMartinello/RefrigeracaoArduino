#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h> 
#include <functional>
#include <ArduinoJson.h>


const char* ssid = "Alini";
const char* password = "35178989";

#define DHTPIN D3
#define DHTTYPE DHT11

#define WIFI_SSID "Alini"
#define WIFI_PASS "35178989"

#define RELE_PIN 5
#define RELE_COOLER 4

DHT dht(DHTPIN, DHTTYPE);
WiFiServer server(80);

void temperaturaUmidade(float temperatura, float umidade){
  HTTPClient http;
  WiFiClient client;

  String url = "http://192.168.2.114:5000/temperatura";

  http.begin(client, url);
  http.addHeader("Content-Type", "application/json");

  // Criar um objeto JSON
  DynamicJsonDocument jsonDoc(200);
  jsonDoc["temperatura"] = temperatura;
  jsonDoc["umidade"] = umidade;

  String data;
  serializeJson(jsonDoc, data);

  int httpResponseCode = http.POST(data);

  Serial.print("Código de resposta da API: ");
  Serial.println(httpResponseCode);

  if (httpResponseCode > 0) {
    Serial.print("Resposta da API: ");
    Serial.println(http.getString());
  } else {
    Serial.print("Erro na requisição. Código de erro: ");
    Serial.println(httpResponseCode);
  }

  http.end();

  // return httpResponseCode;
}

void validaTemperatura(float umidade, float temperatura){
  if(temperatura < 22){
    digitalWrite(RELE_PIN, LOW);
  }
  if(temperatura >= 22){
    digitalWrite(RELE_COOLER, LOW);
  }
  
  temperaturaUmidade(temperatura, umidade);
}


// put function declarations here:
int myFunction(int, int);

void setup() {
  IPAddress local_IP(192,168,1,123); //Manda um ip ai
  IPAddress gateway(192,168,2,1);
  IPAddress subnet(255,255,255,0);

  pinMode(RELE_PIN, OUTPUT);
  pinMode(RELE_COOLER, OUTPUT);

  digitalWrite(RELE_PIN, HIGH);
  digitalWrite(RELE_COOLER, HIGH);

  Serial.begin(9600);
  dht.begin();
  Serial.println();
  Serial.println();
  Serial.print("Conectando-se a ");
  Serial.println(ssid);
  if (!WiFi.config(local_IP, gateway, subnet)) {
    Serial.println("STA Failed to configure");

    
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.println("Conexão WiFi estabelecida");
    Serial.print("Endereço IP: ");
    Serial.println(WiFi.localIP());
    server.begin();
  }
}



void loop() {
  WiFiClient client = server.available();

  digitalWrite(RELE_PIN, HIGH);
  digitalWrite(RELE_COOLER, HIGH);

  String request = client.readStringUntil('\r');
  client.flush();
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  Serial.print("Umidade: "); Serial.println(h);
  Serial.print("Temperatura: "); Serial.println(t);

  validaTemperatura(h, t);
  delay(30000);
  
  client.stop();
}
