#**********************************************************************************************

# 1. SET WORKING DIRECTORY AND LOAD PACKAGES

## Load stargarzer package for summary statistics and regression tables
library(stargazer)

## Load Applied Econometrics Package for testing and heteroskedasticity robust standard errors
library(AER)

## Load ggplot2 Package for Nice Graphs and Easily Fitting Curves (NEW)
library(ggplot2)

#**********************************************************************************************

# 2. LOAD DATA

## Load dataset on wages and relevant variables
mydata=read.csv(file="match_dif_stats.csv")

## Broad overview of data
summary(mydata)

## Creating a dataframe converting all values into positive from mydata
mydatapos=abs(mydata)

## Plotting variables against each other
pdf("career_win_score.pdf")
ggplot(mydata, aes(y=mydatapos$Score, x=mydatapos$Career.Win..)) +                        
  geom_point(alpha = .3) +                                            
  stat_smooth(method = "lm", formula = y ~ x, col="blue") +     
  ggtitle("Relationship Between Career Win Percentage and Score") +                    
  theme(plot.title = element_text(hjust = 0.5)) +                      
  scale_x_continuous(name="Win Percentage", limits=c(0, 1)) +                            
  scale_y_continuous(name="Score", limits=c(0, 3))
dev.off()

pdf("rank_score.pdf")
ggplot(mydata, aes(y=mydatapos$Score, x=mydatapos$Rank)) +                        
  geom_point(alpha = .3) +                                            
  stat_smooth(method = "lm", formula = y ~ x, col="blue") +     
  ggtitle("Relationship Between Career Win Percentage and Score") +                    
  theme(plot.title = element_text(hjust = 0.5)) +                      
  scale_x_continuous(name="Rank", limits=c(0, 1100)) +                            
  scale_y_continuous(name="Score", limits=c(0, 3))
dev.off()

pdf("current_win_score.pdf")
ggplot(mydata, aes(y=mydatapos$Score, x=mydatapos$Current.Year.Win..)) +                        
  geom_point(alpha = .3) +                                            
  stat_smooth(method = "lm", formula = y ~ x, col="blue") +     
  ggtitle("Relationship Between Current Year Win Percentage and Score") +                    
  theme(plot.title = element_text(hjust = 0.5)) +                      
  scale_x_continuous(name="Win Percentage", limits=c(0, 1)) +                            
  scale_y_continuous(name="Score", limits=c(0, 3))
dev.off()

pdf("top_10_win_score.pdf")
ggplot(mydata, aes(y=mydatapos$Score, x=mydatapos$Career.Won.against.Top.10..)) +                        
  geom_point(alpha = .3) +                                            
  stat_smooth(method = "lm", formula = y ~ x, col="blue") +     
  ggtitle("Relationship Between Career Win Against Top 10 % and Score") +                    
  theme(plot.title = element_text(hjust = 0.5)) +                      
  scale_x_continuous(name="Against Top 10 %", limits=c(0, 1)) +                            
  scale_y_continuous(name="Score", limits=c(0, 3))
dev.off()


## Sequential Hypothesis Testing
lin_reg = lm(Score ~ Rank + Career.Win.. + Career.Double.Fault.. + Career.Ace.. + Career.Break.Point.Saved.. + Career.Won.against.Top.10.. +
               Career.Won.on.Hard.Court.. + Career.Won.on.Clay.Court.. + Career.Ace.Against.. + Career.First.Serve.Points.Return.Won.. + Career.Points.Won.. +
               Current.Year.Win.. + Current.Year.Double.Fault.. + Current.Year.Ace.. + Current.Year.Break.Point.Saved.. + Current.Year.Won.against.Top.10.. + 
               Current.Year.Won.on.Hard.Court.. + Current.Year.Won.on.Clay.Court.. + Current.Year.Ace.Against.. + Current.Year.First.Serve.Points.Return.Won.. + 
               Current.Year.Points.Won.., data=mydatapos)
cov=vcovHC(lin_reg, type = "HC1")    
se=sqrt(diag(cov))

stargazer(lin_reg, type="text", se=se)

alias(lin_reg)

linearHypothesis(lin_reg,c("Rank=0"),vcov = vcovHC(lin_reg, "HC1"))

mydata$CareerWin2 = mydata$Career.Win.. * mydata$Career.Win..
mydata$WonTop10_2 = mydata$Career.Won.against.Top.10.. * mydata$Career.Won.against.Top.10..

simple_reg_quad = lm(Score ~ Career.Win.. + CareerWin2 + Career.Won.against.Top.10.. + WonTop10_2, data=mydata)
cov2=vcovHC(simple_reg_quad, type = "HC1")    
se2=sqrt(diag(cov2))

simple_reg_linear = lm(Score ~ Career.Win.. + Career.Won.against.Top.10.., data=mydata)
cov3=vcovHC(simple_reg_linear, type = "HC1")    
se3=sqrt(diag(cov3))

stargazer(simple_reg_linear, simple_reg_quad, type="text", se=list(se3, se2))

alias(simple_reg)
linearHypothesis(simple_reg,c("WonTop10_2=0"),vcov = vcovHC(simple_reg, "HC1"))

double_fault_reg = lm(Score ~ Career.Double.Fault.. + Current.Year.Double.Fault.., data=mydatapos)
cov4=vcovHC(double_fault_reg, type = "HC1")    
se4=sqrt(diag(cov4))

stargazer(simple_reg_linear, simple_reg_quad, double_fault_reg, type="text", se=list(se2, se3, se4))

