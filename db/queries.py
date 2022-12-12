import db.connection

# Drop previous table of same name if one
conn = db.connection.dbCon()
cursor = conn.cursor()


def 등록_구분자항목(params):
    sqlQuery = "INSERT INTO dsdl_item (dsdl_grp_cd, dsdl_item_cd, dsdl_item_nm, acvt_stts, otpt_sqnc, reg_user_id, reg_dtm) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sqlQuery, params)
    return cursor.rowcount


def 조회_구분자항목(params):
    sqlQuery = "SELECT dsdl_grp_cd, dsdl_item_cd, dsdl_item_nm, acvt_stts, otpt_sqnc, reg_user_id, reg_dtm FROM dsdl_item WHERE dsdl_grp_cd = %(dsdl_grp_cd)s"
    cursor.execute(sqlQuery, params)
    rows = cursor.fetchall()
    return rows


def 수정_구분자항목(params):
    sqlQuery = "UPDATE dsdl_item SET dsdl_item_nm = (%s) WHERE dsdl_grp_cd = (%s) AND dsdl_item_cd = (%s)"
    cursor.execute(sqlQuery, params)
    return cursor.rowcount


def 삭제_구분자항목(params):
    sqlQuery = "DELETE FROM dsdl_item WHERE dsdl_grp_cd=%(dsdl_grp_cd)s AND dsdl_item_cd=%(dsdl_item_cd)s"
    cursor.execute(sqlQuery, params)
    # conn.commit()
    # cursor.close()
    # conn.close()
    return cursor.rowcount
