DEFAULT_COLORS = {
    'Blocks': {'0': (151, 107, 75, 255), '1': (128, 128, 128, 255), '2': (28, 216, 94, 255), '3': (27, 197, 109, 255),
               '4': (253, 221, 3, 255), '5': (151, 107, 75, 255), '6': (140, 101, 80, 255), '7': (150, 67, 22, 255),
               '8': (185, 164, 23, 255), '9': (185, 194, 195, 255), '10': (119, 105, 79, 255),
               '11': (119, 105, 79, 255), '12': (174, 24, 69, 255), '13': (133, 213, 247, 255),
               '14': (191, 142, 111, 255), '15': (191, 142, 111, 255), '16': (140, 130, 116, 255),
               '17': (144, 148, 144, 255), '18': (191, 142, 111, 255), '19': (191, 142, 111, 255),
               '20': (163, 116, 81, 255), '21': (233, 207, 94, 255), '22': (98, 95, 167, 255),
               '23': (141, 137, 223, 255), '24': (122, 116, 218, 255), '25': (109, 90, 128, 255),
               '26': (119, 101, 125, 255), '27': (226, 196, 49, 255), '28': (151, 79, 80, 255),
               '29': (175, 105, 128, 255), '30': (170, 120, 84, 255), '31': (141, 120, 168, 255),
               '32': (151, 135, 183, 255), '33': (253, 221, 3, 255), '34': (235, 166, 135, 255),
               '35': (197, 216, 219, 255), '36': (230, 89, 92, 255), '37': (104, 86, 84, 255),
               '38': (144, 144, 144, 255), '39': (181, 62, 59, 255), '40': (146, 81, 68, 255), '41': (66, 84, 109, 255),
               '42': (251, 235, 127, 255), '43': (84, 100, 63, 255), '44': (107, 68, 99, 255),
               '45': (185, 164, 23, 255), '46': (185, 194, 195, 255), '47': (150, 67, 22, 255),
               '48': (128, 128, 128, 255), '49': (43, 143, 255, 255), '50': (170, 48, 114, 255),
               '51': (192, 202, 203, 255), '52': (23, 177, 76, 255), '53': (255, 218, 56, 255),
               '54': (200, 246, 254, 255), '55': (191, 142, 111, 255), '56': (43, 40, 84, 255), '57': (68, 68, 76, 255),
               '58': (142, 66, 66, 255), '59': (92, 68, 73, 255), '60': (143, 215, 29, 255), '61': (135, 196, 26, 255),
               '62': (121, 176, 24, 255), '63': (110, 140, 182, 255), '64': (196, 96, 114, 255),
               '65': (56, 150, 97, 255), '66': (160, 118, 58, 255), '67': (140, 58, 166, 255),
               '68': (125, 191, 197, 255), '69': (190, 150, 92, 255), '70': (93, 127, 255, 255),
               '71': (182, 175, 130, 255), '72': (182, 175, 130, 255), '73': (27, 197, 109, 255),
               '74': (96, 197, 27, 255), '75': (36, 36, 36, 255), '76': (142, 66, 66, 255), '77': (238, 85, 70, 255),
               '78': (121, 110, 97, 255), '79': (191, 142, 111, 255), '80': (73, 120, 17, 255),
               '81': (245, 133, 191, 255), '82': (255, 120, 0, 255), '83': (255, 120, 0, 255), '84': (255, 120, 0, 255),
               '85': (192, 192, 192, 255), '86': (191, 142, 111, 255), '87': (191, 142, 111, 255),
               '88': (191, 142, 111, 255), '89': (191, 142, 111, 255), '90': (144, 148, 144, 255),
               '91': (13, 88, 130, 255), '92': (213, 229, 237, 255), '93': (253, 221, 3, 255),
               '94': (191, 142, 111, 255), '95': (255, 162, 31, 255), '96': (144, 148, 144, 255),
               '97': (144, 148, 144, 255), '98': (253, 221, 3, 255), '99': (144, 148, 144, 255),
               '100': (253, 221, 3, 255), '101': (191, 142, 111, 255), '102': (229, 212, 73, 255),
               '103': (141, 98, 77, 255), '104': (191, 142, 111, 255), '105': (144, 148, 144, 255),
               '106': (191, 142, 111, 255), '107': (11, 80, 143, 255), '108': (91, 169, 169, 255),
               '109': (78, 193, 227, 255), '110': (48, 186, 135, 255), '111': (128, 26, 52, 255),
               '112': (103, 98, 122, 255), '113': (48, 208, 234, 255), '114': (191, 142, 111, 255),
               '115': (33, 171, 207, 255), '116': (238, 225, 218, 255), '117': (181, 172, 190, 255),
               '118': (238, 225, 218, 255), '119': (107, 92, 108, 255), '120': (92, 68, 73, 255),
               '121': (11, 80, 143, 255), '122': (91, 169, 169, 255), '123': (106, 107, 118, 255),
               '124': (73, 51, 36, 255), '125': (141, 175, 255, 255), '126': (159, 209, 229, 255),
               '127': (128, 204, 230, 255), '128': (191, 142, 111, 255), '129': (255, 117, 224, 255),
               '130': (160, 160, 160, 255), '131': (52, 52, 52, 255), '132': (144, 148, 144, 255),
               '133': (231, 53, 56, 255), '134': (166, 187, 153, 255), '135': (253, 114, 114, 255),
               '136': (213, 203, 204, 255), '137': (144, 148, 144, 255), '138': (96, 96, 96, 255),
               '139': (191, 142, 111, 255), '140': (98, 95, 167, 255), '141': (192, 59, 59, 255),
               '142': (144, 148, 144, 255), '143': (144, 148, 144, 255), '144': (144, 148, 144, 255),
               '145': (192, 30, 30, 255), '146': (43, 192, 30, 255), '147': (211, 236, 241, 255),
               '148': (181, 211, 210, 255), '149': (220, 50, 50, 255), '150': (128, 26, 52, 255),
               '151': (190, 171, 94, 255), '152': (128, 133, 184, 255), '153': (239, 141, 126, 255),
               '154': (190, 171, 94, 255), '155': (131, 162, 161, 255), '156': (170, 171, 157, 255),
               '157': (104, 100, 126, 255), '158': (145, 81, 85, 255), '159': (148, 133, 98, 255),
               '160': (0, 0, 200, 255), '161': (144, 195, 232, 255), '162': (184, 219, 240, 255),
               '163': (174, 145, 214, 255), '164': (218, 182, 204, 255), '165': (100, 100, 100, 255),
               '166': (129, 125, 93, 255), '167': (62, 82, 114, 255), '168': (132, 157, 127, 255),
               '169': (152, 171, 198, 255), '170': (228, 219, 162, 255), '171': (33, 135, 85, 255),
               '172': (181, 194, 217, 255), '173': (253, 221, 3, 255), '174': (253, 221, 3, 255),
               '175': (129, 125, 93, 255), '176': (132, 157, 127, 255), '177': (152, 171, 198, 255),
               '178': (255, 0, 255, 255), '179': (49, 134, 114, 255), '180': (126, 134, 49, 255),
               '181': (134, 59, 49, 255), '182': (43, 86, 140, 255), '183': (121, 49, 134, 255),
               '184': (100, 100, 100, 255), '185': (149, 149, 115, 255), '186': (255, 0, 255, 255),
               '187': (255, 0, 255, 255), '188': (73, 120, 17, 255), '189': (223, 255, 255, 255),
               '190': (182, 175, 130, 255), '191': (151, 107, 75, 255), '192': (26, 196, 84, 255),
               '193': (56, 121, 255, 255), '194': (157, 157, 107, 255), '195': (134, 22, 34, 255),
               '196': (147, 144, 178, 255), '197': (97, 200, 225, 255), '198': (62, 61, 52, 255),
               '199': (208, 80, 80, 255), '200': (216, 152, 144, 255), '201': (203, 61, 64, 255),
               '202': (213, 178, 28, 255), '203': (128, 44, 45, 255), '204': (125, 55, 65, 255),
               '205': (186, 50, 52, 255), '206': (124, 175, 201, 255), '207': (144, 148, 144, 255),
               '208': (88, 105, 118, 255), '209': (144, 148, 144, 255), '210': (192, 59, 59, 255),
               '211': (191, 233, 115, 255), '212': (144, 148, 144, 255), '213': (137, 120, 67, 255),
               '214': (103, 103, 103, 255), '215': (254, 121, 2, 255), '216': (191, 142, 111, 255),
               '217': (144, 148, 144, 255), '218': (144, 148, 144, 255), '219': (144, 148, 144, 255),
               '220': (144, 148, 144, 255), '221': (239, 90, 50, 255), '222': (231, 96, 228, 255),
               '223': (57, 85, 101, 255), '224': (107, 132, 139, 255), '225': (227, 125, 22, 255),
               '226': (141, 56, 0, 255), '227': (255, 255, 255, 255), '228': (144, 148, 144, 255),
               '229': (255, 156, 12, 255), '230': (131, 79, 13, 255), '231': (224, 194, 101, 255),
               '232': (145, 81, 85, 255), '233': (255, 0, 255, 255), '234': (53, 44, 41, 255),
               '235': (214, 184, 46, 255), '236': (149, 232, 87, 255), '237': (255, 241, 51, 255),
               '238': (225, 128, 206, 255), '239': (224, 194, 101, 255), '240': (99, 50, 30, 255),
               '241': (77, 74, 72, 255), '242': (99, 50, 30, 255), '243': (140, 179, 254, 255),
               '244': (200, 245, 253, 255), '245': (99, 50, 30, 255), '246': (99, 50, 30, 255),
               '247': (140, 150, 150, 255), '248': (219, 71, 38, 255), '249': (249, 52, 243, 255),
               '250': (76, 74, 83, 255), '251': (235, 150, 23, 255), '252': (153, 131, 44, 255),
               '253': (57, 48, 97, 255), '254': (248, 158, 92, 255), '255': (107, 49, 154, 255),
               '256': (154, 148, 49, 255), '257': (49, 49, 154, 255), '258': (49, 154, 68, 255),
               '259': (154, 49, 77, 255), '260': (85, 89, 118, 255), '261': (154, 83, 49, 255),
               '262': (221, 79, 255, 255), '263': (250, 255, 79, 255), '264': (79, 102, 255, 255),
               '265': (79, 255, 89, 255), '266': (255, 79, 79, 255), '267': (240, 240, 247, 255),
               '268': (255, 145, 79, 255), '269': (191, 142, 111, 255), '270': (122, 217, 232, 255),
               '271': (122, 217, 232, 255), '272': (121, 119, 101, 255), '273': (128, 128, 128, 255),
               '274': (190, 171, 94, 255), '275': (122, 217, 232, 255), '276': (122, 217, 232, 255),
               '277': (122, 217, 232, 255), '278': (122, 217, 232, 255), '279': (122, 217, 232, 255),
               '280': (122, 217, 232, 255), '281': (122, 217, 232, 255), '282': (122, 217, 232, 255),
               '283': (128, 128, 128, 255), '284': (150, 67, 22, 255), '285': (122, 217, 232, 255),
               '286': (122, 217, 232, 255), '287': (79, 128, 17, 255), '288': (122, 217, 232, 255),
               '289': (122, 217, 232, 255), '290': (122, 217, 232, 255), '291': (122, 217, 232, 255),
               '292': (122, 217, 232, 255), '293': (122, 217, 232, 255), '294': (122, 217, 232, 255),
               '295': (122, 217, 232, 255), '296': (122, 217, 232, 255), '297': (122, 217, 232, 255),
               '298': (122, 217, 232, 255), '299': (122, 217, 232, 255), '300': (144, 148, 144, 255),
               '301': (144, 148, 144, 255), '302': (144, 148, 144, 255), '303': (144, 148, 144, 255),
               '304': (144, 148, 144, 255), '305': (144, 148, 144, 255), '306': (144, 148, 144, 255),
               '307': (144, 148, 144, 255), '308': (144, 148, 144, 255), '309': (122, 217, 232, 255),
               '310': (122, 217, 232, 255), '311': (117, 61, 25, 255), '312': (204, 93, 73, 255),
               '313': (87, 150, 154, 255), '314': (181, 164, 125, 255), '315': (235, 114, 80, 255),
               '316': (122, 217, 232, 255), '317': (122, 217, 232, 255), '318': (122, 217, 232, 255),
               '319': (96, 68, 48, 255), '320': (203, 185, 151, 255), '321': (96, 77, 64, 255),
               '322': (198, 170, 104, 255), '323': (182, 141, 86, 255), '324': (228, 213, 173, 255),
               '325': (129, 125, 93, 255), '326': (9, 61, 191, 255), '327': (253, 32, 3, 255),
               '328': (200, 246, 254, 255), '329': (15, 15, 15, 255), '330': (226, 118, 76, 255),
               '331': (161, 172, 173, 255), '332': (204, 181, 72, 255), '333': (190, 190, 178, 255),
               '334': (191, 142, 111, 255), '335': (217, 174, 137, 255), '336': (253, 62, 3, 255),
               '337': (144, 148, 144, 255), '338': (85, 255, 160, 255), '339': (122, 217, 232, 255),
               '340': (96, 248, 2, 255), '341': (105, 74, 202, 255), '342': (29, 240, 255, 255),
               '343': (254, 202, 80, 255), '344': (131, 252, 245, 255), '345': (255, 156, 12, 255),
               '346': (149, 212, 89, 255), '347': (236, 74, 79, 255), '348': (44, 26, 233, 255),
               '349': (144, 148, 144, 255), '350': (55, 97, 155, 255), '351': (31, 31, 31, 255),
               '352': (238, 97, 94, 255), '353': (28, 216, 94, 255), '354': (141, 107, 89, 255),
               '355': (141, 107, 89, 255), '356': (233, 203, 24, 255), '357': (168, 178, 204, 255),
               '358': (122, 217, 232, 255), '359': (122, 217, 232, 255), '360': (122, 217, 232, 255),
               '361': (122, 217, 232, 255), '362': (122, 217, 232, 255), '363': (122, 217, 232, 255),
               '364': (122, 217, 232, 255), '365': (146, 136, 205, 255), '366': (223, 232, 233, 255),
               '367': (168, 178, 204, 255), '368': (50, 46, 104, 255), '369': (50, 46, 104, 255),
               '370': (127, 116, 194, 255), '371': (249, 101, 189, 255), '372': (252, 128, 201, 255),
               '373': (9, 61, 191, 255), '374': (253, 32, 3, 255), '375': (255, 156, 12, 255),
               '376': (160, 120, 92, 255), '377': (191, 142, 111, 255), '378': (160, 120, 100, 255),
               '379': (251, 209, 240, 255), '380': (191, 142, 111, 255), '381': (254, 121, 2, 255),
               '382': (28, 216, 94, 255), '383': (221, 136, 144, 255), '384': (131, 206, 12, 255),
               '385': (87, 21, 144, 255), '386': (127, 92, 69, 255), '387': (127, 92, 69, 255),
               '388': (127, 92, 69, 255), '389': (127, 92, 69, 255), '390': (253, 32, 3, 255),
               '391': (122, 217, 232, 255), '392': (122, 217, 232, 255), '393': (122, 217, 232, 255),
               '394': (122, 217, 232, 255), '395': (191, 142, 111, 255), '396': (198, 124, 78, 255),
               '397': (212, 192, 100, 255), '398': (100, 82, 126, 255), '399': (77, 76, 66, 255),
               '400': (96, 68, 117, 255), '401': (68, 60, 51, 255), '402': (174, 168, 186, 255),
               '403': (205, 152, 186, 255), '404': (140, 84, 60, 255), '405': (140, 140, 140, 255),
               '406': (120, 120, 120, 255), '407': (255, 227, 132, 255), '408': (85, 83, 82, 255),
               '409': (85, 83, 82, 255), '410': (75, 139, 166, 255), '411': (227, 46, 46, 255),
               '412': (75, 139, 166, 255), '413': (122, 217, 232, 255), '414': (122, 217, 232, 255),
               '415': (249, 75, 7, 255), '416': (0, 160, 170, 255), '417': (160, 87, 234, 255),
               '418': (22, 173, 254, 255), '419': (117, 125, 151, 255), '420': (255, 255, 255, 255),
               '421': (73, 70, 70, 255), '422': (73, 70, 70, 255), '423': (255, 255, 255, 255),
               '424': (146, 155, 187, 255), '425': (174, 195, 215, 255), '426': (77, 11, 35, 255),
               '427': (119, 22, 52, 255), '428': (255, 255, 255, 255), '429': (63, 63, 63, 255),
               '430': (23, 119, 79, 255), '431': (23, 54, 119, 255), '432': (119, 68, 23, 255),
               '433': (74, 23, 119, 255), '434': (78, 82, 109, 255), '435': (39, 168, 96, 255),
               '436': (39, 94, 168, 255), '437': (168, 121, 39, 255), '438': (111, 39, 168, 255),
               '439': (150, 148, 174, 255), '440': (255, 255, 255, 255), '441': (255, 255, 255, 255),
               '442': (3, 144, 201, 255), '443': (123, 123, 123, 255), '444': (191, 176, 124, 255),
               '445': (55, 55, 73, 255), '446': (255, 66, 152, 255), '447': (179, 132, 255, 255),
               '448': (0, 206, 180, 255), '449': (91, 186, 240, 255), '450': (92, 240, 91, 255),
               '451': (240, 91, 147, 255), '452': (255, 150, 181, 255), '453': (255, 255, 255, 255),
               '454': (174, 16, 176, 255), '455': (48, 255, 110, 255), '456': (179, 132, 255, 255),
               '457': (255, 255, 255, 255), '458': (211, 198, 111, 255), '459': (190, 223, 232, 255),
               '460': (141, 163, 181, 255), '461': (255, 222, 100, 255), '462': (231, 178, 28, 255),
               '463': (155, 214, 240, 255), '464': (233, 183, 128, 255), '465': (51, 84, 195, 255),
               '466': (205, 153, 73, 255), '467': (233, 207, 94, 255), '468': (255, 255, 255, 255),
               '469': (191, 142, 111, 255)},
    'Walls': {'0': (0, 0, 0, 0), '1': (52, 52, 52, 255), '2': (88, 61, 46, 255), '3': (61, 58, 78, 255),
              '4': (73, 51, 36, 255), '5': (52, 52, 52, 255), '6': (91, 30, 30, 255), '7': (27, 31, 42, 255),
              '8': (31, 39, 26, 255), '9': (41, 28, 36, 255), '10': (74, 62, 12, 255), '11': (46, 56, 59, 255),
              '12': (75, 32, 11, 255), '13': (67, 37, 37, 255), '14': (15, 15, 15, 255), '15': (52, 43, 45, 255),
              '16': (88, 61, 46, 255), '17': (27, 31, 42, 255), '18': (31, 39, 26, 255), '19': (41, 28, 36, 255),
              '20': (15, 15, 15, 255), '21': (0, 0, 0, 0), '22': (113, 99, 99, 255), '23': (38, 38, 43, 255),
              '24': (53, 39, 41, 255), '25': (11, 35, 62, 255), '26': (21, 63, 70, 255), '27': (88, 61, 46, 255),
              '28': (81, 84, 101, 255), '29': (88, 23, 23, 255), '30': (28, 88, 23, 255), '31': (78, 87, 99, 255),
              '32': (86, 17, 40, 255), '33': (49, 47, 83, 255), '34': (69, 67, 41, 255), '35': (51, 51, 70, 255),
              '36': (87, 59, 55, 255), '37': (69, 67, 41, 255), '38': (49, 57, 49, 255), '39': (78, 79, 73, 255),
              '40': (85, 102, 103, 255), '41': (52, 50, 62, 255), '42': (71, 42, 44, 255), '43': (73, 66, 50, 255),
              '44': (52, 52, 52, 255), '45': (60, 59, 51, 255), '46': (48, 57, 47, 255), '47': (71, 77, 85, 255),
              '48': (52, 52, 52, 255), '49': (52, 52, 52, 255), '50': (52, 52, 52, 255), '51': (52, 52, 52, 255),
              '52': (52, 52, 52, 255), '53': (52, 52, 52, 255), '54': (40, 56, 50, 255), '55': (49, 48, 36, 255),
              '56': (43, 33, 32, 255), '57': (31, 40, 49, 255), '58': (48, 35, 52, 255), '59': (88, 61, 46, 255),
              '60': (1, 52, 20, 255), '61': (55, 39, 26, 255), '62': (39, 33, 26, 255), '63': (30, 80, 48, 255),
              '64': (53, 80, 30, 255), '65': (30, 80, 48, 255), '66': (30, 80, 48, 255), '67': (53, 80, 30, 255),
              '68': (30, 80, 48, 255), '69': (43, 42, 68, 255), '70': (30, 70, 80, 255), '71': (78, 105, 135, 255),
              '72': (52, 84, 12, 255), '73': (190, 204, 223, 255), '74': (64, 62, 80, 255), '75': (65, 65, 35, 255),
              '76': (20, 46, 104, 255), '77': (61, 13, 16, 255), '78': (63, 39, 26, 255), '79': (51, 47, 96, 255),
              '80': (64, 62, 80, 255), '81': (101, 51, 51, 255), '82': (77, 64, 34, 255), '83': (62, 38, 41, 255),
              '84': (48, 78, 93, 255), '85': (54, 63, 69, 255), '86': (138, 73, 38, 255), '87': (50, 15, 8, 255),
              '88': (0, 0, 0, 0), '89': (0, 0, 0, 0), '90': (0, 0, 0, 0), '91': (0, 0, 0, 0), '92': (0, 0, 0, 0),
              '93': (0, 0, 0, 0), '94': (32, 40, 45, 255), '95': (44, 41, 50, 255), '96': (72, 50, 77, 255),
              '97': (78, 50, 69, 255), '98': (36, 45, 44, 255), '99': (38, 49, 50, 255), '100': (32, 40, 45, 255),
              '101': (44, 41, 50, 255), '102': (72, 50, 77, 255), '103': (78, 50, 69, 255), '104': (36, 45, 44, 255),
              '105': (38, 49, 50, 255), '106': (0, 0, 0, 0), '107': (0, 0, 0, 0), '108': (138, 73, 38, 255),
              '109': (94, 25, 17, 255), '110': (125, 36, 122, 255), '111': (51, 35, 27, 255), '112': (50, 15, 8, 255),
              '113': (135, 58, 0, 255), '114': (65, 52, 15, 255), '115': (39, 42, 51, 255), '116': (89, 26, 27, 255),
              '117': (126, 123, 115, 255), '118': (8, 50, 19, 255), '119': (95, 21, 24, 255), '120': (17, 31, 65, 255),
              '121': (192, 173, 143, 255), '122': (114, 114, 131, 255), '123': (136, 119, 7, 255),
              '124': (8, 72, 3, 255), '125': (117, 132, 82, 255), '126': (100, 102, 114, 255),
              '127': (30, 118, 226, 255), '128': (93, 6, 102, 255), '129': (64, 40, 169, 255),
              '130': (39, 34, 180, 255), '131': (87, 94, 125, 255), '132': (6, 6, 6, 255), '133': (69, 72, 186, 255),
              '134': (130, 62, 16, 255), '135': (22, 123, 163, 255), '136': (40, 86, 151, 255),
              '137': (183, 75, 15, 255), '138': (83, 80, 100, 255), '139': (115, 65, 68, 255),
              '140': (119, 108, 81, 255), '141': (59, 67, 71, 255), '142': (17, 172, 143, 255),
              '143': (90, 112, 105, 255), '144': (62, 28, 87, 255), '145': (0, 0, 0, 0), '146': (120, 59, 19, 255),
              '147': (59, 59, 59, 255), '148': (229, 218, 161, 255), '149': (73, 59, 50, 255), '150': (0, 0, 0, 0),
              '151': (102, 75, 34, 255), '152': (0, 0, 0, 0), '153': (255, 145, 79, 255), '154': (221, 79, 255, 255),
              '155': (240, 240, 247, 255), '156': (79, 255, 89, 255), '157': (154, 83, 49, 255),
              '158': (107, 49, 154, 255), '159': (85, 89, 118, 255), '160': (49, 154, 68, 255),
              '161': (154, 49, 77, 255), '162': (49, 49, 154, 255), '163': (154, 148, 49, 255),
              '164': (255, 79, 79, 255), '165': (79, 102, 255, 255), '166': (250, 255, 79, 255),
              '167': (70, 68, 51, 255), '168': (0, 0, 0, 0), '169': (5, 5, 5, 255), '170': (59, 39, 22, 255),
              '171': (59, 39, 22, 255), '172': (163, 96, 0, 255), '173': (94, 163, 46, 255), '174': (117, 32, 59, 255),
              '175': (20, 11, 203, 255), '176': (74, 69, 88, 255), '177': (60, 30, 30, 255),
              '178': (111, 117, 135, 255), '179': (111, 117, 135, 255), '180': (25, 23, 54, 255),
              '181': (25, 23, 54, 255), '182': (74, 71, 129, 255), '183': (111, 117, 135, 255),
              '184': (25, 23, 54, 255), '185': (52, 52, 52, 255), '186': (38, 9, 66, 255), '187': (149, 80, 51, 255),
              '188': (82, 63, 80, 255), '189': (65, 61, 77, 255), '190': (64, 65, 92, 255), '191': (76, 53, 84, 255),
              '192': (144, 67, 52, 255), '193': (149, 48, 48, 255), '194': (111, 32, 36, 255),
              '195': (147, 48, 55, 255), '196': (97, 67, 51, 255), '197': (112, 80, 62, 255), '198': (88, 61, 46, 255),
              '199': (127, 94, 76, 255), '200': (143, 50, 123, 255), '201': (136, 120, 131, 255),
              '202': (219, 92, 143, 255), '203': (113, 64, 150, 255), '204': (74, 67, 60, 255),
              '205': (60, 78, 59, 255), '206': (0, 54, 21, 255), '207': (74, 97, 72, 255), '208': (40, 37, 35, 255),
              '209': (77, 63, 66, 255), '210': (111, 6, 6, 255), '211': (88, 67, 59, 255), '212': (88, 87, 80, 255),
              '213': (71, 71, 67, 255), '214': (76, 52, 60, 255), '215': (89, 48, 59, 255), '216': (158, 100, 64, 255),
              '217': (62, 45, 75, 255), '218': (57, 14, 12, 255), '219': (96, 72, 133, 255), '220': (67, 55, 80, 255),
              '221': (64, 37, 29, 255), '222': (70, 51, 91, 255), '223': (51, 18, 4, 255), '224': (57, 55, 52, 255),
              '225': (68, 68, 68, 255), '226': (148, 138, 74, 255), '227': (95, 137, 191, 255),
              '228': (160, 2, 75, 255), '229': (100, 55, 164, 255), '230': (0, 117, 101, 255)},
    'Globals': {'Space': (51, 102, 153, 255), 'Sky': (155, 209, 255, 255), 'Earth': (84, 57, 42, 255),
                'Rock': (72, 64, 57, 255), 'Hell': (51, 0, 0, 255), 'Lava': (255, 30, 0, 240),
                'Honey': (255, 172, 0, 240), 'Water': (0, 12, 255, 128), 'Wire': (255, 0, 0, 112),
                'Wire1': (0, 0, 255, 112), 'Wire2': (0, 255, 0, 112), 'Wire3': (255, 255, 0, 112)},
    'Paints': {'0': (0, 0, 0, 0), '1': (255, 0, 0, 255), '2': (255, 127, 0, 255), '3': (255, 255, 0, 255),
               '4': (127, 255, 0, 255), '5': (0, 255, 0, 255), '6': (0, 255, 127, 255), '7': (0, 255, 255, 255),
               '8': (0, 127, 255, 255), '9': (0, 0, 255, 255), '10': (127, 0, 255, 255), '11': (255, 0, 255, 255),
               '12': (255, 0, 127, 255), '13': (255, 0, 0, 255), '14': (255, 127, 0, 255), '15': (255, 255, 0, 255),
               '16': (127, 255, 0, 255), '17': (0, 255, 0, 255), '18': (0, 255, 127, 255), '19': (0, 255, 255, 255),
               '20': (0, 127, 255, 255), '21': (0, 0, 255, 255), '22': (127, 0, 255, 255), '23': (255, 0, 255, 255),
               '24': (255, 0, 127, 255), '25': (75, 75, 75, 255), '26': (255, 255, 255, 255),
               '27': (175, 175, 175, 255), '28': (255, 178, 125, 255), '29': (25, 25, 25, 255),
               '30': (200, 200, 200, 150)}}
