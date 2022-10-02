# Python3 implementation to find the
# defanged version of the IP address

# Function to generate a
# defanged version of IP address.
def defanged_address(address):
    address=address.replace('.','[.]')
    return address
# Driver Code
address=input("enter address")
print(defanged_address(address))
# This code is contributed by Rayan AL_Mrayat

