from flask import Flask, request, jsonify
import psutil
# import docker
# client = docker.from_env() # docker client initialization
import socket

# Get the server's hostname
server_name = socket.gethostname()

app=Flask(__name__)

@app.route('/')
def get_server_spec():
    cpu_usage=psutil.cpu_percent()
    memory_usage=psutil.virtual_memory().percent
    storage_usage=psutil.disk_usage("/").percent

    server_specs={
        'server_name': server_name,
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'storage_usage':storage_usage
    }
    print(server_specs)
    return jsonify(server_specs)


# @app.route('/containers')
# def get_docker_ps():
#     containers= client.containers.list(all)
#     container_names = []
#     for container in containers:
#         container_names.append(container.name)
#     print(container_names)
#     return jsonify(container_names)
#
#
# @app.route('/logs')
# def get_docker_logs():
#     docker_container = request.args.get('container')
#     container1=client.containers.get(docker_container)
#     logs = container1.logs(timestamps=True,tail='all').decode('utf-8')
#     return jsonify(logs)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

