#importing the connector for mysql
import mysql.connector

def get_countries(mycursor,mydb):

     #Calling the Close cursor functions
    mycursor = CloseCursor(mycursor, mydb)

    # User's country
    country = input("Enter all or specific country:  ").strip()

    # Create tuple
    my_data = (country,)

    try:

        if country.lower() == "all":
            # Create Query for all countries
            sql_query = 'SELECT * from EmployeesPerCountry;'
            mycursor.execute(sql_query)
        else:
            # Create Query for specific input
            sql_query = 'SELECT * from EmployeesPerCountry WHERE country_name = %s;'
          
            mycursor.execute(sql_query, my_data)

        # Results from the query
        query_result = mycursor.fetchall()

        # Check if user entered value is valid
        if not query_result:
            print(f"There is no country named {country} in the table")
            return

        # Looping through the results
        for record in query_result:
            print(f"Name: {record[0]}, NUM_EMP: {record[1]}")

    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")
        


# Function to get the managers
def get_managers(mycursor, mydb):

    #Calling the Close cursor function
    mycursor = CloseCursor(mycursor, mydb)
    #Users manager 
    manager = input("Enter all or specific department:  ")

     # Create tuple
    my_data = (manager,)

    try:
        if manager.lower() == "all":
            # Create Query for all titles
            sql_query = 'SELECT * FROM managers;'
            mycursor.execute(sql_query)
        else:
              # Create Query for specific input
            sql_query = 'SELECT * FROM managers WHERE department_name = %s;'
            mycursor.execute(sql_query, my_data)

        # Results from the query
        query_result = mycursor.fetchall()


      # Check if user entered value is valid
        if not query_result:
            print(f"There is no department named {manager} in the table")
            return

        # Looping through the results
        for record in query_result:
           print(f"Department Name: {record[5]}, Number of Managers:{record[6]}")

    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")
        

#Function to get the job titles
def get_jobtitles(mycursor, mydb):

    #Calling the Close cursor function
    mycursor = CloseCursor(mycursor, mydb)
    #Users dependent 
    Dependents = input("Enter all or specific job title:  ")

     # Create tuple
    my_data = (Dependents,)

    try:
        if Dependents.lower() == "all":
            # Create Query for all titles
            sql_query = 'SELECT * FROM DependentsByJobTitle;'
            mycursor.execute(sql_query)
        else:
              # Create Query for specific input
            sql_query = 'SELECT * FROM DependentsByJobTitle WHERE job_title = %s;'
            mycursor.execute(sql_query, my_data)

        # Results from the query
        query_result = mycursor.fetchall()

        # Check if user entered value is valid
        if not query_result:
            print(f"No records found for {Dependents} department")
            return

        # Looping through the results
        for record in query_result:
            print(f"Job Title: {record[0]}, Dependent: {record[1]}")

    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")
        


#Function to get the Hires
def get_Hires(mycursor, mydb):

    #Calling the Close cursor function  
    mycursor = CloseCursor(mycursor, mydb)

      #Users Hire
    Hires = input(" View hiring data by year and department:  ")

    # Create tuple
    my_data = (Hires,)

    try:
        if Hires.lower() == "all":
            # Create Query for all hires
            sql_query = 'SELECT * FROM DepartmentHiresByYear;'
            mycursor.execute(sql_query)
        else:
              # Create Query for specific input
            sql_query = 'SELECT * FROM DepartmentHiresByYear WHERE YEAR = %s;'
            mycursor.execute(sql_query, my_data)

        # Results from the query
        query_result = mycursor.fetchall()

         # Check if user entered value is valid
        if not query_result:
            print(f"No records found for {Hires} department")
            return

        # Looping through the results
        for record in query_result:
            print(f"YEAR: {record[0]}, DEPARTMENT NAME: {record[1]}, EMPLOYEES HIRED: {record[2]}")

    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")
        


#Function to get the Titles by Salaries
def get_Salary_Title(mycursor, mydb):

    #Calling the Close cursor function
    mycursor = CloseCursor(mycursor, mydb)
    #User title
    Salary = input("Enter all or specific title: ")

     # Create tuple
    my_data = (Salary,)

    try:
        if Salary.lower() == "all":
            # Create Query for all salaries
            sql_query = 'SELECT * FROM AvgSalaryByJobTitlee;'
            mycursor.execute(sql_query)
        else:
             # Create Query for specific input
            sql_query = 'SELECT * FROM AvgSalaryByJobTitlee WHere job_title = %s;'
            mycursor.execute(sql_query, my_data)

        # Results from the query
        query_result = mycursor.fetchall()

         # Check if user entered value is valid  
        if not query_result:
            print(f"No records found for {Salary} department")
            return

        # Looping through the results
        for record in query_result:
            print(f"Job Title: {record[0]}, Average Salary: {record[1]}, Number of Employees: {record[2]}")

    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")
        



