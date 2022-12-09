import db.connection

# Drop previous table of same name if one 
conn = db.connection.dbCon()
cursor = conn.cursor()

# Insert some data into table
sqlQuery = "INSERT INTO dsdl_item (dsdl_grp_cd, dsdl_item_cd, dsdl_item_nm, acvt_stts, otpt_sqnc, reg_user_id, reg_dtm) VALUES (%s, %s, %s, %s, %s, %s, %s)"
params = ('A0001', 'A0003', '맞팔', 'Y', 0, 'SYSTEM', 'DATE_FORMAT(now(), "%Y%m%d%H%i%s")')
cursor.execute(sqlQuery, params)
print("Inserted",cursor.rowcount,"row(s) of data.")

# # Read data
# cursor.execute("SELECT * FROM inventory;")
# rows = cursor.fetchall()
# print("Read",cursor.rowcount,"row(s) of data.")
# # Print all rows
# for row in rows:
#     print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))

# # Update a data row in the table
# cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s;", (300, "apple"))
# print("Updated",cursor.rowcount,"row(s) of data.")

# # Delete a data row in the table
# cursor.execute("DELETE FROM inventory WHERE name=%(param1)s;", {'param1':"orange"})
# print("Deleted",cursor.rowcount,"row(s) of data.")

# Cleanup
conn.commit()
cursor.close()
conn.close()
print("Done.")