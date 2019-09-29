#install.packages("SuperExactTest")
#install.packages("openxlsx", dependencies = TRUE)
#install.packages("dplyr")
#install.packages("tidyverse")
library(SuperExactTest)
library("dplyr")
require(openxlsx)
library(tidyverse)

xlsx_sheet <- read.xlsx("Fig1_Venn_David.xlsx", sheet = 1, startRow = 1, colNames = FALSE)
cats <- unique(xlsx_sheet$X2)
data <- lapply(cats, function(x,s) xlsx_sheet[xlsx_sheet$X2 == x,]$X1)
Result <- supertest(data,n=20687)


sink("human.txt")
"Human Fig1"
"Sets:"
cats
"Result:"
summary(Result)
sink(file=NULL)


# plot(Result, Layout="landscape", sort.by="size", keep=FALSE,
# 	bar.split=c(70,180), show.elements=TRUE, elements.cex=0.7,
# 	elements.list=subset(summary(Result)$Table,Observed.Overlap <= 20),
# 	show.expected.overlap=TRUE,expected.overlap.style="hatchedBox",
# 	color.expected.overlap='red')
# dev.off()