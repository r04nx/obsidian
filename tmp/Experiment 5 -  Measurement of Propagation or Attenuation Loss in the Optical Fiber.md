---
share_link: https://share.note.sx/np4tc93z#2sMj3Fl4B7zP+94wl0KbwmxO86K8Vapi/VhGhcAi2p4
share_updated: 2025-03-06T15:31:02+05:30
---


| Field      | Details     |
| ---------- | ----------- |
| **Name**   | Rohan Pawar |
| **UID**    | 2023201020  |
| **Course** | OFC         |
| **Branch** | EXTC        |
|            |             |

## Aim
To measure the propagation or attenuation loss in an optical fiber.

## Theory
### Attenuation in Optical Fiber
Attenuation in optical fibers refers to the reduction in intensity of the light beam with respect to distance traveled through the transmission medium. It is an important consideration in optical fiber communication because it determines the maximum transmission distance before signal regeneration is required.

The main causes of attenuation in optical fibers include:
1. **Absorption**: Due to impurities in the fiber material that convert light energy into heat.
2. **Scattering**: Primarily Rayleigh scattering caused by microscopic variations in the fiber material density.
3. **Bending losses**: Macro-bending and micro-bending cause light to escape from the fiber core.

## Equipment Required
- Scientech 2501A TechBook with Power Supply Cord
- Optical Fiber Cable (0.5m and 1m)
- Scientech Oscilloscope with necessary connecting probe
- Function Generator
- AC Amplifier

## Connection Diagram
![[Pasted image 20250306144604.png]]
*Figure 1: Connection diagram for measurement of attenuation loss*

## Procedure
1. Connect the TechBook Power Supply with mains cord to TechBook Scientech 2501A.
2. Make the connections as shown in the connection diagram:
   - Connect the Function Generator 1 KHz sine wave output to emitter input.
   - Connect 0.5 m optic fiber between emitter output and detector input.
   - Connect Detector output to amplifier input.
3. Put the mode switch SW1 to Analog to drive the emitter in analog mode.
4. Switch 'On' the Power Supply of TechBook and Oscilloscope.
5. Set the Oscilloscope channel 1 to $$ 0.5 \text{ V/Div} $$ and adjust 4-6 div amplitude by using X1 probe with the help of variable potentiometer in Function Generator block at input of emitter.
6. Observe the output signal from detector on Oscilloscope.
7. Adjust the amplitude of the received signal as that of transmitted one with the help of gain adjusts pot in AC amplifier block. Note this amplitude and name it $$ V_1 $$.
8. Now replace the previous fiber optic cable with 1 m cable without disturbing any previous setting.
9. Measure the amplitude at the receiver side again at output of amplifier. Note this value and name it $$ V_2 $$.
10. Calculate the propagation (attenuation) loss with the help of the formula: 
    
$$
α = -[log(V₁/V₂)]/(L₁+L₂)
$$    
    Where:
    - $$ \alpha $$ = loss in nepers/meter (1 neper = 8.686 dB)
    - $$ L_1 $$ = length of shorter cable (0.5 m)
    - $$ L_2 $$ = Length of longer cable (1 m)

## Observations

### Waveforms

1. **Detector output (for 0.5m Cable)**  $$ \text{CH1-0.1V/div; TB-0.5mS} $$
![[Pasted image 20250306150208.png]]
	 
*Figure 3: Detector output for 0.5m Cable*

2. **Detector output (for 1m Cable)** ($$ \text{CH1-0.1V/div; TB-0.5mS} $$)
   ![[Pasted image 20250306150240.png]]
   *Figure 4: Detector output for 1m Cable*

3. **Amplifier output (for 0.5m Cable)** ($$ \text{CH1-0.1V/div; TB-0.5mS} $$)
   ![[Pasted image 20250306150308.png]]
   *Figure 5: Amplifier output for 0.5m Cable*

4. **Amplifier output (for 1m Cable)** ($$ \text{CH1-0.1V/div; TB-0.5mS} $$)
   ![[Pasted image 20250306150322.png]]
   *Figure 6: Amplifier output for 1m Cable*

### Recorded Values
#### Case 1 (0.5m cable):
- $$ V_1 = 14.32 \text{ V} $$ (Amplitude at amplifier output with 0.5m cable)
- $$ V_1 = 2.4 \text{ V} $$ (Amplitude at detector output with 0.5m cable)

#### Case 2 (1m cable):
- $$ V_2 = 8.8 \text{ V} $$ (Amplitude at amplifier output with 1m cable)
- $$ V_2 = 1.44 \text{ V} $$ (Amplitude at detector output with 1m cable)
- $$ L_1 = 0.5 \text{ m} $$ (Length of shorter cable)
- $$ L_2 = 1.0 \text{ m} $$ (Length of longer cable)

## Calculations
Based on the recorded values:

### Amplifier Measurements:
$$ V_1 = 14.32 \text{ V} $$ (for 0.5m cable)
$$ V_2 = 8.8 \text{ V} $$ (for 1m cable)
$$ L_1 = 0.5 \text{ m} $$
$$ L_2 = 1.0 \text{ m} $$

Using the formula for attenuation loss:
$$ \alpha = -[\log(V_1/V_2)]/(L_1+L_2) $$

Substituting the values:
$$ \alpha = -[\log(14.32/8.8)]/(0.5+1.0) $$
$$ \alpha = -[\log(1.627)]/(1.5) $$
$$ \alpha = -(0.2114/1.5) = -0.1409 \text{ nepers/meter} $$

Converting to decibels:
$$ \alpha = -0.1409 \times 8.686 \text{ dB} = -1.224 \text{ dB} $$

### Detector Measurements:
$$ V_1 = 2.4 \text{ V} $$ (for 0.5m cable)
$$ V_2 = 1.44 \text{ V} $$ (for 1m cable)
$$ L_1 = 0.5 \text{ m} $$
$$ L_2 = 1.0 \text{ m} $$

Using the formula for attenuation loss:
$$ \alpha = -[\log(V_1/V_2)]/(L_1+L_2) $$

Substituting the values:
$$ \alpha = -[\log(2.4/1.44)]/(0.5+1.0) $$
$$ \alpha = -[\log(1.667)]/(1.5) $$
$$ \alpha = -(0.2219/1.5) = -0.1479 \text{ nepers/meter} $$

Converting to decibels:
$$ \alpha = -0.1479 \times 8.686 \text{ dB} = -1.285 \text{ dB} $$
### Calculations Handwritten:
![[Pasted image 20250306152208.png]]

*Figure 7: Calculation of attenuation loss*
## Conclusion

![[Pasted image 20250306152045.png]]
