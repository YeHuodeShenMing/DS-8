OK_FORMAT = True
test = {   'name': 'q5_7',
    'points': [0, 2, 3],
    'suites': [   {   'cases': [   {   'code': ">>> # It looks like your table doesn't have all 3 columns that are\n>>> # in the inventory table.\n>>> remaining_inventory.num_columns\n3",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> #It looks like you forgot to subtract off the sales.\n>>> remaining_inventory.column("count").item(0) != 45\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> remaining_inventory.where(1, 'grape')\nbox ID | fruit name | count\n57930  | grape      | 162", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
