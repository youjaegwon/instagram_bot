import connection
import datetime

# Drop previous table of same name if one
conn = connection.dbCon()
cursor = conn.cursor()

now = datetime.datetime.utcnow()


def 등록_구분자항목(params):
    sqlQuery = "INSERT INTO dsdl_item (dsdl_grp_cd, dsdl_item_cd, dsdl_item_nm, acvt_stts, otpt_sqnc, reg_user_id, reg_dtm) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sqlQuery, params)
    conn.commit()
    cursor.close()
    conn.close()
    return cursor.rowcount


def 조회_구분자항목(params):
    sqlQuery = "SELECT dsdl_grp_cd, dsdl_item_cd, dsdl_item_nm, acvt_stts, otpt_sqnc, reg_user_id, reg_dtm FROM dsdl_item WHERE dsdl_grp_cd = (%s)"
    cursor.execute(sqlQuery, params)
    rows = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return rows


def 수정_구분자항목(params):
    sqlQuery = "UPDATE dsdl_item SET dsdl_item_nm = (%s) WHERE dsdl_grp_cd = (%s) AND dsdl_item_cd = (%s)"
    cursor.execute(sqlQuery, params)
    conn.commit()
    cursor.close()
    conn.close()
    return cursor.rowcount


def 삭제_구분자항목(params):
    sqlQuery = "DELETE FROM dsdl_item WHERE dsdl_grp_cd=%(dsdl_grp_cd)s AND dsdl_item_cd=%(dsdl_item_cd)s"
    cursor.execute(sqlQuery, params)
    conn.commit()
    cursor.close()
    conn.close()
    return cursor.rowcount


print("========= 구분자 DB Tester Start =========")

print("1. 등록")
params = ('A0001', 'A0005', '일상', 'Y', 0,
          'SYSTEM', now.strftime('%Y%m%d%H%M%S'))
rowcount = 등록_구분자항목(params)
print("Inserted", rowcount, "row(s) of data.")

print("2. 조회")
params = ('A0001')
rows = 조회_구분자항목(params)
for row in rows:
    print("Data row = (%s)" % (row[0]))

print("3. 수정")
params = ('좋아요반사', 'A0001', 'A0005')
rowcount = 수정_구분자항목(params)
print("Updated", rowcount, "row(s) of data.")

print("4. 삭제")
params = {'dsdl_grp_cd': "A0001", 'dsdl_item_cd': 'A0005'}
rowcount = 삭제_구분자항목(params)
print("Deleted", rowcount, "row(s) of data.")
print("========= 구분자 DB Tester End =========")
