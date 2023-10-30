

class B():
    def myfunc2(self):
        print("hello this is myfunc 2")

class C():
    def myfunc2(self):
        print("hello this is myfunc 3")

class D(B,C):
    pass

D = D()

# D.myfunc3()
D.myfunc2()
# D.myfunc1()

"""
select user_name from users 
join training_details on user.user_id = training_details.user_id
group by  user.username, training_details.Training_id,training_details.Training_date
having count(*) > 1
order by Training_details.Training_date DESC;

"""

"""
df["column_name"].fillna(df["column_name"].mean())


list = []
np_array = np.array()
"""