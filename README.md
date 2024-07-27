Here's a clean and detailed README for your project:

---

# Data Analysis Project

This project involves performing data analysis on sales data. The analysis includes computing customer revenue, monthly revenue, product revenue, and identifying top customers. The project is containerized using Docker and includes automated tests to ensure the correctness of the analysis functions.

## Project Structure

```plaintext
.
├── Dockerfile
├── Dockerfile.test
├── README.md
├── data_analysis.py
├── docker-compose.yml
├── orders.csv
├── requirements.txt
└── test_data_analysis.py
```

- **Dockerfile**: Docker configuration for the main application.
- **Dockerfile.test**: Docker configuration for running tests.
- **data_analysis.py**: Main script containing the data analysis functions.
- **docker-compose.yml**: Docker Compose file to manage services.
- **orders.csv**: Sample data file used for analysis.
- **requirements.txt**: List of dependencies required for the project.
- **test_data_analysis.py**: Unit tests for the data analysis functions.

## Setup and Usage

### Prerequisites

- Docker
- Docker Compose

### Build and Run the Application

1. **Clone the Repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Build the Docker Images**:
    ```sh
    docker-compose build
    ```

3. **Run the Application**:
    ```sh
    docker-compose up app
    ```

### Run the Tests

1. **Build the Docker Images** (if not already done):
    ```sh
    docker-compose build
    ```

2. **Run the Tests**:
    ```sh
    docker-compose up test
    ```

## Data Analysis Functions

### `compute_customer_revenue(df)`

Computes the total revenue for each customer.

**Parameters**:
- `df` (DataFrame): The input dataframe containing sales data.

**Returns**:
- DataFrame: A dataframe with customer IDs and their corresponding total revenue, sorted by total revenue in descending order.

### `compute_monthly_revenue(df)`

Computes the total revenue for each month.

**Parameters**:
- `df` (DataFrame): The input dataframe containing sales data.

**Returns**:
- DataFrame: A dataframe with months and their corresponding total revenue, sorted by month.

### `compute_product_revenue(df)`

Computes the total revenue for each product.

**Parameters**:
- `df` (DataFrame): The input dataframe containing sales data.

**Returns**:
- DataFrame: A dataframe with product IDs and their corresponding total revenue, sorted by total revenue in descending order.

### `get_top_customers(df, top_n=2)`

Identifies the top customers based on total revenue.

**Parameters**:
- `df` (DataFrame): The input dataframe containing sales data.
- `top_n` (int): The number of top customers to return (default is 2).

**Returns**:
- DataFrame: A dataframe with the top N customers and their corresponding total revenue, sorted by total revenue in descending order.

## Running Analysis Manually

If you want to run the analysis manually without Docker:

1. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

2. **Run the Script**:
    ```sh
    python data_analysis.py orders.csv
    ```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify this README as per your project's specific details and requirements.
