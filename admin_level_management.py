# admin_level_management.py
import sql_queries

def add_admin_level(access_level_name):
    """ Adds a new admin level to the database and returns its ID """
    return sql_queries.add_admin_level(access_level_name)

def update_admin_level(access_level_id, new_name):
    """ Updates the name of an existing admin level """
    sql_queries.update_admin_level(access_level_id, new_name)

def delete_admin_level(access_level_id):
    """ Deletes an admin level from the database """
    sql_queries.delete_admin_level(access_level_id)

def get_admin_level(access_level_id):
    """ Retrieves a specific admin level by ID """
    return sql_queries.fetch_admin_level(access_level_id)

def get_all_admin_levels():
    """ Retrieves all admin levels """
    return sql_queries.fetch_all_admin_levels()

# You may need to implement additional functions depending on your application needs.
