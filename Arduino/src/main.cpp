#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>

const char* ssid = "";
const char* password = "";

#define DHTPIN D1
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
WiFiServer server(80);

String html = R"(
<!DOCTYPE html>
<html>
  
</html>
)";

// put function declarations here:
int myFunction(int, int);

void setup() {
  IPAddress local_IP(192,168,1,169); //Manda um ip ai
  IPAddress gateway(192,168,1,1);
  IPAddress subnet(255,255,255,0);

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

  if (!client) {
    return;
  }

  // Ler a primeira linha da solicitação (exemplo: GET /path HTTP/1.1)
  String request = client.readStringUntil('\r');
  client.flush();
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  Serial.print("Umidade: "); Serial.println(h);
  Serial.print("Temperatura: "); Serial.println(t);

  // Verificar se a solicitação é para "/get-data"
  if (request.indexOf("/get-data") != -1) {
      client.print("HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n");
      client.print(String(h) + ";" + String(t));
      return;
  } else {
      client.println("HTTP/1.1 200 OK");
      client.println("Content-type:text/html");
      client.println("Connection: close");
      client.println();
      client.print(html);
  }
  
  delay(1);
  client.stop();


}

// put function definitions here:
int myFunction(int x, int y) {
  return x + y;
}