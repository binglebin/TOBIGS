rm(list=ls())

#1. 작업공간 지정해주기
setwd("C:/Users/CHAEBIN/Desktop")

#2. 데이터 불러오기
data = read.csv("Auction_master_train.csv", fileEncoding = "utf-8")

#3. 데이터 확인해보기
head(data)
str(data)

colSums(is.na(data)) #결측치 확인

#4. 필요없는 열 제거
df = subset(data, select = -c(Auction_key, Appraisal_company, Final_result, Creditor, addr_si, addr_dong, addr_li, addr_san, addr_bunji1, addr_bunji2, addr_etc, road_name, road_bunji1, road_bunji2, Specific)) 
#설명
# Auction_key 고유키값 삭제
# Appraisal_company Factor , Creditor Factor 회사이름 y변수에 영향을 미치지 않음
# Final_result 값이 하나밖에 없음
# addr_si, addr_dong, addr_li, addr_san, addr_bunji1, addr_bunji2, addr_etc, road_name, road_bunji1, road_bunji2,  위도 경도를 사용하여 분석하여 주소값 사용 x
# Specific Factor가 대부분이 결측치


#날짜데이터로 변경
df$Appraisal_date = as.Date(df$Appraisal_date)
df$First_auction_date = as.Date(df$First_auction_date)
df$Final_auction_date = as.Date(df$Final_auction_date)
df$Preserve_regist_date = as.Date(df$Preserve_regist_date)
df$Close_date = as.Date(df$Close_date)

str(df)
colSums(is.na(df))
#결측치 확인

# 문제 1. 파생변수 3개 이상 만들기
# 1) 경매가 이루어진 기간
df$auction_period = df$Final_auction_date - df$First_auction_date
df$auction_period = as.numeric(df$auction_period)
# 2) 위치 cluster
library(ggplot2)
library(caret)
ggplot(df, aes(point.x, point.y )) +geom_point() #두개의 군집
df.kmeans <- kmeans(df[,c(24,25)], centers = 2, iter.max = 10000) #군집수 2개로 k-means
df.kmeans$center
df.kmeans$cluster
df$cluster <- as.factor(df.kmeans$cluster)
# 3) 아파트 총층수 분의 현재 층수
df$CurrentPerTotal_Floor = df$Current_floor / df$Total_floor

#위도 경도 데이터 삭제
df = subset(df, select = -c(point.x, point.y ))
# 회귀분석을 위한 날짜 데이터 삭제
df = subset(df, select = -c(Appraisal_date, First_auction_date, Final_auction_date, Preserve_regist_date, Close_date ))

str(df)
summary(df)



# 회귀분석.
lm = lm(Hammer_price ~ ., data = df)
summary(lm)
# cluster 변수에서 NA 값 발생 제거하고 회귀분석

df = subset(df, select = -c(cluster))
lm = lm(Hammer_price ~ ., data = df)
summary(lm)

#다중공선성 확인
#install.packages("car")
library("car")
vif(lm)
#다중공선성 발생 vif가 가장큰 변수 하나씩 삭제 후 재검정
df = subset(df, select = -c(Total_land_auction_area))
df = subset(df, select = -c(Total_building_auction_area))
df = subset(df, select = -c(Total_appraisal_price))
df = subset(df, select = -c(Auction_count))
df = subset(df, select = -c(Total_building_area))
lm = lm(Hammer_price ~ ., data = df)
vif(lm)
#모든 변수 vif 10이하

#최종 모델에 사용될 변수 레이블과의 분포
par(mfrow = c(4, 4))
plot(df$Auction_class, df$Hammer_price)
plot(df$Bid_class, df$Hammer_price)
plot(df$Claim_price, df$Hammer_price)
plot(df$Auction_miscarriage_count , df$Hammer_price)
plot(df$Total_land_gross_area , df$Hammer_price)
plot(df$Total_land_real_area , df$Hammer_price)
plot(df$Minimum_sales_price , df$Hammer_price)
plot(df$addr_do , df$Hammer_price)
plot(df$Apartment_usage , df$Hammer_price)
plot(df$Total_floor , df$Hammer_price)
plot(df$Current_floor , df$Hammer_price)
plot(df$Share_auction_YorN , df$Hammer_price)
plot(df$Close_result , df$Hammer_price)
plot(df$auction_period , df$Hammer_price)
plot(df$CurrentPerTotal_Floor , df$Hammer_price)

# 회귀분석 결과
summary(lm)
#Multiple R-squared:  0.9905,	Adjusted R-squared:  0.9905
# p-value: < 2.2e-16
#모델 유의! 설명력 99.05%!



#데이터 train, test 분리 7:3
#install.packages("caret")
library(caret)
idx <- createDataPartition(y = df$Hammer_price, p = 0.7, list =FALSE)
train<- df[idx,]
test <- df[-idx,]
str(train)


#전진선택법, 후진제거법, 단계적회귀
#설명변수를 넣지않은 모델
fit.con <- lm(Hammer_price ~ 1, train)
#다 적합한 모델
fit.full <- lm(Hammer_price~., train)

# 전진선택법
fit.forward <- step(fit.con, list(lower=fit.con, upper=fit.full), direction = "forward")
# 후진제거법
fit.backward <- step(fit.full, list(lower=fit.con, upper = fit.full), direction = "backward")
# 단계적회귀방법(stepwise)
fit.both <- step(fit.con, list(lower=fit.con, upper=fit.full), direction = "both")

summary(fit.forward) # Multiple R-squared:  0.9921,	Adjusted R-squared:  0.992 
summary(fit.backward) # Multiple R-squared:  0.9921,	Adjusted R-squared:  0.992 
summary(fit.both) # Multiple R-squared:  0.9921,	Adjusted R-squared:  0.992

#cross validation
cv <- trainControl(method = "cv", number = 5, verbose = T)

#lm
str(test)
colSums(is.na(train))
train.lm <- train(Hammer_price~.,train, method = "lm", trControl =cv)
predict.lm <- predict(train.lm,test[,-14])
y <- test[,14]
RMSE(predict.lm,y) #57322164

#r^2값
1 - sum((y-predict.lm)^2)/sum((y-mean(y))^2) #0.9837919

#이상치 확인
library(car)
outlierTest(fit.backward, order=TRUE)

#test에 대입
predicted <- predict(fit.backward, test[ ,-14])
y <- test[,14]
RMSE(predicted,y) #57365707
#오히려 높아짐