#Function to get the Departments by Salaries
def Department_Salary(mycursor, mydb):

    #Calling the Close cursor function
    mycursor = CloseCursor(mycursor, mydb)  
    #User Department
    Salary = input("Enter all or specific Department: ")

     # Create tuple
    my_data = (Salary,)

    try:
        if Salary.lower() == "all":
            # Create Query for all departments
            sql_query = 'SELECT * FROM AvgSalaryByDepartment;'
            mycursor.execute(sql_query)
        else:
            # Create Query for specific input
            sql_query = 'SELECT * FROM AvgSalaryByDepartment WHere department_name = %s;'
            mycursor.execute(sql_query, my_data)

        # Results from the query
        query_result = mycursor.fetchall()

         # Check if user entered value is valid
        if not query_result:
            print(f"No records found for {Salary} department")
            return


        # Looping through the results
        for record in query_result:
            print(f"Department Name: {record[0]}, Average Salary: {record[1]}, Number of Employees: {record[2]}")

    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")
        
    
#Function to get the employee dependents
def get_Emp_Dependents(mycursor, mydb):

    #Calling the Close cursor function
    mycursor = CloseCursor(mycursor, mydb)
     
    # User Department
    EmpD = input("Enter 'all' or employee First and LastName: ")

    try:
        if EmpD.lower() == "all":
            # Create Query for all dependents
            sql_query = 'SELECT * FROM EmployeeDependents;'
            mycursor.execute(sql_query)
        else:
            # Get first name and last name as separate inputs
            first_name, last_name = EmpD.split()

            # Create tuple
            my_data = (first_name, last_name)

            # Create Query for specific input
            sql_query = "SELECT first_name, last_name, `Number of Dependents` FROM EmployeeDependents WHERE first_name = %s AND last_name = %s;"
            mycursor.execute(sql_query, my_data)

        # Results from the query
        query_result = mycursor.fetchall()

          # Check if user entered value is valid
        if not query_result:
            print(f"No records found for {EmpD}")
            return

        # Looping through the results
        for record in query_result:
            print(f"Name: {record[0]} {record[1]}, Number Of Dependents: {record[2]}")

    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")
        


#Function to get the locations
def get_Location(mycursor, mydb):

    #Calling the Close cursor function
    mycursor = CloseCursor(mycursor, mydb)
    #user region
    region = input("Enter 'all' or specific region:")
       
         #Create Tuple
    my_data = (region,)

    try:
        if region.lower() == "all":
            # Create Query for all dependents
            sql_query = 'SELECT * FROM regions;'
            mycursor.execute(sql_query)
        else:
            # Create Query for specific input
            sql_query = " SELECT * FROM regions WHERE region_name = %s;"
            mycursor.execute(sql_query, my_data)

        # Results from the query
        query_result = mycursor.fetchall()

          # Check if user entered value is valid
        if not query_result:
            print(f"The region named {region} was not found in table")
            return

        # Looping through the results
        for record in query_result:
            print(f"ID: {record[0]}, Region Name: {record[1]}")

    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")
        


#Function to add a dependent
def addDependent(mycursor, mydb):

    #Calling the Close cursor function
    mycursor = CloseCursor(mycursor, mydb)

    try:
        # User dependent input
        FirstName = input("Enter a First Name: ")
        LastName = input("Enter a Last Name: ")
        Rela = input("Enter relationship: ")
        empID = int(input("Enter employee ID number: "))

         # Create the query 
        sql_query= """INSERT INTO dependents (first_name, last_name, relationship, employee_id) VALUES('{}', '{}', '{}','{}');""".format(FirstName, LastName, Rela, empID)

        # Execute the query
        mycursor.execute(sql_query)
        print(f"The New dependent was added succesfully")
        # Commit the changes
        mydb.commit()


    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")


