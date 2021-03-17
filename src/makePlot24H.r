
# R Script
# Plot data from DHT22
#	Last 24 hours
# JD Linares
# 6 Feb 2021

# Usage:
#	Only one .csv file can be in the directory
#	Columns: timestame

library(readr)
library(dplyr)
library(lubridate)
library(ggplot2)

# Read data from CSV
fileNames <- list.files()
recentData <- fileNames[grep("*csv",fileNames)]
data <- read_csv(recentData,col_names=c("Timestamp","Temperature","Humidity"))

# Plot last 24 hours
data_clean <- data %>% 
		filter(Timestamp > Sys.time()-ddays(1) ) %>%
		mutate(Time = with_tz(as_datetime(Timestamp),tzone="US/Central")) %>%
		mutate(Temp = Temperature) 

colors <- c("Temperature"="darkblue","Humidity"="darkred")

p <- ggplot(data_clean,aes(x=Time)) +
		geom_point(aes(y=Temp,color="Temperature"),size=1) +
		geom_point(aes(y=((Humidity+100)/2.5),color="Humidity"),size=1) +
		labs(
			 title="Temperature and Humidity Data",
			 x="Time",
			 y="Temperature (F)",
			 color="Legend"
			 )+
		scale_color_manual(values=colors)+
		theme(legend.position=c(0.92,0.1))+
		scale_y_continuous(
		   sec.axis = sec_axis(~.*2.5-100,name="Humidity (%)"),
		   limits=c(50,80)
			) +
		guides(color=guide_legend(title=NULL))

plotName <- paste0("plot",as.double(Sys.time()),".png")
ggsave(plotName,width=10,height=5)

