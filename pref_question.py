import random


def pref_location():
    pref_city_dict = {}
    pref_url_dict = {}

    with open('prefectural_office_location.txt', encoding='UTF-8')as f:
        for i in f:
            txt_lines = i.rstrip().split(',')
            pref = txt_lines[0]
            city = txt_lines[1]
            url = txt_lines[2]

            if pref not in pref_city_dict:
                pref_city_dict[pref] = city

            if url not in pref_url_dict:
                pref_url_dict[pref] = url

    pref_name = []
    for i in pref_city_dict.keys():
        pref_name.append(i)

    random_pref = random.choice(pref_name)

    city_name = pref_city_dict[random_pref]
    pref_url = pref_url_dict[random_pref]

    return random_pref, city_name, pref_url

if __name__ == '__main__':
    pref_location()
