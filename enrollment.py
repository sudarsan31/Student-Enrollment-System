from flask import *
import psycopg2,webbrowser
import csv
try:
      connection= psycopg2.connect(user = "postgres",
                                  password = "sudarishu",
                                  host = "127.0.0.1",
                                  port = "5432");
      print("DataBase Opened Successfully")
      print("--------------------------------------------")
except:
      print("not connected")
      print(" ")

cursor=connection.cursor()
cursor.execute("create table enrollment(Name varchar(15),DOB varchar(10),Sex varchar(10),Email varchar(50),Contact varchar(10),FatherName varchar(20),MotherName varchar(20),FatherOccupation varchar(20), MotherOccupation varchar(20),Qualification varchar(10),Medium varchar(10),Percentage varchar(10),Certificate varchar(10),Institute varchar(50),Country varchar(10), State varchar(15),District varchar(15),Address Varchar(100))")
print("Table created Successfully")
          
obj=Flask(__name__)

@obj.route('/')
def register():
    return render_template("register.html")


@obj.route('/Not_Eligible')
def f2():
    s='''<b><h1>Sorry,You are not Eligible</h1></b>
    <b><h3>Your percentage should be above 60%</h3></b>  
    <a href="/">Go back to home page</a>'''
    return s

@obj.route('/view')
def view():
    cursor.execute("select * from enrollment") 
    value=cursor.fetchall()
    return render_template("final.html",value=value)

@obj.route('/done',methods=["POST","GET"])
def done(): 
    p=request.form.get("Percentage")
    if(request.method=="POST" and p>="60" or p>="60%"):
          n=request.form.get("Name")
          d=request.form.get("DOB")
          s=request.form.get("Sex")
          e=request.form.get("Email")
          c=request.form.get("Contact")
          f=request.form.get("FatherName")
          m=request.form.get("MotherName")
          fo=request.form.get("FatherOccupation")
          mo=request.form.get("MotherOccupation")
          q=request.form.get("Qualification")
          me=request.form.get("Medium")
          p=request.form.get("Percentage")
          ce=request.form.get("Certificate")
          i=request.form.get("Institute")
          coun=request.form.get("Country")
          state=request.form.get("State")
          dist=request.form.get("District")
          addr=request.form.get("Address")
          cursor.execute("insert into enrollment values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(n,d,s,e,c,f,m,fo,mo,q,me,p,ce,i,coun,state,dist,addr))
          cursor.execute("select * from enrollment")
          value=cursor.fetchall()
          csvfile=open('D:\\Enroll.csv',"w",newline='')         #This is for writing the data into Excel sheet
          for v in value:
              csvfile.write(str(v[0])+","+str(v[1])+","+str(v[2])+","+str(v[3])+","+str(v[4])+","+str(v[5])+","+str(v[6])+","+str(v[7])+","+str(v[8])+","+str(v[9])+","+str(v[10])+","+str(v[11])+","+str(v[12])+","+str(v[13])+","+str(v[14])+","+str(v[15])+","+str(v[16])+","+str(v[17])+"\n")
          csvfile.close()                          #here the Excel sheet code is getting over 
          s='''<b><h1>Registration Succesful</h1></b>
          <b><h2>You can View your Submission Details</h2></b>
          <a href="/view">View Details</a>'''     
          print("Registration details stored succesfully in Database")
          return s  
 
    else:
          return redirect(url_for("f2"))             


if __name__=="__main__":
    webbrowser.open_new("http://127.0.0.1:5000/")
    obj.run()

connection.commit()