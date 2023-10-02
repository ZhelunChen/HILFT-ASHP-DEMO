> **Note**: 
>
> For better readability of this document, it is recommended to use a Markdown viewer or tool.
>
> **Disclaimer**: 
> 
> The information contained in this document is for general information purposes only. While we strive to keep the information up to date and correct, we make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability with respect to the content provided. Any reliance you place on such information is strictly at your own risk.
> 
> Certain commercial entities, equipment, or materials may be identified in this document in order to describe an experimental procedure or concept adequately. Such identification is not intended to imply recommendation or endorsement by the National Institute of Standards and Technology, nor is it intended to imply that the entities, materials, or equipment are necessarily the best available for the purpose.

## Table of Contents

Overview
- [Introduction](#introduction)
- [Repository Structure](#repository-structure)
- [Data Description](#data-description)


Technical Details
- [Methodology](#methodology)
- [Software Testbed](#software-testbed)
- [Hardware Testbed](#hardware-testbed)
  - [System Configuration](#system-configuration)
  - [Local Control Sequence](#local-control-sequence)
- [Test Scenarios](#test-scenarios)

Additional Information
- [Contact Information](#contact-information)
- [Cite the Datasets](#cite-the-datasets)
- [References](#references)

## Introduction
This document provides comprehensive details of the datasets generated from the project titled, "Hardware-in-the-Loop Laboratory Performance Verification of Flexible Building Equipment in a Typical Commercial Building." This project is financially supported by the U.S. Department of Energy under grant number EE-0009153. These datasets are obtained from extensive hardware-in-the-loop (HIL) testing of an Air Source Heat Pump (ASHP) system at the National Institute of Standards and Technology (NIST), conducted under a diverse range of conditions and operational settings. 

## Repository Structure
**[data](data)** contains all datasets. This folder contains three levels of subfolders:
- Level-1 (Atlanta, Buffalo, NewYork, Tucson): These folders present different locations where testing was performed.
- Level-2 (Eff, Shed, Shift): These folders present various operational scenarios for the Air Source Heat Pump system.
- Level-3 (Default, DenOcc, EnergySave, etc.): These folders present specific case scenarios under the respective operational scenario. These scenarios are further explained in [Test Scenarios](#test-scenarios).

**[assets](assets)** contains related figures, metadata, and data schema.

## Data Description
For each scenario, there are two files: 
- `data.csv`: Official dataset. Refer to [metadata](assets/metadata.csv) for data point definitions.
- `raw.mat`: Raw HIL simulation data.

See `assets/ashp_brick.ttl` for the Brick model that represents the data points and their relationships. The following figure shows the data point relationships created under the Brick model.

![The Schematic Diagram of the ASHP Brick Model](assets/ashp_brick_diagram.jpg)

## Methodology
The datasets in this repository were generated using an Air Source Heat Pump Hardware-In-the-Loop Flexible load Testbed (i.e., ASHP HILFT). The figure below depicts the overall framework of a HILFT, which includes three parts: a virtual building model, a Grid-interactive Efficient Building (GEB) control model, and a hardware testbed. The virtual building model further includes a zone load model, an occupant comfort & behavior model, and an airflow model. More details about the development and integration of the HILFT can be found in [^1].

![Framework of the HILFT and Associated Data Flow Schema](assets/hil_approach.jpg)

## Software Testbed
### Zone Load Model
The zone load model was adapted from [Commercial Prototype Building Models](https://www.energycodes.gov/prototype-building-models). The highlighted zone, **Perimeter_ZN_1**, was selected for HIL study while other zones were served by ideal load systems within EnergyPlus. 

![Small Office Building](assets/small_office_building.png)

### Occupant Behaviors and Airflow Simulation
The occupant behavior model was adapted from Langevin et al. [^2]. Indoor airflow simulation was used to enhance the simulation of the local ambient environment of each occupant agent in the model, using the approach documented in [^3].

## Hardware Testbed
### System Configuration
The system is a two-stage ASHP. The figure below depicts the system configuration. THe ASHP HILFT utilizes the NIST ASHP testing facility, which is equipped with two environmental chambers that emulate indoor and outdoor air conditions. Water-cooled, electrically heated AHUs are included in both chambers to create the outdoor weather conditions and the zone load. 

![Air Source Heat Pump](assets/ashp_diagram.jpg)

### Local Control Sequence
The heat pump system is controlled based on the zone return air temperature. When return air temperature is 0.28 °C (0.5 °F) higher than the cooling setpoint, the heat pump operates in low-speed mode until the temperature drops below the cooling setpoint. When return air temperature is 0.56 °C (1 °F) above the cooling setpoint, the heat pump operates in high-speed mode until the temperature drops below 0.28 °C (0.5 °F) above the cooling setpoint and then switches back to low-speed mode.

## Test Scenarios
This data repository includes real-time HIL ASHP testing data considering:
- Locations: Atlanta, Buffalo, New York, and Tucson; 
- Grid-interactive Efficient Building (GEB) scenarios: Efficiency (Eff), Load Shedding (Shed), and Load Shifting (Shift); 
- Other variations: weather condition, control strategy, building type, occupancy, occupant behavior, and thermal energy storage (TES). 

The **Default** cases (i.e., the third column of the table) were tested with typical summer weather, using a rule-based control (RBC) strategy, with a typical building type, occupancy, and occupant behaviors, and without TES. Each subsequent column header points to the deviation from this default setting.

| Location | GEB Scenario | Default | ExtrmSum | TypShldr | ExtrmWin | MPC | STD2019 | DenOcc | EnergySave | TES | MPC&TES |
| ---      | ---          | ---     | ---      | ---      | ---      | --- | ---     | ---    | ---        | --- | ---     |
| Atlanta  | Eff          | x       | x        | x        | x        | x   | x       | x      | x          |     |         |
|          | Shed         | x       | x        |          |          | x   | x       | x      | x          |     |         |
|          | Shift        | x       | x        |          |          | x   | x       | x      | x          | x   | x       |
| Buffalo  | Eff          | x       | x        | x        | x        | x   | x       | x      | x          |     |         |
|          | Shed         | x       | x        |          | x        | x   | x       | x      | x          |     |         |
|          | Shift        | x       | x        |          | x        | x   | x       | x      | x          | x   | x       |
| New York | Eff          | x       | x        | x        | x        | x   | x       | x      | x          |     |         |
|          | Shed         | x       | x        | x        | x        | x   | x       | x      | x          |     |         |
|          | Shift        | x       | x        | x        | x        | x   | x       | x      | x          | x   | x       |
| Tucson   | Eff          | x       | x        | x        | x        | x   | x       | x      | x          |     |         |
|          | Shed         | x       | x        | x        | x        | x   | x       | x      | x          |     |         |
|          | Shift        | x       | x        | x        | x        | x   | x       | x      | x          | x   | x       |

### Default
- Weather: Typical summer
- Building type: ASHRAE 90.1-2004
- Occupancy: 7
- Occupant behaviors: 4 (57%) occupants care about saving energy with 80% restriction probability
- Thermostat (dual) setpoints:
  - Occupied: 68 degF - 78 degF
  - Setback: 55 degF - 90 degF
- Control strategy: Rule-based control
  - Eff: No reset
  - Shed: Relax setpoints by 2 degF during peak
  - Shift: Precool or preheat by x degF for y hours, then relax setpoints by 2 degF during peak. The actual values of x and y vary by scenario.
- Thermal energy storage: None

### ExtrmSum
Same as **Default** except:
- Weather: Extreme summer

### TypShldr
Same as **Default** except:
- Weather: Typical shoulder

### ExtrmWin
Same as **Default** except:
- Weather: Extreme winter

### MPC
Same as **Default** except:
- Control strategy: Model Predictive Control
  - Eff: Minimize overall energy use during prediction horizon
  - Shed: Minimize energy use during peak hours energy use
  - Shift: Minimize whole-day time-of-use cost

### STD2019
Same as **Default** except:
- Building type: ASHRAE 90.1-2019

### DenOcc
Same as **Default** except:
- Occupancy: 11

### EnergySave
Same as **Default** except:
- Occupant behaviors: 6 (86%) occupants care about saving energy with 90% restriction probability

### TES
Same as **Default** except:
- Building type: On top of the ASHRAE 90.1-2004 envelope, additional internal surface layers with phase change material were added to the ceiling and walls.

### MPC&TES
A combination of **MPC** and **TES**

## Contact Information
For any additional questions, clarifications, or feedback, please reach out to:

- **Jin Wen, PhD**: 
  - **Email**: jw325@drexel.edu

- **Zhelun Chen, PhD**: 
  - **Email**: zl.chen.career@gmail.com


## Cite the Datasets
Please cite the datasets as below:

*TBD*

## References
[^1]: Chen, Zhelun, et al. "Development of a Hardware-in-theloop Testbed for Laboratory Performance Verification of Flexible Building Equipment in Typical Commercial Buildings." arXiv preprint arXiv:2301.13412 (2023). [[Paper](https://arxiv.org/abs/2301.13412)]

[^2]: Langevin, J., et al. "Simulating the human-building interaction: Development and validation of an agent-based model of office occupant behaviors." Building and Environment 88 (2015): 27-45. 

[^3]: Zhang, Yun, et al.  "CFD-Trained ANN Model for Approximating Near-occupant Condition in Real-time Simulations." ASHRAE Topical Conference Proceedings. American Society of Heating, Refrigeration and Air Conditioning Engineers, Inc., 2022.
