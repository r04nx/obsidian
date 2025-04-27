# 📊 Experiment 6: Measuring Bit Error Rate

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfu0kJWCjwUOk02fJs2OeKe5HYjR0hxYlXIpzXmZsYKRbd3dvDDjkrS2O_ADejPg88bsGPKuvPypnBXhO1uljO13uyDl1F7JnzHJnhkuz2PoyFz5KM98mB0hf_xrH8f18RG7hTV0XAzmXrNAYl4lw?key=MstmW3FLUUiHdoaLYRUB-73p)

> [!info] Student Details
> | Parameter | Value |
> | :---------- | :----------------------------- |
> | **Name**    | **Rohan Prakash Pawar**        |
> | **UID**     | **2023201020**                 |
> | **Exp no.** | **06**                         |
> | **Aim**     | **To Measure Bit Error Rate.** |

## 🔬 Equipment Required
- Scientech 2501A TechBook with Power Supply and mains cord
- Optical Fiber Cable

## 📚 Theory

In digital communication systems, data is transmitted in the form of binary bits (0s and 1s). However, due to various channel imperfections and noise, some bits may be received incorrectly, leading to transmission errors. **Bit Error Rate (BER)** is a fundamental parameter that quantifies these errors, providing insight into the reliability and performance of a communication link.

BER is defined as:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcmFzQt1zEfSFvx6FbgMS-fUgDMSzhrnrDEwNV0dMAIQNjq6ebsGvxvO8mrga6egCc452sJKGWVCqlvZQf9KkGQtX5jXTo9uJA--lU8EUz3nktE2yutr9ebFJDtEw9VQ0VAkSkXutyT0ZegUknZGzo?key=MstmW3FLUUiHdoaLYRUB-73p)

where:

- **E** = Number of erroneous bits received
- **N** = Total number of bits transmitted (CLK×Td), where CLK is the clock frequency and Td is the duration of transmission.

> [!note]
> A lower BER indicates a more reliable communication system, while a higher BER suggests increased data corruption, requiring error correction techniques.

### 🔍 Significance of BER in Optical Fiber Communication

Optical fiber communication is widely used due to its advantages such as high bandwidth, long-distance transmission capability, and low signal attenuation. However, like any transmission medium, optical fibers are prone to **bit errors** caused by:

1. **Attenuation**: Loss of signal power as light propagates through the fiber.  
2. **Dispersion**: Broadening of optical pulses, leading to inter-symbol interference.  
3. **Noise**: Introduced by electronic components, external interference, or thermal fluctuations.
4. **Optical Fiber Bending and Impurities**: Physical deformations in the fiber can cause losses and increase BER.  
5. **Synchronization Errors**: Mismatches between transmitter and receiver timing lead to misinterpretation of bits.  
6. **Modulation and Detection Limitations**: The method used to encode digital data into optical signals (e.g., NRZ, Manchester coding) affects BER.

By measuring BER, engineers can analyze how different conditions, such as noise levels and clock frequency, impact the performance of an optical fiber communication system.

### 📈 Impact of Noise and Clock Frequency on BER

By conducting multiple observations at different noise levels and clock frequencies, we can analyze how each factor affects BER:

#### At Low Noise Levels 🔉
- The received signal closely matches the transmitted signal.  
- Minimal bit errors are observed.  
- BER remains low.

#### At High Noise Levels 🔊
- The signal becomes distorted due to increased interference.  
- The receiver misinterprets some bits, leading to a higher BER.

#### At Different Clock Frequencies ⏱️
- Higher clock frequencies result in faster data transmission, but also increase the likelihood of synchronization errors and inter-symbol interference.  
- The optimal frequency for minimal BER can be determined from observations.

## ⚙️ Procedure

1. Connect the TechBook Power Supply with mains cord to TechBook Scientech2501A.
   - Ensure that all switched faults are off.
2. Establish connections according to the connection diagram.

3. Connect patch cords between points 'a & b' and 'c & d'.

4. Connect the 64 KHz Clock from Clock generator to the Clock input of the Data generator.

5. Route the Data Generator output to the emitter input.

6. Connect the fiber optic cable between the emitter output and detector input terminals.

7. Direct the detector output to the 'Signal In' socket of the Noise Generator.

8. Position the selection switch toward the Bit Error Counter Block for error counting.

9. Set the mode switch SW1 to Digital position to operate the emitter in Digital mode, enabling the LED to rapidly alternate between 'On' and 'Off' states.

10. Power on the TechBook by switching on its Power Supply.

11. Set the Noise Generator's Level potentiometer near the minimum position initially.

12. Initiate counting by pressing the Start/Stop switch, observe the Error Count on the 7-Segment Display for a specific time duration (Td), then press Start/Stop again to terminate counting.

13. Document readings for various clock frequencies, time durations, and noise levels in the observation table.

14. Adjust the Level potentiometer between minimum and maximum positions to analyze how variable noise affects the error count.

## 📊 Connection Diagram



## 📝 Observation

### Noise Level-1 (Lower noise setting)

| Sr No. | CLK Frequency | Time Duration (Td) | Total Bits (N) N = (CLK×Td) | Bit Error Value (E) | Bit Error Rate (E/N) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **64KHz** | **5Sec** | **320** | **7** | **0.0219** |
|  |  | **10Sec** | **640** | **13** | **0.0203** |
| **2** | **128KHz** | **5Sec** | **640** | **15** | **0.0234** |
|  |  | **10Sec** | **1280** | **30** | **0.0234** |
| **3** | **256 KHz** | **5Sec** | **1280** | **15** | **0.0117** |
|  |  | **10Sec** | **2560** | **30** | **0.0117** |

### Noise Level-2 (Higher noise setting)

| Sr No. | CLK Frequency | Time Duration (Td) | Total Bits (N) N = (CLK×Td) | Bit Error Value (E) | Bit Error Rate (E/N) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **64KHz** | **5Sec** | **320** | **155** | **0.4843** |
|  |  | **10Sec** | **640** | **278** | **0.434** |
| **2** | **128KHz** | **5Sec** | **640** | **259** | **0.404** |
|  |  | **10Sec** | **1280** | **475** | **0.374** |
| **3** | **256 KHz** | **5Sec** | **1280** | **275** | **0.2148** |
|  |  | **10Sec** | **2560** | **512** | **0.2** |

## 🔍 Conclusion

This experiment involved a thorough analysis of Bit Error Rate (BER) in optical fiber communication systems. We conducted measurements under various conditions, specifically examining how different noise levels and clock frequencies impact transmission reliability. 

Our observations revealed that increased noise levels significantly degraded signal quality, resulting in higher error rates. We also noted how transmission speeds (clock frequencies) affected the system's performance, with certain combinations of parameters yielding better results than others.

The experiment highlighted several critical factors affecting optical fiber communication quality:
- Signal-to-noise ratio plays a fundamental role in determining BER
- Proper synchronization is essential for accurate data interpretation
- Optical fiber quality directly impacts transmission integrity
- External interference must be minimized for optimal performance

These findings emphasize the importance of precise system calibration and noise management techniques in developing robust digital communication networks. By understanding and controlling these variables, engineers can design more reliable optical fiber communication systems with minimized error rates.
