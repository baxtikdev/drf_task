from datetime import datetime


def validate_serializer_fields(serializer, data, validation_messages):
    if not serializer.is_valid():
        error_messages = serializer.errors
        error_message = "Валидация не удалась для следующих полей {}: {}".format(
            ", ".join(error_messages.keys()), data)
        validation_messages.append(error_message)
        return validation_messages


def format_datetime(date_str):
    formats = ['%Y-%m-%dT%H:%M:%S.%f%z', '%Y-%m-%dT%H:%M:%S%z']
    for date_format in formats:
        try:
            parsed_date = datetime.strptime(date_str, date_format)
            return parsed_date.strftime('%H:%M %d.%m.%Y')
        except ValueError:
            continue
    return ''
