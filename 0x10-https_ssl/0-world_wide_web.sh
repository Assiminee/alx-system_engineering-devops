#!/usr/bin/env bash
# Displays information about subdomains

subdomains=("www" "lb-01" "web-01" "web-02")
get_param() {
    dig "$1" | grep -A1 'ANSWER SECTION:' | awk "NR==2 {print $2}"
}

if [ $# -gt 1 ];
then
    subdomain="$2.$1"
    rec_type=$(get_param "$subdomain" "\$4")
    ip=$(get_param "$subdomain" "\$5")
    echo "The subdomain $2 is a $rec_type record and points to $ip"
elif [ $# -eq 1 ];
then
    for subdomain in "${subdomains[@]}";
    do
        sub="$subdomain.$1"
        rec_type=$(get_param "$sub" "\$4")
        ip=$(get_param "$sub" "\$5")
        echo "The subdomain $subdomain is a $rec_type record and points to $ip"
    done
fi
