# a simple dns resolver made in Python.

# how it works:
1. The target domain (e.g. 'example.com')
2. A wordlist containing possible subdomains (ex: 'wordlist.txt')

For each word in the wordlist, the script tries to resolve the subdomain '<word>.<domain>' using the 'socket.getaddrinfo' function. If the subdomain exists and can be resolved, the script prints the subdomain name along with its IP address. Otherwise, it silently ignores it.

## Requirements

- Python 3.x
- Internet access to resolve domains

## How to use

1. Clone the repository (if applicable) or download the 'dnsResolver.py' script.

2. Prepare a wordlist with the subdomains you want to test, for example:
www
ftp
blog
admin
mail

3. Run the script passing the target domain and the path to the wordlist:
```bash
python3 dnsResolver.py example.com wordlist.txt
```

