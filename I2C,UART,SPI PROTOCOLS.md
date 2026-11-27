New embedded task...   
Make 2 Arduinos communicate with each other using i2c and UART protocol in tinkercad.

**I2C PROTOCOL**  
**:inter integrated circuit**

\>it is a bus interface connection protocol

\>used in **serial communication**

\>widely accepted in short distance communication

\>**only 5V accepted**

\>it is **synchronous(ie. It have SCL, thereby giving same time for all master and slaves)**

\>it is **half duplex(i.e.. It can only transmit or receive at an time)**

\>it use 2 bi-directional open-drain line for data communication called:  
    →**serial data(SDA)** **:-** TRANSMIT DATA TAKE PLACE HERE  
    → **serial clock(SCL):-**carries clock signal

I2C operates in 2 modes: Master and Slaves

UART PROTOCOL

**UART Communication Protocol**

**UART (Universal Asynchronous Receiver/Transmitter)**

**Usage:** Simple, point-to-point communication.

**Speed:** Moderate (typically up to 1 Mbps, but can go higher).

**Number of Devices:** Typically only two devices (one-to-one).

**Wiring:**

TX (Transmit) of one device to RX (Receive) of the other.

GND (Ground) connected between devices.

**Pros:**

Simple to implement.

No clock signal needed.

Full-duplex communication.

**Cons:**

Limited to two devices.

Requires precise timing for higher speeds.

**When to use UART:**

Simple communication between two devices (e.g., microcontroller to GPS module, Bluetooth module).

When simplicity and ease of implementation are prioritized.

When full-duplex communication is needed.

#  **Serial Peripheral Interface (SPI)**

# 

A Serial Peripheral Interface (SPI) facilitates short-distance communication between peripheral integrated circuits and microcontrollers. 

It is a protocol that is synchronous serial communication. 

It is allowed to transfer high-speed data. 

It is allowed to transfer high-speed data. (**FULL DUPLLEX**)

* **SPI Bus:** SPI bus is a physical connection over the data transferring between the slave devices and the master. It contains four signal lines as below.  
  * **Slave Select (SS):** In Slave Select, each slave device contains a dedicated SS pin. If the master will communicate with the specific slave. Multiple slave devices can be shared with the as same as MOSI, MISO, and SCK lines but it must have separated SS lines.  
  * M**aster Out Slave In (MOSI):** In Master Out Slave In, MOSI can share the data or information from the master to other slave devices.  
  * **Master In Slave Out (MISO):** In Master In Slave Out, MISO can share the data or information from the slave device with the master.  
  * **Serial Clock (SCK):** In Serial Clock, this clock signal is used by the master and the slave devices for coordinating the data transfer timings.

IN I2C PROTOCOL CODE USED:  
 

MASTER:

\#include \<Wire.h\>

void setup()  
{  
  Wire.begin();  
  Serial.begin(9600);  
}

byte x \= 0;

void loop()  
{  
  Wire.beginTransmission(4);  
  Wire.write("x is ");  
  Wire.write(x);  
  Wire.endTransmission();  
  x++;  
  delay(500);  
}

SLAVE:

\#include \<Wire.h\>

void setup()  
{  
  Wire.begin(4);  
  Wire.onReceive(recieveEvent);  
  Serial.begin(9600);  
}

void loop()  
{  
  delay(100);  
}

void recieveEvent(int howMany)  
{  
  while (1 \< Wire.available())  
  {  
    char c \= Wire.read();  
    Serial.print(c);  
  }  
  int x \= Wire.read();  
  Serial.println(x);  
}

IN UART PROTOCOL CODE USED :(SAME FOR BOTH AURDINO)

\#include \<SoftwareSerial.h\>  
SoftwareSerial mySerial(10, 11); // RX, TX

void setup() {  
  Serial.begin(4200);  
  mySerial.begin(4200);  
   //Serial.println("Enter data to send to the other Arduino:");  
}

void loop() {  
  // Check if data is available on the Serial Monitor  
  if (Serial.available() \> 0\) {  
    String data \= Serial.readStringUntil('\\n');  
    mySerial.println(data);  // Send data to Arduino 1  
    Serial.print("Sent: ");  
    Serial.println(data);  // Display sent message on the Serial Monitor  
  }

  // Check if data is available from Arduino 1  
  if (mySerial.available() \> 0\) {  
    String receivedData \= mySerial.readStringUntil('\\n');  
    Serial.print("Received: ");  
    Serial.println(receivedData);  // Display received message on the Serial Monitor  
  }  
}

