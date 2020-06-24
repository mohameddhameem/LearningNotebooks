print()
from math import ceil

# limit
TALK_TIME_LIMIT = 120 
SMS_LIMIT = 50
DATA_LIMIT = 5

# charges
BASE = 50.0
EXTRA_CALL_CHARGE = 0.25 # per min
EXTRA_SMS_CHARGE = 0.15 # per sms
EXTRA_DATA_CHARGE = 10.7 # per GB

TAX_RATE = 0.07  # 7%

# input
call = int(input('Talk time (mins): '))
sms = int(input('SMS             : '))
data = float(input('Data (GB)       : '))

# processing
extra_call, extra_sms, extra_data = 0, 0, 0

if call > TALK_TIME_LIMIT:
    extra_call = call - TALK_TIME_LIMIT
if sms > SMS_LIMIT:
    extra_sms = sms - SMS_LIMIT
if data > DATA_LIMIT:
    extra_data = data - DATA_LIMIT
    extra_data = cei1l(extra_data)

a_call = extra_call*EXTRA_CALL_CHARGE
a_sms = extra_sms*EXTRA_SMS_CHARGE
a_data = extra_data*EXTRA_DATA_CHARGE

subtotal = BASE + a_call + a_sms + a_data
tax = subtotal*TAX_RATE

# output
print()
print('Bill'.center(30))
print('='*30)

print(f"{'Base charge':21s}: ${BASE:6.2f}")
print('Additional charges:')
print(f"   {'Talk time':18s}: ${a_call:6.2f}")
print(f"   {'SMS':18s}: ${a_sms:6.2f}")
print(f"   {'Data':18s}: ${a_data:6.2f}")
print('-'*30)
print(f"{'Sub-total':21s}: ${subtotal:6.2f}")
print(f"{'GST (7%)':21s}: ${tax:6.2f}")
print('-'*30)
print(f"{'TOTAL':21s}: ${subtotal + tax:6.2f}")
print('='*30)


print()