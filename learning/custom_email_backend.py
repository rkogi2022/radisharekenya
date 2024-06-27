# custom_email_backend.py

from django.core.mail.backends.smtp import EmailBackend
import smtplib

class CustomEmailBackend(EmailBackend):
    def _get_connection(self):
        if self.use_ssl:
            connection_class = smtplib.SMTP_SSL
            connection_kwargs = {
                'host': self.host,
                'port': self.port,
                'local_hostname': self.local_hostname,
                'timeout': self.timeout,
                'source_address': self.source_address,
            }
        else:
            connection_class = smtplib.SMTP
            connection_kwargs = {
                'host': self.host,
                'port': self.port,
                'local_hostname': self.local_hostname,
                'timeout': self.timeout,
                'source_address': self.source_address,
            }

            if self.use_tls:
                connection_kwargs['starttls'] = True

        return connection_class(**connection_kwargs)
