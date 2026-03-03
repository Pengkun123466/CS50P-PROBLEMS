import csv 
import sys

def main():
    Command_argument()
    csv_before = sys.argv[1]
    csv_after = sys.argv[2]

    reader_csv = read_csv(csv_before)
    wrirer_csv = write_csv(reader_csv,csv_after)
    

def Command_argument():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    
def read_csv(csv_before):
    try:
        with open (csv_before) as file:
            read_list = []
            reader = csv.DictReader(file)
            for row in reader:
                read_list.append(row)
            return read_list
               
    except FileNotFoundError:
        sys.exit(f"Could not read {csv_before}")

def write_csv(reader_csv,csv_after):
    with open (csv_after,"w") as file:
        writer = csv.DictWriter(file,fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader_csv:
            full_name = row["name"]
            house = row["house"]
            last,first = full_name.split(", ")
            writer.writerow({"first": first, "last": last, "house": house})    
        return csv_after


if __name__ == "__main__":
    main()