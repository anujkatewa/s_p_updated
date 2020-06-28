from binarytree import Node
import random
from matplotlib import pyplot as plt

def pie(cl):
    c = []
    c.append(cl)
    c.append(100-cl)
    cll = ['May have diabetes','May not have diabetes']
    explode = (0.1, 0)
    plt.figure(figsize =(10, 7)) 
    plt.pie(c, explode = explode, labels = c ,shadow = True ,center = (0,0)) 
    plt.legend(cll, loc = (0.9,1))
    plt.show()

#question set
dict = {
    #common questions
    1:('Increased thirst','Increased urge to urinate','Increased appetite','Impaired vision'),
    #common questions on type 1 and type 2
    3:('Sleeplessness','Trembling','Sweating','Anxiety','Confusion','Nightmares','Seizures','Sadness','Unconciousness','Numbness','Sleep Walking','Making unusal noises','Leg cramps','Slurred speech','Flushed face','Pale skin','Stomach pains','Deep breathimg','Difficult concentrating','Dehydration','Lack of coordination'),
    #common questions on type 2 and pre-diabete
    4:('Impatience','Infections','Over weight'),
    #questions to confirm type 1
    5:('Weight reduction','Fruity breath odour','Bed wetting','Weakness','Mood swings','Nausea','Vomiting'),
    #questions to confirm type 2
    6:('Weight variation','Tiredness','Slow healing wounds','Dry skin','Aches and pains','Recurrent fungal infection','Rapid heart beat','Area of darkened skin'),
    #questions to confirm pre-diabetes
    8:('Itchy skin','Family history','Depression and stress','Tingling sensation','Recurring gum infections','History of heart disease'),
    #confirming statements
    2:"    You don't have diabetes",
    7:"    You have Type 1 diabetes",
    9:"    You have Type 2 diabetes",
    10:"    You have Pre-Diabetes",
}

''' traversal of tree
1 = common questions
2 = you don't have diabetes
3 = common questions to type 1 and type 2
4 = common questions to type 2 and pre-diabetes
5 = questions to confirm type 1
6 = questions to confirm type 2
7 = you have type 1 diabetes
8 = questions to confirm pre-diabetes
9 = you have type 2 diabetes
10 = you have pre-diabetes '''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.left.left = Node(2)
root.right.left.right = Node(6)
root.right.right.left = Node(6)
root.right.right.right = Node(7)
root.right.left.right.left = Node(8)
root.right.left.right.right = Node(9)
root.right.left.right.left.left = Node(2)
root.right.left.right.left.right = Node(10)
root.right.right.left.left = Node(2)
root.right.right.left.right = Node(9)
print(root)

sp = []
print("Please answer in Yes and No only!")
while root!=None:
    if root.val == 2 or root.val == 7 or root.val == 9 or root.val == 10:
        print(dict[root.val])
        if root.val!=2: 
            print("\n    Symptoms present: ")
            for i in sp:
                print("        "+i)
            if root.val == 7:
                cd = (len(sp)/32)*100
            elif root.val == 9:
                cd = (len(sp)/36)*100
            elif root.val == 10:
                cd = (len(sp)/13)*100
            print("\n    Confidence level = ", cd)
            pie(cd)
        root = root.left
    else:
        a = list(dict[root.val])
        if root.val == 3:
            a = random.choices(a, k=7)
        n=0
        for i in a:
            print("    "+ i +" ?") #pass to html
            ans = input().lower() #get from html
            if ans =='yes':
                n = n + 1
                sp.append(i)
            elif ans!='no':
                print("    Please answer in yes and no only!")
        n = n/len(a)
        if n >= 0.5:
            root = root.right
        else :
            root = root.left