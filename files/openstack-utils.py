#!/usr/bin/env python

import argparse

from keystoneauth1 import session
from keystoneauth1.identity import v3
from novaclient import client as novaclient


def authSession(auth_url,
                project_domain_name,
                project_name,
                user_domain_name,
                username,
                password):

    auth = v3.Password(auth_url=auth_url,
                       project_domain_name=project_doamin_name,
                       project_name=project_name,
                       user_domain_name=user_domain_name,
                       username=username,
                       password=password)

    sess = session.Session(auth=auth)
    return sess
    

def novaClient(session):

    client = novaclient.Client('2', session=session)

    return client


def getInstanceHost(client, instance_id):
    """Get the host machine of this guest vm"""

    instance_info = client.servers.get(instance_id)

    # TODO

def parseArguments(): 
    """Parsing arguments from command line"""

    parser = argparse.ArgumentParser(
                      description="OpenStack toolkits")

    parser.add_argument('--os-auth-url', help="Authentication URL for Keystone V3 API",
                        required=True)
    parser.add_argument('--os-project-domain-name', help="Project's domain name",
                        required=True)
    parser.add_argument('--os-project-name', help="Project name",
                        required=True)
    parser.add_argument('--os-user-domain-name', help="User's domain name",
                        required=True)
    parser.add_argument('--os-username', help="User name",
                        required=True)
    parser.add_argument('--os-password', help="Password for this user",
                        required=True)

    args = parser.parse_args()
    return args


def takeAction(args):
    """Taking actions depend on what arguments you type in command line"""

     pass  


def main():

    args = parseArguments()

    takeAction(args)

if __name__ == '__main__':
    main()
