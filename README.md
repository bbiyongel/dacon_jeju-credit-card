# Post COVID-19시대, 신용카드 사용량 예측  
  
> URL : https://dacon.io/competitions/official/235615/overview/  
  

1. 주제  
	- AI 알고리즘 활용 카드 사용 금액 예측  

2. 목표  
	- 신용카드 사용 내역 데이터를 활용한 지역별, 업종별 월간 카드 사용 총액 예측  

3. 배경
	- 신용카드 사용량을 분석을 통한  ‘Post COVID-19 시대’ 신용카드 사용량 예측 모델 개발  
    - 지역 경제 위축 및 중소상공인 경영난 해소를 위한 대책 마련  

4. 평가 척도  
	- RMSLE (Root Mean Square Logarithmic Error)  
	- 제주 지역에 3배 가중치 부여  

5. 외부 데이터  
	- 공공 데이터와 같은 법적인 제약이 없는 경우에만 사용 가능  
	- 공공데이터 다운을 받은 경우 링크를 게시해야 함  
	- 크롤링 시 코드 제출 필수  
	- 2020.04.30 데이터까지만 사용 가능  

6. 데이터 정보  

| No | 컬럼명 | TYPE | 설명 |
|:---:|:---|:---|:---|
| 0 | REG_YYMM | DATE | 연월 |
| 1 | CARD_SIDO_NM | VARCHER | 카드이용지역_시도 (가맹점 주소 기준) |
| 2 | CARD_CCG_NM | VARCHER | 카드이용지역_시군구 (가맹점 주소 기준) |
| 3 | STD_CLSS_NM | VARCHER | 업종명 |
| 4 | HOM_SIDO_NM | VARCHER | 거주지역_시도 (고객 집주소 기준) |
| 5 | HOM_CCG_NM | VARCHER | 거주지역_시군구 (고객 집주소 기준) |
| 6 | AGE | CATEGORY | 연령대 |
| 7 | SEX_CTGO_CD | CATEGORY | 성별 (1: 남성, 2: 여성) |
| 8 | FLC | CATEGORY | 가구생애주기 |
| 9 | CSTMR_CNT | NUMBER | 이용고객수 (명) |
| 10 | AMT | NUMBER | 이용금액 (원) |
| 11 | CNT | NUMBER | 이용건수 (건) |

  
*가구생애주기 (1: 1인가구, 2: 영유아자녀가구, 3: 중고생자녀가구, 4: 성인자녀가구, 5: 노년가구)  


- 0~8컬럼까지의 유니크 값에 대한 통계자료(ex. **202004, 서울, 강서구, 건강보조식품 소매업종에서 서울시 양천구에서 사는 10대 남자 1인가구인 그룹** : 10명, 31만원, 4건 이용)  
- 이용자수 & 이용건수 : 만약 세 사람 A, B, C가 각각 1만원, 2만원, 3만원 결제 후 C가 승인 취소 한다면 이용자 수는 3명, 이용건수는 2건, 이용 금액은 1만원+2만원 = 3만원 집계([토론 링트](https://dacon.io/competitions/official/235615/talkboard/400991?page=1&dtype=recent&ptype=pub))  


---

# Study Log  
