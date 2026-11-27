Task: Design and Implement an FM Receiver Using RTL-SDR and GNU Radio  
 **Requirements**  
1\. Configure the RTL-SDR and select a local FM broadcast station.   
2\. Develop a GNU Radio flowgraph incorporating necessary elements.  
3\. Visualize the received RF spectrum .Recover the transmitted audio and play it through the system's audio output.  
 **Deliverables**  
 1\. A working GNU Radio flowgraph.   
 2\. A demonstration of reception and intelligible audio playback from a local FM station 

***LET BEGIN WITH CONCEPT:***  
*WE  ARE LIVING IN AN WORLD SURROUNDED BY SIGNALS, IN THIS TASK WE NEED  TO CAPTURE AN AUDIBLE FM SIGNAL*  
*FOR THAT  USE RTL-SDR*

*WHAT IS RTL SDR*  
      *IT USED FOR RECIEVING SIGNAL HERE*

*IN THIS TASK WE NEED TO INSTALL GNU RADIO*  
*WE USE DIFFERENT BLOCK IN GNU RADIO TO RECIEVE THE SIGNAL ,TUNE SIGNAL AND FILTER SIGNAL*  
   
***RECIEVE SIGNAL:***  
*WE USED **Soapy RTLSDR  SOURC**E BLOCK*   
     *Here  it is used to stream samples from a RTLSDR device(i.e . it act as an receiver)*

*PRE REQUIRED KNOWLEDGE BEFORE RECIEVING SIGNAL:*  
***SAMPLE RATE**: IT IS LIKE NUMBER OF SIGNAL PROCESSED ,RECIEVED IN AN SECOND REPRESENTED IN UNIT OF FREQUENCY THAT IS HERTZ*

*WE USED HERE ABOUT 2.04MHz Bcz We need to capture an large amount of signal*   
*(it has an relation with bandwidth)*  
***Bandwidth**: it is range of frequency or we can say as difference btw upper and lower frequency in an continuous band of frequency*

***Central frequency**: it is frequency we are looking in an range of frequency(just hoping for audible signal at this point)*  
*We create **QT GUI RANGE** so we can adjust the central frequency(the stuff we are looking for) at   the time we checking for require frequency*

   
 ***QT GUI TIME SINK :** Used to display multiple signal in time*  
***QT GUI FREQUENCY SINK :** Used to display multiple signal in time*

***BY THIS MUCH U HAVE SUCEESSFULLY RECIEVED SIGNAL AND U CAN SEE IT ON RUNNING WHILE RUNNIG U NEED TO SELECT AN CENTRAL FREQUENCY THEN ON THAT FREQUENCY FOLLOWING CHANGES AND PROCEDURE WILL TAKE PLACE TO GET ULTIMATE REQUIREMENT(AUDIO NEEDED)*** 

***PROCESS 2 FILTERING:***

*For that we  need **RATIONAL RESAMPLER***

***WHAT RATIONAL RESAMNPLER CAN DO:***  
  ***It will decrease the sample rate***

***WHY DO  WE NEED THEM:***  
***—-----\>WE CAN DECREASE SAMPLE RATE ACCORDINGLY WHICH WILL BE 48KHz AT END OF FLOWCHART***   
***—----\>BY DECREASING SAMPLE RATE AND FOCUSING ON ONE FREQUENCY MAINLY(CENTRAL FREQUENCY ) IT AUTOMATICALLY FILTER OTHER(i.e. It will be mainly focusing on central frequency we give)***

***PROCESS 3  PROCESSING:***  
  ***Here we  need to read the data  in IQ signal for that we use  WBFM Reciever***

***GK about signal:***  
***Fm signal and so on have two component with them they are***  
***in \-phase (I) and Quadrature(Q) together called IQ signals***  
***They have phase difference of 90***  
   
***QUADRATURE RATE:Rate at which IQ signals are captured***  
***Audio Decimation: decrease sample rate such that it can be played bby speakers***

***PROCESS 4 HEARNG SIGNAL***  
***TO HEAR THE  PROCESSED SIGNAL WE NEED AUDIO SINK WHICH IS SET AT SAMPE RATE OF 48KHz WHICH IS COMMON SAMPLE RATE FOR SPEAKERS IN DEVICE***

***Part2***  
***Transmitting an radio signal using HackRF One***

*We select an .wav file containing audio to be transmitted in **Wave File Source***  
*Now we need to decide our **audio rate(**the rate at which our audio signal to be processed,industrial standard is 48kHz**)** and **quadrature rate(**the rate at which IQ signals to be processed ,(note: quadrature rate is an multiple of audio rate)**)***  
*For this purposes we use **WBFM Transmit block***

***Note1:minimum sample rate of HackRF One is 2MHz therefore sample rate is 2 MHZ***  
***Note2:OsmocomSink is responsible for converting IQ signal into radio signal and transmitting through HackRF One***

*We use **Ration Resampler** here bcz rate of IQ SIGNAL (i.e. quadrature rate) should be equal to 2MHz(sample rate) in Osmocom Sink then only our iq signal can be converted to proper radio signal and transmitted*

*So we place Rational Resampler in between WBFM Transmit and Osmocom Sink*   
*To find interpolation and decimation we need to divide 2Mhz with our quadrature rate(here i used  480kHz, so on dividing we  get fraction of 25/6, so interpolation is 25 and decimation is 6\)*  
*So now we can successfully transmit,we can also add QT GUI Frequency Sink*  
*To see the graph*  

   
 