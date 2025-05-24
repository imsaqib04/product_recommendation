import pandas as pd
import ipywidgets as widgets
from IPython.display import display

# # Load your data
# products = pd.read_csv("marketing_sample_for_walmart_com-walmart_com_product_review__20200701_20201231__5k_data.tsv")  
train_data = pd.read_csv('marketing_sample_for_walmart_com-walmart_com_product_review__20200701_20201231__5k_data.tsv',sep='\t')

# Get unique users and products
unique_users = ratings['UserID'].unique()

# Dropdown for selecting user
user_dropdown = widgets.Dropdown(
    options=unique_users,
    description='User ID:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

# Button to get recommendations
recommend_button = widgets.Button(description="Get Recommendations", button_style='success')

# Output area
output = widgets.Output()

# Dummy hybrid recommender function (replace with your actual model)
def hybrid_recommend(user_id, top_n=5):
    # For demo purposes, return top-rated products
    top_products = products.head(top_n)
    return top_products[['ProductID', 'ProductName', 'Price']]

# Hybrid Recommendations (Combine Content-Based and Collaborative Filtering)
def hybrid_recommendations(train_data,target_user_id, item_name, top_n=10):
    # Get content-based recommendations
    content_based_rec = content_based_recommendations(train_data,item_name, top_n)

    # Get collaborative filtering recommendations
    collaborative_filtering_rec = collaborative_filtering_recommendations(train_data,target_user_id, top_n)
    
    # Merge and deduplicate the recommendations
    hybrid_rec = pd.concat([content_based_rec, collaborative_filtering_rec]).drop_duplicates()
    
    return hybrid_rec.head(10)

# Show UI
display(user_dropdown, recommend_button, output)
