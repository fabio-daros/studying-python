"""
Unary Logic Structure
    - not, is
Binary Logic Structure
    - and, or
"""
active = True
logged = False

if active or logged:
    print('Welcome user!')
else:
    print('You need activate your account. Please check your email address')

if not active:  # Pythonic mode
    print('You need activate your account. Please check your email address')
else:
    print('Welcome user!')

print(not active)
print(not logged)
