#!/usr/bin/env bash
# Displays information about subdomains

subdomains=("www" "lb-01" "web-01" "web-02")
subdomain_info() {
    dig "$1" | grep -A1 'ANSWER SECTION:' | sed -r "s/$1./$2/g" | awk 'NR==2 {print "The subdomain " $1 " is a " $4 " record and points to " $5}' 
}

if [ $# -eq 2 ];
then
    subdomain_info "$2.$1" "$2"
elif [ $# -eq 1 ];
then
    for subdomain in "${subdomains[@]}";
    do
        subdomain_info "$subdomain.$1" "$subdomain"
    done
fi
