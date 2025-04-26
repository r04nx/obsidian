# 📊 Experiment 6: Measuring Bit Error Rate in Optical Fiber Communication

![[ofc_banner.jpg]]

> [!info] Experiment Details
> - **Name:** Rohan Prakash Pawar
> - **UID:** 2023201020
> - **Experiment No:** 06
> - **Aim:** To Measure Bit Error Rate in Optical Fiber Communication Systems

## 🔬 Equipment Required

> [!note] Essential Equipment
> - Scientech 2501A TechBook with Power Supply and mains cord
> - Optical Fiber Cable

## 📚 Theoretical Background

> [!abstract] What is Bit Error Rate?
> In digital communication systems, data is transmitted as binary bits (0s and 1s). Due to channel imperfections and noise, some bits may be received incorrectly. **Bit Error Rate (BER)** quantifies these errors, providing insight into the reliability and performance of a communication link.

### Definition of BER

BER is mathematically defined as:

![[BER_formula.jpg]]

Where:
- **E** = Number of erroneous bits received
- **N** = Total number of bits transmitted (CLK×Td)
  - CLK = Clock frequency
  - Td = Duration of transmission

> [!tip] Interpretation
> A lower BER indicates a more reliable communication system, while a higher BER suggests increased data corruption, requiring error correction techniques.

### Significance in Optical Fiber Communication

Optical fiber communication offers high bandwidth, long-distance transmission capability, and low signal attenuation. However, like any transmission medium, optical fibers are prone to **bit errors** caused by:

1. **Attenuation** ↓ - Loss of signal power as light propagates through the fiber
2. **Dispersion** 📈 - Broadening of optical pulses, leading to inter-symbol interference
3. **Noise** 🔊 - Introduced by electronic components, external interference, or thermal fluctuations
4. **Optical Fiber Bending and Impurities** - Physical deformations causing signal losses
5. **Synchronization Errors** ⏱️ - Timing mismatches between transmitter and receiver
6. **Modulation and Detection Limitations** - Impact of encoding methods (e.g., NRZ, Manchester coding)

By measuring BER, engineers can analyze how different conditions impact system performance.

### Impact of Noise and Clock Frequency

> [!important] Key Factors Affecting BER
> Our experiment examines how noise levels and clock frequencies influence BER:

#### At Low Noise Levels 🔉
- The received signal closely matches the transmitted signal
- Minimal bit errors are observed
- BER remains low

#### At High Noise Levels 🔊
- The signal becomes distorted due to increased interference
- The receiver misinterprets more bits
- Higher BER is observed

####
