class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initializes variables
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
    
    def power(self) -> None:
        """
        Turns tv on and off by flipping boolean.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        If tv is on then either unmutes or mutes tv.
        If tv is muted and then is unmuted it will return to its previous volume (prev_volume).
        """
        if self.__status:
            if not self.__muted:
                self.__prev_volume = self.__volume
                self.__volume = 0
                self.__muted = True
            else:
                self.__volume = self.__prev_volume
                self.__muted = False

    def channel_up(self) -> None:
        """
        If tv is on then increase channel by one.

        If channel is at the max channel then it circles around to the min channel.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        If tv is on then decrease channel by one.

        If channel is at the min channel then it circles around to the max channel.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        If tv is on and not muted then it increases the volume by one.

        If it is muted it reverts to the previous volume and increase by one.

        It does not increase if it is at max volume.
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__prev_volume
                self.__muted = False

            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        If tv is on and not muted then it decreases the volume by one.

        If it is muted it reverts to the previous volume and decreases by one.

        It does not decreases if it is at min volume.
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__prev_volume
                self.__muted = False

            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns a string that includes the power status, channel number, and volume.
        """
        return(f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}")