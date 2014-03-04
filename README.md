fbpoke
======

## Summary

A really sad script that checks your Facebook for pokes and automatically pokes people back. Code-wise, theres a lot of jagaloonery going on here. I'm passing a fake user-agent so facebook allows the connection, and I'm not using the facebook API, since they don't have a poke method. Also, you've got to store your creds in plaintext. Sorry bout that.

## Usage

Just edit the script and add your credentials. The script doesn't use OAuth, but it transmits your creds over HTTPS. Sorry bout it.

## Example

```
$ python fbpoke.py 
[+] Setting some variables
[+] Instantiating Mechanize browser
[+] Requesting Facebook poke page to authenticate
[+] Filling username and password into fields
[+] Submitting request with forms and storing response
[+] Starting auto-poke loop
[+] Poked! Total Pokes: 1
[+] Poked! Total Pokes: 2
[+] Poked! Total Pokes: 3
[+] Poked! Total Pokes: 4
[+] Poked! Total Pokes: 5
[+] Waiting for poke...
[+] Waiting for poke...
^C[X] Ctrl-C detected!
[+] Terminating
====================================================================================================
```

## Todo

* Add logging
* Improve script so it logs/outputs poker's name
* Maybe use OAuth since my method is horrible
* Improve garbage collection. The script crashed after a few hours.
