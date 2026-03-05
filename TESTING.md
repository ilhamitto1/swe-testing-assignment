# Testing Strategy

The Quick-Calc application was tested using both unit testing and integration testing.

Unit tests were created to verify the correctness of individual calculator functions such as addition, subtraction, multiplication, and division.

Integration tests were used to verify that different parts of the application work correctly together, simulating basic user interactions with the calculator.

---

# Testing Pyramid

The testing pyramid recommends having many unit tests, fewer integration tests, and very few end-to-end tests.

In this project, most tests are unit tests because they verify the core calculation logic quickly and efficiently. A smaller number of integration tests ensure that the system components work correctly together.

This structure follows the testing pyramid principles discussed in the lecture.

---

# Black-box vs White-box Testing

Unit tests in this project follow a white-box testing approach because they directly test the internal functions of the calculator.

Integration tests follow a black-box testing approach because they simulate user interactions and verify the system behavior without focusing on internal implementation details.

---

# Regression Testing

Regression testing ensures that previously working functionality continues to work after changes are made to the code.

The existing test suite can be used for regression testing. Whenever new features are added or code changes are made, running the tests will help detect if any existing functionality is broken.

---

# Test Results

| Test Name | Type | Result |
|-----------|------|--------|
| Addition test | Unit | Pass |
| Subtraction test | Unit | Pass |
| Multiplication test | Unit | Pass |
| Division test | Unit | Pass |
| Division by zero | Unit | Pass |
| Negative numbers | Unit | Pass |
| Decimal numbers | Unit | Pass |
| Large numbers | Unit | Pass |
| User addition flow | Integration | Pass |
| Clear function test | Integration | Pass |