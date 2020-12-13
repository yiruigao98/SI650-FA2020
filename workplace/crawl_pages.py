import csv
import wikipedia

city_file = './data/cities_split3.csv'


with open(city_file, 'r', encoding = 'utf-8') as f:
    lines = f.readlines()

# city_country_list = []
for line in lines:
# modified_list = ['Hong Kong,Hong Kong']

# for line in modified_list:
    line = line.split(',')
    city, country = line[0], line[1]

    search = wikipedia.search('city ' + city + " " + country)
    # search = wikipedia.search(city)
    try:
        page_content = wikipedia.page(search[0]).content

        print(city)
        # print(page_content)

        w_file_name = './data/docs/{}/{}_{}_doc.csv'.format(city[0].lower(), city, country)
        with open(w_file_name, 'w+', encoding='utf-8') as wf:
            wf.write(page_content)
        
        # city_country_list.append((city, country))
    except:
        continue


# with open('./data/fianl_cities.csv', 'wb', newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(city_country_list)

