![https://lh7-rt.googleusercontent.com/docsz/AD_4nXfmlKCfzzMU_ItXs5lED_k2-B5ZHYUVA09Ity712NxTk17PxiQMYVBHOLodet3S836q3PLYyYFvdn8sJCe0Gb41Cv71KLmXmol0AP7q-xoqIS7FH8uT1_fZcoO-Y-r3JYbA0gyJ2A?key=9IsdFjwKLUUEcTFPSyJtVewv](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfu0kJWCjwUOk02fJs2OeKe5HYjR0hxYlXIpzXmZsYKRbd3dvDDjkrS2O_ADejPg88bsGPKuvPypnBXhO1uljO13uyDl1F7JnzHJnhkuz2PoyFz5KM98mB0hf_xrH8f18RG7hTV0XAzmXrNAYl4lw?key=MstmW3FLUUiHdoaLYRUB-73p)

| Name        | Rohan Prakash Pawar            |
| :---------- | :----------------------------- |
| **UID **    | **2023201020**                 |
| **Exp no.** | **06**                         |
| **Aim**     | **To Measure Bit Error Rate.** |

**Equipments Required :**  
* Scientech 2501A TechBook with Power Supply and mains cord
* Optical Fiber Cable

**Theory:** 

In digital communication systems, data is transmitted in the form of binary bits (0s and 1s). However, due to various channel imperfections and noise, some bits may be received incorrectly, leading to transmission errors. **Bit Error Rate (BER)** is a fundamental parameter that quantifies these errors, providing insight into the reliability and performance of a communication link.

BER is defined as:
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcmFzQt1zEfSFvx6FbgMS-fUgDMSzhrnrDEwNV0dMAIQNjq6ebsGvxvO8mrga6egCc452sJKGWVCqlvZQf9KkGQtX5jXTo9uJA--lU8EUz3nktE2yutr9ebFJDtEw9VQ0VAkSkXutyT0ZegUknZGzo?key=MstmW3FLUUiHdoaLYRUB-73p)
where:

* EEE \= Number of erroneous bits received,

* N \= Total number of bits transmitted (CLK×Td), where CLK is the clock frequency and Td is the duration of transmission.

A lower BER indicates a more reliable communication system, while a higher BER suggests increased data corruption, requiring error correction techniques.

#### **Significance of BER in Optical Fiber Communication**

Optical fiber communication is widely used due to its advantages such as high bandwidth, long-distance transmission capability, and low signal attenuation. However, like any transmission medium, optical fibers are prone to **bit errors** caused by:

1. **Attenuation**: Loss of signal power as light propagates through the fiber.  
2. **Dispersion**: Broadening of optical pulses, leading to inter-symbol interference.  
3. **Noise**: Introduced by electronic components, external interference, or thermal fluctuations.

4. **Optical Fiber Bending and Impurities**: Physical deformations in the fiber can cause losses and increase BER.  
5. **Synchronization Errors**: Mismatches between transmitter and receiver timing lead to misinterpretation of bits.  
6. **Modulation and Detection Limitations**: The method used to encode digital data into optical signals (e.g., NRZ, Manchester coding) affects BER.

By measuring BER, engineers can analyze how different conditions, such as noise levels and clock frequency, impact the performance of an optical fiber communication system.

#### **Impact of Noise and Clock Frequency on BER**

By conducting multiple observations at different noise levels and clock frequencies, we can analyze how each factor affects BER:

1. **At Low Noise Levels**:

   * The received signal closely matches the transmitted signal.  
   * Minimal bit errors are observed.  
   * BER remains low.

2. **At High Noise Levels**:

   * The signal becomes distorted due to increased interference.  
   * The receiver misinterprets some bits, leading to a higher BER.

3. **At Different Clock Frequencies**:

   * Higher clock frequencies result in faster data transmission, but also increase the likelihood of synchronization errors and inter-symbol interference.  
   * The optimal frequency for minimal BER can be determined from observations.

**Procedure:**

1. Connect the TechBook Power Supply with mains cord to TechBook Scientech2501A.

   ·Ensure that all switched faults are off.

2. Make the connections as shown in connection diagram.

3. Connect patch cords between ‘a & b’ and ‘c & d’.  
4. Connect the 64 KHz Clock from Clock generator to the Clock in socket of Datagenerator.  
5. Connect Data Generator output to the emitter input.

6. Connect the fiber optic cable between emitter output and detector input.

7. Connect the detector output to ‘Signal In’ socket of Noise Generator.

