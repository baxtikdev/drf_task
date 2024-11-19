import calendar
from datetime import datetime, timedelta
from decimal import Decimal

from docopt import printable_usage
from num2words import num2words


def text_format(workbook, color: str = None, bold: bool = None, border: int = None,
                font_size: int = 14, align: str = 'center'):
    custom_format = {
        "font_name": "Times New Roman",
        "font_size": font_size,
        'align': align,
        'valign': 'vcenter',
        "text_wrap": True
    }
    if color is not None:
        custom_format['fg_color'] = color
    if bold is not None:
        custom_format['bold'] = bold
    if border is not None:
        custom_format['border'] = border

    custom_format['num_format'] = '#,##0'
    return workbook.add_format(custom_format)


def format_amount(amount):
    if isinstance(amount, str):
        return amount

    if amount:
        amount_decimal = amount
        if type(amount) != Decimal:
            amount_decimal = Decimal(amount)
        formatted_with_commas = "{:,.2f}".format(amount_decimal)
        return formatted_with_commas.replace(',', ' ')
    return "0"


def number_to_words(number):
    words = num2words(number, lang='ru', to='currency', currency='UZS')
    capitalized_text = words.capitalize()
    return capitalized_text


def generate_dates(startDate, endDate):
    if isinstance(startDate, str):
        startDate = datetime.strptime(startDate, '%Y-%m-%d')
    if isinstance(endDate, str):
        endDate = datetime.strptime(endDate, '%Y-%m-%d')

    data = []
    date = startDate
    while date <= endDate:
        data.append({
            'date': date.strftime('%d.%m.%Y'),
            'date2': date,
            'atotal': 0,
            'patient': 0,
            'insurance': 0,
            'inpatient': 0,
            'analysisAmount': 0
        })
        date += timedelta(days=1)

    return data


def format_date(date_str):
    formats = ['%Y-%m-%dT%H:%M:%S.%f%z', '%Y-%m-%dT%H:%M:%S%z']
    for date_format in formats:
        try:
            parsed_date = datetime.strptime(date_str, date_format)
            return parsed_date.strftime('%H:%M %d.%m.%Y')
        except ValueError:
            continue
    return ''


def generate_month_dates(year, month):
    num_days = calendar.monthrange(year, month)[1]
    month_dates = [day for day in range(1, num_days + 1)]
    return month_dates


MONTHS = {
    1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',
    7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'
}
