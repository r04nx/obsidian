# Phase 2: Advanced Optimization Framework

## Introduction
This document outlines our progress and achievements in Phase 2 of the project, following the completion of Phase 1. After thorough analysis and evaluation, we moved forward with more sophisticated approaches to optimize data transmission using LoRa devices.

## Key Findings and Decisions

After Phase 1, we reached an important conclusion: **no single compression algorithm is perfect or universal for all scenarios**. This insight led us to consider implementing multiple compression algorithms and selecting them dynamically based on various factors including:

- Data type
- Criticality of information
- Payload size
- Transmission distance
- Environmental conditions
- Other relevant physical parameters

We conducted extensive research on potential approaches, including academic literature review and patent analysis, to ensure our solution would be both innovative and effective.

## ML-Based Optimization Framework

Based on our research, we determined that a Machine Learning (ML) approach would be optimal for building a comprehensive framework. Our solution involves:

- A **tinyML model** deployed on edge devices
- Dynamic optimization of transmission performance
- Real-time adaptation to surrounding environmental conditions
- Payload-specific optimizations

## Benchmarking Tool Development

To validate our approach, we created a specialized benchmarking tool that:

- Simultaneously observes and computes performance metrics on the device itself
- Provides real-time feedback through a Captive Web Portal interface
- Ensures testing conditions remain consistent across different scenarios

The following screenshots demonstrate our benchmarking tool in action:
![[Pasted image 20250501110546.png]]
![[Pasted image 20250501110600.png]]
![[Pasted image 20250501110517.png]]
![[Pasted image 20250501111010.png]]
## Hardware Limitations and Solutions

### Initial Hardware Specifications
Our initial implementation utilized the following hardware:
- **LoRa TTGO T1 and T3 Display boards**
- 2MB RAM and 8MB Flash memory

### Hardware Challenges
After initial testing, we discovered that the TTGO devices were not capable of handling the computational workload required for our sophisticated ML-based approach. This limitation led us to explore alternative architectures.

### Architectural Evolution
We developed an improved system architecture that incorporates an external Single Board Computer (SBC), which:

1. Preprocesses data and payload with full OS support
2. Offloads processing, compression, and encoding operations
3. Transmits processed payload to the TTGO board via network

#### Communication Methods:
- **Current Implementation**: WiFi network using access point and client mode
- **Future Implementation**: Direct communication via:
  - Serial communication/COM port
  - GPIO pins connecting SBC and LoRa TTGO board

## TinyML Model Development

### Data Collection and Training
We've made significant progress in developing our TinyML model:

1. Collected approximately 1,000 data transmission entries using traditional approaches
2. Generated comprehensive benchmarking results
3. Trained an ML model focused on:
   - Error reduction
   - Signal-to-Noise Ratio (SNR) improvement
   - Received Signal Strength Indicator (RSSI) optimization

Despite the complexity and time-intensive nature of this sophisticated ML model development, we've achieved a significant milestone with **95.9% accuracy**.

### Model Optimization for Edge Deployment
To deploy the model on resource-constrained edge devices, we:

1. Generated the initial model in H5 format (serialized version)
2. Converted the model using float16 precision to:
   - Reduce the model size to just a few kilobytes
   - Optimize performance for edge deployment

### Implementation Strategy
Our implementation plan involves:

1. Transferring the optimized model to an SD card
2. Porting the model into the SPIFFS (SPI Flash File System) on the LoRa TTGO board
3. Loading the model as needed during operation

### Software Integration
We've developed a `model_handler.h` file, compiled using Python to generate C++-compatible code, which:
- Handles model operations
- Enables efficient execution on the target hardware
