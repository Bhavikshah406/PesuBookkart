import os
import requests
import json



service = 'https://PesuBookkart.mybluemix.net'

while(1):
	choice=int(input("enter your choice\n1)create a category\n2)insert a book in a particular category\n3)get all books in a category\n4)get the price of a book\n5)Remove a book\n6)Remove a category\n7)Modify the price of the book\n8)end\n"))

	if(choice==1):
		
		book=input("enter the category you want to add : "+"\n")
		detail=[1,book]
		print(book)
		#data = json.dumps(detail)
		r = requests.post(service + "/" + "1" + "/" + book)
		print ("Message ID: " + str(r.json()))

	elif(choice==2):
		
		category=input("enter the category you want to add book into "+"\n")
		book=input("enter the details of the book you want to put in our bookkart library with space in between==> name,price,description,number of copies "+"\n")
		bookwithdetails = book.split()
		print(bookwithdetails)
		#detail=[2,category,bookwithdetails]
		#data = json.dumps(detail)
		r = requests.post(service + "/" + "2" + "/" + category + "/" + bookwithdetails[0] + "/" + bookwithdetails[1]+ "/" + bookwithdetails[2]+ "/" +bookwithdetails[3]) 
		print ("Message ID: " + str(r.json()))

	elif(choice==3):
		
		category=input("enter the category "+"\n")
		#detail=[3,category]
		#data = json.dumps(detail)
		r = requests.get(service + "/" + "3" + "/" + category)
		print ("Message ID: " + str(r.json()))

	elif(choice==4):
		
		category=input("enter the category "+"\n")
		book=input("enter the book name"+"\n")
		#detail=[4,category,book]
		#data = json.dumps(detail)
		r = requests.get(service + "/" + "4" + "/" + category + "/" + book)
		print ("Message ID: " + str(r.json()))


	elif(choice==5):
		
		category=input("enter the category "+"\n")
		book=input("enter the book name"+"\n")
		#detail=[5,category,book]
		#data = json.dumps(detail)
		r = requests.delete(service  + "/" + "5" + "/" + category + "/" + book )
		print ("Message ID: " + str(r.json()))

	elif(choice==6):
		
		category=input("enter the category "+"\n")
		#detail=[6,category]
		#data = json.dumps(detail)
		r = requests.delete(service + "/" + "6" + "/" + category)
		print ("Message ID: " + str(r.json()))

	elif(choice==7):
		
		category=input("enter the category "+"\n")
		book=input("enter the book name"+"\n")
		newcost=input("enter the new cost"+"\n")
		#detail=[7,category,book,newcost]
		#data = json.dumps(detail)
		r = requests.put(service+ "/" + "7" + "/" + category + "/" + book + "/" + newcost)
		print ("Message ID: " + str(r.json()))

	elif(choice==8):
		break
	else:
		print("wrong choice \n")


os._exit(0)
