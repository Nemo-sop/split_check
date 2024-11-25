import unittest
import time
from Friendship_conserver import Friendship_conserver

class FriendshipConserverTest(unittest.TestCase):
    def test_case_1(self):
        """Test with small input."""
        start_time = time.time()
        guest_expensess = {'nico': 1000, 'tomas': 2000}
        divider = Friendship_conserver()
        
        divider.divide_expensess(guest_expensess)
        divider.balance(guest_expensess)
        transfers = divider.calculate_transfers()
        
        elapsed_time = time.time() - start_time
        self.assertLessEqual(elapsed_time, 10, "Test exceeded the timeout limit of 10 seconds")
        
        expected_transfers = ["nico transfers 500.0 to tomas"]
        self.assertEqual(transfers, expected_transfers)

    def test_case_2(self):
        """Test with multiple guests with uneven contributions."""
        start_time = time.time()
        guest_expensess = {'nico': 1000, 'tomas': 2000, 'jose': 6000}
        divider = Friendship_conserver()
        
        divider.divide_expensess(guest_expensess)
        divider.balance(guest_expensess)
        transfers = divider.calculate_transfers()
        
        elapsed_time = time.time() - start_time
        self.assertLessEqual(elapsed_time, 10, "Test exceeded the timeout limit of 10 seconds")
        
        expected_transfers = [
            "tomas transfers 1000.0 to jose",
            "nico transfers 2000.0 to jose"
        ]
        self.assertEqual(transfers, expected_transfers)

    def test_case_3(self):
        """Test with equal contributions."""
        start_time = time.time()
        guest_expensess = {'nico': 3000, 'tomas': 3000, 'jose': 3000}
        divider = Friendship_conserver()
        
        divider.divide_expensess(guest_expensess)
        divider.balance(guest_expensess)
        transfers = divider.calculate_transfers()
        
        elapsed_time = time.time() - start_time
        self.assertLessEqual(elapsed_time, 10, "Test exceeded the timeout limit of 10 seconds")
        
        expected_transfers = []
        self.assertEqual(transfers, expected_transfers)

    def test_case_4(self):
        """Test with zero contribution from one guest."""
        start_time = time.time()
        guest_expensess = {'nico': 0, 'tomas': 3000, 'jose': 6000}
        divider = Friendship_conserver()
        
        divider.divide_expensess(guest_expensess)
        divider.balance(guest_expensess)
        transfers = divider.calculate_transfers()
        
        elapsed_time = time.time() - start_time
        self.assertLessEqual(elapsed_time, 10, "Test exceeded the timeout limit of 10 seconds")
        
        expected_transfers = [
            "nico transfers 3000.0 to jose"
        ]
        self.assertEqual(transfers, expected_transfers)

if __name__ == "__main__":
    unittest.main()
