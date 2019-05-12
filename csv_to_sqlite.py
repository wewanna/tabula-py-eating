import csv
import sqlite3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input', help="input file (.csv file)")
parser.add_argument('output', help="output file (.dv file)")
args = parser.parse_args()

input_filename = args.input
output_filename = args.output

f = open(input_filename, 'r', encoding='utf-8')
reader = csv.reader(f)
data = []
for line in reader:
    data.append(list(map(lambda x: 'NA' if x == '' else x, line)))
f.close()


con = sqlite3.connect(output_filename)
cur = con.cursor()
schema = "("
values_schema = "("
for w in data[0]:
    schema += w + " text, "
    values_schema += "?, "
schema = schema[:-2] + ")"
values_schema = values_schema[:-2] + ")"
print(schema)
cur.execute("CREATE TABLE Data" + schema + ";")
for line in data[1:]:
    cur.execute("INSERT INTO Data VALUES" + values_schema + ";", line)
con.commit()
