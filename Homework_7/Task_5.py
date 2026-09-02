system_telemetry = [ 
("srv_01", 12.5, 64, "online"), 
("srv_02", 85.0, 92, "online"), 
("srv_03", 0.0, 0, "offline"), 
("srv_04", 45.2, 78, "online"), 
("srv_05", 95.1, 99, "online") 
]


active_servers =[]
active_nodes_count = 0
metrics = {}
cpu_load_all = 0
max_load = 0

for  node_name, cpu_load, ram_usage, status in system_telemetry:
    if status == "online": 
        active_servers.append(node_name) 
        active_nodes_count += 1
        cpu_load_all += cpu_load
        if max_load < cpu_load: max_load = cpu_load

average_cpu = round(cpu_load_all / active_nodes_count,2)
metrics['average_cpu'] = average_cpu
res = {'active_nodes_count':active_nodes_count, 'metrix':metrics}
print(f"""Активные узлы в сети: {active_servers}
Итоговый отчет телеметрии: 
{res}""")


