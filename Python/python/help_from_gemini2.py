# ==============================================================================
# Module Imports
# ==============================================================================
# datetime: For working with dates and times (e.g., order timestamps).
# random: For simulating random data (e.g., quantities, prices, order times).
# math: For mathematical operations (e.g., ceil for rounding up).
# collections.defaultdict: A specialized dictionary for easier accumulation.
from datetime import datetime, timedelta
import random
import math
from collections import defaultdict

# ==============================================================================
# Configuration & Constants
# ==============================================================================
PRODUCT_CATEGORIES = ("Electronics", "Books", "Clothing", "Home Goods", "Food")
CUSTOMER_TIERS = {"Bronze": 0.05, "Silver": 0.10, "Gold": 0.15, "Platinum": 0.20} # Tier: Discount %
MIN_ORDER_VALUE_FOR_DISCOUNT = 50.0

# ==============================================================================
# Data Generation Function (Using *args, **kwargs, random, datetime, tuples, list comprehensions)
# ==============================================================================
def generate_customer_orders(num_orders: int,
                             start_date: datetime,
                             category_prices: dict = None,
                             **extra_params) -> list[tuple]:
    """
    Generates a list of simulated customer orders.

    Args:
        num_orders (int): The number of orders to generate.
        start_date (datetime): The starting date for order timestamps.
        category_prices (dict, optional): A dictionary mapping categories to (min_price, max_price).
                                          Defaults to a predefined range if None.
        **extra_params: Additional parameters for customization (e.g., 'max_days_span').

    Returns:
        list[tuple]: A list where each tuple represents an order:
                     (order_id, timestamp, customer_id, category, quantity, unit_price, customer_tier)
    """
    print(f"\n--- Generating {num_orders} Customer Orders ---")

    # Define default prices if not provided via kwargs
    if category_prices is None:
        category_prices = {
            "Electronics": (50, 500),
            "Books": (10, 50),
            "Clothing": (20, 150),
            "Home Goods": (15, 200),
            "Food": (5, 30)
        }

    # Extract max_days_span from extra_params or use a default
    max_days_span = extra_params.get('max_days_span', 30) # Using .get() for safe access

    orders = []
    for i in range(num_orders):
        order_id = f"ORD-{i + 1:04d}"
        
        # Random timestamp within a span
        # Using timedelta from datetime module
        timestamp = start_date + timedelta(days=random.randint(0, max_days_span),
                                           hours=random.randint(0, 23),
                                           minutes=random.randint(0, 59))

        customer_id = f"CUST-{random.randint(100, 999)}"
        
        # Pick a random category
        category = random.choice(PRODUCT_CATEGORIES)
        
        # Determine price based on category_prices dict
        min_p, max_p = category_prices.get(category, (10, 100)) # Default if category not in dict
        unit_price = round(random.uniform(min_p, max_p), 2)
        
        quantity = random.randint(1, 10)
        
        # Pick a random customer tier
        customer_tier = random.choice(list(CUSTOMER_TIERS.keys()))

        # An order is stored as a tuple for immutability
        order_tuple = (order_id, timestamp, customer_id, category, quantity, unit_price, customer_tier)
        orders.append(order_tuple)

    print("--- Order Generation Complete ---")
    return orders

