from audioop import add
from tkinter import E
from typing import Type
from flask import Flask, render_template, request,redirect, url_for
import sqlite3
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Offices')
def viewoffice():
    con = sqlite3.connect("gsatest.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Offices")
    rows = cur.fetchall()
    return render_template("viewOffice.html", rows = rows)

@app.route('/addOffice')
def addoffice():
    return render_template("addOffice.html")

@app.route('/saveOffice', methods = ["POST","GET"])
def saveoffice():
    msg = "msg"
    if request.method == "POST":  
        try:  
            Office_name = request.form["Office_name"]  
            City = request.form["City"]  
            Square_ft = request.form["Square_ft"]
             
            with sqlite3.connect("gsatest.db") as con:  
                con.execute("PRAGMA foreign_keys = 1")
                cur = con.cursor()  
                cur.execute("INSERT into Offices (Office_name, City, Square_ft) values (?,?,?)",(Office_name,City,Square_ft))  
                con.commit()  
                msg = "GSA Office successfully Added" 
        except:  
        
            msg = "We can not add that office to the list." 
        finally:   
            return redirect(url_for('viewoffice'))
            

@app.route("/deleteOffice")  
def deleteoffice():  
    return render_template("deleteOffice.html")  
 
@app.route("/deleterecordOffice",methods = ["POST"])  
def deleterecordOffice():  
    Office_name = request.form["Office_name"]  
    
    with sqlite3.connect("gsatest.db") as con:  
        con.execute("PRAGMA foreign_keys = 1")
        try:  
            cur = con.cursor()  
            cur.execute("DELETE from Offices where Office_name = ?", (Office_name,))  
    
            msg = "Office Successfully Deleted" 
        except:  
            msg = "Cannot be Deleted, Office is managing an active Rental Agreement" 
        finally:  
            return render_template("deleteOfficeRecord.html",msg = msg)



@app.route('/Agencies')
def viewagencies():
    con = sqlite3.connect("gsatest.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Agency")
    rows = cur.fetchall()
    return render_template("viewAgencies.html", rows = rows)

@app.route('/addAgency')
def addagency():
    return render_template("addAgency.html")

@app.route('/saveAgency', methods = ["POST","GET"])
def saveagency():
    msg = "msg"
    if request.method == "POST":  
        try:  
            Agency_id = request.form["Agency_id"]  
            Agency_name = request.form["Agency_name"]  
            Address = request.form["Address"]
            Phone = request.form["Phone"]
             
            with sqlite3.connect("gsatest.db") as con:  
                con.execute("PRAGMA foreign_keys = 1")
                cur = con.cursor()  
                cur.execute("INSERT into Agency (Agency_id, Agency_name, Address, Phone) values (?,?,?,?)",(Agency_id, Agency_name, Address,Phone))  
                con.commit()  
                msg = "Agency successfully Added" 
        except:  
        
            msg = "We can not add that agency to the list." 
        finally:   
            return redirect(url_for('viewagencies'))
            

@app.route("/deleteAgency")  
def deleteagency():  
    return render_template("deleteAgency.html")  
 
@app.route("/deleterecordAgency",methods = ["POST"])  
def deleterecordAgency():  
    Agency_id = request.form["Agency_id"]  
    
    with sqlite3.connect("gsatest.db") as con:  
        con.execute("PRAGMA foreign_keys = 1")
        try:  
            cur = con.cursor()  
            cur.execute("DELETE from Agency where Agency_id = ?", (Agency_id,))  
    
            msg = "Agency Successfully Deleted" 
        except:  
            msg = "Cannot be Deleted, Agency is in an active Rental Agreement" 
        finally:  
            return render_template("deleteAgencyRecord.html",msg = msg)



@app.route('/Rentals')
def viewrentals():
    con = sqlite3.connect("gsatest.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Rental")
    rows = cur.fetchall()
    return render_template("viewRentals.html", rows = rows)

@app.route('/addRental')
def addrentals():
    return render_template("addRental.html")

@app.route('/saveRental', methods = ["POST","GET"])
def saverentals():
    msg = "msg"
    if request.method == "POST":  
        try:  
            Rental_id = request.form["Rental_id"]  
            rent_amount = request.form["rent_amount"]  
            end_date = request.form["end_date"]
            
             
            with sqlite3.connect("gsatest.db") as con:  
                con.execute("PRAGMA foreign_keys = 1")
                cur = con.cursor()  
                cur.execute("INSERT into Rental (Rental_id, rent_amount, end_date) values (?,?,?)",(Rental_id, rent_amount, end_date))  
                con.commit()  
                msg = "Rental successfully Added" 
        except:  
        
            msg = "We can not add that agency to the list." 
        finally:   
            return redirect(url_for('viewrentals'))
            

@app.route("/deleteRental")  
def deleterental():  
    return render_template("deleteRental.html")  
 
@app.route("/deleterecordRental",methods = ["POST"])  
def deleterecordRental():  
    Rental_id = request.form["Rental_id"]  
    
    with sqlite3.connect("gsatest.db") as con:  
        con.execute("PRAGMA foreign_keys = 1")
        try:  
            cur = con.cursor()  
            cur.execute("DELETE from Rental where Rental_id = ?", (Rental_id,))  
    
            msg = "Rental Successfully Deleted" 
        except:  
            msg = "Cannot be Deleted, Rental is in an active Rental Agreement with one or more Agencies" 
        finally:  
            return render_template("deleteRentalRecord.html",msg = msg)
    



@app.route('/Agreements')
def viewagreements():
    con = sqlite3.connect("gsatest.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Agreement NATURAL JOIN Managed")
    rows = cur.fetchall()
    return render_template("viewAgreements.html", rows = rows)

@app.route('/addAgreement')
def addagreement():
    return render_template("addAgreement.html")

@app.route('/saveAgreement', methods = ["POST","GET"])
def saveagreement():
    msg = "msg"
    if request.method == "POST":  
        try:  
            Agreement_id = request.form["Agreement_id"]  
            agency_id = request.form["agency_id"]  
            rental_id = request.form["rental_id"]
            Office_name = request.form["Office_name"]
            
             
            with sqlite3.connect("gsatest.db") as con:  
                con.execute("PRAGMA foreign_keys = 1")
                cur = con.cursor()  
                cur.execute("INSERT into Agreement (Agreement_id, agency_id, rental_id) values (?,?,?)",(Agreement_id, agency_id, rental_id))  
                cur.execute("INSERT into Managed (Agreement_id, Office_name) values (?,?)", (Agreement_id, Office_name))
                con.commit()
                
                msg = "Agreement successfully Added" 
        except:  
        
            msg = "We can not add that agreement to the list." 
        finally:   
            return redirect(url_for('viewagreements'))
            

@app.route("/deleteAgreement")  
def deleteagreement():  
    return render_template("deleteAgreement.html")  
 
@app.route("/deleterecordAgreement",methods = ["POST"])  
def deleterecordAgreement():  
    Agreement_id = request.form["Agreement_id"]  
    
    with sqlite3.connect("gsatest.db") as con:  
        con.execute("PRAGMA foreign_keys = 1")

        try:  
            cur = con.cursor()  
            cur.execute("DELETE from Managed where Agreement_id = ?", (Agreement_id,))  
            cur.execute("DELETE from Agreement where Agreement_id = ?", (Agreement_id,))
            con.commit()
            msg = "Agreement Successfully Deleted" 
        except:  
            msg = "Cannot be Deleted" 
        finally:  
            return render_template("deleteAgreementRecord.html",msg = msg)

