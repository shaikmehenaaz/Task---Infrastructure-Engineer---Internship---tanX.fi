import unittest
import pandas as pd
from data_analysis import compute_customer_revenue, compute_monthly_revenue, compute_product_revenue, get_top_customers

class TestDataAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data = {
            'customer_id': [1, 2, 3, 1, 2, 3],
            'product_id': [1, 2, 3, 1, 2, 3],
            'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-02-01', '2023-02-02', '2023-02-03'],
            'revenue': [30, 20, 10, 60, 40, 30]
        }
        cls.df = pd.DataFrame(data)

    def test_compute_customer_revenue(self):
        result = compute_customer_revenue(self.df)
        self.assertEqual(result.shape[0], 3)  # Should be 3 customers
        self.assertAlmostEqual(result['total_revenue'].iloc[0], 90.0)

    def test_compute_monthly_revenue(self):
        result = compute_monthly_revenue(self.df)
        self.assertEqual(result.shape[0], 2)  # Should be 2 months
        self.assertAlmostEqual(result['total_revenue'].iloc[0], 90.0)

    def test_compute_product_revenue(self):
        result = compute_product_revenue(self.df)
        self.assertEqual(result.shape[0], 3)  # Should be 3 products
        self.assertAlmostEqual(result['total_revenue'].iloc[0], 90.0)

    def test_get_top_customers(self):
        result = get_top_customers(self.df, top_n=2)
        self.assertEqual(result.shape[0], 2)  # Top 2 customers
        self.assertAlmostEqual(result['total_revenue'].iloc[0], 90.0)

if __name__ == '__main__':
    unittest.main()
