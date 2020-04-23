import subprocess


class DockerManager:

    def __init__(self):
        pass

    @staticmethod
    def docker_compose_up(docker_compose_file):
        compose_up = ["docker-compose", "-f", docker_compose_file, "up", "-d"]
        subprocess.run(compose_up)

    @staticmethod
    def docker_compose_down(docker_compose_file):
        compose_down = ["docker-compose", "-f", docker_compose_file, "down"]
        subprocess.run(compose_down)

    def ping(self, docker_name):
        pass

    def prune_container(self, docker_name):
        pass

    def prune_orphans(self):
        pass
