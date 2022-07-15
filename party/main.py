from __future__ import annotations
from abc import abstractmethod
from typing import List


class Party:
    """
    Интерфейс места проведения мероприятия
    """

    def __init__(self, place: str):
        self.place = place

    def __str__(self):
        return f'{self.place}'

    _observers: List[Friend] = []

    @abstractmethod
    def add_friend(self, observer: Friend) -> None:
        """
        Добавление Friend() в наблюдатели мероприятия
        """

        self._observers.append(observer)

    @abstractmethod
    def del_friend(self, observer: Friend) -> None:
        """
        Удаление Friend() из наблюдателей мероприятия
        """

        self._observers.remove(observer)

    @abstractmethod
    def send_invites(self, event_time: str) -> None:
        """
        Рассылка приглашения всем Friend(), которые находятся в наблюдателях
        """

        if self._observers:
            for observer in self._observers:
                observer.invite_place = self.place
                observer.invite_time = event_time
        else:
            print('Список гостей пуст')


class Friend:
    """
    Интерфейс друга
    """

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    invite_place: str = None
    invite_time: str = None

    @abstractmethod
    def show_invite(self) -> str:
        """
        Возвращает текст послденего приглашения, которое получил Friend()
        """

        if self.invite_place:
            return f'{self.invite_place}: {self.invite_time}'
        else:
            return 'No party...'


if __name__ == '__main__':

    party = Party("Midnight Pub")

    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    print(john.show_invite() == "Midnight Pub: Saturday, 10:00 AM")
    print(lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM")
    print(nick.show_invite() == "Midnight Pub: Friday, 9:00 PM")
    print(chuck.show_invite() == "No party...")
