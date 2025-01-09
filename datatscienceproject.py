#Linear model code 
library(ISLR) 
library(boot) 
RNGKind(sample.kind "Rounding") 
set.seed(1) 
#Converting number of Installs from factor to numeric 
googleplaystoresInstalls<-as.numeric(gsub(",", ", googleplaystore$Installs)) 
#Convert Genres to factor 
googleplaystore$Genres<-factor (googleplaystore$Genres) 
#Convert Category variables to dummy variables 
googleplaystore<- fastDummies::dummy_cols(googl leplaystore, select_columns "ca tegory") 
#Final linear model that was decided on 
Im.fit=1m(Rating-Reviews Installs, data-googl leplaystore, subset googleplaystor e) 
#Check for collinearity 
VIF(Im(Rating-Reviews Installs, data=googleplaystore)) 
#LOOCV of model 
cv.error rep (0,5) for (i in 1:5) { print(i) glm.fit-glm(Rating-poly(Reviews Installs, i), data-googleplaystore) error[i]=cv.glm(googleplaystore,glm.fit) $delta [1] cv.error [1] 
#Always roll with $delta [1]
 }
cv.error 
# #Finding MSE of linear fit model 
# #Repeated with 10 different seeds for 10 iterations of prediction testing. 
set.seed(1) 
train sample (6935,5548) 
Im.fit=1m(Rating-Reviews Installs, data googleplaystore, subset-train) mean((Rating-predict(Im.fit.googleplaystore)) [-train]^2)

#Decision tree code 
library(tree) 
set.seed(1) 
train sample (1:nrow(googleplaystore), nrow(googleplaystore)/2) 
tree.google_apps tree (Rating, data googleplaystore, subset train) 
summary(tree.google.apps) 
tree.google apps 
#Decision tree plot 
plot(tree.google_apps) 
text(tree.google apps, pretty 0) 
##Pruning the tree is not helpful since size 
##is only 5 terminal nodes 
cv.google_apps 
cv.tree(tree.google_apps) 
plot(cv.google_apps) 
google_apps.test 
googleplaystore[-train, "Rating"] 
yhat predict(tree.google apps, newdata- googleplaystore[-train,]) 
plot(yhat, goog le_apps.test) abline (0,1) 
#MSE of decision tree 
mean((yhat-google_apps.test)^2) 
#Random forests code 
library(random Forest) 
set.seed(1) rf.google apps = random Forest (Rating-. 
                                             data googleplaystore, 
                                             subset train, 
                                             importance TRUE) 
yhat.rf predict(rf.google apps, googleplaystore[-train,]) 
#MSE with random forest method 
mean((yhat.rf-new_google_apps.test)^2)