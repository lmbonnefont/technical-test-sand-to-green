# RegenWise Technical Test: Irrigation Smart-Pipeline 💧

Welcome to the RegenWise technical assessment!

This repository contains a prototype of our **Smart Irrigation Engine**. Our mission is to transform arid lands into green ecosystems by optimizing every drop of water. This pipeline processes soil sensor data to calculate precise irrigation needs.

---

## 🏗 Codebase Architecture

The project is structured for simplicity and readability:

1.  **`main.py`**: The entry point to run the engine.
2.  **`use_cases.py`**: Orchestrates the irrigation pipeline.
3.  **`serialization.py`**: Handles loading and parsing data from external sources.
4.  **`lib.py`**: The core business logic for irrigation calculations.
5.  **`entities.py`**: Contains the domain models (e.g., `SensorReading`, `IrrigationAdvice`).


## 🎯 Technical Test Objectives

Your mission is to improve this prototype to make it **reliable, extensible, and scalable**.

### 1. Setup & Exploration
- Clone the repository.
- Create a virtual environment (python -m venv .venv) and install dependencies using `make install`.
- Explore the codebase to understand how data flows from `readings.csv` to the final advice.

### 2. Code Quality & Bug Hunting
- Identify and fix intentional bugs in the pipeline (e.g., data filtering, logical inconsistencies).
- Clean up any "dead code" or unused constants left behind during rapid prototyping.
- Improve the logging and error handling for corrupted data.

### 3. Extensibility: Climate Zones
We use the **Trewartha climate classification** to adjust our irrigation strategies.
- Implement logic to differentiate calculations for **Arid (B)** and **Tropical (A)** zones. 
- In Arid environments, we will add 1L per percentage point below target and take into account the wind speed in the target_humidity (target_humidity = 30.0 + (reading.et0 * kc * 10.0) + (reading.wind_speed * 0.1)). 
- In Tropical environments, we will add 0.25L per percentage point above target. 
- Ensure your design allows for the **easy addition of new zones** (e.g., Subtropical C, which will take into account the air temperature in the target_humidity).

---

## 🧠 AI Usage Policy

In RegenWise, AI is a partner, not a replacement. **The use of Copilot, ChatGPT, Claude, etc., is authorized and encouraged.**
---

## 🛠 Usage

### Prerequisites
- Python 3.10+
- `make`

### Installation
```bash
make install
```

### Run the Pipeline
```bash
export PYTHONPATH=$PYTHONPATH:.
python3 src/main.py
```

### Run Tests
```bash
make test
```
