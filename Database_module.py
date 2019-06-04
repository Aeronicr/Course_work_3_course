import sqlite3

connection = sqlite3.connect("Dental_clinic.db")
def read_from_db_pat():
        query = "SELECT * FROM patients"
        result = connection.execute(query)
        return result
        connection.close()

def sort_alpha_pat():
        query = "SELECT * FROM patients ORDER BY surname"
        result = connection.execute(query)
        return result
        connection.close()

def sort_id_pat():
        query = "SELECT * FROM patients ORDER BY id_patient DESC"
        result = connection.execute(query)
        return result
        connection.close()

def sort_date_pat():
        query = "SELECT * FROM patients ORDER BY date_birth"
        result = connection.execute(query)
        return result
        connection.close()

def sort_date_pat_down():
        query = "SELECT * FROM patients ORDER BY date_birth DESC"
        result = connection.execute(query)
        return result
        connection.close()

def sort_sex1_pat():
        query = "SELECT * FROM patients ORDER BY sex DESC"
        result = connection.execute(query)
        return result
        connection.close()

def sort_sex2_pat():
        query = "SELECT * FROM patients ORDER BY sex"
        result = connection.execute(query)
        return result
        connection.close()

################################################################
        # Doctors
################################################################

def read_from_db_doc():
        query = "SELECT * FROM doctors"
        result = connection.execute(query)
        return result
        connection.close()

def sort_alpha_doc():
        query = "SELECT * FROM doctors ORDER BY surname"
        result = connection.execute(query)
        return result
        connection.close()

def sort_id_doc():
        query = "SELECT * FROM doctors ORDER BY id_doctor DESC"
        result = connection.execute(query)
        return result
        connection.close()

def sort_id_cab():
        query = "SELECT * FROM doctors ORDER BY cabinet_number"
        result = connection.execute(query)
        return result
        connection.close()

def sort_id_spec():
        query = "SELECT * FROM doctors ORDER BY specialty"
        result = connection.execute(query)
        return result
        connection.close()

##################################################################
        # Medicines
##################################################################

def read_from_db_med():
        query = "SELECT * FROM price_list"
        result = connection.execute(query)
        return result
        connection.close()

def sort_alpha_med():
        query = "SELECT * FROM price_list ORDER BY title"
        result = connection.execute(query)
        return result
        connection.close()

def sort_id_medicines():
        query = "SELECT * FROM price_list ORDER BY destination_code DESC"
        result = connection.execute(query)
        return result
        connection.close()

def sort_cost1_medicines():
        query = "SELECT * FROM price_list ORDER BY cost_service"
        result = connection.execute(query)
        return result
        connection.close()

def sort_cost2_medicines():
        query = "SELECT * FROM price_list ORDER BY cost_service DESC"
        result = connection.execute(query)
        return result
        connection.close()

######################################################################
        # Discount
######################################################################

def read_from_db_dis():
        query = "SELECT * FROM discount"
        result = connection.execute(query)
        return result
        connection.close()

def sort_id_dis():
        query = "SELECT * FROM discount ORDER BY discount_code DESC"
        result = connection.execute(query)
        return result
        connection.close()

def sort_id_alpha():
        query = "SELECT * FROM discount ORDER BY categories_citizen"
        result = connection.execute(query)
        return result
        connection.close()

def sort_interest1_dis():
        query = "SELECT * FROM discount ORDER BY interest_discount"
        result = connection.execute(query)
        return result
        connection.close()

def sort_interest2_dis():
        query = "SELECT * FROM discount ORDER BY interest_discount DESC"
        result = connection.execute(query)
        return result
        connection.close()

########################################################################
        # Visited
########################################################################

def read_from_db_vis():
        query = "SELECT * FROM appeals"
        result = connection.execute(query)
        return result
        connection.close()

def read_vis_pat():
        query = "SELECT id_patient, surname FROM patients"
        result = connection.execute(query)
        return result
        connection.close()

def read_vis_doc():
        query = "SELECT id_doctor, surname FROM doctors"
        result = connection.execute(query)
        return result
        connection.close()

def read_vis_dis():
        query = "SELECT discount_code, categories_citizen FROM discount"
        result = connection.execute(query)
        return result
        connection.close()




