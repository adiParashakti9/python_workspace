#filter by key :
#Keep only those key-value pairs where the key starts with "router"
devices={"router":"192.168.1.1","switch_1":"192.168.1.2","router_2":"192.168.1.3","switch_2":"192.168.1.4"}
filtered_devices={k:v for k,v in devices.items() if k.startswith("router")}
print(filtered_devices)
 