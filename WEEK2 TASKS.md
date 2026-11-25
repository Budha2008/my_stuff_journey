**TASK1:Binary counter in TinkerCad using 8 LEDs and a pushbutton**

on each click on switch it will take count an represent the count in form of binary representation using led by glowing and not glowing

for this i used aurdino,breadboard,8 led so on



the logic of code:

take count

convert to binary of 8 bit(used mathematical method (ie. division by 2,and taking reminders))into an list

then glow bulb with corresponding 1 in binary and pin



references:

jortin.com

youtube video

google image for circuit

amrita nots for code



**TASK2:Using an LCD display without a microcontroller (TinkerCad)**

here binary message(ascill value in binary)is given as input using switches (by deciding its state)

we need LCD,Potentiometer,slide switches,push button,power source

&#x20;



logics:

potentiometer-----to contrl contrast of lcd in VO pin

RS(high)\_\_\_used for treating data as character

RS(low)\_\_\_\_used for treating data as command and instruction

RW\_\_\_it is alway kept low here bcz during low state we write data into it

D0-D7:it is data pins to which we enter our signal

VCC:we connect to power supply

gnd:connect to ground

E(enable):this is connected to push button bcz once we set our switches for data on high state then to enter those data we should push enable button



***DISCLAIMER(MERA MISTAKE):***

***THERE ARE TWO LED PIN SHOWNED IN BOTTOM OF LCD WHERE ONE AT LAST IS TO BE CONNECTED TO NEUTRAL(GND(CATHODE)) AND OTHER TO POERSUPPLY LINE(ANODE)***

***OTHER WISE OUR LCD WOULD NOT GLOW UP***



ONCE ALL CONNECTION IS READY WE SHOULD CONFIGURE OUR LCD FROM 8BIT TO 4 BIT MODE

0010 0000----activite 4 bit mode



to clear diaplay:

0000

0001

to return home:

0000

0010

display on no cursor:

0000

1100



&#x20;**for above command we should ensure our RS is low and we should give all above command after setting to 4 bit mode  then only we should change RS stae and start entering data**



reference:

https://youtu.be/cXpeTxC3\_A4?si=w1OjAu6fgDIh-wkY





**TASK3:Displaying numbers on a 7-segment LED**

We need to just display number on the 7 segment led using aurdino

steps:

connect all pin properly

**there are two common(it can be both for  powersupply(anode) or it can be both for ground(cathode)) in  which we use only one common here and other is left free**

now it time for code  logic:

we use for loop in which corresponding stuff is made high



***DISCLLAIMER{Mara misconception}:***

***0 or LOW(IN ARDINO) does not alway implies low state similarly 1 or HIGH(in aurdino) does not always implies high  state IN CIRCUIT***

&#x20; ***IT ALL  DECIDED BY THE POTENTIAL DIFFERENCE,HOW WE SET POTENTIAL DIFFERENCE DECIDE THE STATE***

***HERE ON CODE WE CAN SEE 0 USED TO LIGH UP AN CERTAIN SEGMENT BCZ OUR 7  SEGMENT LED IS SUBJECTED TO 5V POWER SUPPLY ALL TIME SO WE USE 0 THEREBY CREATE AN POTENTIAL DIFFERNCE*** 

***WHICH SEND SIGNALS***

&#x20;         ***AT THE SAME TIME IF WE USE 1 THEN NO POTENTIAL DIFFERENCE IS CREAATED AND NO SIGNAL GOES AND ACT LIKE LOW STATE IN CIRCUIT***

***CHANCE FOR CONFUSION:***

***POTENTIAL DIFFERENCE PRESENT----->SIGNAL GOES----->HIGH STATE IN CIRCUIT***

***1---->CREATE A HIGH STATE AT  AN POINT***

***IF 1-----1 => IT IMPLIES LOW STATE IN CIRCUIT BCZ NO POTENTIAL DIFFERENCE AND NO SIGNAL SEND***



*REFERENCE:
FOR CONNECTION :https://youtu.be/Ss4W2FBGr1Y?si=znKjRYDWynhUdYrj*

*FOR CODE:https://www.youtube.com/redirect?event=video\_description\&redir\_token=QUlxb01IYjRSSUNRR0hRbjgtTHM5VnJZMGlCc3xBSTVJdTV1M2NPdVRsQ1lISWdITHVhOWpYUGZGMUgwN2JEdXU3ZVIyZWpNZWpYVWdXWkJ5RlExVXFOb0RVRkhvMFVlLXRlSTB4eDVjNjlBNnVtYmpVSWJRQjZQSGVhUUk2S25V\&q=https%3A%2F%2Fsimplecircuitslol.blogspot.com%2F2024%2F03%2Farduino-code-7-segment-display.html\&v=Ss4W2FBGr1Y*























