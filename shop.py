
class Product:
    """Represents a product with SKU, name, and price."""

    def __init__(self, sku, name, price):
        # Validate product information
        if not sku:
            raise ValueError("SKU is required.")

        if not name:
            raise ValueError("Product name is required.")

        if price < 0:
            raise ValueError("Price cannot be negative.")

        # Initialize product attributes
        self.sku = sku
        self.name = name
        self.price = price

    def __repr__(self):
        # Return a readable representation of the product
        return (
            f"Product(sku={self.sku!r}, "
            f"name={self.name!r}, price={self.price})"
        )


def find_by_name(products, text):
    # Normalize the search text for case-insensitive matching
    search_text = text.strip().casefold()

    # Return an empty list if the search text is empty
    if not search_text:
        return []

    # Find products whose names contain the search text
    return [
        product
        for product in products
        if search_text in product.name.casefold()
    ]


def apply_discount(price, percent):
    # Validate the discount percentage
    if not 0 <= percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    # Ensure the price is not negative
    if price < 0:
        raise ValueError("Price cannot be negative.")

    # Calculate and return the discounted price
    return price * (1 - percent / 100)


def add_tax(price, rate=0.2):
    # Validate price and tax rate
    if price < 0:
        raise ValueError("Price cannot be negative.")

    if rate < 0:
        raise ValueError("Tax rate cannot be negative.")

    # Calculate the final price including tax
    return price * (1 + rate)


# Create sample products
products = [
    Product("101", "Laptop", 1000),
    Product("102", "Mouse", 50),
    Product("103", "Keyboard", 80)
]

# Search for a product by name
print(find_by_name(products, "lap"))

# Apply a 10% discount to the price
print(apply_discount(1000, 10))

# Add 20% tax to the price
print(add_tax(1000))
