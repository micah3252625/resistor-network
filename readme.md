# Resistance Calculator with GUI

## Overview
This Python application calculates the total resistance for resistors connected in **series** or **parallel**. It uses **Object-Oriented Programming (OOP)** concepts to represent resistors and resistor networks, while a **Tkinter GUI** provides a user-friendly interface.

## Features
- Add resistors and see the list of added resistors in real-time.
- Calculate the total resistance for resistors in **series** or **parallel**.
- Clear all resistors and start a new calculation.
- Interactive GUI built with Tkinter.

## OOP Concepts Used
- **Encapsulation:** Each resistor is represented as an object with encapsulated resistance data.
- **Modularity:** The application is divided into classes (`Resistor`, `ResistorNetwork`, `ResistanceCalculatorApp`), each handling specific tasks.
- **Abstraction:** Users interact with a simple GUI that hides the complexity of resistor calculations.
- **Reusability:** Classes are designed to be reusable in other resistor-related projects.

## How to Run
1. Enter resistor values in the input field.
2. Add resistors to the network using the "Add Resistor" button.
3. Calculate the total resistance in series or parallel.
4. Clear the list of resistors to reset the network.

## Classes
- **Resistor**: Represents an individual resistor.
- **ResistorNetwork**: Manages multiple resistors and calculates total resistance.
- **ResistanceCalculatorApp**: Handles the GUI and user interaction.
