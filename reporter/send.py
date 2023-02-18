import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.exchange_declare(exchange="json_exchange", exchange_type="direct")

try:
    filename = "".join(sys.argv[1])
    report_name = "".join(sys.argv[2])
except:
    raise Exception(
        "Veuillez spécifier le nom du fichier json à envoyer et un nom de rapport"
    )

message = f"{report_name}\n"
with open(filename, "r") as file:
    message += file.read()


channel.basic_publish(exchange="json_exchange", routing_key="json_queue", body=message)
print(" [x] Sent the json file")
connection.close()
