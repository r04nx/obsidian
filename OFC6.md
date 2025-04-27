![https://lh7-rt.googleusercontent.com/docsz/AD_4nXfmlKCfzzMU_ItXs5lED_k2-B5ZHYUVA09Ity712NxTk17PxiQMYVBHOLodet3S836q3PLYyYFvdn8sJCe0Gb41Cv71KLmXmol0AP7q-xoqIS7FH8uT1_fZcoO-Y-r3JYbA0gyJ2A?key=9IsdFjwKLUUEcTFPSyJtVewv](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf9TX7YPxEKbXa7yl5m1saDKjf44SdNMC2vwF8aXX0YJtvb8oKYgoaoNLP75ky_MpcSDQc-QgzTqbfaENV91V1j0FGsFby9JTQevL-s379nKzjtV66Y8oIdvSC08FVg5ocRsrwtxtbSmrQmZboIfw?key=MstmW3FLUUiHdoaLYRUB-73p)
> [!info] Student & Experiment Details
> 
> | | |
> |:--|:--|
> |**Name**|**Rohan Prakash Pawar**|
> |**UID**|**2023201020**|
> |**Exp no.**|**06**|
> |**Aim**|**To Measure Bit Error Rate.**|

---

> [!info] Equipment Used
> 
> - **Scientech 2501A TechBook** (with Power Supply)
>     
> - **Optical Fiber Cable**
>     

---
## Theoretical Background

> [!abstract] Introduction In digital communication, data is transmitted as binary digits (0s and 1s). Transmission imperfections like noise and dispersion may cause bit errors. **Bit Error Rate (BER)** quantifies these errors, providing a measure of link quality.

The BER formula is:
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXem50kVdT5kUopQ__LrqWUeny5zZ6Yqwg6LNAr212_XY2LKjz43HCBLdb4dItadHW2B7c99pO-PLXbD-jE17e16izpYlwNj92gmZ1eWSfQctgxSWuq6h1zyJ2CkO4hHO_VsmUOwPuBvoQORA0wUl6M?key=MstmW3FLUUiHdoaLYRUB-73p)
Where:

- **E** = Number of erroneous bits detected
    
- **N** = Total bits transmitted (N = CLK × Td)
    

Lower BER = higher reliability. Higher BER = more system errors.

---

> [!info] Importance of BER in Optical Fiber Communication
> 
> - **Attenuation**: Loss of signal strength.
>     
> - **Dispersion**: Overlapping of pulses.
>     
> - **Noise**: Internal and external disturbances.
>     
> - **Physical Defects**: Bending, impurities.
>     
> - **Synchronization Errors**: Timing mismatches.
>     
> - **Encoding Limitations**: Effects of modulation methods.
>     

Understanding BER helps enhance the performance and reliability of fiber optic systems.

---

> [!info] Factors Affecting BER
> 
> - **Low Noise**: Minimal errors, low BER.
>     
> - **High Noise**: Increased distortion, high BER.
>     
> - **Clock Frequency Variations**: Faster clocks may cause synchronization errors leading to higher BER.
>     

---

## Procedure

> [!checklist] Procedure
> 
> 1. Power the Scientech 2501A TechBook.
>     
> 2. Turn off all fault switches.
>     
> 3. Make connections as per the diagram.
>     
> 4. Link 'a' to 'b' and 'c' to 'd' with patch cords.
>     
> 5. Feed a 64 KHz clock to the Data Generator.
>     
> 6. Connect Data Generator output to the emitter.
>     
> 7. Join emitter output to detector input with fiber.
>     
> 8. Connect detector output to Noise Generator "Signal In".
>     
> 9. Set switch to Bit Error Counter mode.
>     
> 10. Set mode to "Digital" for quick emitter switching.
>     
> 11. Power on the TechBook.
>     
> 12. Set noise to minimum initially.
>     
> 13. Start error counting and record results.
>     
> 14. Repeat for various clock rates and noise levels.
>     

---

## Connection Diagram
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXecK1_ThPb0v96BNM3s3G7k25iL36s2yiOwTMS1FeffqghiEeUFMHsyc04Sf1qDxe4NG_JttMzG9wyD-KGSfxZbKwQ75v5gYH7QMqsDrkO2WPN5YmFdbKRgM_ltj5CZ-rjyraJTODH_jlZhH73sFNY?key=MstmW3FLUUiHdoaLYRUB-73p)
---

## Experimental Observations

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXez0ke6y3FJcfLeZuLUTpUQp0dBjgTTmLWrMVKSWB8uz4sdMUgeCEdzQrnoNDE2KIT8lvHd9YYgZzUSF5wciWoGzTP9QPHTUN4tUVmeVpXCLMIna33T9zKdvRGNNd-PysyJoXZwxWAs2iSbUgwLgXU?key=MstmW3FLUUiHdoaLYRUB-73p)

> [!example] Low Noise Results


> Noise Level-1 (Set the “Noise Level” knob to some lower level)

| Sr. No. | Clock Frequency | Time (Td) | Total Bits (N) | Bit Errors (E) | BER (E/N) |
| :-----: | :-------------: | :-------: | :------------: | :------------: | :-------: |
|    1    |     64 KHz      |   5 sec   |      320       |       7        |  0.0219   |
|         |                 |  10 sec   |      640       |       13       |  0.0203   |
|    2    |     128 KHz     |   5 sec   |      640       |       15       |  0.0234   |
|         |                 |  10 sec   |      1280      |       30       |  0.0234   |
|    3    |     256 KHz     |   5 sec   |      1280      |       15       |  0.0117   |
|         |                 |  10 sec   |      2560      |       30       |  0.0117   |

> [!example] High Noise Results

> Noise Level-2 (Set the “Noise Level” knob to some higher level)

|Sr. No.|Clock Frequency|Time (Td)|Total Bits (N)|Bit Errors (E)|BER (E/N)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|64 KHz|5 sec|320|155|0.4843|
|||10 sec|640|278|0.4340|
|2|128 KHz|5 sec|640|259|0.4040|
|||10 sec|1280|475|0.3740|
|3|256 KHz|5 sec|1280|275|0.2148|
|||10 sec|2560|512|0.2000|

---

> [!summary] Conclusion Through this study:
> 
> - Higher noise levels increased bit errors.
>     
> - Faster clock rates led to synchronization issues.
>     
> - Managing noise and clock frequency improves system reliability.
>     

