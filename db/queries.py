import db.connection
# Drop previous table of same name if one


def 등록_구분자항목(params):
    conn = db.connection.dbCon()
    cursor = conn.cursor()
    sqlQuery = "INSERT INTO dsdl_item (dsdl_grp_cd, dsdl_item_cd, dsdl_item_nm, acvt_stts, otpt_sqnc, reg_user_id, reg_dtm) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sqlQuery, params)
    conn.commit()
    cursor.close()
    conn.close()
    return cursor.rowcount


def 조회_구분자항목(params):
    conn = db.connection.dbCon()
    cursor = conn.cursor()
    sqlQuery = "SELECT dsdl_grp_cd, dsdl_item_cd, dsdl_item_nm, acvt_stts, otpt_sqnc, reg_user_id, reg_dtm FROM dsdl_item WHERE dsdl_grp_cd = %(dsdl_grp_cd)s AND dsdl_item_cd = %(dsdl_item_cd)s"
    cursor.execute(sqlQuery, params)
    rows = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return rows


def 수정_구분자항목(params):
    conn = db.connection.dbCon()
    cursor = conn.cursor()
    sqlQuery = "UPDATE dsdl_item SET dsdl_item_nm = (%s) WHERE dsdl_grp_cd = (%s) AND dsdl_item_cd = (%s) AND mod_user_id = 'SYSTEM' AND mod_dtm = (%s)"
    cursor.execute(sqlQuery, params)
    conn.commit()
    cursor.close()
    conn.close()
    return cursor.rowcount


def 삭제_구분자항목(params):
    conn = db.connection.dbCon()
    cursor = conn.cursor()
    sqlQuery = "DELETE FROM dsdl_item WHERE dsdl_grp_cd=%(dsdl_grp_cd)s"
    cursor.execute(sqlQuery, params)
    conn.commit()
    cursor.close()
    conn.close()
    return cursor.rowcount
