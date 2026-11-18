
class Product:
    def __init__(self, sku, name, price):
        if not sku:
            raise ValueError("SKU is required.")

        if not name:
            raise ValueError("Product name is required.")

        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.sku = sku
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(sku={self.sku!r}, name={self.name!r}, price={self.price})"


def find_by_name(products, text):
    search_text = text.strip().casefold()

    if not search_text:
        return []

    return [
        product
        for product in products
        if search_text in product.name.casefold()
    ]


def apply_discount(price, percent):
    if not 0 <= percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    if price < 0:
        raise ValueError("Price cannot be negative.")

    return price * (1 - percent / 100)


def add_tax(price, rate=0.2):
    if price < 0:
        raise ValueError("Price cannot be negative.")

    if rate < 0:
        raise ValueError("Tax rate cannot be negative.")

    return price * (1 + rate)


# Example usage
products = [
    Product("101", "Laptop", 1000),
    Product("102", "Mouse", 50),
    Product("103", "Keyboard", 80)
]

print(find_by_name(products, "lap"))
print(apply_discount(1000, 10))
print(add_tax(1000))
##Com

##CC