import grpc
from settings_pb2_grpc import MyServiceServicer, add_MyServiceServicer_to_server
from settings_pb2 import HelloRequest, HelloResponse
from concurrent import futures

class MyServiceImplementation(MyServiceServicer):
    def SayHello(self, request, context):
        return HelloResponse(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_MyServiceServicer_to_server(MyServiceImplementation(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
