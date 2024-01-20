args = commandArgs(trailingOnly=TRUE)
mode=args[1] ## "lm" "poi"
core=as.numeric(args[2])
LinOut.df_rds<-args[3]
name=args[4]

current<-getwd()
setwd("/lab/solexa_weissman/cweng/Projects/MitoTracing_Velocity/SecondaryAnalysis/Donor4Donor9")
source("activate.R")
Sys.setenv(RENV_PATHS_CACHE = "/lab/solexa_weissman/cweng/Packages/R/x86_64-pc-linux-gnu-library/4.1-focal")
setwd(current)
library(EZsinglecell2)
library(scMitoTracing)
library(dplyr)
library(tibble)
library(openxlsx)
## Read in the LinOut.gene.df file
print("Read in")
print(LinOut.df_rds)
LinOut.df<-readRDS(LinOut.df_rds)


## Run regression
if(mode=="lm"){
print("run linear model")
LinOut.result<-Run_Lin_regression(LinOut.df,n.cores=core)
}else if(mode=="poi"){
print("run poisson model")
LinOut.result<-Run_Lin_regression_poi(LinOut.df,n.cores=core)
}

saveRDS(LinOut.result,paste(name,"RDS",sep="."))
write.xlsx(LinOut.result,paste(name,"xlsx",sep="."),rowNames=T)
