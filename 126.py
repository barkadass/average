Grodes = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
Students = {'Anna','Ilya','Amalia','Maria','Misha'}
Students = {'Anna':(5,3,3,5,4),'Ilya':(2,2,2,3),'Amalia':(4,5,5,2),'Maria':(4,4,3),'Misha':(5,5,5,4,5)}
a = sum(Grodes[0])
b = sum(Grodes[1])
c = sum(Grodes[2])
d = sum(Grodes[3])
e = sum(Grodes[4])
average = {'Anna':(a/5),'Ilya':(b/4), 'Amalia':(c/4), 'Maria':(d/3), 'Misha':(e/5)}
print(average)
