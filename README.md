# quantitative-strategies
Welcome to the **Quantitative Strategies** repository! This project is dedicated to exploring and implementing various quantitative research methods for finance. The repository is structured to facilitate learning, testing, and applying quantitative strategies.

## Table of Contents
1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Usage](#usage)

## Introduction

This repository is designed for learning and testing quantitative research methods in finance. It contains various modules that handle different aspects of quantitative trading, from data sourcing to strategy implementation and portfolio management.

## Project Structure

The repository is organised into the following main directories:

- **data/**: Functions for sourcing and preprocessing historical market data.
- **indicators/**: Functions for adding technical indicators to the historical data.
- **models/**: Machine learning models for predicting market movements.
- **optimisers/**: Algorithms for cash allocation and portfolio optimisation, including risk management.
- **portfolio/**: Tools for managing position adjustments against existing trade positions.
- **strategies/**: Definitions of overall trading strategies through combination of the tools defined in the above sections.

## Installation

To get started with this project, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/oliverbezani/quantitative-strategies.git
cd quantitative-strategies
pip install -r requirements.txt
```

## Usage

Here’s a brief overview of how to use the main components of the repository to create a strategy:

- **Data Sourcing**: Use the scripts in the `data` module to fetch and preprocess market data for different tickers and time periods.
- **Indicator Calculation**: Expand your data with technical indicators using functions in the `indicators` module.
- **Model Training**: Further preprocess your input data before training and executing a machine learning algorithm in the `models` module.
- **Optimisation**: Optimise your portfolio allocation with risk consideration using a methodology in the `optimisers` module.
- **Portfolio Management**: Manage your trade positions with tools from the `portfolio` module.
- **Strategy Definition**: Save your overall strategy to the `strategies` module ready for execution in the `main.py` file.
