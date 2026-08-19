# Week 2 Model Report

## Project
SmartPOS AI - Intelligent POS Features

## Day 1: Baseline Sales Prediction

A baseline sales prediction model was built using Linear Regression.

- Training Samples: 2,400,710
- Testing Samples: 600,178

The model was successfully trained using historical sales data.

---

## Day 2: Model Evaluation

The baseline model was evaluated using RMSE and MAE.

- RMSE: 761.74
- MAE: 250.41

An Actual vs Predicted Sales graph was also generated.

---

## Day 3: Demand Forecasting

A demand forecasting model was created for the GROCERY I product category.

A 7-day moving average was used to forecast future demand based on historical daily sales.

A demand forecast visualization was also generated.

---

## Day 4: Inventory Prediction

Inventory prediction logic was created using recent sales velocity.

- Product Category: GROCERY I
- Current Inventory: 5,000,000
- Average Daily Sales: 245,306.21
- Estimated Days Until Stockout: 20.38 days

An inventory prediction graph was also generated.

---

## Day 5: Feature Improvements

The sales prediction model was improved by adding time-series features.

Features added:

- Previous day sales, lag_1
- Previous 7 days sales, lag_7
- 7-day rolling mean
- Promotion data

Improved Model Results:

- Training Samples: 1,341
- Testing Samples: 336
- RMSE: 36,803.90
- MAE: 24,865.40

---

## Day 6: Product Recommendations

A simple product recommendation system was built using product co-occurrence.

The system identified product categories that frequently appeared together in the same store and date.

Example:

- BEVERAGES + BREAD/BAKERY: 83,605 transactions

This recommendation prototype can help identify products that may be recommended together.

---

## Conclusion

During Week 2, multiple machine learning features were developed for the SmartPOS AI project.

The work included:

- Baseline Sales Prediction
- Model Evaluation
- Demand Forecasting
- Inventory Prediction
- Feature Improvements
- Product Recommendations

The project used historical sales data to build and evaluate machine learning and time-series based solutions.