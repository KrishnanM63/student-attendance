import sqlite3

class attendance:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.c=self.con.cursor()
        self.c.execute("""
             CREATE TABLE IF NOT EXISTS students(
                pid INTEGER NOT NULL PRIMARY KEY,
                sid INTEGER NOT NULL,
                name TEXT NOT NULL
             )          
                       """)
        self.con.commit()
        
        self.c.execute("""
              CREATE TABLE IF NOT EXISTS attendancedetai(
                  pid INTEGER NOT NULL PRIMARY KEY,
                  sid INTEGER NOT NULL,
                  status TEXT NOT NULL,
                  date TEXT NOT NULL
                  
              )         
                       """)
    def insert(self,sid,name):
        sql="""
        INSERT INTO students  VALUES(NULL,?,?)
        """
        self.c.execute(sql,(sid,name)) 
        self.con.commit()
    def attendance_insert(self,sid,status,date):
        sql="""
        INSERT INTO attendancedetai VALUES(NULL,?,?,?)
        """   
        self.c.execute(sql,(sid,status,date))
        self.con.commit()
    def studelist(self):
        return self.c.execute("SELECT *FROM students").fetchall()    
    def fetch(self,sid):
       return self.c.execute("SELECT * FROM   attendancedetai WHERE sid=? ",(sid,)).fetchall()
    def showstddetail(self,sid):
        return self.c.execute("SELECT * FROM   students WHERE sid=? ",(sid,)).fetchall()
       
   
          
    
       
