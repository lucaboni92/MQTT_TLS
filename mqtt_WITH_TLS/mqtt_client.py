import paho.mqtt.client as mqtt
from config import *
import ssl

def main():

	client = mqtt.Client()

	try:
		client.username_pw_set(username, password=passwd)
		client.tls_set(ca_cert, certfile, keyfile, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS, ciphers=None)
		client.connect(broker)
		client.publish("cmnd/sonoff-test01/power1", payload="toggle", qos=0)
	except KeyboardInterrupt:
        # to intercept CRTL+C interrupt 		
		print ("\nQuitting...")
	except Exception as e:
		# unexpected exception
		print("Unexpected error: ", e)

if __name__ == "__main__":
	main()
        
