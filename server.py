import a2s
import time
from datetime import datetime

IP = "135.148.151.140"
PORT = 60404  # prueba también 60405 si no responde

servidor_online = False

def check_server(ip, port):
    try:
        info = a2s.info((ip, port))
        players = a2s.players((ip, port))
        
        return {
            "online": True,
            "name": info.server_name,
            "map": info.map_name,
            "players": len(players),
            "max_players": info.max_players,
            "ping": round(info.ping, 2)
        }
    except Exception as e:
        return {"online": False}

def ahora():
    return datetime.now().strftime("%H:%M:%S")

while True:
    estado = check_server(IP, PORT)

    if estado["online"]:
        if not servidor_online:
            print(f"[{ahora()}] 🟢 SERVIDOR ACTIVO")
            servidor_online = True

        print(f"[{ahora()}] 🟢 ONLINE | "
              f"Jugadores: {estado['players']}/{estado['max_players']} | "
              f"Ping: {estado['ping']}ms | "
              f"Mapa: {estado['map']}")

        time.sleep(600)  # 10 minutos

    else:
        if servidor_online:
            print(f"[{ahora()}] 🔴 SERVIDOR CAÍDO")

        else:
            print(f"[{ahora()}] 🔴 Sigue caído")

        servidor_online = False
        time.sleep(30)  # 30 segundos