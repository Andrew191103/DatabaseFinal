import product_management as pm

def main():
    print("Welcome to the Product Management System!")

    while True:
        print("\nOptions:")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Product")
        print("5. View All Products")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_product()
        elif choice == '2':
            update_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            view_product()
        elif choice == '5':
            view_all_products()
        elif choice == '6':
            print("Exiting the Product Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_product():
    product_name = input("Enter the product name: ")
    product_price = float(input("Enter the product price: "))
    product_description = input("Enter the product description: ")
    release_date = input("Enter the release date (YYYY-MM-DD): ")
    product_quantity = int(input("Enter the product quantity: "))
    category_id = int(input("Enter the category ID: "))
    stock_quantity = int(input("Enter the stock quantity: "))
    restock_threshold = int(input("Enter the restock threshold: "))
    last_restocked = input("Enter the last restocked date (YYYY-MM-DD): ")

    pm.add_product(product_name, product_price, product_description, release_date, product_quantity, category_id, stock_quantity, restock_threshold, last_restocked)
    print("Product added successfully.")

def update_product():
    product_id = int(input("Enter the ID of the product to update: "))
    product_name = input("Enter the new product name: ")
    product_price = float(input("Enter the new product price: "))
    product_description = input("Enter the new product description: ")
    release_date = input("Enter the new release date (YYYY-MM-DD): ")
    product_quantity = int(input("Enter the new product quantity: "))
    category_id = int(input("Enter the new category ID: "))
    stock_quantity = int(input("Enter the new stock quantity: "))
    restock_threshold = int(input("Enter the new restock threshold: "))
    last_restocked = input("Enter the new last restocked date (YYYY-MM-DD): ")

    pm.update_product(product_id, product_name, product_price, product_description, release_date, product_quantity, category_id, stock_quantity, restock_threshold, last_restocked)
    print("Product updated successfully.")

def delete_product():
    product_id = int(input("Enter the ID of the product to delete: "))
    pm.delete_product(product_id)
    print("Product deleted successfully.")

def view_product():
    product_id = int(input("Enter the ID of the product to view: "))
    product = pm.fetch_product(product_id)
    if product:
        print(f"Product ID: {product[0]}")
        print(f"Name: {product[1]}")
        print(f"Price: {product[2]}")
        print(f"Description: {product[3]}")
        print(f"Release Date: {product[4]}")
        print(f"Quantity: {product[5]}")
        print(f"Category ID: {product[6]}")
        print(f"Stock Quantity: {product[7]}")
        print(f"Restock Threshold: {product[8]}")
        print(f"Last Restocked: {product[9]}")
    else:
        print("Product not found.")

def view_all_products():
    products = pm.fetch_all_products()
    if products:
        print("\nAll Products:")
        for product in products:
            print(f"Product ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}")
    else:
        print("No products found.")

if __name__ == "__main__":
    main()
