## Loading the R Packages required for Time Series Anlaysis
install.packages("tseries")
install.packages("forecast")
require(tseries)
require(forecast)
require(nlme)
require(lmtest)
require(stats)
confidence_intv <- 0.95

## Loading the required Raw Data for Trend [F(t)] analysis
data <- read.csv("C:/Users/Chiku/Desktop/IE 594 Time Series - Inflation Rate/Inflation rate in US 25yrs.csv",
                 header=TRUE)
attach(data)
data_title <- c("Inflation Rate in the USA, monthly, (Mean subtracted)")
inflation_ts <- ts(data$inflation, frequency = 12, start = 1)
inflation <- inflation_ts-mean(inflation_ts)
inflation

## Plotting the Mean subtracted Data
plot(inflation, main=c(data_title), ylab="Inflation Rate in the USA", xlab="No of months, Starting 1990", col='black', type='l')

##### Trend fitting for F(t) #####
linear <- lm(inflation ~ months)
summary(linear)
rss_linear <- sum(residuals(linear)^2)

poly2 <- lm(inflation ~ poly(months, 2, raw = TRUE))
summary(poly2)
rsspoly2 <- sum(residuals(poly2)^2)

poly3 <- lm(inflation ~ poly(months, 3, raw = TRUE))
summary(poly3)
rsspoly3 <- sum(residuals(poly3)^2)

poly4 <- lm(inflation ~ poly(months, 4, raw = TRUE))
summary(poly4)
rsspoly4 <- sum(residuals(poly4)^2)

poly5 <- lm(inflation ~ poly(months, 5, raw = TRUE))
summary(poly5)
rsspoly5 <- sum(residuals(poly5)^2)

##### ARMA Modeling and Adequacy check for X(t)#####
data_residuals <- read.csv("C:/Users/Chiku/Desktop/IE 594 Time Series - Inflation Rate/Final residuals.csv",
                 header=TRUE)
attach(data_residuals)
data_residuals_title <- c("Residuals X(t)")
residuals_ts <- ts(residuals, frequency = 12, start = 1)

## Plotting Residuals X(t)
plot(residuals_ts, main=c(data_residuals_title), ylab="Residuals X(t)", xlab="No of months, Starting 1990", col='black', type='l')

## ARMA Modeling and F-test Checks
fit1 <- arima(residuals_ts, order=c(1,0,0))
summary(fit1)
rssfit1 <- sum(residuals(fit1)^2)

fit2 <- arima(residuals_ts, order=c(1,0,1))
summary(fit2)
rssfit2 <- sum(residuals(fit2)^2)

fit3 <- arima(residuals_ts, order=c(2,0,1))
summary(fit3)
rssfit3 <- sum(residuals(fit3)^2)

fit4 <- arima(residuals_ts, order=c(3,0,2))
summary(fit4)
rssfit4 <- sum(residuals(fit4)^2)

fit5 <- arima(residuals_ts, order=c(4,0,3))
summary(fit5)
rssfit5 <- sum(residuals(fit5)^2)

fit6 <- arima(residuals_ts, order=c(5,0,4))
summary(fit6)
rssfit6 <- sum(residuals(fit6)^2)

fit7 <- arima(residuals_ts, order=c(6,0,5))
summary(fit7)
rssfit7 <- sum(residuals(fit7)^2)

## Plotting the Roots for the adequate model ARMA (5,4)
plot(fit6)

##### Forecasting and Generating the Graphs #####

# One-step ahead prediction
onestep.for <- fitted.Arima(fit6)[1:300]
data_prediction <- c("One-step ahead prediction plot")
plot(onestep.for, main=c(data_prediction), ylab="X(t)", xlab="No of months, Starting 1990", col='black', type='l')

write.csv(onestep.for, "C:/Users/Chiku/Desktop/IE 594 Time Series - Inflation Rate/one step ahead.csv")

# Forecasting for next 12 months
forecast(fit6, 12)
forecast_1yr <- forecast(fit6, 12)
data_forecast <- c("Forecasting Inflation rate for next 12 months")
plot(forecast_1yr, main=c(data_forecast), ylab="X(t)", xlab="No of months, Starting 1990", col='black', type='l')

# Joint Optimization
integrated_model = arima(inflation, order=c(5,0,4), xreg=NULL)
joint_pred = predict(integrated_model, n.ahead=ceiling(length(inflation)*(1-confidence_intv)), newxreg=NULL)
ts.plot(inflation, joint_pred$pred, main="vs Forecast with 95% Confidence Interval")

# Comparing Forecasts with Raw data and exporting Forecasts
write.csv(forecast_1yr, "C:/Users/Chiku/Desktop/IE 594 Time Series - Inflation Rate/12 month forecasts.csv")

??fitted.Arima
