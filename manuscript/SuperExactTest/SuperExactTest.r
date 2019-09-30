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
Result <- supertest(data,n=19608)
sink("Fig1_Venn_David.txt")
"Fig1_Venn_David.xlsx"
"Sets:"
cats
"Result:"
summary(Result)
sink(file=NULL)

xlsx_sheet <- read.xlsx("Fig2_Venn_David.xlsx", sheet = 1, startRow = 1, colNames = FALSE)
cats <- unique(xlsx_sheet$X2)
data <- lapply(cats, function(x,s) xlsx_sheet[xlsx_sheet$X2 == x,]$X1)
Result <- supertest(data,n=20993)
sink("Fig2_Venn_David.txt")
"Fig2_Venn_David.xlsx"
"Sets:"
cats
"Result:"
summary(Result)
sink(file=NULL)

xlsx_sheet <- read.xlsx("Fig3_David_Venn.xlsx", sheet = 1, startRow = 1, colNames = FALSE)
cats <- unique(xlsx_sheet$X2)
data <- lapply(cats, function(x,s) xlsx_sheet[xlsx_sheet$X2 == x,]$X1)
Result <- supertest(data,n=19608)
sink("Fig3_David_Venn.txt")
"Fig3_David_Venn.xlsx"
"Sets:"
cats
"Result:"
summary(Result)
sink(file=NULL)
