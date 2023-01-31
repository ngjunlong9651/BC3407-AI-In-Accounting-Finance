df = fread("/Users/junlongng/Downloads/DBS_SingDollar.csv")
model = lm(df$DBS ~ df$SGD, data = df)

predict = predict(model, newdata =df)
rmse = mean((df$DBS - predict)^2) ^0.5
rmse
