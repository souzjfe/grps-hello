import grpc
from settings_pb2 import HelloRequest
from settings_pb2_grpc import MyServiceStub

def run():
    # Crie um canal gRPC para se conectar ao servidor
    channel = grpc.insecure_channel('localhost:50051')

    # Crie um cliente gRPC
    client = MyServiceStub(channel)

    # Faça uma chamada para o serviço SayHello
    response = client.SayHello(HelloRequest(name='Jeferson'))

    # Exiba a resposta do servidor
    print('Resposta do servidor:', response.message)

if __name__ == '__main__':
    run()
