import requests
import contextlib
import time
import os




DEFAULT_DOMAIN = "www.google.com"


#colors
Red = "\033[0;31m"
White = "\033[0;37m"
Cyan = "\033[0;36m"
Green = "\033[0;32m"
Yellow = "\033[0;33m"



def get_file(urls):
    for i in urls:
        with open("proxy.txt","w") as f:
            f.write(i)



#--------API---------
def socks5():
    url = ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt","https://raw.githubusercontent.com/shiftytr/proxy-list/master/socks5.txt"]
    re = [requests.get(i).text for i in url]
    get_file(re)


def socks4():
    url = ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt","https://raw.githubusercontent.com/shiftytr/proxy-list/master/socks4.txt"]
    re = [requests.get(i).text for i in url]
    get_file(re)


def http():
    url = ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt","https://raw.githubusercontent.com/shiftytr/proxy-list/master/http.txt"]
    re = [requests.get(i).text for i in url]
    get_file(re)


def https():
    re = requests.get("https://raw.githubusercontent.com/shiftytr/proxy-list/master/https.txt").text
    with open("proxy.txt","w") as f:
        f.write(re)
#----------------------





uss = input("choose http[h], https[hs], socks4[s4], socks5[s5] =>? ")
if uss == "h":
    http()
elif uss == "s4":
    socks4()
elif uss == "s5":
    socks5()
elif uss == "hs":
    https()
else:
    print(Red+"\nError!\n")
    os._exit(0)





def test_proxy(ip, domain=DEFAULT_DOMAIN):
    proxies = {"http": f"http://{ip}",
        "https": f"http://{ip}"}
    with contextlib.suppress(requests.RequestException):
        response = requests.get(f"http://{domain}", proxies=proxies, timeout=5)
        if response.status_code >= 200 and response.status_code < 300:
            return True
    return False





def test_ip_addresses(ip_file, output_file, domain=DEFAULT_DOMAIN):
    with open(ip_file, "r") as file:
        ip_addresses = file.read().splitlines()

    results = []

    for i, ip in enumerate(ip_addresses, start=1):
        is_working = test_proxy(ip, domain=domain)
        if is_working:
            results.append((ip))

        progress = i / len(ip_addresses) * 100
        print(Cyan+f'\rTesting - Progress: {progress:.1f}% | {"." * (i % 4)}    ',end="",flush=True)
        time.sleep(0.1)

    with open(output_file, "w") as file:
        for ip in results:
            file.write(ip+"\n")

    print(White+"\n\nTesting complete.")




def get_domain_choice():
    domain_choice = input(White+"Enter Domain For Test Proxies (default: www.google.com): ")
    return domain_choice.strip() or DEFAULT_DOMAIN


def main():
    input_file = "proxy.txt"
    output_file = "hit.txt"
    print(Green+"\nTesting in progress...")
    time.sleep(1)

    domain = get_domain_choice()
    print(White+"\nUsing domain: "+Yellow+domain)

    test_ip_addresses(input_file, output_file, domain=domain)
    print(White+"Results saved to", Yellow+output_file)
    os.remove(input_file)


if __name__ == "__main__":
    main()

