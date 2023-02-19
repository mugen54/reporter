import pika
from report_filler import ReportFiller


def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.exchange_declare(exchange="json_exchange", exchange_type="fanout")
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange="json_exchange", queue=queue_name)

    print(" [*] Waiting for file. To exit press CTRL+C")
    filler = ReportFiller()

    def callback(ch, method, properties, body):
        with open("data_samples/input.json", "wb") as file:
            index = str(body).index("\\n")-1
            file.write(body[index:])
        filler.generate("species_template.html", "input.json", "style.css", body[:index])

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True
    )


    channel.start_consuming()

    