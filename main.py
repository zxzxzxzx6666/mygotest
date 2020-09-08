def sortdict(input_value):
    key1 = list(input_value.keys())[0]
    key2 = list(input_value[key1].keys())[0]
    key3 = list(input_value[key1][key2].keys())[0]
    key4 = list(input_value[key1][key2][key3].keys())[0]
    value4 = input_value[key1][key2][key3][key4]
    output_value = {
        value4: {
            key4: {
                key3: {
                    key2: key1
                }
            }
        }
    }
    return output_value,value4,key4,key3,key2,key1