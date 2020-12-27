from datetime import datetime 
import requests

icon_numbers = ['01', '02', '03', '04', '09', '10', '11', '13', '50']
icon_codes = []
for icon in icon_numbers:
    changed_icon = icon
    changed_icon += 'd'
    icon_codes.append(changed_icon)
    changed_icon = icon
    changed_icon += 'n'
    icon_codes.append(changed_icon)

print(icon_codes)

for code in icon_codes:      
    with open(f'web/static/icon/{code}@4x.png', 'wb') as file_out:
        response = requests.get(
            f'http://openweathermap.org/img/wn/{code}@4x.png',
            stream=True
        )
        if not response.ok:
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
            file_out.write(block)


