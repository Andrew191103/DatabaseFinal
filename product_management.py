# product_management.py
import sql_queries

def add_product(product_name, product_price, product_description, release_date, product_quantity, category_id, stock_quantity, restock_threshold, last_restocked):
    product_data = (product_name, product_price, product_description, release_date, product_quantity, category_id, stock_quantity, restock_threshold, last_restocked)
    sql_queries.add_product(product_data)
    print("Product added successfully.")

def update_product(product_id, product_name, product_price, product_description, release_date, product_quantity, category_id, stock_quantity, restock_threshold, last_restocked):
    updated_data = (product_name, product_price, product_description, release_date, product_quantity, category_id, stock_quantity, restock_threshold, last_restocked, product_id)
    sql_queries.update_product(updated_data)
    print("Product updated successfully.")

def delete_product(product_id):
    sql_queries.delete_product(product_id)
    print("Product deleted successfully.")

def fetch_all_products():
    return sql_queries.fetch_products()

def fetch_product(product_id):
    return sql_queries.fetch_product(product_id)
