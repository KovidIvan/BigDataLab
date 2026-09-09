db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

host = db_config.get("connection").get("host")
port = db_config.get("connection").get("port")
ssl_mode = db_config.get("connection").get("ssl_mode", "verify-full")
db_config["connection"]["user"] = "admin"
db_config["connection"]["max_connections"] = 100

print(f"SSL Mode: {ssl_mode}")
print("Параметры соединения:")
for key, value in db_config["connection"].items():
    print(f"* {key}: {value}")
