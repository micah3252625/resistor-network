# Resistance Calculator Application

## Project Overview

The **Resistance Calculator** is a Python application that allows users to calculate the total resistance for resistors connected in **series** or **parallel**. The program uses **Object-Oriented Programming (OOP)** principles and provides a **Graphical User Interface (GUI)** using Tkinter to facilitate user interaction.

Users can:
- Add resistor values to the list.
- View the total resistance in either a **series** or **parallel** configuration.
- Clear all resistors and reset the calculation.

### Features:
- **Object-Oriented Design**: Classes encapsulate resistors and resistor networks.
- **GUI**: User-friendly interface built with Tkinter.
- **Series and Parallel Resistance Calculations**: The app supports calculations for both configurations.
- **Resistor List Display**: A live list of added resistors is shown in the GUI.

### How OOP Is Used
- **Encapsulation:**
  - The Resistor class encapsulates the details of individual resistors (resistance values) and provides methods to access them.
  - The ResistorNetwork class encapsulates the operations and management of multiple Resistor objects, providing methods to calculate series and parallel resistance.
    
- **Modularity:**
  - The application is divided into different classes, each with its specific responsibilities (resistor management, calculations, and GUI management). This makes the code easier to maintain and extend.
    
- **Abstraction:**
  - The user interacts with a simple GUI without needing to understand the underlying resistor calculations, which are abstracted away inside the ResistorNetwork class.
    
- **Reusability:**
  - The Resistor and ResistorNetwork classes can be reused in other projects that deal with resistors, without modifying the GUI code.
  
- **Object Interaction:**
  - The ResistanceCalculatorApp class interacts with instances of Resistor and ResistorNetwork, leveraging OOP to create a structured program where components work together seamlessly.
