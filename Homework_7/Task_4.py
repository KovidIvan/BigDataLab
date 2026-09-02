requested_roles = ["guest", "developer", "guest", "admin", 
"developer", "guest"]
required_admin_roles = {"admin", "security_officer", 
"audit_manager"}

req_roles_set = set(requested_roles)
intersec = req_roles_set.intersection(required_admin_roles)
dif = req_roles_set.difference(required_admin_roles)
check = "security_officer" in req_roles_set
print(f"""Уникальные запрошенные роли: {req_roles_set}
Общие административные роли: {intersec} 
Недостающие административные роли: {dif} 
Наличие роли security_officer в запросе: {check}""")
