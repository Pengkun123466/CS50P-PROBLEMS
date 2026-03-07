import sys
import csv
import requests
import json
from tabulate import tabulate
#L6读取csv文件
#L4用requests网络请求
#计算盈亏

def check_csv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith("csv"):
        sys.exit("Not a CSV file")

    return sys.argv[1]


def read_csv(funds_csv):
    holdings = []
    try:
        with open (funds_csv,"r") as csvfile:
            funds = csv.DictReader(csvfile)
            try:
                for row in funds:
                    row["shares"] = float(row["shares"])
                    row["total_cost"] = float(row["total_cost"])
                    holdings.append(row)
            except ValueError:
                sys.exit("Wrong Value")
    except FileNotFoundError:
            sys.exit(f"Could not read {funds_csv}")
    return holdings


def get_funds(code):
    url = f"http://fundgz.1234567.com.cn/js/{code}.js"
    try:
        response = requests.get(url)
        response.raise_for_status()
        raw_text = response.text
        clean_text = raw_text[8:-2]
        data_dict = json.loads(clean_text)
        gsz = float(data_dict["gsz"])
        return gsz

    except requests.RequestException:
        sys.exit(f"Network error while fetching data for {code}")


def calculate(funds_list):
    total_pnl = 0.0

    for fund in funds_list:
        shares = fund["shares"]
        price = fund["current_price"]
        total_cost = fund["total_cost"]
        fund_value = shares * price
        fund_pnl = fund_value - total_cost
        fund["pnl"] = fund_pnl

        total_pnl = total_pnl + fund_pnl
    
    return total_pnl


def update(funds_csv):
    holdings = read_csv(funds_csv)

    target_code = input("请输入修改基金代码: ")
    new_shares = float(input("请输入修改后的总份额: "))

    is_found = False

    for fund in holdings:
        if fund["fund_code"] == target_code:
            fund["shares"] = new_shares
            is_found = True
            break
        else:
            pass

    if is_found == False:
        new_cost = float(input("请输入该基金的投入总成本: "))
        new_fund = {"fund_code":target_code,"shares":new_shares,"total_cost":new_cost}
        holdings.append(new_fund)

    with open (funds_csv,"w",newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["fund_code", "shares", "total_cost"])
        writer.writeheader()
        writer.writerows(holdings)


def main():
    funds_csv = check_csv()

    while True:
        i = input("是否需要修改持仓份额？(y/n)")
        if i == "y":
            update(funds_csv)
        elif i == "n":
            break
        else:
            continue

    funds_list = read_csv(funds_csv)
    #print(funds_list)
    for fund in funds_list:
        code  = fund["fund_code"]
        current_price = get_funds(code)
        fund["current_price"] = current_price
    #print(funds_list)

    total_pnl = calculate(funds_list)

    print("\n" + "="*40)
    print("        个人基金持仓实时监控大屏")
    print("="*40)
    
    print(tabulate(funds_list, headers="keys", tablefmt="grid", floatfmt=".2f"))
    
    print("="*40)

    print(f"你的总仓位历史实时累计盈亏为: {total_pnl:.2f} 元\n")

if __name__ == "__main__":
    main()