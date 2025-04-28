# Anti-DUI

## Description

This project uses data on individual factors (including body weight, gender, and number of drinks consumed) alongside measured Blood Alcohol Concentration (BAC) values to build a regression model that predicts BAC levels. The model is incorporated into a web-based tool designed to estimate how many drinks an individual should consume to reach a specific BAC or intoxication level, empowering users to make responsible and informed drinking decisions. The project includes data cleaning, exploratory analysis, model evaluation, and visualization of results.

## Project Structure

- `data/raw/` - Original data
- `data/processed/` - Cleaned data
- `notebooks/` - Jupyter notebooks for exploratory data analysis, data pre-processing, model training, evaluation, and selection
- `src/` - Python scripts with helper functions
- `output/` - Saved models, plots, and performance metrics
- `website/` - Code for website estimating drinks required to achieve desired intoxication level

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Open the notebooks in the `notebooks/` folder to run the project.

## Requirements

See `requirements.txt` for all dependencies.

## Results

Final Model (Linear Regression):
- R2 Value: 0.9518
- MSE: 0.0001

## License

This project is open-source under the [MIT License](LICENSE).
