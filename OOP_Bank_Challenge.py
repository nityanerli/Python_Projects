#!/usr/bin/env python
# coding: utf-8

# ## Object Oriented Programming Challenge

# ##### Bank Account

# In[51]:


class BankAccount():
    
    def __init__(self,accountId,balance):
        
        self.accountId = accountId
        self.balance = balance
        
    def deposite(self,dep_amount):
        self.balance =+ dep_amount
        print("Amount Deposited in your account")
        print('Your total balance is {}'.format(self.balance))
    
    def withdraw(self,wdrw_amt):
            if self.balance >= wdrw_amt:
                self.balance -= wdrw_amt
                print('You have withdrawn {}'.format(wdrw_amt))
            else:
                print('Funds Unavailable!')
            


# In[52]:


acct1 = BankAccount('Jose',100)


# In[53]:


acct1.accountId


# In[54]:


acct1.balance


# In[58]:


acct1.deposite(1000)


# In[42]:


acct1.withdraw(50)


# In[43]:


acct1.balance


# In[44]:


acct1.withdraw(1000)


# In[ ]:




