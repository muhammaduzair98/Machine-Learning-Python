import random as rd

string = """1 	6.25	3.75	5.76	7.50	24.11	9.00	56.39	
2 	7.00	4.75	8.84	8.50	35.29	9.50	73.89	
3 	9.75	10.00	3.07	6.50	35.29	7.50	72.12	
4 	9.75	9.75	2.69	5.50	28.82	5.50	62.02	
5 	5.50	1.50	4.03	8.00	24.11	7.50	50.66	
6 	7.25	5.00	8.84	6.50	28.23	7.50	63.33	
7 	9.87	9.75	4.61	10.00	31.17	6.50	71.92	
8 	9.00	9.75	4.61	7.50	22.35	7.50	60.72	
9 	9.87	10.00	6.92	10.00	42.35	9.00	88.15	
10 	9.00	8.50	2.30	5.00	22.94	6.00	53.75	
11 	9.87	9.75	6.15	9.00	28.23	7.00	70.01	
12 	9.75	9.75	6.53	9.00	37.05	9.50	81.60
13 	9.75	10.00	5.00	5.00	26.47	8.00	64.22	
14 	9.75	10.00	7.69	10.00	30.00	10.00	77.44	
15 	5.00	4.75	1.53	5.50	22.35	6.00	45.14	
16 	9.62	8.75	8.84	5.00	27.05	10.00	69.28	
17 	8.87	8.50	6.73	6.00	24.70	8.00	62.81	
18 	6.75	8.75	6.53	6.00	14.11	5.00	47.16	
19 	8.87	9.75	5.00	9.50	35.88	6.00	75.01	
20 	6.50	9.50	6.15	5.50	22.35	6.00	56.01	
21 	4.75	4.25	1.73	7.00	31.17	7.50	56.41	
22 	6.75	4.50	5.76	0.00	32.94	6.00	55.96	
23 	9.25	7.25	3.46	7.50	34.11	10.00	71.58	
24 	9.62	9.75	5.76	0.00	27.05	6.50	58.70	
25 	8.87	7.50	5.00	0.00	33.52	9.50	64.40	
26 	7.25	7.00	4.23	0.00	28.82	8.50	55.80	
27 	9.75	9.75	5.38	8.00	35.29	8.50	76.68	
28 	9.87	9.75	5.38	9.00	38.23	9.00	81.24	
29 	9.75	10.00	6.53	6.00	31.17	8.00	71.46	
30 	9.00	7.50	4.61	7.00	21.17	5.00	54.29	
31 	9.62	9.75	7.30	6.50	25.88	7.00	66.07
32 	9.50	9.00	6.15	8.00	30.58	5.50	68.74	
33 	9.37	9.00	2.30	6.00	35.88	10.00	72.57	
34 	8.87	8.25	5.76	6.00	34.11	6.50	69.51	
35 	9.37	9.25	6.53	5.50	27.05	7.00	64.72	
36 	9.25	9.12	3.07	7.50	29.41	5.00	63.36	
37 	9.37	8.12	4.23	6.00	25.29	6.00	59.02	
38 	9.12	5.50	8.07	6.00	15.29	7.50	51.50	
39 	7.25	7.87	5.00	0.00	27.05	6.00	53.18	
40 	8.25	3.50	3.07	8.00	21.76	7.00	51.59"""


def data_set(val):
  val= val.split("\t")
  val = " ".join(val)
  val = val.split("\n")
  val = " ".join(val)
  val = val.split("  ")
  val = " ".join(val)
  val = val.split(" ")
  return val


string = set_data(string)
string = [float(val) for val in string]
r=0

for i in range(0,len(string),8):
  del string[i-r]
  r+=1



dataset = []
Y = string[6::7]

for i in range(0,len(string),7):
  temp=[1]
  dataset.append(temp+string[i:i+6])





def hypothesis(val, t):
  size= len(val[0])
  temp=[]
  for k in range(len(dataset)):
    sum=0
    for i in range(len(val[k])):
      sum= sum + (val[k][i] * t[i])
    temp.append(sum)
  return temp


def cost(m, val, y):
    total = 0
    for i in range(m):
        squared_error = (y[i] - val[i]) ** 2
        total += squared_error
    
    return total * (1 / (2*m))

def newCost(m,appro,y,indeval,val):
  total=0
  for i in range(m):
    squared_error = (appro[i]-y[i]) * val[i][indeval]
    total += squared_error
  
  temp= total * (0.00015 / (m))
  return abs(temp)


theta = [1,2,3,4,5,6,7]  # initial  guess
m = len(dataset)
result=[]
for i in range(m):
    approvalimate_values = hypothesis(dataset, theta)
    print("Theta = ", theta, " , COST = ", cost(m,Y , approvalimate_values),'\n')
    result.append(cost(m, Y, approvalimate_values))
    for k in range(len(theta)):
      theta[k]=theta[k]-new_cost(m,Y,approvalimate_values,k,dataset)



print("\nTheta with  : ",theta," is having minimum cost which is  ",min(result))