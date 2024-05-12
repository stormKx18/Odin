# Test Identification


class TestSimple:
    def test_my_test_1(self):
        self.result = "test_my_test_1"
        assert self.result == "test_my_test_1"

    def my_test_2(self):
        self.result = "my_test_2"
        assert self.result == "my_test_2"

    def my_test_3_test(self):
        self.result = "my_test_3_test"
        assert self.result == "my_test_3_test"
