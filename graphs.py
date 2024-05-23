import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the CSV data
df = pd.read_csv('videogames.csv')

# Create a directory to save the images if it doesn't exist
output_dir = 'static'
os.makedirs(output_dir, exist_ok=True)

# Define a color palette
colors = plt.get_cmap('tab20').colors

# Custom function to autopct only if slice is larger than a threshold
def autopct_generator(limit):
    def inner_autopct(pct):
        return ('%.1f%%' % pct) if pct > limit else ''
    return inner_autopct

# Generate graphs
def generate_graphs():
    # Example: Sales by Genre (Pie Chart)
    sales_by_genre = df.groupby('Genre')['Sales'].sum()
    plt.figure(figsize=(10, 6))
    sales_by_genre.plot(kind='pie', autopct=autopct_generator(3), startangle=90, colors=colors)
    plt.title('Sales by Genre')
    plt.ylabel('')  # Hide the y-label to make it cleaner
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'sales_by_genre.png'), bbox_inches='tight')
    plt.close()

    # Example: Sales by Platform (Horizontal Bar Chart)
    sales_by_platform = df.groupby('Platform')['Sales'].sum().sort_values()
    plt.figure(figsize=(10, 6))
    sales_by_platform.plot(kind='barh', color=colors)
    plt.title('Sales by Platform')
    plt.xlabel('Sales')
    plt.ylabel('Platform')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'sales_by_platform.png'), bbox_inches='tight')
    plt.close()

    # Example: Sales by Rating (Line Chart)
    sales_by_rating = df.groupby('Rating')['Sales'].sum()
    plt.figure(figsize=(10, 6))
    sales_by_rating.plot(kind='line', marker='o', color='b')
    plt.title('Sales by Rating')
    plt.xlabel('Rating')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'sales_by_rating.png'), bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_graphs()
