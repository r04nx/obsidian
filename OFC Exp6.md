# 📊 Experiment 6: Measuring Bit Error Rate

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfu0kJWCjwUOk02fJs2OeKe5HYjR0hxYlXIpzXmZsYKRbd3dvDDjkrS2O_ADejPg88bsGPKuvPypnBXhO1uljO13uyDl1F7JnzHJnhkuz2PoyFz5KM98mB0hf_xrH8f18RG7hTV0XAzmXrNAYl4lw?key=MstmW3FLUUiHdoaLYRUB-73p)

> [!info] Experiment Details
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
