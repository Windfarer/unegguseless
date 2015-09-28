from email import message_from_file
import re
import xlwt

re_name = re.compile(r"客户:\s(\w+)\s(\d+)")
re_detail = re.compile(r"\)\s(.+)颜色:")
re_color = re.compile(r"颜色:\s(\w+?)价格:")
re_price = re.compile(r"价格:\s(.+?)万元")
re_mileage = re.compile(r"里程:\s(.+?)万公里")
re_seller = re.compile(r"车商:\s(.+?)电话:\s([0-9\s]+)")
re_content = re.compile(r"联系内容:\s(.+)")
re_bd = re.compile(r"@(\w+)\s")
wb = xlwt.Workbook()
ws = wb.add_sheet("data", cell_overwrite_ok=True)

f = open('a.eml')
msg = message_from_file(f)

for part in msg.walk():
    data = part.get_payload(decode=True)
    if data:
        data = data.decode('utf-8').replace('<br/>', '\n').replace('&nbsp;', '')
        data = [line for line in data.split('\n') if line]
        count = 0
        for line in data:
            print(count)
            bd = re_bd.search(line)
            name = re_name.search(line)
            detail = re_detail.search(line)
            color = re_color.search(line)
            price = re_price.search(line)
            mileage = re_mileage.search(line)
            seller = re_seller.search(line)
            content = re_content.search(line)
            if bd:
                bd = bd.group(1)
                ws.write(count, 0, bd)
                if name:
                    name, phone = name.groups()
                    ws.write(count, 1, name)
                    ws.write(count, 2, phone)
                if detail:
                    detail = detail.group(1)
                    ws.write(count, 3, str(detail))
                if color:
                    color = color.group(1)
                    ws.write(count, 4, str(color))
                if price:
                    price = price.group(1)
                    ws.write(count, 5, str(price))
                if mileage:
                    mileage = mileage.group(1)
                    ws.write(count, 6, str(mileage))
                if seller:
                    seller, seller_phone = seller.groups()
                    if seller:
                        ws.write(count, 7, str(seller))
                    if seller_phone:
                        ws.write(count, 8, seller_phone)
                elif content:
                    content = content.group(1)
                    ws.write(count, 3, str(content))

                count += 1


wb.save("output.xls")
