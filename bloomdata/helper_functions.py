# import pandas as pd
# import numpy as np
# import random

# # Part 2 functions ===========================

# adjectives = ["blue", "large", "grainy", "substantial", "potent", "thermonuclear"]
# nouns = ["food", "house", "tree", "bicycle", "toupee", "phone"]

# def random_phrase():
#     adj = random.choice(adjectives)
#     # noun = np.random.choice(nouns)
#     # random_index = random.randint(0, len(nouns)-1)
#     # noun = nouns[random_index]
#     noun = random.sample(nouns, 1)[0] # ["house"]

#     return adj + " " + noun

# # print(random_phrase())
# # print(random_phrase())
# # print(random_phrase())

# def random_float(min_val, max_val):
#     return random.uniform(min_val, max_val)

# # print(random_float(2,4))
# # print(random_float(2,4))
# # print(random_float(2,4))

# def random_bowling_score():
#     return random.randint(0, 300)

# # print(random_bowling_score())
# # print(random_bowling_score())
# # print(random_bowling_score())

# def silly_tuple():
#     return (random_phrase(), round(random_float(1,5), 1), random_bowling_score())

# # print(silly_tuple())
# # print(silly_tuple())
# # print(silly_tuple())

# def silly_tuple_list(num_tuples):
#     tuple_list = []
#     for item in range(num_tuples):
#        tuple_list.append(silly_tuple())

#     return tuple_list

# # print(silly_tuple_list(5))


# # Part 3 Functions =======================

# test_df = pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]]))
# null_df = pd.DataFrame(np.array([[1,np.nan,3], [4,5,np.nan], [np.nan,8,np.nan]]))

# def null_count(df):
#     return df.isnull().sum().sum()

# # print(null_count(test_df))
# # print(null_count(null_df))

# def train_test_split(df, frac=0.8):
#     train = df.sample(frac=frac)
#     test = df.drop(train.index).sample(frac=1.0)

#     return train,test

# # print(train_test_split(test_df))

# def randomize(df, seed):
#     randomized_df =  df.sample(frac=1.0, random_state=seed)
#     return randomized_df

# # print(randomize(test_df, 10))

# address_df = pd.DataFrame({'address': ['890 Jennifer Brooks\nNorth Janet, WY 24785',
#                                        '8394 Kim Meadow\nDarrenville, AK 27389',
#                                        '379 Cain Plaza\nJosephburgh, WY 06332',
#                                        '5303 Tina Hill\nAudreychester, VA 97036']})

# def addy_split(addy_series):

#     # blank dataframe
#     df = pd.DataFrame()
#     # lists to add info to
#     city_list = []
#     state_list = []
#     zip_list = []

#     for addy in addy_series:
#         # find the values in the strings
#         second_half = addy.split('\n')[1]
#         city = second_half.split(',')[0]
#         state = second_half.split()[-2]
#         zip = second_half.split()[-1]
#         # add the strings to the lists
#         city_list.append(city)
#         state_list.append(state)
#         zip_list.append(zip)

#     # add the lists as new columns on the df
#     df['city'] = city_list
#     df['state'] = state_list
#     df['zip'] = zip_list

#     return df

# # print(addy_split(address_df['address']))

# def abbr_2_st(state_series, abbr_2_st=True):
#     state_dict = {
#         "AK": "Alaska",
#         "AL": "Alabama",
#         "AR": "Arkansas",
#         "AZ": "Arizona",
#         "CA": "California",
#         "CO": "Colorado",
#         "CT": "Connecticut",
#         "DE": "Delaware",
#         "FL": "Florida",
#         "GA": "Georgia",
#         "HI": "Hawaii",
#         "IA": "Iowa",
#         "ID": "Idaho",
#         "IL": "Illinois",
#         "IN": "Indiana",
#         "KS": "Kansas",
#         "KY": "Kentucky",
#         "LA": "Louisiana",
#         "MA": "Massachusetts",
#         "MD": "Maryland",
#         "ME": "Maine",
#         "MI": "Michigan",
#         "MN": "Minnesota",
#         "MO": "Missouri",
#         "MS": "Mississippi",
#         "MT": "Montana",
#         "NC": "North Carolina",
#         "ND": "North Dakota",
#         "NE": "Nebraska",
#         "NH": "New Hampshire",
#         "NJ": "New Jersey",
#         "NM": "New Mexico",
#         "NV": "Nevada",
#         "NY": "New York",
#         "OH": "Ohio",
#         "OK": "Oklahoma",
#         "OR": "Oregon",
#         "PA": "Pennsylvania",
#         "RI": "Rhode Island",
#         "SC": "South Carolina",
#         "SD": "South Dakota",
#         "TN": "Tennessee",
#         "TX": "Texas",
#         "UT": "Utah",
#         "VA": "Virginia",
#         "VT": "Vermont",
#         "WA": "Washington",
#         "WI": "Wisconsin",
#         "WV": "West Virginia",
#         "WY": "Wyoming"
#     }

#     def abbrev_replace(abbrev):
#         return state_dict[abbrev]
    
#     def state_replace(state_name):
#         reverse_state_dict = dict((v, k) for k, v in state_dict.items())
#         return reverse_state_dict[state_name]
    
#     if abbr_2_st:
#         return state_series.apply(abbrev_replace)
#     else:
#         return state_series.apply(state_replace)

# addy_states = addy_split(address_df['address'])['state']

# full_state_names_column = abbr_2_st(addy_states)

# # print(abbr_2_st(full_state_names_column, abbr_2_st=False))

# def list_2_series(list_2_series, df):
#     new_column = pd.Series(list_2_series)
#     return pd.concat([df, new_column], axis=1)

# # print(list_2_series([10, 11, 12], test_df))

# outlier_df = pd.DataFrame(
#     {'a': [1,2,3,4,5,6],
#      'b': [4,5,6,7,8,9],
#      'c': [7, 1000, 9, 10, 11, 12]}
# )

# def rm_outlier(df):
#     # I had to put this because df.iteritems wasn't working
#     df.iteritems = df.items

#     cleaned_df = pd.DataFrame()

#     for (columnName, columnData) in df.iteritems():
#         Q1 = columnData.quantile(0.25)
#         Q3 = columnData.quantile(0.75)
#         IQR = Q3 - Q1
#         lower_bound = Q1 - 1.5 * IQR
#         upper_bound = Q3 + 1.5 * IQR
#         # print(lower_bound, upper_bound)

#         mask = columnData.between(lower_bound, upper_bound, inclusive='both')
#         cleaned = columnData.loc[mask]

#         cleaned_df[columnName] = cleaned

#     return cleaned_df

# # print(rm_outlier(outlier_df))

# def split_dates(date_series):
#     # MM/DD/YYYY
#     df = pd.DataFrame()

#     month_list = []
#     day_list = []
#     year_list = []

#     for date in date_series:
#         month_list.append(date.split('/')[0])
#         day_list.append(date.split('/')[1])
#         year_list.append(date.split('/')[2])

#     df['month'] = month_list
#     df['day'] = day_list
#     df['year'] = year_list

#     return df


# print(split_dates(pd.Series(['01/13/2016','02/14/2017','03/15/2018','04/16/2019'])))


'''
THIS IS PART OF THE FINAL MODULE ON SPRINT 1
'''

import random

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']


def random_phrase(list1, list2):
    adjective = random.choice(list1)
    noun = random.choice(list2)

    return str(adjective) + ' ' + str(noun)

if __name__ == '__main__':
    pass
    # print(random_phrase(adjectives, nouns))