#filtering values using key
devices={"switch_1":"active","router":"inactive","switch_2":"active","firewall":"inactive"}
active_devices={k:v for k,v in devices.items() if v=="active"}
print((active_devices))
