from setuptools import setup

setup(
    name='commons',
    version='1.0',
    description='A useful module',
    author='Rahul R',
    author_email='rahul.r@attinadsoftware.com',
    packages=['commons', 'commons.utils', 'commons.action', 'commons.bootstrap', 'commons.constants',
              'commons.component', 'commons.config', 'commons.docker_manager', 'commons.download_manager',
              'commons.mqtt', 'commons.exceptions', 'commons.topic_generator', 'commons.view',
              'commons.schema', 'commons.keys',
              'commons.topic_router'],
    install_requires=['wheel', 'wget', 'paho-mqtt', 'singleton-decorator', 'marshmallow', 'flask_restplus', 'flask_api',
                      "apscheduler"]
)
