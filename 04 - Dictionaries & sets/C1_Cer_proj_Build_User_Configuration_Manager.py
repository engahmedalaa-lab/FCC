test_settings = {
    'theme': 'dark',
    'fontsize': 12,
    'language': 'en',
}

def add_setting(set_dic,dic_tuple):
    key, value = dic_tuple
    key = key.lower()
    value = value.lower()
   
    if key in set_dic:
        return (f'Setting \'{key}\' already exists! Cannot add a new setting with this name.')
    else:
        set_dic.update({key.lower():value.lower()})
        return (f'Setting \'{key}\' added with value \'{value}\' successfully!')

add_setting({'theme': 'light'}, ('volume', 'high'))

def update_setting(set_dic,dic_tuple):
    key, value = dic_tuple
    key = key.lower()
    value = value.lower()
    if key not in set_dic:
        return (f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.')
    set_dic [key] = value  
    return(f'Setting \'{key}\' updated to \'{value}\' successfully!')
       
def delete_setting(set_dic, key):
    key = key.lower()

    if key not in set_dic:
        return ('Setting not found!')
   
    set_dic.pop(key, set_dic[key])
    return(f'Setting \'{key}\' deleted successfully!')

def view_settings(set_dic):
    if len(set_dic) == 0:
        return ('No settings available.')

    view_str = 'Current User Settings:\n'

    for key, value in set_dic.items():
        cab_key = key.capitalize()
        view_str += f'{cab_key}: {value}\n'
   
    return view_str