# Product Recommendation System

This project implements a product recommendation system using Python and the pandas, scikit-learn, and spaCy libraries. The system is designed to provide personalized product suggestions to users based on a hybrid approach, combining content-based and collaborative filtering techniques.

## Project Overview

The recommendation engine analyzes a dataset of Walmart products and user reviews. It performs the following key steps:
1.  **Data Loading & Preprocessing**: Loads raw data, cleans it, and handles missing values.
2.  **Feature Engineering**: Creates a combined "tags" feature from product attributes like category, brand, and description for content analysis.
3.  **Content-Based Recommendations**: Recommends products that are similar in their textual features (e.g., brand, category, description) to a given product.
4.  **Collaborative Filtering**: Recommends products to a user based on the preferences of other users with similar tastes.
5.  **Hybrid Recommendation**: Combines the strengths of both models to generate a final, robust list of recommendations.

## Technology Stack

* **Python**: The core programming language used for the entire project.
* **Pandas**: Essential for data manipulation and analysis.
* **NumPy**: Used for numerical operations on the data.
* **Scikit-learn**: Provides the core algorithms for TF-IDF vectorization and cosine similarity calculations.
* **SpaCy**: A natural language processing library used for text cleaning and tokenization.
* **Matplotlib & Seaborn**: Libraries for data visualization to help with exploratory data analysis (EDA).
* **Jupyter Notebook**: The development environment where the code was written and executed.

## Getting Started

### Prerequisites

* Python 3.x
* Required libraries can be installed using pip:
    ```bash
    pip install pandas numpy scikit-learn spacy matplotlib seaborn
    ```
* To use spaCy, you also need to download the English language model:
    ```bash
    python -m spacy download en_core_web_sm
    ```

### How to Run the Notebook

1.  Clone this repository to your local machine.
2.  Ensure you have the required dataset file (`marketing_sample_for_walmart_com-walmart_com_product_review__20200701_20201231__5k_data.tsv`) in the same directory as the notebook.
3.  Open the Jupyter Notebook and run each cell sequentially to see the data processing, analysis, and recommendation generation in action.

## Project Structure

* `recommandation.ipynb`: The main Jupyter Notebook containing all the code.
* `README.md`: This file.
* `dataset.tsv`: The dataset file used for the project.
