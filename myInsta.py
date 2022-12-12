import db.queries
import datetime
from util import utils
from util import logger

log = logger.logger

# 태그 등록 함수

# #광고성글이 포함하고 있는 단어 리스트
# block_text_list = ['부업', '광고', '협찬' ,'협찬', '재테크', '출금', '공짜', '수익', '카톡', '원금', '할인', '이벤트', '부자', 'Repost', '구매', '예약', '영업', '문의전화', '오시는', '주소' ]


def setListHashTag():
    print("태그 대량 등록 시작")

    cnt = 0
    dsdlGrpCd = 'A0001'
    tags = [{'dsdl_grp_cd': 'A0001', 'dsdl_item_cd': 'A0002',
             'dsdl_item_nm': '좋아요', 'acvt_stts': 'Y', 'otpt_sqnc': 0},
            {'dsdl_grp_cd': 'A0001', 'dsdl_item_cd': 'A0003',
             'dsdl_item_nm': '데일리', 'acvt_stts': 'Y', 'otpt_sqnc': 0},
            {'dsdl_grp_cd': 'A0001', 'dsdl_item_cd': 'A0004',
             'dsdl_item_nm': '팔로우', 'acvt_stts': 'Y', 'otpt_sqnc': 0},
            {'dsdl_grp_cd': 'A0001', 'dsdl_item_cd': 'A0005',
             'dsdl_item_nm': '좋아요반사', 'acvt_stts': 'Y', 'otpt_sqnc': 0},
            {'dsdl_grp_cd': 'A0001', 'dsdl_item_cd': 'A0006',
             'dsdl_item_nm': '맞팔', 'acvt_stts': 'Y', 'otpt_sqnc': 0},
            {'dsdl_grp_cd': 'A0001', 'dsdl_item_cd': 'A0007',
             'dsdl_item_nm': '일상', 'acvt_stts': 'Y', 'otpt_sqnc': 0},
            {'dsdl_grp_cd': 'A0001', 'dsdl_item_cd': 'A0008',
             'dsdl_item_nm': '선팔', 'acvt_stts': 'Y', 'otpt_sqnc': 0},
            {'dsdl_grp_cd': 'A0001', 'dsdl_item_cd': 'A0009',
             'dsdl_item_nm': '소통', 'acvt_stts': 'Y', 'otpt_sqnc': 0},
            {'dsdl_grp_cd': 'A0001', 'dsdl_item_cd': 'A0010',
             'dsdl_item_nm': '일상기록', 'acvt_stts': 'Y', 'otpt_sqnc': 0}]
    delHashTag(dsdlGrpCd)

    for tag in tags:
        tagObj = getHashTag(tag['dsdl_grp_cd'], tag['dsdl_item_cd'])
        if not tagObj:
            params = (tag['dsdl_grp_cd'], tag['dsdl_item_cd'], tag['dsdl_item_nm'], tag['acvt_stts'], tag['otpt_sqnc'], 'SYSTEM',
                      utils.getNowDateTime('%Y%m%d%H%M%S'))
            rowCnt = db.queries.등록_구분자항목(params)
            cnt += rowCnt
    print("태그 : ", cnt, "개 등록 완료")

# 태그 상세 조회 함수


def getHashTag(dsdlGrpCd, dsdlItemCd):
    print("태그 조회")
    params = {'dsdl_grp_cd': dsdlGrpCd, 'dsdl_item_cd': dsdlItemCd}
    row = db.queries.조회_구분자항목(params)
    return row

# 태그 리스트 조회 함수


def getHashTagList(dsdlGrpCd):
    log.info("태그 조회")
    params = {'dsdl_grp_cd': dsdlGrpCd}
    row = db.queries.조회_구분자리스트(params)
    return row

# 태그 수정 함수


def modHashTag(tag):
    print("태그 수정")
    params = (tag['dsdl_item_nm'], tag['dsdl_grp_cd'],
              tag['dsdl_item_cd'], utils.getNowDateTime('%Y%m%d%H%M%S'))
    rowcount = db.queries.수정_구분자항목(params)
    if rowcount > 0:
        print("수정 완료")

# 태그 대량 삭제 함수


def delHashTag(dsdlGrpCd):
    print("태그 대량 삭제")
    if dsdlGrpCd is not None:
        params = {'dsdl_grp_cd': dsdlGrpCd}
        rowcount = db.queries.삭제_구분자항목(params)
        print("삭제 ", rowcount, "개 완료")
    else:
        print("삭제할 그룹 값이 없습니다.")
