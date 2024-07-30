import unittest
import pandas as pd
from io import StringIO
from data_analysis import (
    load_data, preprocess_data, compute_monthly_revenue,
    compute_product_revenue, compute_customer_revenue, get_top_customers
)

class TestDataAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample CSV data
        self.sample_data = StringIO("""order_date,product_id,product_name,product_price,quantity,customer_id
        2023-01-15,101,Product A,10.0,2,201
        2023-01-18,102,Product B,20.0,1,202
        2023-02-20,101,Product A,10.0,1,201
        2023-02-25,103,Product C,30.0,3,203
        2023-03-05,104,Product D,40.0,2,204
        2023-03-10,101,Product A,10.0,5,201
        """)
        
        self.df = pd.read_csv(self.sample_data)
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])
    
    def test_load_data(self):
        # Test the load_data function
        df = load_data('orders.csv')
        self.assertIsInstance(df, pd.DataFrame)
    
    def test_preprocess_data(self):
        # Test the preprocess_data function
        df = preprocess_data(self.df)
        self.assertIn('total_revenue', df.columns)
        self.assertIn('month', df.columns)
        self.assertEqual(df['total_revenue'].sum(), 270.0)
        self.assertEqual(df['month'].nunique(), 3)
    
    def test_compute_monthly_revenue(self):
        # Test the compute_monthly_revenue function
        df = preprocess_data(self.df)
        monthly_revenue = compute_monthly_revenue(df)
        self.assertEqual(monthly_revenue.shape[0], 3)
        self.assertEqual(monthly_revenue['total_revenue'].sum(), 270.0)
    
    def test_compute_product_revenue(self):
        # Test the compute_product_revenue function
        df = preprocess_data(self.df)
        product_revenue = compute_product_revenue(df)
        self.assertEqual(product_revenue.shape[0], 4)
        self.assertEqual(product_revenue.iloc[0]['total_revenue'], 90.0)  # Product C
    
    def test_compute_customer_revenue(self):
        # Test the compute_customer_revenue function
        df = preprocess_data(self.df)
        customer_revenue = compute_customer_revenue(df)
        self.assertEqual(customer_revenue.shape[0], 4)
        self.assertEqual(customer_revenue.iloc[0]['total_revenue'], 90.0)  # Customer 203
    
    def test_get_top_customers(self):
        # Test the get_top_customers function
        df = preprocess_data(self.df)
        top_customers = get_top_customers(df, top_n=2)
        self.assertEqual(top_customers.shape[0], 2)
        self.assertEqual(top_customers.iloc[0]['total_revenue'], 90.0)  # Customer 203
        self.assertEqual(top_customers.iloc[1]['total_revenue'], 80.0)  # Customer 201

if __name__ == "__main__":
    unittest.main()
