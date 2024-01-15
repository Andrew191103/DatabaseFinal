import sql_queries

def add_category(category_name):
    return sql_queries.add_category(category_name)

def update_category(category_id, new_name):
    sql_queries.update_category(category_id, new_name)

def delete_category(category_id):
    sql_queries.delete_category(category_id)

def get_category(category_id):
    return sql_queries.fetch_category(category_id)

def get_all_categories():
    return sql_queries.fetch_all_categories()
