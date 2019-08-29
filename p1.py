#Develop a menu-based python program (menu items: 1.String length 2. Join strings 3. Compare strings 4. Reverse string 5. Check string is palindrome or not
#7. Check word in sentence) by means of user defined functions.
def PrintMenu():
    print("\n     Menu");
    print("1)String Length");
    print("2)Join String");
    print("3)Compare String");
    print("4)Reverce String");
    print("5)Check string is palindrome or not");
    print("6)Check word in Sentence");
    print("7)Exit");

def GetChoice():
    ch=int(input("Enter an integer for choice:"));
    return ch;

def StringLen(s):
    a=len(s);
    return a;

def CheckWord(s):
    l=s.split();
    a=input("Enter the word for search:");
    b=l.index(a);
    c=print(a,"Found at position",b);
    return c;

def ReverceString(s):
    x=s.split();
    a=[];
    for element in x:
        a.append(element[::-1]);
    return a;

def JoinString(s,t):
    m=[];
    s1=m.append(s);
    s1=m.append(t);
    n=''.join(m);
    return n;

def CompareString(s,t):
    if s == t:
        print("Strings are same");
    else:
        print("Strings are not same");

def Palindrome(p):
    

def Choice(ch):
    if ch == 1:
        print("Length of the String is=",StringLen(s));
    elif ch == 2:
        print("Join Strings:",JoinString(s,t));
    elif ch == 3:
        print("Compare Strings",CompareString(s,t));
    elif ch == 4:
        print("reverce String",ReverceString(s));
    elif ch == 5:
        print("Check string is palindrome or not",Palindrome(p));
    elif ch == 6:
        print("Check word in Sentence",CheckWord(s));
    else:
        print("Invalid Choice");

def repeate():
    while True:
        PrintMenu();
        ch=GetChoice();
        if ch==7:
            return;
        else:
            Choice(ch);
    
s="This is String1";
t="String2";
p="abcba";
print("My String Is=",s);
PrintMenu();
repeate();
