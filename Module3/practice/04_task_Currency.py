class Currency:
    def __init__(self, type):
        self.cur=type
        if self.cur=='euro':
            self.cur='eur'

    def value(self, date):
        self.date = date
        import requests
        url = 'https://www.cbr-xml-daily.ru/archive/'+date+'/daily_json.js'
        try:
            return requests.get(url).json()['Valute'][self.cur.upper()]['Value']
        except KeyError:
            return print('ЦБ РФ не установил курс на данную дату')

usd=Currency('usd')
euro=Currency('euro')
usd.value('2020/05/13')
