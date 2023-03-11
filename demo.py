import requests
from bs4 import BeautifulSoup
import re

pdata = [3,4,1,4,3,3,3,4,2,1,2,2,3,2,1,2,4,3,1,4,1,3,3,2,2,3,3,2,4,2,3,4,4,3,2,2,3,3,4,2,1,1,1,3,3,4,3,
         2,1,3,2,3,3,1,3,3,4,4,1,1,1,1,2,3,2,1,1,2,3,1,3,3,1,3,3,2,1,2,3,4,3,2,3,1,4,1,3,2,3,2,2,4,4,3,
         4,2,4,2,4,2,2,2,3,2,1,3,3,1,1,3,2,2,4,1,2,3,3,2,3,1,1,1,3,1,3,4,3,1,1,1,4,1,4,1,4,1,3,4,2,3,2,3,4,1,2,2,4,2,4,1,1,4,3,
          2,1,1,2,4,4,3,1,1,3,1,1,2,1,2,1,1,3,1,2,2,4,4,2,4,3,3]
url = "https://kvsexam23feb23s2.cbtexam.in/Candidate/ResponseSheet.aspx?Urlval=fa871369-2971-460b-9691-98a128654623&Rollno=220423910220081&PgId=21"
search_word = "Answer Given"

# Make a GET request to the website and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all occurrences of the search word in the text of the website
word_list = []
all_words=soup.find_all(string=True)

findname="Name of the Candidate"
for text in all_words:
    if findname in text:
        print(text)

for text in all_words:
    if search_word in text:
        
        # If the search word is found, add it to the list
        word_list.append(text)
        
#print (word_list)
word_list2 = []
input_string = "Answer Given:- 1, Option ID : -605"

for mnstring in word_list:
    # Find the index of the comma
    comma_index = mnstring.find(",")
    # Extract the substring before the comma
    output_string = mnstring[:comma_index]
     #to extract integer
    integers = re.findall('\d+', output_string)

    integers = list(map(int, integers))
    
    word_list2.append(integers)


#print(word_list2) # Output: Hello
ind = 0
right=0
for txt in word_list2:
    try:
        
        if txt[0]==pdata[ind]:
            right=right+1
            
        
        ind=ind+1
    except :
        break    
        

print("total rightr q are",right)