"""
Please use Python 3 to answer question
Welcome to answer with unit testing code if you can
 
After you finish coding, please push to your GitHub account and share the link with us.
"""
from main import sortdict
# Please write a function to reverse the following nested input value into output value

# Input:
input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}

# Output:
output_value = {
  'I': {
    'deserve': {
      'to': {
         'be': 'hire3'
      }
    }
  }
}
# test
mainoutput,value4,key4,key3,key2,key1= sortdict(input_value)
chechoutput,outvalue4,outkey4,outkey3,outkey2,outkey1=sortdict(output_value)
if  mainoutput == output_value:
    print('test pass')
else:
    print('test error')
    print(r'''{key1: 
    {key2: 
        {key3: 
            {key4: value4}
        }
    }
}''')
    if key1 == outvalue4:
        print('key1 pass')
    else:
        print('key1 error')
    if key2 == outkey4:
        print('key2 pass')
    else:
        print('key2 error')
    if key3 == outkey3:
        print('key3 pass')
    else:
        print('key3 error')
    if key4 == outkey2:
        print('key4 pass')
    else:
        print('key4 error')
    if value4 == outkey1:
        print('value4 pass')
    else:
        print('value4 error')
