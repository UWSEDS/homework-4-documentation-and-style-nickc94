"""This module will make HW3 PEP 8 Complaint"""
def test_create_dataframe(dataframe, column_list):
    '''This function will test the 3 conditions from HW2.
The arguments entered are the dataframe and a list of columns
that are inputed as a list of strings. This function will return
either True or False
'''
    list_of_actual_columns = list(dataframe.columns.values)
    for each_column in column_list:
        if each_column not in list_of_actual_columns:
            return False
    type_row0_column_starttime = type(dataframe.iloc[0]['starttime'])
    for index, row in dataframe.iterrows():
        type_variable = type(row['starttime'])
    if type_row0_column_starttime != type_variable:
        return False
    number_of_rows = dataframe.shape[0]
    if number_of_rows < 10:
        return False
    return True



def check_values_correct_types(dataframe):
    '''This function will test that all the columns have values
    of the correct type'''
    for value in list(dataframe.columns):
        return all(isinstance(dataframe[value][a]) == type(dataframe[value][0]) for
                   a in range(len(dataframe[value])))

def check_nan_values(dataframe):
    ''' This function will test if the dataframe has
    NaN values '''
    if dataframe.isnull().values.any():
        return True
    return False

def check_rows_morethan_one(dataframe):
    ''' This function will test if the dataframe has at
    least one row '''
    return len(dataframe) >= 1
