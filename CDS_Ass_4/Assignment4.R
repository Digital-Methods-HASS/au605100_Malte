install.packages("tidyverse")
library(tidyverse)
download.file("https://ndownloader.figshare.com/files/11492171", "data/SAFI_clean.csv", mode = "wb")
df <- read.csv("data/SAFI_clean.csv")
