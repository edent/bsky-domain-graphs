import csv

#   File containing domain names
domains_file = "domains.txt"

#   Placeholders
domains = []
reversed_domains_list = []

#   Turn www.example.com into ["com", "example", "www"]
def split_and_reverse(domain) :
    split_string_array = domain.split(".")
    split_string_array.reverse()
    return split_string_array

def add_domain_to_list(split_string_array) :
    root = ""
    for element in split_string_array:
        root = root + "." + element
        reversed_domains_list.append(root)

#   Read domains in line by line
with open(domains_file) as file :
    domains = file.read().splitlines()

#   Parse through the domains, split, reverse, add them to the list
for domain in domains :
    add_domain_to_list(split_and_reverse(domain))

#   Deduplicate
reversed_domains_list = list(set(reversed_domains_list))

#   Sort
reversed_domains_list.sort()

#   Write domains to a CSV in the correct format
with open('domains.csv', 'w') as file :
    file.write("size,path\n")   #   Add CSV header
    file.write("400,/\n")   #   Add root
    for domain in reversed_domains_list :
            file.write("400,/"+domain+"\n")