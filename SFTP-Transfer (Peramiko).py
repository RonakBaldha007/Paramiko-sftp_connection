"""sftp server connection"""
import logging
import paramiko

logger=logging.getLogger(__name__)

#Now we are going to Set the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

def sftp_transfer():
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname='hostname', username='username',
                    password='password', allow_agent=False, look_for_keys=False)
        sftp = client.open_sftp()

        sftp.put("Source File Path", "Destination File Path")
        sftp.close()
    except paramiko.AuthenticationException:
        logger.error('ERROR : Authentication failed because of irrelevant details!')
    except IOError:
        logger.error('ERROR : Could not connect to %s.', cred['hostname'])

