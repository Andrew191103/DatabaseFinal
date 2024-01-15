import sql_queries

def add_client_type(type_detail):
    return sql_queries.add_client_type(type_detail)

def update_client_type(type_id, new_type_detail):
    sql_queries.update_client_type(type_id, new_type_detail)

def delete_client_type(type_id):
    sql_queries.delete_client_type(type_id)

def get_client_type(type_id):
    return sql_queries.fetch_client_type(type_id)

def get_all_client_types():
    return sql_queries.fetch_all_client_types()
