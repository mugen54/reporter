import pika, sys, os
from report_filler import ReportFiller


def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.exchange_declare(exchange="json_exchange", exchange_type="direct")
    channel.queue_bind(exchange="json_exchange", queue="json_queue")

    print(" [*] Waiting for file. To exit press CTRL+C")
    filler = ReportFiller()

    def callback(ch, method, properties, body):
        with open("data_samples/input.json", "wb") as file:
            index = str(body).index("\\n")-1
            file.write(body[index:])
        filler.generate("species_template.html", "input.json", "style.css", body[:index])

    channel.basic_consume(
        queue="json_queue", on_message_callback=callback, auto_ack=True
    )

    '''
    msg = body.split("\n")
    msg[1]
    '''
    channel.start_consuming()

    