# ==============================================================================
# Data Analysis Function (Using map, filter, lambda, zip, any, all, sets, isinstance, list comprehensions, enumerate)
# ==============================================================================
def analyze_order_data(orders: list[tuple], **analysis_options) -> dict:
    """
    Analyzes the simulated customer order data.

    Args:
        orders (list[tuple]): A list of order tuples.
        **analysis_options: Options for analysis (e.g., min_total_value, specific_category).

    Returns:
        dict: A dictionary containing various analysis results.
    """
    print("\n--- Starting Data Analysis ---")

    results = {}

    # 1. Calculate Total Value for Each Order (using map and lambda)
    # Each order tuple is transformed into its total value (quantity * unit_price)
    # `order` here is the entire tuple: (order_id, timestamp, customer_id, category, quantity, unit_price, customer_tier)
    # We access elements by index: quantity is at index 4, unit_price at index 5.
    order_values = list(map(lambda order: order[4] * order[5], orders))
    results['total_values_per_order'] = order_values
    print(f"Total values for each order (first 5): {order_values[:5]}...")

    # 2. Filter High-Value Orders (using filter and lambda)
    min_total_value = analysis_options.get('min_total_value', 200.0)
    # Filter orders where the calculated total value is above a threshold
    # Note: We need to calculate value *inside* the lambda for filter.
    high_value_orders = list(filter(lambda order: (order[4] * order[5]) >= min_total_value, orders))
    results['high_value_orders_count'] = len(high_value_orders)
    print(f"Number of orders >= ${min_total_value}: {len(high_value_orders)}")
    if high_value_orders:
        print(f"  Example high-value order: {high_value_orders[0]}")

    # 3. Get Unique Categories (using sets)
    # A set is great for quickly getting unique items.
    # A list comprehension extracts all categories first.
    all_categories = [order[3] for order in orders]
    unique_categories = set(all_categories)
    results['unique_categories'] = list(unique_categories) # Convert back to list for consistent output
    print(f"Unique product categories: {', '.join(unique_categories)}")

    # 4. Check if Any Order is from a Specific Category (using any)
    specific_category_check = analysis_options.get('specific_category', 'Electronics')
    # any() checks if at least one item in an iterable satisfies the condition
    is_any_from_specific_category = any(order[3] == specific_category_check for order in orders)
    results['any_from_specific_category'] = is_any_from_specific_category
    print(f"Any orders from '{specific_category_check}'? {is_any_from_specific_category}")

    # 5. Check if All Orders Meet a Minimum Quantity (using all)
    min_quantity_all_check = analysis_options.get('min_quantity_all_check', 1)
    # all() checks if ALL items in an iterable satisfy the condition
    are_all_above_min_quantity = all(order[4] >= min_quantity_all_check for order in orders)
    results['all_above_min_quantity'] = are_all_above_min_quantity
    print(f"Are all orders >= {min_quantity_all_check} quantity? {are_all_above_min_quantity}")

    # 6. Calculate Total Sales per Category (combining defaultdict, zip, map, list comprehension, enumerate)
    sales_by_category = defaultdict(float) # defaultdict simplifies adding to categories

    # Ensure correct data type using isinstance (for robustness)
    for order_idx, order in enumerate(orders): # Using enumerate to get index if needed
        if isinstance(order, tuple) and len(order) == 7: # Basic structural check
            category = order[3]
            quantity = order[4]
            unit_price = order[5]
            sales_by_category[category] += quantity * unit_price
        else:
            print(f"Skipping malformed order at index {order_idx}: {order}")

    # Now, let's process for display/return
    # Extract categories and their total sales from the defaultdict
    categories_list = list(sales_by_category.keys())
    total_sales_list = [sales_by_category[cat] for cat in categories_list]

    # Combine them using zip for display
    # zip combines iterables element-wise
    zipped_sales_data = zip(categories_list, total_sales_list)
    results['sales_by_category'] = dict(zipped_sales_data) # Convert back to dict for result

    print("\nTotal Sales by Category:")
    # Iterate with enumerate for numbered output
    # `item` here will be a tuple like ('Electronics', 1234.56)
    for i, item in enumerate(list(zip(categories_list, total_sales_list)), 1):
        category, total_sales = item # Unpack the zipped item
        print(f"  {i}. {category}: ${total_sales:.2f}")

    # 7. Apply Discounts Based on Customer Tier and Order Value (using map, lambda, if)
    print("\nCalculating potential discounts...")
    eligible_orders_with_discount = []
    for order in orders:
        # Check if customer tier is valid and if order value meets discount threshold
        customer_tier = order[6]
        discount_rate = CUSTOMER_TIERS.get(customer_tier, 0.0) # 0 if tier not found
        total_order_value = order[4] * order[5]

        # Use an if condition within a map-like structure
        if discount_rate > 0 and total_order_value >= MIN_ORDER_VALUE_FOR_DISCOUNT:
            discount_amount = total_order_value * discount_rate
            final_price = total_order_value - discount_amount
            eligible_orders_with_discount.append(
                (order[0], customer_tier, total_order_value, discount_amount, final_price)
            )

    results['discounted_orders_info'] = eligible_orders_with_discount
    print(f"Number of orders eligible for discount: {len(eligible_orders_with_discount)}")
    if eligible_orders_with_discount:
        print(f"  Example discounted order: Order ID {eligible_orders_with_discount[0][0]}, "
              f"Tier: {eligible_orders_with_discount[0][1]}, Original: ${eligible_orders_with_discount[0][2]:.2f}, "
              f"Discount: ${eligible_orders_with_discount[0][3]:.2f}, Final: ${eligible_orders_with_discount[0][4]:.2f}")

    print("\n--- Data Analysis Complete ---")
    return results

# ==============================================================================
# Main Execution Block (Orchestrating the simulation and analysis)
# ==============================================================================
if __name__ == "__main__":
    print("Welcome to the Dynamic Event/Order Data Analyzer!")
    print("This script demonstrates various Python built-in functions and concepts.")

    # --- Step 1: Generate Data ---
    # Using *args and **kwargs for configuration
    # generate_customer_orders(num_orders, start_date, category_prices=None, max_days_span=30)
    
    # We can pass specific number of orders, and use **kwargs for extra_params
    simulated_orders = generate_customer_orders(
        200, # num_orders
        datetime(2025, 6, 1), # start_date
        max_days_span=60, # max_days_span passed via **extra_params
        category_prices={
            "Electronics": (80, 700),
            "Books": (12, 60),
            "Clothing": (30, 200),
            "Food": (10, 50) # Not all categories defined here, demonstrate defaults for others
        }
    )

    # --- Step 2: Analyze Data ---
    # Using **kwargs to pass analysis options
    analysis_results = analyze_order_data(
        simulated_orders,
        min_total_value=150.0,
        specific_category='Books',
        min_quantity_all_check=1
    )

   

    print("\nScript finished. Hope this comprehensive example helps!")