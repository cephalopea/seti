dist_data<-read.csv("./Desktop/Logan/Smith/Senior\ Year/Game\ Theory/Project\ 3/code/dist_data.csv")

agg_data<-read.csv("./Desktop/Logan/Smith/Senior\ Year/Game\ Theory/Project\ 3/code/agg_data.csv")

comm_data<-read.csv("./Desktop/Logan/Smith/Senior\ Year/Game\ Theory/Project\ 3/code/comm_data.csv")

dev_data<-read.csv("./Desktop/Logan/Smith/Senior\ Year/Game\ Theory/Project\ 3/code/dev_data.csv")

arms_data<-read.csv("./Desktop/Logan/Smith/Senior\ Year/Game\ Theory/Project\ 3/code/arms_data.csv")

random_data<-read.csv("./Desktop/Logan/Smith/Senior\ Year/Game\ Theory/Project\ 3/code/randomize_data.csv")

ggplot(agg_data, aes(x=civ1.agg, y=civ2.agg, color=outcome))+
  geom_point()

ggplot(comm_data, aes(x=civ1.com, y=civ2.com, color=outcome))+
  geom_point()

ggplot(dist_data, aes(x=dist, y=rounds, color=outcome))+
  geom_point()+
  geom_jitter()

ggplot(dev_data, aes(x=civ1.dev, y=civ2.dev, color=outcome))+
  geom_point()

ggplot(arms_data, aes(x=civ1.arms, y=civ2.arms, color=outcome))+
  geom_point()

ggplot(random_data %>% filter(rounds<500), aes(x=dist,y=rounds,color=outcome))+
  geom_point()+
  geom_jitter()


