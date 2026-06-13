#swap keys and values of this dictionary
ports={"http":80,"https":443,"ftp":21,"ssh":22}
swapped_ports={v:k for k,v in ports.items()}
print(swapped_ports)