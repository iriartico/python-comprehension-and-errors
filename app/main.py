import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv('./app/data.csv')

    # POPULATION BY COUNTRY
    # country = input('Type Country => ')

    # result = utils.population_by_country(data, country)
    # print(result)

    # if len(result) > 0:
    #     country = result[0]
    #     labels, values = utils.get_population(country)
    #     charts.generate_bar_chart(labels, values)


    # WORLD POPULATION
    data = list(filter(lambda item: item['Continent'] == 'South America', data))
    countries = list(map(lambda item: item['Country/Territory'], data))
    percentages = list(map(lambda item: item['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)


if __name__ == '__main__':
    run()
