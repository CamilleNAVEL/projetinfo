library(tidyverse);library(igraph);library(openxlsx)
g <- make_ring(10)
shortest_paths(g, 8, 2)
E(g)$weight <- seq_len(ecount(g))
shortest_paths(g, 8, 2)
E(g)
plot(g)
E(g)$weight

a=matrix(runif(5*5, min=-10, max=10), ncol=5)
diag(a)=0

g=graph.adjacency(a, mode="undirected", weighted = TRUE)
plot(g)

plot(g, edge.label=round(E(g)$weight, 3))


tgv=read.xlsx("data/tarifs-tgv-inoui-ouigo.xlsx")
tgv=read.csv("data/tarifs-tgv-inoui-ouigo.csv", sep=";")

gares=c("PARIS GARE DE LYON","MONTPELLIER SAINT-ROCH","MARSEILLE ST CHARLES","LYON PART DIEU","BORDEAUX ST JEAN","RENNES")

tgv2=tgv %>% 
  filter(Gare.origine %in% gares & Destination %in% gares) %>% 
  select(origine=Gare.origine,destination=Destination,prix=Prix.minimum) 

tgv2=tgv2 %>% 
  rbind(tgv2 %>% mutate(dest=origine,origine=destination,destination=dest) %>% select(-dest)) %>% 
  group_by(origine,destination) %>% 
  summarise(prix=min(prix),.groups="drop")

tgv3=tgv2 %>% 
  pivot_wider(names_from="destination",values_from="prix")

tgv4=tgv3 %>% 
  select_at(tgv3$origine)

Mtgv=as.matrix(tgv4)
colnames(Mtgv)=NULL
g=graph.adjacency(Mtgv, mode="undirected", weighted = TRUE)
plot(g)
plot(g, edge.label=E(g)$weight)

g2=graph_from_data_frame(d=tgv2, directed=F)
plot(g2)
plot(g2, edge.label=E(g2)$weight)

tgv %>% filter(str_detect(Gare.origine,"PARIS")) %>% select(Gare.origine,Gare.origine...code.UIC) %>% unique()

