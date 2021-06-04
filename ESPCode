#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define mqtt_server "broker.hivemq.com"
#define temperature_topic "my/test/topic"

char* ssid = "TP-LINK_9960";
char* pass = "79803618";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, pass);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");

    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

long lastMsg = 0;

void loop() {
  
  if (!client.connected()) {
    reconnect();
  }

  client.loop();

   long now = millis();
   if (now - lastMsg > 500) {
   lastMsg = now;

    int val = analogRead(A0);

    float mv = val * (5000 / 1024.0); 

    float newTemp = mv/10;
    
      Serial.print("New temperature:");
      Serial.println(String(newTemp).c_str());
      client.publish(temperature_topic, String(newTemp).c_str(), true);
    }
  }
