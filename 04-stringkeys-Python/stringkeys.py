"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        r=self.calculate_hash_value(string)
        self.table[r]=(string)
        return r  

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        r=self.calculate_hash_value(string)
        if(string==self.table[r]):
            return r
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        a=string[0]
        b=string[1]
        hash_value=(ord(a)*100)+(ord(b))
        print(hash_value)
        return hash_value
        # pass


