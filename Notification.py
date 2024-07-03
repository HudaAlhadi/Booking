from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send_notification(self):
        pass


class BasicNotification(Notification):
    def send_notification(self):
        print("Sending basic notification")


class BaseDecorator(Notification):
    def __init__(self, notification):
        self._notification = notification

    def send_notification(self):
        self._notification.send_notification()


class EmailDecorator(BaseDecorator):
    def send_notification(self):
        super().send_notification()
        print("Sending email notification")


class SMSDecorator(BaseDecorator):
    def send_notification(self):
        super().send_notification()
        print("Sending SMS notification")