#Function to add a job
def addJob(mycursor, mydb):

    #Calling the Close cursor function
    mycursor = CloseCursor(mycursor, mydb)

    try:
        # User job input
        Job_Title = input("Enter a Job Title: ")
        min_salary = int(input("Enter minimum salary: "))
        max_salary = int(input("Enter the maximum salary: "))

          # Create the query 
        sql_query= """INSERT INTO jobs (job_title, min_salary, max_salary) VALUES('{}', '{}', '{}');""".format(Job_Title, min_salary, max_salary)

        if (max_salary < min_salary):
            print("maximum salary cannot be less than the minimum salary")
        else:
        # Execute the query
          mycursor.execute(sql_query)
        print(f"The New job was added succesfully")
        # Commit the changes
        mydb.commit()

    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")


#Function to delete a dependent
def DeleteDependent(mycursor, mydb):

     #Calling the Close cursor function
    mycursor = CloseCursor(mycursor, mydb)    

    try:
        # User deoendent input
        empID = int(input("Enter employee ID to be deleted: "))

          #Create Tuple
        mydata = (empID,)

          # Create the query 
        sql_query= 'DELETE FROM dependents WHERE dependent_id = %s;'

        # Execute the query
        mycursor.execute(sql_query,mydata)
        print(f"The dependent was deleted succesfully")
        # Commit the changes
        mydb.commit()

    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")

#Function to delete a job
def DeleteJob(mycursor, mydb):

    #Calling the Close cursor function
    mycursor = CloseCursor(mycursor, mydb)
    try:
        # User job input
        JobID = int(input("Enter job ID to be deleted: "))

           #Create Tuple
        mydata = (JobID,)

          # Create the query 
        sql_query= 'DELETE FROM jobs WHERE job_id = %s;'

        # Execute the query
        mycursor.execute(sql_query,mydata)
        print(f"The job was deleted succesfully")

        # Commit the changes
        mydb.commit()


    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")

#Function to update employee Firstname
def UpdateEmp(mycursor, mydb):

    #Calling the Close cursor function
    mycursor = CloseCursor(mycursor, mydb)

    try:
        # User employee input
        EmpID = int(input("Enter employee ID to be Updated: "))
        FirstName = input("Type in new first name:")

         #Create Tuple
        mydata = ( FirstName, EmpID)

        # Create the query 
        sql_query = "UPDATE employees SET first_name = %s WHERE employee_id = %s"

        # Execute the query
        mycursor.execute(sql_query, mydata)
        print("Employees FirstName was updated successfully")

        # Commit the changes
        mydb.commit()

    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")
        #print(f"The error is {sql_query}")


#Function to update employee Lastname
def UpdateEmpL(mycursor, mydb):
       
       #Calling the Close cursor function
    mycursor = CloseCursor(mycursor, mydb)

    try:
        # User employee input
        EmpID = int(input("Enter employee ID to be Updated: "))
        LastName = input("Type in new last name:")

           #Create Tuple
        mydata = (LastName, EmpID)

        # Create the query 
        sql_query = "UPDATE employees SET last_name = %s WHERE employee_id = %s"

        # Execute the query
        mycursor.execute(sql_query, mydata)
        print(f"Employee LastName was updated successfully")

        # Commit the changes
        mydb.commit()

    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")
       #print(f"The error is {sql_query}")



# Function to update max_salary for a job
def UpdateMaxSal(mycursor, mydb):

    #Calling the Close cursor function
    mycursor = CloseCursor(mycursor, mydb)

    try:
        # User job input
        EmpID = int(input("Enter job ID to be Updated: "))
        Salary = float(input("Type in new max salary:"))

        # Create Tuple
        mydata = (Salary, EmpID)

        # Create the query 
        sql_query = "UPDATE jobs SET max_salary = %s WHERE job_id = %s"

        if Salary == 0:
            print("The maximum salary cannot be 0") 
        else:
            mycursor.execute(sql_query, mydata)
            print("Job data was updated successfully")  

        # Commit the changes
        mydb.commit()

    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")


#Function to update employee Firstname
def UpdateMinSal(mycursor, mydb):

   #Calling the Close cursor function
    mycursor = CloseCursor(mycursor, mydb)

    try:
        # User job input
        EmpID = int(input("Enter job ID to be Updated: "))
        Salary = float(input("Type in new min salary:"))
           
          #Create Tuple
        mydata = (Salary,EmpID)

         # Create the query 
        sql_query = "UPDATE jobs SET min_salary = %s WHERE job_id= %s"

        # Execute the query
        mycursor.execute(sql_query, mydata)
        print("Employee minimum salary was updated successfully")

        # Commit the changes
        mydb.commit()

    except Exception as err:
        print(f"Error occurred: {err}\nPlease enter a valid input.")

        
