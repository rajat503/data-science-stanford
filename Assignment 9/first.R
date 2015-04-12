coin1 <- sample(0:1,1000, replace=TRUE)
coin2 <- sample(0:1,1000, replace=TRUE)
coin3 <- sample(0:1,1000, replace=TRUE)

heads <- coin1+coin2+coin3

data <- data.frame(coin1,coin2,coin3,heads)
filename="results.tsv"
write.table(data, file=filename, quote=FALSE, sep="\t", row.names=FALSE, col.names=TRUE)

new_data <- read.table(filename, header=TRUE, sep="\t")

sum(new_data[,"heads"]>=1)/1000
 
