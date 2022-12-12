import db.queries
import datetime

now = datetime.datetime.utcnow()

print("========= 구분자 DB Tester Start =========")

print("1. 등록")
params = ('A0001', 'A0006', '일상', 'Y', 0,
          'SYSTEM', now.strftime('%Y%m%d%H%M%S'))
rowcount = db.queries.등록_구분자항목(params)
print("Inserted", rowcount, "row(s) of data.")

print("2. 조회")
params = ('A0001')
rows = db.queries.조회_구분자항목(params)
for row in rows:
    print("Data row = (%s)" % (row[0]))

print("3. 수정")
params = ('좋아요반사', 'A0001', 'A0006')
rowcount = db.queries.수정_구분자항목(params)
print("Updated", rowcount, "row(s) of data.")

print("4. 삭제")
params = {'dsdl_grp_cd': "A0001", 'dsdl_item_cd': 'A0006'}
rowcount = db.queries.삭제_구분자항목(params)
print("Deleted", rowcount, "row(s) of data.")
print("========= 구분자 DB Tester End =========")
