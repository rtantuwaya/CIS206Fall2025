import re
# import re, This imports Python's Regular Expression(regex) module

def remove_leading_zeros(ip):
    # This defines a function with one arguments
     new_ip = re.sub(r'\b0+(\d)', r'\1', ip)
#remove leading zeros 
    # \b - Word boundary
    # 0+ - One or more zeros at the start of the segment
    # (\d) - Captures the first non-zero digit
    # r'\1' - Replaces the matched zeros with the captured digit (removing the zeros)
     return new_ip
   


# Test
ip_address = "216.08.094.196"
result = remove_leading_zeros(ip_address)
print(f"Original IP: {ip_address}")
print(f"Without leading zeros: {result}")