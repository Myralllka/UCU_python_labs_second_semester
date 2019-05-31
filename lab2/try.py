def input_ip():

    print("Usage: < ip_addr x.x.x.x > < ip_mask x.x.x.x > ")

    ip_addr, ip_mask = list(map(str, input().strip().split()))

    return (ip_addr, ip_mask)





def encode(ip_in):

    ip_addr_list = list(map(int, ip_in[0].split('.')))

    ip_mask_list = list(map(int, ip_in[1].split('.')))

    print(ip_addr_list, ip_mask_list)

    ip_net = [str(ip_addr_list[i] & ip_mask_list[i]) for i in range(4)]

    ip_host = [str(ip_addr_list[i] & ~ ip_mask_list[i]) for i in range(4)]



    print(".".join(ip_net), ".".join(ip_host))





if __name__ == "__main__":

    encode(input_ip())