8. Put the selection switch towards Bit Error Counter Block to count the bit error.  
9. Put the mode switch SW1 to Digital to drive the emitter in Digital mode. This ensuresthat signal applied to the driver input cause the emitter LED to switch quickly between ‘On’ & ‘Off’ states.  
10. Switch ‘On’ the Power Supply of TechBook

11. Initially Adjust Level pot of Noise Generator near left bottom position.  
12. Press the Start/Stop switch and observe the Error Count on 7-Segment Display of BitError Counter for any time duration ‘Td’ and press the Start/Stop switch again to stop.  
13. Record the readings for different clock frequencies/Time duration/Noise level n the following observation table.  
14. Adjust Level pot for minimum and maximum position to observe effect of variablenoise on the error count.

    

**Connection Diagram:**

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcYlF4penobAm0d8Xh2enDpp47QOrXpFSKeg98wwkodFeZUS-4tdL5S84_sGdy1rJBmWoDrZbE_oXX3nfRoTwxVP378d2aGHGz4R2X01BwNBU8WOFZceChOthF4g3h7mSYgl3fYVEmM-G257gg39BA?key=MstmW3FLUUiHdoaLYRUB-73p)

**Readings :** 
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd4ZQ39VOF6HLwZkpm-fs-3HwBMKSJCvwUvTmDhlMiauWKyEQhgrjEDZ8DXBDdmyrVIUHYwFL5fIIgl88bMJ7xizXhIHGs7QoxVkyu4Jgu2O24XJqvlbzrXea6SeLI_3fnAnkmli5_U08dHLHGXstg?key=MstmW3FLUUiHdoaLYRUB-73p)
**Observation :** 

| Noise Level-1 (Set the “Noise Level” knob to some lower level) |                   |                        |                               |                         |                          |
| :------------------------------------------------------------: | :---------------: | :--------------------: | :---------------------------: | :---------------------: | :----------------------: |
|                           **Sr No.**                           | **CLK Frequency** | **Time Duratio n(Td)** | **Total (N)  N \= (CLK\*Td)** | **Bit Error Value (E)** | **Bit Error Rate (E/N)** |
|                             **1**                              |     **64KHz**     |        **5Sec**        |            **320**            |          **7**          |        **0.0219**        |
|                                                                |                   |       **10Sec**        |            **640**            |         **13**          |        **0.0203**        |
|                             **2**                              |    **128KHz**     |        **5Sec**        |            **640**            |         **15**          |        **0.0234**        |
|                                                                |                   |       **10Sec**        |           **1280**            |         **30**          |        **0.0234**        |
|                             **3**                              |    **256 KHz**    |        **5Sec**        |           **1280**            |         **15**          |        **0.0117**        |
|                                                                |                   |       **10Sec**        |           **2560**            |         **30**          |        **0.0117**        |

| Noise Level-2 (Set the “Noise Level” knob to some higher level) |                   |                        |                            |                         |                          |
| :-------------------------------------------------------------: | :---------------: | :--------------------: | :------------------------: | :---------------------: | :----------------------: |
|                           **Sr No.**                            | **CLK Frequency** | **Time Duratio n(Td)** | **Total N N \= (CLK\*Td)** | **Bit Error Value (E)** | **Bit Error Rate (E/N)** |
|                              **1**                              |     **64KHz**     |        **5Sec**        |          **320**           |         **155**         |        **0.4843**        |
|                                                                 |                   |       **10Sec**        |          **640**           |         **278**         |        **0.434**         |
|                              **2**                              |    **128KHz**     |        **5Sec**        |          **640**           |         **259**         |        **0.404**         |
|                                                                 |                   |       **10Sec**        |          **1280**          |         **475**         |        **0.374**         |
|                              **3**                              |    **256 KHz**    |        **5Sec**        |          **1280**          |         **275**         |        **0.2148**        |
|                                                                 |                   |       **10Sec**        |          **2560**          |         **512**         |         **0.2**          |

**Conclusion:**  
In this experiment, we performed a comprehensive analysis of **Bit Error Rate (BER)** in an optical fiber communication system. We measured the BER under different noise levels and clock frequencies, enabling us to understand how various factors affect data transmission reliability. By introducing controlled noise and adjusting clock frequencies, we observed that higher noise levels and increased transmission speeds led to a greater number of bit errors.  
Through this experiment, we understood the critical role of **signal-to-noise ratio (SNR)**, **synchronization**, and **optical fiber quality** in ensuring error-free data transmission. We also learned that minimizing external interference and optimizing system parameters can significantly reduce BER. These findings emphasize the importance of noise management and precise timing in optical fiber communication, which are crucial for developing efficient and reliable digital communication networks.