#Function to close the cursor object for functions      
def CloseCursor(mycursor, mydb):
    mycursor.close()
    return mydb.cursor()


      

#Menu Function

def print_menu():
    print("\n")
    print("-------- View Data-------")
    print("Choose an option")
    print("1. View employee data count per Country")
    print("2. View manager count by department")
    print("3. View dependent data per job title")
    print("4. View hiring data by year and department")
    print("5. View average Salary data by job title")
    print("6. View salary Salary data by department")
    print("7. View dependent data by employee") 
    print("8. View location data by region")    
    print("\n")
    return
    
    
   
def Add_Data():
    print("-------- Add Data-------")
    print("9. Add a Dependent")
    print("10. Add a Job")
    print("\n")
    
    
    
def Delete_Data():
    print("-------- Delete Data-------")
    print("11. Delete a Dependent")
    print("12. Delete a Job")
    print("\n")

def Update_Data():
    print("-------- Update Data-------")
    print("13. Update employees FirstName: ")
    print("14. Update employees LastName: ")
    print("15. Update jobs Maximum salary: ")
    print("16. Update jobs Minimum salary: ")
    print("\n")


def Exit():
     print("-------- Exit Application-------")
     print("17. Exit ")
     print("\n")
    

  


#calling the print method and handling any invalid input from the user. 
def get_user_choice():
    while True:
        try:
            print_menu()
            Add_Data()
            Delete_Data()
            Update_Data()
            Exit()
            choice = int(input("Enter Choice: "))
            return choice
        except ValueError as err:
            print("Error Occurred:Enter numbers only")


def main():
#create a connector object
    try:
        # Fill in your own information
         mydb = mysql.connector.connect(
            host="mysql-container",
            user="USER ID",
            passwd="YOUR-PASSWORD",
            database="DATABASE-NAME"
        )
         print("Successfully connected to the database!")
    except Exception as err:
        print(f"Error Occured: {err}\nExiting program...")
        quit()

    #create database cursor
    mycursor = mydb.cursor()

    while(True):
        user_choice = get_user_choice()
        if(user_choice == 1):
            #call the function to query the countries
            get_countries(mycursor, mydb)
        elif(user_choice == 2):
             #call the function to query the managers
            get_managers(mycursor, mydb)
        elif(user_choice == 3):
            #call the function to query the job_titles
           get_jobtitles(mycursor, mydb)
        elif(user_choice == 4):
             #call the function to query the hires
            get_Hires(mycursor, mydb)
        elif(user_choice == 5):
              #call the function to query the Salaries by title
            get_Salary_Title(mycursor, mydb)
        elif(user_choice == 6):
          #call the function to query the Salaries by Department
          Department_Salary(mycursor, mydb)
        elif(user_choice == 7):
            #call the function to query the dependents
            get_Emp_Dependents(mycursor,mydb)
            #call the function to query the Location
        elif(user_choice == 8):
            get_Location(mycursor, mydb) 
            #call the function to add a dependent
        elif(user_choice == 9):
            addDependent(mycursor, mydb) 
             #call the function to add a Job
        elif(user_choice == 10):
            addJob(mycursor, mydb) 
              #call the function to Delete a dependent
        elif(user_choice == 11):
            DeleteDependent(mycursor, mydb)
               #call the function to Delete a Job
        elif(user_choice == 12):
            DeleteJob(mycursor, mydb) 
                 #call the function to Update employee FirstName 
        elif(user_choice == 13):
            UpdateEmp(mycursor, mydb) 
                 #call the function to Update employee LastName 
        elif(user_choice == 14):
            UpdateEmpL(mycursor, mydb) 
                #call the function to Update Max salary
        elif(user_choice == 15):
            UpdateMaxSal(mycursor, mydb) 
                 #call the function to Update Min salary
        elif(user_choice == 16):
            UpdateMinSal(mycursor, mydb) 
             #Exit the program
        elif(user_choice == 17):
            print("Bye Bye!!!")
            break 

        #If the user enters an option not listed in the menu
        elif user_choice not in range(1, 18):
             print("Enter a valid choice")

         # close the cursor
        mycursor.close()  


main()

