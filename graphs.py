import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the CSV data
df = pd.read_csv('videogames.csv')

# Create a directory to save the images if it doesn't exist
output_dir = 'static'
os.makedirs(output_dir, exist_ok=True)

# Set seaborn style
sns.set(style="whitegrid")

# Custom function to autopct only if slice is larger than a threshold
def autopct_generator(limit):
    def inner_autopct(pct):
        return ('%.1f%%' % pct) if pct > limit else ''
    return inner_autopct

# Generate graphs
def generate_graphs():
    try:
        # Example: Sales by Genre (Pie Chart)
        sales_by_genre = df.groupby('Genre')['Sales'].sum()
        plt.figure(figsize=(10, 6))
        sales_by_genre.plot(kind='pie', autopct=autopct_generator(3), startangle=90,
                            colors=sns.color_palette("tab20", len(sales_by_genre)))
        plt.title('Sales by Genre')
        plt.ylabel('')  # Hide the y-label to make it cleaner
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'sales_by_genre.png'), bbox_inches='tight')
        plt.close()

        # Example: Sales by Platform (Horizontal Bar Chart)
        sales_by_platform = df.groupby('Platform')['Sales'].sum().sort_values()
        plt.figure(figsize=(10, 6))
        sales_by_platform.plot(kind='barh', color=sns.color_palette("viridis", len(sales_by_platform)))
        plt.title('Sales by Platform')
        plt.xlabel('Sales (by millions)')
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

        # Additional Example: Sales over Time (Line Chart)
        df['Release Date'] = pd.to_datetime(df['Release Date'], errors='coerce')
        sales_over_time = df.groupby(df['Release Date'].dt.year)['Sales'].sum()
        plt.figure(figsize=(10, 6))
        sales_over_time.plot(kind='line', marker='o', color='g')
        plt.title('Sales Over Time')
        plt.xlabel('Year')
        plt.ylabel('Sales')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'sales_over_time.png'), bbox_inches='tight')
        plt.close()

        # Additional Example: Average Rating by Genre (Bar Chart)
        avg_rating_by_genre = df.groupby('Genre')['Rating'].mean().sort_values()
        plt.figure(figsize=(10, 6))
        avg_rating_by_genre.plot(kind='bar', color=sns.color_palette("cubehelix", len(avg_rating_by_genre)))
        plt.title('Average Rating by Genre')
        plt.xlabel('Genre')
        plt.ylabel('Average Rating')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'avg_rating_by_genre.png'), bbox_inches='tight')
        plt.close()

    except Exception as e:
        print(f"Error generating graphs: {e}")

generate_graphs()
