library(ggplot2)
library(reshape2)

data <- read.csv("longGesturePreds.csv")
data$gesture <- factor(data$gesture,c("N","FT","ST","FS","FSA","VSS","BS","SS","C"))
ggplot(data,aes(x=factor(data$gesture))) + geom_bar() + xlab('gesture')+ylab('count')
ggsave("20130427-GesturePredictionsHist.pdf")

